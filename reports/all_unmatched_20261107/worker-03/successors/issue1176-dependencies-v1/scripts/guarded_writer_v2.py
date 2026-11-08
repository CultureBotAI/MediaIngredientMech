"""Issue1176 report-only three-row writer. Immutable task wrapper, not a campaign gate.
Immutable v2 repairs W03-PEPTONE-GUARD-001 after reported isolated reproduction.
Single-author execution; no claim of hostile-concurrency atomicity.
"""
import pathlib,json,hashlib,copy,subprocess,sys,os
import yaml
O=pathlib.Path(__file__).resolve().parents[1]
R=next(p for p in O.parents if (p/'MAPPING_SEMANTICS.md').is_file())
sys.path.insert(0,str(R/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient,validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
PLAN_SHA='28402d766f56a526d43e97b24513db6dc50415189dd57246560009d981629eae'
def require(v,msg):
 if not v:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def regular(p):
 require(p.is_file() and not p.is_symlink(),'not regular input');return p.read_bytes()
def pinned(binding):
 p=O/binding['path']; require(p.resolve().is_relative_to(O),'input escape');b=regular(p);require(sha(b)==binding['sha256'],'pinned input drift');return b
def check_dest(p):
 require(p.is_absolute() and '..' not in p.parts,'absolute nontraversal destination required')
 require(any(p.is_relative_to(O/x) for x in ['payloads-v2','validation/controls-v2']),'outside report/private output')
 require(not any(q.is_symlink() for q in [p,*p.parents]),'symlink output path')
 require(p.resolve()==p,'resolved output alias'); require(not os.path.lexists(p),'existing output')
 if p.parent.exists(): require(not any(q.name.casefold()==p.name.casefold() for q in p.parent.iterdir()),'case alias')
class Writer:
 def __init__(self):
  b=regular(O/'author-plan-v2.json');require(sha(b)==PLAN_SHA,'plan drift');self.plan=json.loads(b)
  self.rows={r['dependency_id']:r for r in self.plan['rows']};require(len(self.rows)==3,'exact three rows')
  self.hashes={k:sha(canon(v)) for k,v in self.rows.items()};self.prepared={}
  for x in self.plan['primary_captures']+self.plan['selected_parent_inputs']:pinned(x)
  p=yaml.safe_load(regular(O/'inputs/targets/Peptone.yaml'));require(p['identifier']=='mesh:D010461','generic parent identity drift')
  p=yaml.safe_load(regular(O/'inputs/targets/Bacto_Peptone.yaml'));require(p['identifier']=='MICRO:0000178','Bacto represented identity drift')
  for x in self.plan['core_unchanged']:require(sha(regular(R/x['path']))==x['sha256'],'W03 existing core drift')
 def fresh_dependency_pins(self):
  # Rebind the complete accepted plan and all scientific dependency inputs immediately
  # before writing. A serial change after prepare must not produce an output.
  b=regular(O/'author-plan-v2.json');require(sha(b)==PLAN_SHA,'fresh plan drift')
  require(json.loads(b)==self.plan,'in-memory plan drift')
  for x in self.plan['primary_captures']+self.plan['selected_parent_inputs']:pinned(x)
  for x in self.plan['core_unchanged']:require(sha(regular(R/x['path']))==x['sha256'],'fresh preserved core drift')
 def source(self,row):
  require(row['dependency_id'] in self.rows and sha(canon(row))==self.hashes[row['dependency_id']],'unlisted/mutated row')
  require(row['native_source_core_member'] is False and row['kind']=='accountable_dependent_owner_proposal','false core origin')
  before=pinned(row['maintained_before']); require(regular(R/row['owner_path'])==before,'maintained before changed')
  old=pinned(row['current_payload']); rec=yaml.safe_load(old)
  origin=row['predecessor_origin']
  if origin:
   work=R.parents[2]/'workers'/f"w{origin['worker']:02d}"/'worktree'
   blob=subprocess.check_output(['git','-C',str(work),'show',origin['head']+':'+origin['git_path']])
   require(blob==old and sha(old)==origin['payload']['sha256'],'foreign committed origin mismatch')
   require(origin['proposal']['owner_path']==row['owner_path'] and origin['proposal']['before_sha256']==sha(before),'foreign owner/before mismatch')
  else:require(old==before and row['owner_path'].endswith('/GYPS.yaml'),'fabricated predecessor')
  require(rec['components'][row['component_index']]==row['original_component'],'component drift')
  require(yaml.safe_load(before)['curation_history']==rec['curation_history'][:len(yaml.safe_load(before)['curation_history'])],'baseline history missing')
  return old,rec,before
 def transformed(self,row,rec,event=None):
  out=copy.deepcopy(rec);out['components'][row['component_index']]=copy.deepcopy(row['new_component'])
  out['component_assertion']['evidence'].extend(copy.deepcopy(row['append_evidence']))
  if event is None:
   event=record_curation_event(out,curator='codex-worker03 /root dependent-origin author',action='COUPLED_PEPTONE_REFERENCE',changes=row['event_text'],previous_status=rec['mapping_status'],new_status=rec['mapping_status'],llm_assisted=True)
  else:out['curation_history'].append(copy.deepcopy(event))
  return out,event
 def prepare(self,pid):
  require(pid in self.rows,'unlisted dependency');row=self.rows[pid];old,rec,before=self.source(row);out,event=self.transformed(row,rec)
  require(not validate_ingredient(out),'native closed-schema invalid');self.prepared[pid]=sha(canon(out))
  return {'row':copy.deepcopy(row),'old_bytes':old,'before_record':rec,'after_record':out,'event':event}
 def write(self,p,dest):
  self.fresh_dependency_pins()
  row=p['row'];old,current,before=self.source(row)
  require(p['old_bytes']==old,'prepared old bytes differ from freshly validated source')
  require(p['before_record']==current,'prepared source differs')
  require(sha(canon(p['after_record']))==self.prepared.get(row['dependency_id']),'prepared output altered')
  expected,event=self.transformed(row,current,p['event']);require(expected==p['after_record'],'unlisted field mutation')
  require(event['curator']=='codex-worker03 /root dependent-origin author' and event['action']=='COUPLED_PEPTONE_REFERENCE' and event['llm_assisted'] is True and event['changes']==row['event_text'],'false attribution/history')
  require(event['previous_status']==event['new_status']==current['mapping_status'],'status changed')
  # All revalidation and no-output checks precede native serialization.
  dest=pathlib.Path(dest);check_dest(dest);write_validated_ingredient(expected,dest)
  require(yaml.safe_load(regular(dest))==expected,'serialization drift')
  return {'dependency_id':row['dependency_id'],'owner_path':row['owner_path'],'before_sha256':sha(before),'predecessor_payload_sha256':sha(old),'payload':{'path':str(dest.relative_to(O)),'sha256':sha(regular(dest))},'component_index':row['component_index'],'before_component':current['components'][row['component_index']],'after_component':expected['components'][row['component_index']],'history_prefix_preserved':expected['curation_history'][:-1]==current['curation_history'],'history_appended':event,'append_evidence':row['append_evidence'],'predecessor_origin_object_sha256':row['predecessor_origin_object_sha256'],'native_source_core_member':False}
