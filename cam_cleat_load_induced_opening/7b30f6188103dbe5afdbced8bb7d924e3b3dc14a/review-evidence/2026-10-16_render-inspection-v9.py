"""Independent target ontology and projection check, plus native decoded contact sheets."""
import sys,json,subprocess,hashlib
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
G=Path(sys.argv[1]);B=Path(sys.argv[2]);O=Path(sys.argv[3]);O.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(G))
from engine import geometry as geo
from src import violation
import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
rows=[];contact_checks=[]
for mf in sorted(B.glob('*/metadata.json')):
 m=json.loads(mf.read_text());case=mf.parent;p=m['phenomenon_data']['scene_params'];D=O/m['task_id'];D.mkdir();frames=sorted(set([0,m['intervention_frame'],m['first_changed_frame'],m['evidence_frame'],60,90,119]));imgs={};mask_checks=[];projection_min=1
 states={b:dict(np.load(case/m['paths'][b]['trajectory'])) for b in ['true','counterfactual']}
 scene,cam,pos,look=geo.setup(p,*violation.camera(p),2048);violation.scene(p)
 for branch,state in states.items():
  path=case/m['paths'][branch]['video']
  for f in frames:
   png=D/f'{branch}-{f:03d}.png'
   subprocess.run(['ffmpeg','-v','error','-i',str(path),'-vf',f'select=eq(n\\,{f})','-vsync','0','-frames:v','1',str(png)],check=True)
   cam.location=pos.copy();cam.location.x+=.025*f/119;cam.rotation_euler=(look-cam.location).to_track_quat('-Z','Y').to_euler()
   geo.clear_dynamic();violation.frame(p,state,f);bpy.context.view_layer.update()
   if m['phenomenon'].startswith('cam_'):
    bb=lambda o:np.array([tuple(o.matrix_world@Vector(v)) for v in o.bound_box])
    base,post,tray=[bb(bpy.data.objects[name]) for name in ['grounded_base','cradle_supported_post','catch_tray']]
    assert np.all(post[:,:2].min(axis=0)>=base[:,:2].min(axis=0)-1e-6*p['scale']) and np.all(post[:,:2].max(axis=0)<=base[:,:2].max(axis=0)+1e-6*p['scale'])
    assert abs(post[:,2].min()-base[:,2].max())<1e-6*p['scale']
    assert post[:,1].max()<tray[:,1].min()
    contact_checks.append(dict(case_id=m['task_id'],branch=branch,frame=f,post_fully_supported=True,post_tray_clearance_m=float(tray[:,1].min()-post[:,1].max())))
   if m['phenomenon'].startswith('interleaved_'):
    rr=.080*p['scale'];centre=np.array([p['pulley_x'],p['book_z']+.10*p['scale']]);rope=bpy.data.objects['pull_rope']
    verts=np.array([tuple(rope.matrix_world@v.co) for v in rope.data.vertices]);gap=np.linalg.norm(verts[:,[0,2]]-centre,axis=1)-rr
    assert gap.min()>-2e-5*p['scale'],'rope enters solid pulley rim'
    stop=bpy.data.objects['right_stop'];eye=bpy.data.objects['spine_rope_eyelet']
    bounds=lambda o:np.array([tuple(o.matrix_world@Vector(v)) for v in o.bound_box])
    sb,eb=bounds(stop),bounds(eye);assert eb[:,2].min()>sb[:,2].max(),'eyelet intersects end bumper'
    contact_checks.append(dict(case_id=m['task_id'],branch=branch,frame=f,minimum_pulley_rope_gap_m=float(gap.min()),eyelet_above_bumper_m=float(eb[:,2].min()-sb[:,2].max())))

   if m['phenomenon'].startswith('stretched_'):
    o=bpy.data.objects['continuous_rubber_band'];vv=np.array([tuple(o.matrix_world@v.co) for v in o.data.vertices]);edges={};volume=0.
    for face in o.data.polygons:
     ids=list(face.vertices)
     for a,b in zip(ids,ids[1:]+ids[:1]):edges[tuple(sorted((a,b)))]=edges.get(tuple(sorted((a,b))),0)+1
     for j in range(1,len(ids)-1):volume+=np.dot(vv[ids[0]],np.cross(vv[ids[j]],vv[ids[j+1]]))/6
    assert all(v==2 for v in edges.values()) and len(vv)-len(edges)+len(o.data.polygons)==0
    length=float(state['length'][f]);top=p['top_z'];middle=top-length/2
    assert abs(vv[:,2].max()-top)<1e-6 and abs(vv[:,2].min()-(top-length))<1e-6
    for face in o.data.polygons:
     q=vv[list(face.vertices)]
     if q[:,2].min()<middle<q[:,2].max():assert np.all(q[:,0]>.025*p['scale']) or np.all(q[:,0]<-.025*p['scale'])
    rest_P=2*(p['natural_length']-2*p['loop_radius']-p['rest_width'])+2*np.pi*p['loop_radius']
    expected=rest_P*p['rest_width']*p['rest_thickness'];assert abs(abs(volume)/expected-1)<.001
    contact_checks.append(dict(case_id=m['task_id'],branch=branch,frame=f,closed_loop_euler_characteristic=0,open_center=True,actual_material_volume=float(abs(volume)),relative_volume_error=float(abs(abs(volume)/expected-1))))
   if m['phenomenon'].startswith('cam_'):names={'left_cam','right_cam','left_cam_grip_marker','right_cam_grip_marker'}
   elif m['phenomenon'].startswith('interleaved_'):names={o.name for o in bpy.data.objects if o.name.startswith('right_leaf_') or o.name.startswith('right_guide_shoe') or o.name in {'right_bound_spine','spine_rope_eyelet'}}
   else:names={'continuous_rubber_band'}
   assert names=={o.name for o in bpy.data.objects if o.get('target')}
   for o in bpy.data.objects:
    if o.name in names:
     for v in o.data.vertices:
      q=world_to_camera_view(scene,cam,o.matrix_world@v.co);assert q.z>0 and 0<q.x<1 and 0<q.y<1
      projection_min=min(projection_min,q.x,q.y,1-q.x,1-q.y)
   if branch=='counterfactual' and f>=m['first_changed_frame']:
    # Render an identity pass using an independently selected explicit object-name set.
    for o in bpy.data.objects:o.color=(1,1,1,1) if o.name in names else (0,0,0,1)
    sh=scene.display.shading;sh.light='FLAT';sh.show_specular_highlight=False;scene.display.render_aa='OFF';scene.world.color=(0,0,0)
    ref=D/f'identity-{f:03d}.png';geo.render_rgb(scene,ref)
    decoded=D/f'mask-{f:03d}.png';subprocess.run(['ffmpeg','-v','error','-i',str(case/m['paths']['counterfactual']['mask']),'-vf',f'select=eq(n\\,{f})','-vsync','0','-frames:v','1',str(decoded)],check=True)
    assert np.array_equal(np.asarray(Image.open(ref)),np.asarray(Image.open(decoded)))
    mask_checks.append(dict(frame=f,targets=sorted(names),decoded_identity_exact=True))
    # Reset the entire scene to original RGB state for the next reference.
    scene,cam,pos,look=geo.setup(p,*violation.camera(p),2048);violation.scene(p)
   imgs[(branch,f)]=png
 # Two rows maintain label order; these are decoded final files, not unsubmitted renderer previews.
 sheet=Image.new('RGB',(420*len(frames),880),'white');draw=ImageDraw.Draw(sheet)
 for row,branch in enumerate(['true','counterfactual']):
  for col,f in enumerate(frames):
   im=Image.open(imgs[(branch,f)]);im.thumbnail((420,420));sheet.paste(im,(col*420,row*440+20));draw.text((col*420+8,row*440+3),f'{branch} frame {f}',fill='black')
 sheet.save(D/'decoded-contact-sheet.jpg')
 rows.append(dict(head_sha=m['generation']['git'],case_id=m['task_id'],status='PASS',target_projection_min_fraction=float(projection_min),independent_identity_frames=mask_checks,visual_review='PENDING'))
(O/'identity-projection-audit.json').write_text(json.dumps(dict(status='PASS',cases=rows,contact_checks=contact_checks),indent=2))
