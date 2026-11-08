import pathlib,hashlib
O=pathlib.Path(__file__).resolve().parents[1];p=O/'scripts/guarded_writer_v1.py';b=p.read_bytes();assert hashlib.sha256(b).hexdigest()=='7eb1aef40ff697e6688ce4f03e52a58016cbe50353cfd9e7ef5f0758971f4e72'
s=b.decode().replace('Single-author execution; no claim of hostile-concurrency atomicity.','Immutable v2 repairs W03-PEPTONE-GUARD-001 after reported isolated reproduction.\nSingle-author execution; no claim of hostile-concurrency atomicity.')
s=s.replace("['payloads','validation/controls']","['payloads-v2','validation/controls-v2']")
anchor=' def source(self,row):\n';assert s.count(anchor)==1
method=""" def fresh_dependency_pins(self):
  # Rebind the complete accepted plan and all scientific dependency inputs immediately
  # before writing. A serial change after prepare must not produce an output.
  b=regular(O/'author-plan-v2.json');require(sha(b)==PLAN_SHA,'fresh plan drift')
  require(json.loads(b)==self.plan,'in-memory plan drift')
  for x in self.plan['primary_captures']+self.plan['selected_parent_inputs']:pinned(x)
  for x in self.plan['core_unchanged']:require(sha(regular(R/x['path']))==x['sha256'],'fresh preserved core drift')
"""
s=s.replace(anchor,method+anchor)
s=s.replace(" def write(self,p,dest):\n  row=p['row'];old,current,before=self.source(row)"," def write(self,p,dest):\n  self.fresh_dependency_pins()\n  row=p['row'];old,current,before=self.source(row)")
q=O/'scripts/guarded_writer_v2.py';assert not q.exists();q.write_text(s)
s=(O/'scripts/build_payloads_v1.py').read_text().replace('guarded_writer_v1','guarded_writer_v2').replace("O/'payloads'","O/'payloads-v2'").replace("validation/diffs","validation/diffs-v2").replace("write-receipts.json","write-receipts-v2.json")
(O/'scripts/build_payloads_v2.py').write_text(s)
s=(O/'scripts/focused_controls_v1.py').read_text().replace('guarded_writer_v1','guarded_writer_v2').replace("validation/controls'","validation/controls-v2'").replace("O/'payloads'","O/'payloads-v2'").replace('validation/focused-controls.json','validation/focused-controls-v2.json')
(O/'scripts/focused_controls_v2.py').write_text(s)
print('v2',hashlib.sha256(q.read_bytes()).hexdigest())
