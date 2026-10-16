"""Independent full decoded media and phenomenon audit; no generator imports."""
import argparse,hashlib,json,math,subprocess
from pathlib import Path
import numpy as np

def decode(path):
 p=subprocess.Popen(['ffmpeg','-v','error','-threads','1','-i',str(path),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],stdout=subprocess.PIPE);size=2048*2048*3
 try:
  for i in range(120):
   b=bytearray()
   while len(b)<size:
    q=p.stdout.read(size-len(b));assert q,'truncated frame';b.extend(q)
   yield np.frombuffer(b,dtype=np.uint8).reshape(2048,2048,3)
  assert not p.stdout.read(1) and p.wait()==0
 finally:
  p.stdout.close()
  if p.poll() is None:p.terminate();p.wait()

def physical(m,t,c):
 from scipy.integrate import solve_ivp,quad
 p=m['phenomenon_data']['scene_params'];n=m['phenomenon'];on=p['onset'];s=p['scale']
 assert p['gravity']==9.81
 for state in [t,c]:
  for key,v in state.items():assert np.isfinite(v).all() and v.shape[0]==120
  assert np.array_equal(state['time'],np.arange(120)/24)
 for key in t:assert np.array_equal(t[key][:on+1],c[key][:on+1]),key
 tb=m['timebase'];assert tb['physical_seconds_per_video_second']==1 and abs(tb['physical_dt']*tb['outer_steps_per_recorded_frame']*24-1)<1e-12
 if n.startswith('cam_'):
  q=t['theta'];k=p['normal_stiffness'];normal_compression=np.maximum(p['rope_radius']-(p['half_pivot_spacing']-p['cam_radius']-p['eccentricity']*np.cos(q)),0)
  E=.5*p['load_mass']*t['velocity']**2+p['cam_inertia']*t['omega']**2-p['load_mass']*9.81*t['drop']+k*normal_compression**2+.018*s*s*(q-p['theta0'])**2+2*p['eccentricity']*math.sin(p['theta0'])*p['normal_preload']*(q-p['theta0'])
  assert np.max(E-E[0])<.01 and abs(t['velocity'][-1])<.003
  assert t['drop'][-1]<p['max_drop']-.1*s and q[-1]<p['theta0']-.02
  assert abs(c['drop'][-1]-p['max_drop'])<1e-9 and np.max(c['theta'])>p['theta0']+.02
  for state in [t,c]:
   assert np.min(state['rope_halfwidth'])>.65*p['rope_radius'] and np.min(state['load_z']-p['load_height']/2-p['tray_top'])>=-1e-9
   assert np.all(state['theta']>=math.radians(24)-1e-9) and np.all(state['theta']<=math.radians(88)+1e-9)
  assert 6*math.pi*.18*s>p['max_drop'] and .078*s>2*p['rope_radius']
  ev=np.flatnonzero((np.arange(120)>on)&(c['theta']>p['theta0']+.015)&(c['drop']>.10*s))[0]
  w=dict(true_energy_max_increase_J=float(np.max(E-E[0])),true_final_drop_m=float(t['drop'][-1]),true_final_velocity=float(t['velocity'][-1]),cf_final_drop_m=float(c['drop'][-1]),cf_max_opening_degrees=float(np.rad2deg(np.max(c['theta'])-p['theta0'])))
 elif n.startswith('interleaved_'):
  alpha=2*p['friction']*p['leaves']**2*p['leaf_thickness']/p['fan_span'];A=quad(lambda u:math.exp(alpha*(1-u*u)),0,1,epsabs=1e-10)[0]
  assert math.isclose(A,p['amplification'],rel_tol=1e-10)
  assert p['boundary_resistance']<p['pull_force']<p['boundary_resistance']*A
  assert np.all(t['displacement']==0) and c['displacement'][-1]==p['stop_displacement'] and c['velocity'][-1]==0
  for state in [t,c]:
   assert np.array_equal(state['weight_drop'],state['displacement'])
   kinetic=.5*(p['pull_mass']+p['booklet_mass'])*state['velocity']**2
   assert np.all(kinetic<=p['pull_force']*state['displacement']+1e-8)
   assert .40*s-state['weight_drop'].max()-.055*s>=.10*s-1e-9
  # Independently reconstruct alternating contact-layer positions and solid thickness.
  N=p['leaves'];h=p['leaf_thickness'];levels=sorted([p['book_z']+(2*j+o-N)*h for o in [0,1] for j in range(N)])
  assert min(np.diff(levels))>=.999*h and .98*h<h
  ev=np.flatnonzero(c['displacement']>p['overlap']+.01*s)[0]
  w=dict(independent_integral_amplification=A,normal_force_parameter=alpha,load_N=p['pull_force'],threshold_N=p['static_threshold'],true_final_displacement=0.,cf_final_displacement=float(c['displacement'][-1]),minimum_leaf_gap_m=.02*h)
 elif n.startswith('stretched_'):
  tau=np.arange(120-on)/24;errors=[]
  C=p['mass']*9.81/(p['temperature0']*(p['initial_stretch']-p['initial_stretch']**-2))
  assert math.isclose(C,p['network_constant'],rel_tol=1e-12)
  for branch,state in [('true',t),('counterfactual',c)]:
   def rhs(time,y):
    T=p['temperature0']+p['temperature_rise']*(1-math.exp(-time/p['heat_tau']));factor=T if branch=='true' else p['temperature0']**2/T;l=y[0]/p['natural_length']
    return [y[1],(p['mass']*9.81-C*factor*(l-l**-2)-p['vertical_damping']*y[1])/p['mass']]
   sol=solve_ivp(rhs,(0,float(tau[-1])),[p['initial_length'],0],t_eval=tau,rtol=1e-10,atol=1e-12).y.T
   err=float(np.max(abs(sol[:,0]-state['length'][on:])));assert err<1e-7;errors.append(err)
   assert np.max(abs(state['velocity'][-10:]))<.025 and np.min(state['load_z']-.05*s)>.20*s
   lam=state['length']/p['natural_length'];width=p['rest_width']/np.sqrt(lam);radius=p['loop_radius']/np.sqrt(lam)
   straight=state['length']-2*radius-width;assert np.all(straight>0)
   perimeter=2*straight+2*math.pi*radius
   rest_perimeter=2*(p['natural_length']-2*p['loop_radius']-p['rest_width'])+2*math.pi*p['loop_radius']
   thickness=p['rest_thickness']*rest_perimeter*p['rest_width']/(perimeter*width)
   assert np.allclose(perimeter*width*thickness,rest_perimeter*p['rest_width']*p['rest_thickness'],rtol=1e-12)
  assert np.array_equal(t['temperature'],c['temperature']) and t['length'][-1]<p['initial_length']-.02*s and c['length'][-1]>p['initial_length']+.02*s
  ev=np.flatnonzero((c['length']>p['initial_length']+.015*s)&(t['length']<p['initial_length']-.015*s))[0]
  w=dict(independent_ode_errors_m=errors,true_final_length=float(t['length'][-1]),cf_final_length=float(c['length'][-1]),initial_length=p['initial_length'],final_temperature_kelvin=float(t['temperature'][-1]))
 else:raise ValueError(n)
 assert int(ev)==m['evidence_frame'];w['evidence_frame']=int(ev);return w

