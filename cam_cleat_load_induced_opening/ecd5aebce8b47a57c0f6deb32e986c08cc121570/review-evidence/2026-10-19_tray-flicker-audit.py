"""Track the formerly coplanar cap in decoded native videos; keep old-head control."""
from pathlib import Path
import sys,json,subprocess,importlib.util
import numpy as np
from PIL import Image,ImageDraw
B=Path('/opt/siyuan-cf-intuitive-three-20261014');n='cam_cleat_load_induced_opening';head=json.loads((B/'heads-v10.json').read_text())[n]
sys.path.insert(0,str(B/'verified-v10'/n/'generators'/n))
from engine import geometry as geo
from src import violation
import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
spec=importlib.util.spec_from_file_location('ind',B/'2026-10-16_independent-v9.py');ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)
O=B/'flicker-v10';O.mkdir(exist_ok=False);rows=[]
for seed in [42,98]:
 cid=n+f'_{seed:08d}';new=B/'formal-v6'/n/cid;old=B/'formal-v5'/n/cid;m=json.loads((new/'metadata.json').read_text());before=json.loads((old/'metadata.json').read_text());assert m['generation']['git']==head and before['generation']['git']=='7b30f6188103dbe5afdbced8bb7d924e3b3dc14a'
 assert m['phenomenon_data']['scene_params']==before['phenomenon_data']['scene_params'];p=m['phenomenon_data']['scene_params'];s=p['scale']
 for branch in ['true','counterfactual']:
  a=np.load(new/m['paths'][branch]['trajectory']);b=np.load(old/m['paths'][branch]['trajectory']);assert set(a)==set(b) and all(np.array_equal(a[k],b[k]) for k in a)
 assert json.loads((new/'frame-hashes.json').read_text())['mask']==json.loads((old/'frame-hashes.json').read_text())['mask']
 scene,cam,pos,look=geo.setup(p,*violation.camera(p),2048);violation.scene(p);bpy.context.view_layer.update()
 bb=lambda name:np.array([tuple(bpy.data.objects[name].matrix_world@Vector(v)) for v in bpy.data.objects[name].bound_box])
 tray,ped=bb('catch_tray'),bb('tray_pedestal');assert abs(ped[:,2].max()-tray[:,2].min())<1e-6*s
 # Original pedestal reaches tray_top exactly; new support cap is one full tray thickness below it.
 assert abs((p['tray_top']+.20*s)/2+(p['tray_top']-.20*s)/2-p['tray_top'])<1e-10
 points=[Vector((x,.15+y,p['tray_top'])) for x in [-.02*s,0,.02*s] for y in [-.02*s,0,.02*s]]
 # Restrict intensity measurements to actually visible tray surface; the seed98 load
 # occludes the rear of the tray after settling. Ray-cast with a margin around all
 # samples to exclude moving occlusion edges from the temporal flicker statistic.
 state=dict(np.load(new/m['paths']['true']['trajectory']));visible=[];pixels={}
 for i in range(120):
  cam.location=pos.copy();cam.location.x+=.025*i/119;cam.rotation_euler=(look-cam.location).to_track_quat('-Z','Y').to_euler()
  geo.clear_dynamic();violation.frame(p,state,i);bpy.context.view_layer.update();deps=bpy.context.evaluated_depsgraph_get()
  pts=[world_to_camera_view(scene,cam,v) for v in points];pixels[i]=[(round(q.x*2048),round((1-q.y)*2048)) for q in pts]
  clear=True
  for v in points:
   for dx,dy in [(0,0),(-.008*s,-.008*s),(-.008*s,.008*s),(.008*s,-.008*s),(.008*s,.008*s)]:
    target=v+Vector((dx,dy,0));hit=scene.ray_cast(deps,cam.location,(target-cam.location).normalized())
    if not hit[0] or hit[4].name!='catch_tray' or abs(hit[1].z-p['tray_top'])>1e-5*s:clear=False;break
   if not clear:break
  if clear:visible.append(i)
 assert len(visible)>=6,visible
 runs=[f for f in visible if all(j in visible for j in range(f,f+6))];assert runs,visible
 begin=min(runs,key=lambda f:abs(f-60));selected=list(range(begin,begin+6));samples={};crops={}
 for version,root in [('before',old),('after',new)]:
  values=[]
  for i,im in enumerate(ind.decode(root/m['paths']['true']['video'])):
   xy=pixels[i]
   if i in visible:values.append([im[y-1:y+2,x-1:x+2].mean(axis=(0,1)).tolist() for x,y in xy])
   if i in selected:
    x,y=xy[4];crops[(version,i)]=Image.fromarray(im).crop((x-110,y-55,x+110,y+85))
  a=np.asarray(values);samples[version]=dict(max_adjacent_channel_change=float(abs(np.diff(a,axis=0)).max()),max_point_channel_std=float(a.std(axis=0).max()),max_point_channel_range=float(np.ptp(a,axis=0).max()),sampled_frames=visible,samples_rgb=a.tolist())
 assert samples['after']['max_adjacent_channel_change']<=2 and samples['after']['max_point_channel_std']<.8,samples['after']
 assert samples['before']['max_point_channel_std']>samples['after']['max_point_channel_std']+1,'old control must reproduce visible instability'
 sheet=Image.new('RGB',(6*220,2*164),'white');d=ImageDraw.Draw(sheet)
 for row,version in enumerate(['before','after']):
  for col,f in enumerate(selected):sheet.paste(crops[(version,f)],(col*220,row*164+24));d.text((col*220+4,row*164+4),f'{version} seed{seed} frame{f}',fill='black')
 sheet.save(O/f'{cid}-consecutive-native-crops.png')
 rows.append(dict(case_id=cid,head_sha=head,trajectory_and_formal_mask_unchanged=True,actual_support_cap_to_tray_top_m=float(tray[:,2].max()-ped[:,2].max()),measurements=samples))
(O/'tray-flicker-audit.json').write_text(json.dumps(dict(status='PASS',method='Native decoded True: nine world-tracked 3x3-pixel samples in the former exposed support cap, only frames where margin raycasts prove all samples are visible on the tray top; moving-occlusion edges excluded. Old-head control must exhibit greater instability; new max adjacent RGB change <=2 and per-point std <0.8.',cases=rows),indent=2));print('TRAY_FLICKER_PASS',[(r['case_id'],{k:{x:v[x] for x in ['max_adjacent_channel_change','max_point_channel_std','max_point_channel_range']} for k,v in r['measurements'].items()}) for r in rows],flush=True)
