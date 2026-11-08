"""Independently verify final report transport, without modifying any inputs."""
import collections
import copy
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

D=Path('reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1')
R=D/'reviews/skeptical'
A=D.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p),'sha256':sha(p)}
read=lambda p:json.loads(p.read_text())
head='26445f23b5a905ac26d864acfbd658570c88769c'
checks=[]
def check(name,condition,detail=None):
    assert condition,(name,detail)
    checks.append({'check':name,'pass':True,'detail':detail})
pre={k:read(D/'cores/pre-review'/f'{k}.json') for k in ['SELECTION','decisions','proposals','evidence']}
fin={k:read(D/'cores/final'/f'{k}.json') for k in pre}
reviewid='W01-SUCCESSOR-INDEPENDENT-REVIEW'
for key in ['decisions','proposals']:
    x=copy.deepcopy(fin[key]);old=pre[key]
    for before,after in zip(old[key],x[key]):
        check(key+' evidence append',after['evidence_ids']==before['evidence_ids']+[reviewid])
        after['evidence_ids']=before['evidence_ids']
        if key=='decisions':
            check('independent review complete binding',after['independent_review']=={'status':'complete','evidence_ids':[reviewid]})
            after['independent_review']=before['independent_review']
        else:
            check('proposal review status',after['successor_review_status']=='complete')
            after['successor_review_status']=before['successor_review_status']
    check('full '+key+' only reviewed metadata change',x==old)
ev=fin['evidence']['evidence'];pe=pre['evidence']['evidence']
check('all1122 pre-review evidence retained',ev[:-1]==pe and len(ev)==1123)
check('only independent native review added',ev[-1]['evidence_id']==reviewid and ev[-1]['capture']=={'root':'artifact','path':'successor-1226-1237-v1/reviews/skeptical/review-v1.yaml','sha256':sha(R/'review-v1.yaml')})
check('evidence top-level metadata unchanged',{k:v for k,v in fin['evidence'].items() if k!='evidence'}=={k:v for k,v in pre['evidence'].items() if k!='evidence'})
sel=fin['SELECTION'];psel=pre['SELECTION']
check('exact selected entries unchanged',sel['selected_entries']==psel['selected_entries'])
check('exact case bindings unchanged',sel['case_bindings']==psel['case_bindings'])
for k in set(psel)-{'created_at','stage','core_paths'}:check('selection invariant '+k,sel[k]==psel[k])
check('final stage',sel['stage']=='final')
for k,v in sel['core_paths'].items():check('selection core '+k,sha(A/v['path'])==v['sha256'])
for row in sel['selected_entries']:
    for key in ['old_capture','selected_capture']:
        v=row[key];check('payload '+row['proposal_id']+' '+key,sha(A/v['path'])==v['sha256'])
check('selection totals',len(sel['selected_entries'])==76 and len(sel['case_bindings'])==188)

h=read(D/'HANDOFF.json');hrefs=[]
def walk(v):
    if isinstance(v,dict):
        if set(['path','sha256'])<=set(v):
            p=D/v['path'];check('handoff exact hash '+v['path'],p.is_file() and sha(p)==v['sha256']);hrefs.append(bind(p))
        for n in v.values():walk(n)
    elif isinstance(v,list):
        for n in v:walk(n)
walk(h)
counts=h['counts'];check('handoff188/76/66/10',counts['cases']==188 and counts['proposals']==76 and counts['changed_payloads']==66 and counts['byte_identical_payloads']==10)
check('handoff dispositions',dict(collections.Counter(r['disposition'] for r in fin['decisions']['decisions']))==h['case_dispositions'])
check('handoff four science and closed76 typing',counts['science_payloads']==4 and counts['typing_only_payloads']==62 and counts['typing_entries']==76 and counts['science_typing_entries']==5 and counts['typing_only_entries']==71)
req=read(D/'remaining-requirements-v1.json');decs=fin['decisions']['decisions'];props=fin['proposals']['proposals'];di={r['case_id']:r for r in decs};pi={r['proposal_id']:r for r in props}
check('requirement104 precise records',len(req['case_requirements'])==104 and set(x['case_id'] for x in req['case_requirements'])=={x['case_id'] for x in decs if x.get('missing_requirement')})
for row in req['case_requirements']:
    c=di[row['case_id']]
    for k in ['source','proposal_ids','disposition','missing_requirement']:check('requirement full field '+k,row[k]==c[k])
check('all76 obligations retained',len(req['proposal_integration_obligations'])==76 and len({x['proposal_id'] for x in req['proposal_integration_obligations']})==76)
for row in req['proposal_integration_obligations']:
    p=pi[row['proposal_id']]
    for k in ['integration_obligations','integration_requirements','depends_on_proposals']:check('obligation field '+k,row[k]==p.get(k, [] if k=='depends_on_proposals' else None))
check('requirements bind actual precores',req['source_decisions_sha256']==sha(D/'cores/pre-review/decisions.json') and req['source_proposals_sha256']==sha(D/'cores/pre-review/proposals.json'))

