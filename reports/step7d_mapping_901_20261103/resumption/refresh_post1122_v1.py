"""External post-#1122 native refresh orchestration; default prints plan only.

Root executes only after the guarded four-comment correction is applied and
independently reviewed. Stop on first failure; preserve all old Step7d report
bytes, outputs and failure receipts. No source/snapshot regeneration or suite.
"""
from __future__ import annotations
import argparse, collections, datetime, hashlib, json, os, stat, subprocess, sys
from pathlib import Path
D=Path(__file__).resolve().parent
RUN=D.parent
W=RUN/'step7d'
RUNNER=RUN/'run_step7d_mim.py'
BASE='7d35035f6c521c69fad94f73381c6a6eb7251fff'
BEFORE='cd7775a22114ea2d5dd324a532e4cc0d1f335504cd3cfe8c4efe93961cc148e4'
AFTER='d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef'
RECEIPT_SHA='45af9515590918e3420327668d4b89f564457cf97eea9404a34c4da7d17f0e4b'
REPORT='reports/step7d_mapping_901_20261103'
PRIOR=REPORT+'/companion-review.json'
SUCCESSOR=REPORT+'/refresh-v2/companion-review.json'
COMPANION_RECEIPT=REPORT+'/refresh-v2/companion-refresh-receipt.json'
PRIOR_COPY=REPORT+'/refresh-v2/prior-companion-review.json'
ASSEMBLER='reports/sssom_completion_20260921/assemble_review.py'
BASE_REVIEW='reports/sssom_completion_20260921/review.json'
SEMANTIC='reports/semantic_review_20260921/resolution/current-review.json'
MAPPING_RECEIPT='reports/sssom_completion_20260921/mapping_changes/issue901-step7d-reviewed-owner-forms.json'
SELECTORS=('tests/test_ingredient_bundle.py','.github/workflows/qc-reviewed-sssom.yaml')
FULL='output/step7d-post1122-full-v1'
COMPANION='output/step7d-post1122-companion-v1'
REVIEWED='output/step7d-post1122-reviewed-v1'
SUPPORTED='output/step7d-post1122-supported-v1'
SUMMARY=D/'step7d-post1122-orchestration-v1.json'
TRACE=D/'step7d-post1122-command-trace-v1.jsonl'
SNAPSHOTS={'UNIFIED_INGREDIENT_MAPPING.tsv':'f6a8eb844e578d79da9538abf99c244fc25b2c928c50c64c0477b1218092a0f1',
 'UNIFIED_INGREDIENT_MAPPING.provenance.json':'075fcc6ef6eca25c1e63d65889df37d4893be2b1b9d3630df90704012dc2c831'}
_CODE=Path(__file__).read_bytes()
SCHEMA_CODE='''from pathlib import Path
from sssom.parsers import parse_sssom_table
from sssom.validators import SchemaValidationType, validate
p=Path("output/step7d-post1122-supported-v1/ingredient_mappings.sssom.tsv")
validate(parse_sssom_table(p), validation_types=[SchemaValidationType.JsonSchema, SchemaValidationType.PrefixMapCompleteness, SchemaValidationType.StrictCurieFormat])
print("PASS supported SSSOM native JSON Schema, prefix-map completeness and strict CURIE format")
'''
COMMANDS=[
 ('01-assemble',['python','-B',ASSEMBLER]),
 ('02-assemble-check',['python','-B',ASSEMBLER,'--check']),
 ('03-export-full',['just','export-kgx',FULL]),
 ('04-semantic-build',['python','-B','reports/semantic_review_20260921/resolution/build_review.py','--bundle',FULL]),
 ('05-semantic-integrity',['python','-B','-m','mediaingredientmech.validation.semantic_release','--root','.','--report',SEMANTIC]),
 ('06-assemble-after-semantic-check',['python','-B',ASSEMBLER,'--check']),
 ('07-companion-refresh',['python','-B','scripts/refresh_unchanged_cohort.py','--root',str(W),'--baseline',BASE,'--prior-review',PRIOR,'--output',SUCCESSOR,'--receipt',COMPANION_RECEIPT,'--prior-copy',PRIOR_COPY]),
 ('08-companion-export',['python','-B','-m','mediaingredientmech.export.ingredient_bundle','export','--review',SUCCESSOR,'--output',COMPANION]),
 ('09-reviewed-export',['just','export-reviewed-sssom',BASE_REVIEW,REVIEWED]),
 ('10-reviewed-qc-schema',['just','qc-reviewed-sssom',BASE_REVIEW,REVIEWED]),
 ('11-supported-export',['just','export-supported-kgx',SEMANTIC,SUPPORTED]),
 ('12-supported-qc',['just','qc-supported-kgx',SEMANTIC,SUPPORTED]),
 ('13-supported-schema',['python','-B','-c',SCHEMA_CODE]),
]
MUTATION_TAGS=['assembler-constant','paired-selectors']
def sha(raw):return hashlib.sha256(raw).hexdigest()
def require(ok,msg):
 if not ok:raise ValueError('post1122 orchestration: '+msg)