def review(case,head):
 m=json.loads((case/'metadata.json').read_text());assert m['generation']['git']==head and m['render']['native'] and m['render']['res']==[2048,2048]
 paths=[case/m['paths'][b]['video'] for b in ['true','counterfactual']]+[case/m['paths']['counterfactual'][k] for k in ['mask','mask_overlay']]
 for f in paths:
  d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));s=d['streams'][0]
  assert s['codec_name']=='h264' and s['width']==s['height']==2048 and s['avg_frame_rate']=='24/1' and int(s['nb_frames'])==120 and float(d['format']['duration'])==5
 for k,v in json.loads((case/'manifest.json').read_text()).items():
  f=case/k;assert f.stat().st_size==v['bytes'] and hashlib.sha256(f.read_bytes()).hexdigest()==v['sha256']
 readers=[decode(f) for f in paths];first=None;active_frames=[];border_min=2048;mask_min=2048*2048
 try:
  for i in range(120):
   a,b,mask,overlay=[next(q) for q in readers]
   if first is None and not np.array_equal(a,b):first=i
   assert i>=m['intervention_frame'] or np.array_equal(a,b)
   assert np.array_equal(mask[:,:,0],mask[:,:,1]) and np.array_equal(mask[:,:,0],mask[:,:,2]) and np.all((mask==0)|(mask==255))
   active=mask[:,:,0]>0
   if active.any():
    yy,xx=np.where(active);border=min(xx.min(),yy.min(),2047-xx.max(),2047-yy.max());assert border>2 and len(xx)>500
    border_min=min(border_min,int(border));mask_min=min(mask_min,len(xx));active_frames.append(i)
    assert np.all(overlay[active]==[255,0,0])
   assert np.array_equal(overlay[~active],b[~active])
  for q in readers:assert next(q,None) is None
 finally:
  for q in readers:q.close()
 assert first==m['first_changed_frame']==m['mask_start_frame'] and active_frames==list(range(first,120))
 t=dict(np.load(case/m['paths']['true']['trajectory']));c=dict(np.load(case/m['paths']['counterfactual']['trajectory']));w=physical(m,t,c)
 for b in ['true','counterfactual']:assert (case/m['paths'][b]['prompt']).read_text()==m['descriptions'][b]
 return dict(status='PASS',head_sha=head,case_id=m['task_id'],first_changed_frame=first,minimum_target_border_px=border_min,minimum_mask_pixels=mask_min,physical_witnesses=w,decoded_frames_each_stream=120,visual_inspection='PENDING',browser_playback='PENDING')

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('root',type=Path);a.add_argument('--heads',type=Path,required=True);a.add_argument('--versions',type=Path,required=True);a.add_argument('--output',type=Path,required=True);v=a.parse_args();h=json.loads(v.heads.read_text());versions=json.loads(v.versions.read_text());rows=[]
 for n,head in h.items():
  cases=sorted((v.root/('formal-'+versions[n])/n).glob('*/metadata.json'));assert len(cases)==2
  for mf in cases:rows.append(review(mf.parent,head));print('INDEPENDENT PASS',mf.parent.name,flush=True)
 assert len(rows)==2*len(h)
 v.output.write_text(json.dumps(dict(status='PASS',cases=rows,formal_streams=8*len(h),visual_and_browser_pending=True),indent=2))
