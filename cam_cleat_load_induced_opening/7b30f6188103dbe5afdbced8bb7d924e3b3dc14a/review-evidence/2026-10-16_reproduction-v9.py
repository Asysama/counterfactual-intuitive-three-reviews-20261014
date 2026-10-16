"""Independent cross-run verification: exact recipe/trajectory/mask, bounded RGB rounding."""
from pathlib import Path
import sys,json,importlib.util,numpy as np
B=Path(sys.argv[1]);H=json.loads((B/'heads-v9.json').read_text());V=json.loads((B/'current-versions-v9.json').read_text());spec=importlib.util.spec_from_file_location('ind',B/'2026-10-14_independent-audit.py');ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind);rows=[]
for n,h in H.items():
 cid=n+'_00000042';a=B/('formal-'+V[n])/n/cid;b=B/('reproduction-'+V[n])/n/cid;m=json.loads((a/'metadata.json').read_text());r=json.loads((b/'metadata.json').read_text())
 assert m==r and m['generation']['git']==h
 for branch in ['true','counterfactual']:
  x=np.load(a/m['paths'][branch]['trajectory']);y=np.load(b/m['paths'][branch]['trajectory']);assert set(x)==set(y) and all(np.array_equal(x[k],y[k]) for k in x)
 ha=json.loads((a/'frame-hashes.json').read_text());hb=json.loads((b/'frame-hashes.json').read_text());assert ha['mask']==hb['mask']
 rels=[m['paths']['true']['video'],m['paths']['counterfactual']['video'],m['paths']['counterfactual']['mask'],m['paths']['counterfactual']['mask_overlay']];results={}
 for label,rel in zip(['true','counterfactual','mask','overlay'],rels):
  if ha[label]==hb[label]:results[rel]=dict(frames=120,decoded_frame_hashes_exact=True,max_channel_difference=0,total_differing_pixels=0);continue
  readers=[ind.decode(a/rel),ind.decode(b/rel)];mx=total=per=0
  try:
   for i in range(120):
    x,y=[next(q) for q in readers];delta=abs(x.astype(np.int16)-y);pixels=int(np.any(delta,axis=2).sum());mx=max(mx,int(delta.max()));total+=pixels;per=max(per,pixels)
   for q in readers:assert next(q,None) is None
  finally:
   for q in readers:q.close()
  assert mx<=2 and per<=64 and total<=1024
  results[rel]=dict(frames=120,decoded_frame_hashes_exact=False,max_channel_difference=mx,total_differing_pixels=total,max_differing_pixels_per_frame=per)
 rows.append(dict(generator=n,head_sha=h,case_id=cid,status='PASS',recipe_and_trajectory_exact=True,mask_exact=True,streams=results))
(B/'reproduction-independent-v9.json').write_text(json.dumps(dict(status='PASS',cases=rows,tolerance='Cross-run RGB only: max 2 intensity levels,64 pixels/frame,1024 pixels/stream; exact mask and trajectories. Within-pair prefix remains exact.'),indent=2));print('Independent reproduction PASS',flush=True)