native=read(R/'native-inspect-v2.json')
for item in native['source']['inputs']:check('native input preserved '+item['path'],sha(Path(item['path']))==item['sha256'])
prior=read(D/'checks/preservation-before-seal-v1.json')
for item in prior['predecessor_inputs']:check('original source preserved '+item['path'],sha(Path(item['path']))==item['sha256'])
packets=[]
for row in prior['preserved_private_packets']:
    p=Path(row['path']);check('prior manifest preserved '+str(p),sha(p)==row['sha256']);m=read(p);members=m.get('files',[]);links=m.get('symlinks',[])
    for item in members:check('prior immutable member '+str(p.parent/item['path']),sha(p.parent/item['path'])==item['sha256'])
    for item in links:
        link=p.parent/item['path'];check('prior symlink preserved '+str(link),link.is_symlink() and os.readlink(link)==item['target'] and hashlib.sha256(os.readlink(link).encode()).hexdigest()==item['target_sha256'])
    packets.append({'manifest':bind(p),'members_rechecked':len(members),'symlinks_rechecked_without_traversal':len(links)})

commands=[]
for cmd in [['git','rev-parse','HEAD'],['git','branch','--show-current'],['git','diff','--name-only','HEAD','--'],['git','status','--short']]:
    p=subprocess.run(cmd,capture_output=True,text=True);commands.append({'argv':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});check('read-only Git command',p.returncode==0)
check('same source head',commands[0]['stdout'].strip()==head)
check('same assigned branch',commands[1]['stdout'].strip()==h['branch'])
check('no existing tracked changes',commands[2]['stdout']=='')
check('no visible staged or untracked changes',commands[3]['stdout']=='','New report subtree is ignored and independently inventoried; this does not claim a global ignored-file inventory.')
inventory=[]
for p in sorted(D.rglob('*')):
    check('no successor symlink '+str(p),not p.is_symlink())
    if p.is_file():inventory.append({'path':str(p.relative_to(D)),'sha256':sha(p),'bytes':p.stat().st_size})

out={'schema_version':1,'reviewer':'OpenAI Codex /root/skeptical_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verdict':'pass_with_limitations','scope':'Final immutable pre-review→final assembly transport and whole successor report inventory; no renewed scientific scope or candidate edits. The report renders absent depends_on_proposals as an empty list; actual core objects are compared without normalizing them.','complete_scoped_assembly_review':True,'source_head':head,'final_selection':bind(D/'cores/final/SELECTION.json'),'final_cores':{k:bind(D/'cores/final'/f'{k}.json') for k in ['decisions','proposals','evidence']},'handoff_json':bind(D/'HANDOFF.json'),'handoff_markdown':bind(D/'HANDOFF.md'),'scoped_scientific_review':bind(R/'final-successor-review-v1.json'),'native_review':bind(R/'review-v1.yaml'),'native_markdown':bind(R/'review-v1.md'),'native_completion':bind(R/'native-review-completion-v1.json'),'remaining_requirements':bind(D/'remaining-requirements-v1.json'),'checks_passed':len(checks),'checks':checks,'handoff_reference_bindings':hrefs,'source_preservation':{'predecessor_cores_and_payloads':len(prior['predecessor_inputs']),'native_inputs':len(native['source']['inputs']),'prior_packets':packets},'git_observation':commands,'final_metadata_changes':{'decisions':'Only exact independent-review status and appended evidence ID across188 rows.','proposals':'Only successor_review_status and appended evidence ID across76 rows.','evidence':'All1122 pre-review entries preserved, one exact native independent-review capture appended,1123 total.','selection':'Exact76 selected entries and188 case bindings unchanged; stage, timestamps and core paths updated.'},'synthesis_assessment':['HANDOFF JSON/Markdown faithfully preserve4 scientific versus62 provenance-only scopes,10 unchanged payloads, full188/76 accounting and actual author/reviewer identities.','One per-string Fe name correction and individually retained bicarbonate pointer negatives are represented accurately; original negative lineage is preserved.','Se/W supplied-form uncertainty remains; no source-number or missing-hydrate inference of equality/disjointness is restored. Case110 historical workflow category remains qualified.','104 inherited requirement texts and76 integration obligations are preserved separately; they are not all recategorized as fresh scientific barriers.','Root native schema76, complete partonomy and83-row projection results are scoped and attributed, not claimed as independent science approval.','Failed helper attempts and focused-check limitations remain available; no full suite or new-head green CI is claimed.'],'new_findings':[],'inventory_before_outer_seal':inventory,'inventory_exclusions':['This final-assembly-review-v1.json (not yet created when inventory was hashed).','Future outer MANIFEST.json (must include this receipt and cannot hash itself).'],'script':bind(Path(__file__)),'limits':['No whole-owner/role/maintained installation/canonical export/release approval.','No campaign-wide issue1226/1237 closure, coordinator37-candidate rewrite or new research scope.','This check binds precommit working-tree bytes. Root must stage exactly this packet, create its outer seal and publish through ordinary commit/push; final pushed-head equivalence remains a separate tool-only check.','Independent final-assembly helper v1 failed on absent dependency field versus rendered empty-list default; v2 checks only that documented report default. No payload/core/report input was changed.','No new source/Git/GitHub mutation by this reviewer. Read-only initial attempt at checks/remaining-requirements-v1.json failed because the actual report is at D root; ignored-inclusive path discovery located and verified the correct file.','Task output-path override uses native inspect/validate/render under D, not fixed-path saver registration.'],'whole_owner_approval':False,'release_approval':False}
with (R/'final-assembly-review-v1.json').open('x') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'path':str(R/'final-assembly-review-v1.json'),'sha256':sha(R/'final-assembly-review-v1.json'),'checks_passed':len(checks),'inventoried_files':len(inventory),'prior_file_members_rechecked':sum(x['members_rechecked'] for x in packets)}))