def regular(path):
 path=Path(path).absolute();info=path.lstat()
 require(path.resolve()==path and stat.S_ISREG(info.st_mode)and info.st_nlink==1,'aliased/nonregular file: '+str(path))
 return path.read_bytes()
def absent(path):
 require(Path(path).absolute()==Path(path).resolve(),'aliased output: '+str(path))
 require(not os.path.lexists(path),'output exists: '+str(path))
def git(*args):return subprocess.check_output(['git','-C',str(W),*args])
def native_tag(tag):return 'step7d-post1122-'+tag+'-v1'
def tracked():return [x for x in git('ls-files','-z').decode().split('\0')if x]
def current_report_files():return {str(p.relative_to(W))for p in (W/REPORT).rglob('*')if p.is_file()or p.is_symlink()}
def modifications(before):
 old=('REVIEWED_SOURCE = "'+BEFORE+'"').encode();new=('REVIEWED_SOURCE = "'+AFTER+'"').encode()
 require(before[ASSEMBLER].count(old)==1 and new not in before[ASSEMBLER],'assembler constant not exact old endpoint')
 result={ASSEMBLER:before[ASSEMBLER].replace(old,new)}
 for name in SELECTORS:
  base=git('show',BASE+':'+name)
  require(before[name]==base and base.count(PRIOR.encode())==1 and SUCCESSOR.encode()not in base,'selector has nonbaseline changes: '+name)
  result[name]=base.replace(PRIOR.encode(),SUCCESSOR.encode())
 return result

def preflight():
 require(sha(regular(Path(__file__)))==sha(_CODE),'orchestrator bytes changed')
 require(git('rev-parse',BASE+'^{commit}').decode().strip()==BASE,'durable companion baseline missing')
 require(git('merge-base',BASE,'HEAD').decode().strip()==BASE,'HEAD not descended from companion baseline')
 require(sha(regular(W/'mappings/ingredient_mappings.sssom.tsv'))==AFTER,'guarded four-comment canonical correction not applied')
 require(sha(regular(W/MAPPING_RECEIPT))==RECEIPT_SHA,'corrected single batch25 not applied')
 for name,value in SNAPSHOTS.items():require(sha(regular(W/name))==value,'reviewed snapshot pair changed')
 old_reports={name:regular(W/name)for name in current_report_files()}
 require(PRIOR in old_reports and old_reports[PRIOR]==git('show',BASE+':'+PRIOR),'prior Step7d companion not immutable baseline bytes')
 frozen={};expected={}
 source_roots=('data/ingredients','data/curated','src','scripts','tests','.github/workflows')
 require(not git('diff','--name-only',BASE,'--',*source_roots),'unexpected source/code/test/workflow drift from durable baseline')
 baseline_paths=set(git('ls-tree','-r','--name-only',BASE,'--',*source_roots).decode().splitlines())
 current_paths={n for n in tracked()if n.startswith(tuple(x+'/'for x in source_roots))}
 require(current_paths==baseline_paths,'source/code/test/workflow tracked membership changed')
 for name in tracked():
  if name.startswith(('data/ingredients/','data/curated/','src/','scripts/','tests/','.github/workflows/','mappings/'))or name in [*SNAPSHOTS,'MAPPING_SEMANTICS.md','justfile','pyproject.toml','uv.lock','.python-version']:
   frozen[name]=regular(W/name)
 assembler=regular(W/ASSEMBLER);require(assembler==git('show',BASE+':'+ASSEMBLER),'assembler differs beyond the expected baseline')
 before={ASSEMBLER:assembler,**{n:frozen[n]for n in SELECTORS}}
 expected=modifications(before)
 frozen.update(old_reports);frozen[ASSEMBLER]=assembler
 frozen[Path(__file__).as_posix()]=_CODE
 for target in [W/FULL,W/COMPANION,W/REVIEWED,W/SUPPORTED,W/REPORT/'refresh-v2',SUMMARY,TRACE]:absent(target)
 for tag,_ in COMMANDS:
  for suffix in ['.json','.log']:absent(RUN/'logs'/(native_tag(tag)+suffix))
 for tag in MUTATION_TAGS:
  log=D/(native_tag(tag)+'.json');absent(log);absent(log.with_name(log.stem+'-journal'))
  for name in ([ASSEMBLER]if tag=='assembler-constant'else SELECTORS):absent(log.with_name(log.stem+'.before-'+Path(name).name))
 return frozen,old_reports,before,expected

