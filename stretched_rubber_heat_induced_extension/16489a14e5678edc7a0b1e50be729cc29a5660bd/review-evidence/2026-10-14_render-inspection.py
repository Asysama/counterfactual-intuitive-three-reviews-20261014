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
rows=[]
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
(O/'identity-projection-audit.json').write_text(json.dumps(dict(status='PASS',cases=rows),indent=2))
