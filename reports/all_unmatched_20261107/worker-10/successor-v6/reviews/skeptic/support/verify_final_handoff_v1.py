from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
R=Path.cwd();A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6';P=R/'.temp/all-unmatched-worker-10/successor-v6/skeptic';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def js(p):return json.loads(p.read_text())
def check(n,v):checks.append({'check':n,'pass':bool(v)})
def cap(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
def refs(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x and isinstance(x['path'],str):
   base=R if x['path'].startswith(('reports/','reviews/')) else A
   check('exact handoff reference '+x['path'],sha(base/x['path'])==x['sha256'])
  for v in x.values():refs(v)
 elif isinstance(x,list):
  for v in x:refs(v)
h=js(S/'HANDOFF.json');md=(S/'HANDOFF.md').read_text();scopes=js(S/'subagent-scopes.json');v=js(P/'final-core-native-verification-v1.json')
check('exact announced handoff JSON',sha(S/'HANDOFF.json')=='c8e087b45b6123b364fb6c63a90d7770a19d62e9e166ad12142ada16c2a2208e')
check('exact announced handoff Markdown',sha(S/'HANDOFF.md')=='b2ef1362ee6a0c04c4b36df4be21c8f89ead5fb4c91096dbc6c083286253ebac')
refs(h);refs(scopes)
for x in v['bindings']:check('unchanged exact prior assembly input '+x['path'],sha(R/x['path'])==x['sha256'])
science=js(S/'reviews/skeptic/scientific-review-v1.json');rows={x['proposal_id']:x for x in science['payload_assessments']}
check('handoff all five exact scientific bindings',len(h['changed_payloads'])==5 and {x['proposal_id'] for x in h['changed_payloads']}==set(rows))
for x in h['changed_payloads']:
 check('handoff final payload '+x['proposal_id'],x['after']['sha256']==rows[x['proposal_id']]['after']['sha256'] and x['before']['sha256']==rows[x['proposal_id']]['before']['sha256'])
check('exact accounting repeated',h['accounting']==js(S/'accounting.json'))
check('exact native pair repeated',h['native_review']==js(S/'native/saved-pair.json'))
cmd=js(S/'native-check-command.json');stdout=js(S/'native-check.stdout');stderr=(S/'native-check.stderr').read_text()
check('full native check actual exit0',cmd['exit_code']==0)
check('full native check exact base and command',cmd['argv']==['.temp/all-unmatched-worker-10/venv/bin/python','scripts/record_review.py','check','--base','3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b','--require-reviews'])
check('full native check actual complete timing',datetime.fromisoformat(cmd['finished_at'])>datetime.fromisoformat(cmd['started_at']))
check('full native1028 declared scopes only',stdout=={'repository':'CultureBotAI/MediaIngredientMech','valid_reviews':1028,'coverage':'declared_scopes_only'} and h['native_complete_review_check']==stdout)
check('exact harmless deprecation warning only',stderr=='topClass is deprecated - use top_class\n')
audit=js(S/'structural-audit.json')
check('structural audit actual PASS188/127',audit['structural_accounting']=='PASS' and audit['accounted_case_count']==188 and audit['proposal_count']==127 and audit['scientific_adequacy_or_approval_established'] is False)
check('original finding IDs preserved',h['original_finding_ids']==['W09-W10-SKEPTIC-DIFCO-COMPONENT-METHOD','W09-W10-SKEPTIC-COMPONENT-CLOSURE'])
check('no whole owner approval',h['maintained_application_or_export_approval'] is False and scopes['owner_or_export_approval'] is False)
check('scope root author versus independent scientist','/root' in scopes['author']['identity'] and '/root/preparation_skeptic' in scopes['independent_science']['identity'] and 'prior review involvement' in scopes['independent_science']['scope'])
check('original HCl authorship disclosed for retention only','Authored the original four S1 HCl proposals' in scopes['independent_retention']['scope'] and 'not an independent HCl science claim' in scopes['independent_retention']['scope'])
check('no future head approval in handoff','final exact assembly review/seal precede' in h['status'] and 'no retrospective review-head claim' in h['publication'])
check('explicit timing unknown and actual finish','earliest recorded S6 preflight milestone' in h['timing'] and 'exact earlier reading start remains unknown' in h['timing'])
check('prior S4/S5 limitations retained','not transfer blanket' in ' '.join(h['retained_limits']) and 'sealed carbonate/calf and ISP4' in ' '.join(h['retained_limits']))
check('old findings not terminally closed','No historical finding or GitHub issue is closed' in ' '.join(h['retained_limits']))
check('historical/current PARTIAL distinction','Historical HCl reassessments stay verbatim' in md and 'explicit new active bindings state UNKNOWN' in md)
for link in re.findall(r'\]\(([^)]+)\)',md):
 if not link.startswith(('https:','http:','#')):check('handoff local link '+link,(S/link.split('#')[0]).resolve().exists())
check('source HEAD unchanged',subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='3e190a0f6c5a978ca8ed7e3bc7b6a2d66935548b')
out={'at':datetime.now(timezone.utc).isoformat(),'reviewer':'OpenAI Codex /root/preparation_skeptic','scope':'Exact final handoff, completed native check and authorship/timing/limits metadata; no repeated broader scientific or future-head approval.','checks':checks,'check_count':len(checks),'failures':[x for x in checks if not x['pass']],'native_full_check':{'executed_by':'root; not rerun by skeptic','exit_code':cmd['exit_code'],'stdout':stdout,'stderr_exact':stderr},'bindings':[cap(S/x) for x in ['HANDOFF.json','HANDOFF.md','subagent-scopes.json','native-check-command.json','native-check.stdout','native-check.stderr','structural-audit.json']]}
p=P/'final-handoff-verification-v1.json'
with p.open('x') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'path':str(p),'sha256':sha(p),'checks':len(checks),'failures':out['failures']},indent=2))