class Orchestrator:
 def __init__(self,frozen,old_reports,before,expected,summary_handle,trace_handle):
  self.frozen=frozen;self.old_reports=old_reports;self.before=before;self.expected=expected
  self.summary_handle=summary_handle;self.trace_handle=trace_handle
  self.state={'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1122','state':'running','operator_sha256':sha(_CODE),
   'baseline':BASE,'execution_head':git('rev-parse','HEAD').decode().strip(),'canonical_sha256':AFTER,'receipt25_sha256':RECEIPT_SHA,
   'old_report_sha256':{n:sha(b)for n,b in old_reports.items()},'commands':[],'guarded_edits':[],
   'source_snapshot_regeneration':False,'scientific_approval_added':False,'supervisor_binding':None,
   'outputs':{'full':FULL,'companion':COMPANION,'reviewed':REVIEWED,'supported':SUPPORTED,'companion_review':SUCCESSOR}}
  self.save()
 def save(self):
  self.summary_handle.seek(0);self.summary_handle.truncate();self.summary_handle.write(json.dumps(self.state,indent=2)+'\n');self.summary_handle.flush()
 def event(self,value):self.trace_handle.write(json.dumps(value)+'\n');self.trace_handle.flush()
 def check(self):
  for name,raw in self.frozen.items():require(regular(Path(name)if name.startswith('/')else W/name)==raw,'frozen input drift: '+name)
  for name,raw in self.old_reports.items():require(regular(W/name)==raw,'old Step7d report overwritten: '+name)
  require(set(self.old_reports)<=current_report_files(),'old Step7d report disappeared')
  require(sha(regular(W/'mappings/ingredient_mappings.sssom.tsv'))==AFTER and sha(regular(W/MAPPING_RECEIPT))==RECEIPT_SHA,'canonical/receipt changed during refresh')
 def guarded_edit(self,tag,names):
  self.check()
  from scripts import step7a_guarded_publication as publication
  from scripts import promote_heptahydrate_ncit as guarded
  outputs={Path(n):self.expected[n]for n in names}
  inputs={(Path(n)if n.startswith('/')else W/n):b for n,b in self.frozen.items()}
  log=D/(native_tag(tag)+'.json')
  backups={log.with_name(log.stem+'.before-'+Path(n).name):self.before[n]for n in names}
  result={'phase':'post1122-'+tag,'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1122',
   'approval':'NONE: exact endpoint/companion selector synchronization only','scientific_approval_added':False,'supervisor_binding':None,
   'input_sha256':{str(p):sha(b)for p,b in inputs.items()},'output_sha256':{str(p):sha(b)for p,b in outputs.items()},'operator_sha256':sha(_CODE)}
  publication.publish(W,outputs,inputs,log,backups,result,apply=True,validate_scope=self.check)
  saved=json.loads(regular(log));publication.completed_journal(W,log,saved,previous={Path(n):self.before[n]for n in names})
  for name in names:
   require(regular(W/name)==self.expected[name],'written code differs from exact replacement');self.frozen[name]=self.expected[name]
  self.check();entry={'tag':native_tag(tag),'files':names,'receipt':str(log),'receipt_sha256':sha(regular(log))};self.state['guarded_edits'].append(entry);self.event(entry);self.save()
 def run(self,tag,argv):
  self.check()
  for rel in { '03-export-full':FULL,'08-companion-export':COMPANION,'09-reviewed-export':REVIEWED,'11-supported-export':SUPPORTED}.get(tag, '').split():absent(W/rel)
  command=[sys.executable,str(RUNNER),'step7d',native_tag(tag),'--','env','UV_OFFLINE=1',*argv]
  entry={'tag':native_tag(tag),'argv':argv,'runner_argv':command,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  self.state['commands'].append(entry);self.event(entry);self.save()
  process=subprocess.run(command,cwd=W,check=False)
  receipt=RUN/'logs'/(native_tag(tag)+'.json');entry['exit_code']=process.returncode
  if receipt.is_file():entry.update(receipt=str(receipt),receipt_sha256=sha(regular(receipt)))
  self.save();self.event(entry)
  require(process.returncode==0,'native command failed; preserve receipt and stop: '+tag)
  self.check()
 def finish(self):
  self.check()
  review=json.loads(regular(W/BASE_REVIEW));plan=json.loads(regular(D/'owner-plan.json'))
  selected=[d for d in review['decisions']if d.get('owner_record')in plan['owners']]
  require(len(selected)==105 and collections.Counter(d['disposition']for d in selected)=={'WITHHOLD':105},'selected row support changed')
  companion=json.loads(regular(W/COMPANION_RECEIPT))
  require(len(companion['owner_hashes_unchanged'])==20 and sum(companion['claim_counts'].values())==51 and companion['scientific_approval_added']is False,'companion counts/approval changed')
  require(regular(W/PRIOR_COPY)==self.old_reports[PRIOR],'prior companion copy differs')
  from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain
  proof=verify_mapping_chain(W);require(len(proof['receipt_paths'])==25 and proof['reviewed_sha256']==AFTER,'single25 receipt chain drift')
  # Assert final files are precisely baseline selectors with one path replacement.
  for name in SELECTORS:require(regular(W/name)==git('show',BASE+':'+name).replace(PRIOR.encode(),SUCCESSOR.encode()),'selector contains another change')
  semantic=json.loads(regular(W/SEMANTIC))
  self.state.update(state='complete',selected_rows=105,selected_dispositions={'WITHHOLD':105},companion_owners=20,
   companion_claims=companion['claim_counts'],old_step7d_report_bytes_unchanged=True,paired_selector_only=True,
   native_receipts=25,semantic_release_verdict=semantic['release_verdict'],full_qc_suite_and_final_independent_review='pending root runs',
   output_sha256={name:sha(regular(W/name))for name in [ASSEMBLER,*SELECTORS,SUCCESSOR,COMPANION_RECEIPT,PRIOR_COPY,BASE_REVIEW,SEMANTIC]})
  self.save();self.event({'state':'complete','summary':str(SUMMARY)})

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--execute',action='store_true');args=ap.parse_args()
 if not args.execute:
  print(json.dumps({'mode':'plan_only_no_writes','operator_sha256':sha(_CODE),'required_canonical':AFTER,'required_receipt25':RECEIPT_SHA,
   'guarded_edits':[{'phase':'before01','file':ASSEMBLER,'only':'REVIEWED_SOURCE '+BEFORE+' -> '+AFTER},
     {'phase':'after07-before08','files':SELECTORS,'only':PRIOR+' -> '+SUCCESSOR}],
   'commands':[{'tag':native_tag(tag),'argv':argv}for tag,argv in COMMANDS],
   'outputs':{'full':FULL,'companion':COMPANION,'reviewed':REVIEWED,'supported':SUPPORTED,'successor_review':SUCCESSOR},
   'summary':str(SUMMARY),'command_trace':str(TRACE),'no_full_qc_suite':True},indent=2));return
 sys.path[:0]=[str(W),str(W/'src')]
 from plugins.lock_manager import LockManager
 from plugins.repository_settings import RepositorySettings
 target=RepositorySettings.from_environment().get_target('mediaingredientmech');require(target.path.resolve()==W,'configured root differs');target.open()
 with LockManager().lock('mediaingredientmech','Step7d post1122 native dependency refresh'):
  frozen,old_reports,before,expected=preflight()
  # Hold exclusive fresh external receipts before any maintained changes.
  with SUMMARY.open('x')as summary,TRACE.open('x')as trace:
   orchestration=Orchestrator(frozen,old_reports,before,expected,summary,trace)
   try:
    orchestration.guarded_edit('assembler-constant',[ASSEMBLER])
    for tag,argv in COMMANDS:
     if tag=='07-companion-refresh':
      (W/REPORT/'refresh-v2').mkdir(mode=0o700)
      for name in [SUCCESSOR,COMPANION_RECEIPT,PRIOR_COPY]:absent(W/name)
     if tag=='08-companion-export':orchestration.guarded_edit('paired-selectors',list(SELECTORS))
     orchestration.run(tag,argv)
    orchestration.finish()
   except Exception as error:
    orchestration.state.update(state='failed',error=str(error),stop='First failure; no automatic retry, cleanup, overwrite or rollback. Preserve native receipts/journals.')
    orchestration.save();orchestration.event({'state':'failed','error':str(error)});raise
 print(json.dumps({'state':'complete','summary':str(SUMMARY),'summary_sha256':sha(regular(SUMMARY))},indent=2))
if __name__=='__main__':main()
