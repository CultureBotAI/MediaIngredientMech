"""Append a native timing-attribution successor; preserve all prior observations."""
from pathlib import Path
import copy, datetime, hashlib, json, subprocess, yaml
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v4';N=S/'native-v2';N.mkdir()
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
def bind(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,value):
 with p.open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
def run(label,argv):
 start=now();res=subprocess.run(argv,text=True,capture_output=True)
 for ext,value in [('stdout',res.stdout),('stderr',res.stderr)]:
  with (N/(label+'.'+ext)).open('x') as f:f.write(value)
 save(N/(label+'-command.json'),{'started_at':start,'finished_at':now(),'argv':argv,'exit_code':res.returncode})
 assert res.returncode==0,(label,res.stdout,res.stderr)
 return res
oldpair=load(S/'native/saved-pair.json');old=R/oldpair['files'][0]['path']
review=yaml.safe_load(old.read_text());original=copy.deepcopy(review)
finding=S/'reviews/retention/native-timing-finding-v1.json'
assert sha(finding)=='8d77a8b60e928622d837b8afe53dae8afed53e90433d148f24bdd6b9a54d9b6d'
science=S/'reviews/skeptic/scientific-review-v1.json';retention=S/'reviews/retention/author-core-retention-review-v1.json'
milestone=load(S/'source-assessment.json')['at']
receipt={'recorded_at':now(),'finding':bind(finding),'finding_status':'Recorded before this append-only correction','prior_native_pair':oldpair,'prior_handoff':bind(S/'HANDOFF.json'),'issue_lineage':bind(S/'issue-linked-correction.json'),'issue_url':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6719089745','original_timestamp_meaning':{'started_at':review['started_at'],'finished_at':review['finished_at'],'meaning':'Original script wrapper construction timestamps, not scientific reading duration'},'successor_started_at':milestone,'successor_start_meaning':'Earliest recorded root source-assessment milestone; reading began earlier, and exact earlier review start is unknown. This is not a recovered full review start.','independent_science':{'report':bind(science),'reviewed_at':load(science)['reviewed_at'],'exact_review_start':'Not recorded in this report; do not infer from report generation or audit timing'},'independent_retention':{'report':bind(retention),'completed_at':load(retention)['completed_at'],'actual_review_start_exact':load(retention)['actual_review_start_exact']},'successor_finish_meaning':'Actual new native observation assembly completion, recorded immediately before serialization','unchanged_science_targets_checks_assessments':True,'candidate_and_final_core_unchanged':True,'old_pair_and_handoff_preserved':True,'github_or_historical_finding_mutation':False}
save(N/'timing-correction.json',receipt)
argv=load(S/'native/inspection-command.json')['argv']
for p in [R/x['path'] for x in oldpair['files']]+[finding,N/'timing-correction.json',S/'HANDOFF.json',S/'reviews/retention/native-handoff-review-v1.json',S/'reviews/skeptic/final-assembly-review-v2.json']:
 argv+=['--input',str(p.relative_to(R))]
inspection=json.loads(run('inspection',argv).stdout);save(N/'inspection.json',inspection)
review['source']=inspection['source']
review['review_id']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-w10-carbonate-completeness-successor-v2'
review['title']+='; timing attribution successor'
review['started_at']=milestone.replace('+00:00','Z')
review['limitations']+=['Timing successor for SV4-NATIVE-TIMING-001: started_at is the earliest recorded root source-assessment milestone (source-assessment.json.at), not a recovered beginning of all review work. Reading began earlier; its exact start remains unknown. finished_at is actual completion of this new native observation assembly.','The preserved first canonical pair uses wrapper-generation timestamps 2026-11-08T08:21:53.960684Z and 2026-11-08T08:21:53.961287Z. They are not the scientific review duration. This successor clarifies attribution without changing its scientific assessment.','Independent source and retention review timing belongs to the exact reports bound in native-v2/timing-correction.json. Their report completion and execution timestamps do not establish an unknown full review interval.']
review['summary']+=' This append-only native successor clarifies timing attribution; the prior canonical pair and finding remain immutable, and scientific assessments are unchanged.'
for eid,p,summary in [('TIMING-FINDING',finding,'Independent finding recorded before correction: original wrapper timing was insufficiently attributed.'),('TIMING-CORRECTION',N/'timing-correction.json','Exact original timestamps, known root milestone, unknown earlier start and independent report timing attribution; no science change.')]:
 review['evidence'].append({'evidence_id':eid,'kind':'prior_review' if eid.endswith('FINDING') else 'record_content','reference':str(p.relative_to(R)),'accessed_at':now(),'support':'supports','locator':'Complete exact artifact','snapshot_sha256':sha(p),'summary':summary})
for key in ['targets','checks','assessments','findings','actions','scope','scientific_review','reviewer']:
 assert review[key]==original[key],key
review['finished_at']=now()
class Dumper(yaml.SafeDumper):
 def ignore_aliases(self,data):return True
with (N/'review-input.yaml').open('x') as f:f.write(yaml.dump(review,Dumper=Dumper,sort_keys=False,allow_unicode=True,width=110))
py='.temp/all-unmatched-worker-10/venv/bin/python'
run('validate',[py,'scripts/record_review.py','validate',str((N/'review-input.yaml').relative_to(R))])
run('save',[py,'scripts/record_review.py','save','--content',str((N/'review-input.yaml').relative_to(R))])
bundle=R/'reviews/structured'/review['review_id']
pair={'review_id':review['review_id'],'targets':3,'scientific_scope':'Only component completeness, unchanged from first pair; timing attribution clarified','files':[bind(bundle/n) for n in ['review.yaml','review.md']],'canonical_native_saver_run':True,'owner_role_export_approval':False,'supersedes_timing_attribution_only':oldpair['review_id'],'timing_correction':bind(N/'timing-correction.json')}
save(N/'saved-pair.json',pair);print(json.dumps(pair,indent=2))
