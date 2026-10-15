"""Independent decoder checks for every published browser derivative."""
import json,subprocess,hashlib,sys
from pathlib import Path
import numpy as np
R=Path('/opt/siyuan-cf-intuitive-three-20261014');H=json.loads((R/'heads-v8.json').read_text())
V=json.loads((R/'current-versions-v8.json').read_text())
def decode(path):
 p=subprocess.Popen(['ffmpeg','-v','error','-threads','1','-i',str(path),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],stdout=subprocess.PIPE);n=1024*1024*3
 try:
  for i in range(120):
   b=bytearray()
   while len(b)<n:
    chunk=p.stdout.read(n-len(b));assert chunk,'truncated frame';b.extend(chunk)
   yield np.frombuffer(b,np.uint8).reshape(1024,1024,3)
  assert not p.stdout.read(1) and p.wait()==0
 finally:
  p.stdout.close()
  if p.poll() is None:p.terminate();p.wait()
for name,head in H.items():
 if len(sys.argv)>1 and name not in sys.argv[1:]:continue
 results=[];root=R/('formal-'+V[name])/name
 for mf in sorted(root.glob('*/metadata.json')):
  m=json.loads(mf.read_text());assert m['generation']['git']==head;case=mf.parent
  rels=[m['paths']['true']['video'],m['paths']['counterfactual']['video'],m['paths']['counterfactual']['mask'],m['paths']['counterfactual']['mask_overlay']]
  paths=[case/rel.replace('.mp4','_browser.mp4') for rel in rels];proof=[]
  for path in paths:
   d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]));s=d['streams'][0]
   assert s['codec_name']=='h264' and s['width']==s['height']==1024 and s['avg_frame_rate']=='24/1' and int(s['nb_frames'])==120 and float(d['format']['duration'])==5
   proof.append(dict(path=str(path.relative_to(case)),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
  readers=[decode(p) for p in paths];mask_start=None
  try:
   for i in range(120):
    a,b,mask,o=[next(x) for x in readers]
    if i<m['intervention_frame']:assert np.array_equal(a,b)
    assert np.all((mask==0)|(mask==255)) and np.array_equal(mask[:,:,0],mask[:,:,1]) and np.array_equal(mask[:,:,1],mask[:,:,2])
    if mask.any():
     if mask_start is None:mask_start=i
    else:assert i<m['mask_start_frame']
   for x in readers:assert next(x,None) is None
  finally:
   for x in readers:x.close()
  assert mask_start==m['mask_start_frame'];results.append(dict(case_id=m['task_id'],decoded_frames_per_stream=120,binary_review_mask=True,exact_review_prefix=True,streams=proof))
 assert len(results)==2
 out=R/('independent-audits-'+V[name])/(name+'-browser-media.json');out.parent.mkdir(exist_ok=True,parents=True);out.write_text(json.dumps(dict(status='PASS',head_sha=head,decoder=subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0],cases=results),indent=2));print('BROWSER MEDIA PASS',name,flush=True)
