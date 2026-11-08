from pathlib import Path
import json,hashlib,datetime
P=Path('.temp/all-unmatched-worker-08/issue-1201-v1').resolve()
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1201-v1';O=S/'independent/mechanics'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=(P/'test_assemble_successor.py').read_text().split('\ncontrols=[',1)[0]
fixture=P/'vitamins_mixtures/evidence-reuse-controls'
source=source.replace("FIXTURE=BASE/'assembler-controls'",'FIXTURE=Path('+repr(str(fixture))+')')
ns={'__file__':str(P/'test_assemble_successor.py')};exec(compile(source,str(P/'test_assemble_successor.py'),'exec'),ns)
setup=ns['setup'];mutate=ns['mutate_input'];module=ns['module'];write=ns['write']
controls=[]
def run(name,fn,accept=False):
 root,c=setup(name);fn(root,c)
 try:out=module.assemble(c,root)
 except AssertionError as e:
  assert not accept,(name,str(e));controls.append({'control':name,'outcome':'rejected','assertion':str(e)});return
 assert accept,name+' unexpectedly accepted'
 rows=out['evidence.json']['evidence'];assert sum(x['evidence_id']=='e0' for x in rows)==1
 assert out['assembly-provenance.json']['reused_identical_parent_evidence']==[{'group':'a','evidence_id':'e0'},{'group':'b','evidence_id':'e0'}]
 controls.append({'control':name,'outcome':'accepted','one_parent_row_retained':True,'both_reuse_events_recorded':True})
def reuse(root,c):
 for i in [0,1]:mutate(root,c,'evidence',lambda x:x.append({'evidence_id':'e0'}),i)
run('identical-parent-reuse-two-groups',reuse,True)
run('changed-parent-row',lambda r,c:mutate(r,c,'evidence',lambda x:x.append({'evidence_id':'e0','new':'unsupported'})))
run('duplicate-new-id-within-group',lambda r,c:mutate(r,c,'evidence',lambda x:x.extend([{'evidence_id':'new'},{'evidence_id':'new'}])))
def across(r,c):
 for i in [0,1]:mutate(r,c,'evidence',lambda x:x.append({'evidence_id':'new'}),i)
run('duplicate-new-id-between-groups',across)
run('collide-generated-peer-id',lambda r,c:mutate(r,c,'evidence',lambda x:x.append({'evidence_id':'w08-1201-peer-a'})))
def dup_parent(r,c):
 p=r/c['parent_inputs']['evidence']['path'];d=json.loads(p.read_text());d['evidence'].append({'evidence_id':'e0'});c['parent_inputs']['evidence']['sha256']=write(p,d)
run('duplicate-parent-index-ids',dup_parent)
parent={x['evidence_id']:x for x in json.loads((R/'evidence.json').read_text())['evidence']};combined=json.loads((S/'evidence.json').read_text())['evidence'];by={x['evidence_id']:x for x in combined};prov=json.loads((S/'assembly-provenance.json').read_text());events=prov['reused_identical_parent_evidence'];assert all(by[x['evidence_id']]==parent[x['evidence_id']] for x in events);assert len(combined)==len(by)
report={'reviewer':'/root/vitamins','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Immutable assembler evidence-reuse mechanism supplement; no source science approval.','helper_sha256':sha(P/'assemble_successor.py'),'controls':controls,'positive_controls':1,'negative_controls':5,'actual_assembly':{'input_hashes':{str(p.relative_to(R)):sha(p) for p in [R/'evidence.json',S/'evidence.json',S/'assembly-provenance.json']},'reused_identical_parent_rows':len(events),'combined_rows':len(combined),'all_reused_rows_exactly_equal_parent':True,'all_combined_evidence_ids_unique':True},'source_inspection':'The exception is restricted to IDs present in the frozen parent index and requires whole-object equality. Every reuse is recorded. All other ID collisions still reach the final uniqueness assertion. Parent duplicate IDs are separately rejected.','test_harness_note':'The old generic duplicate_evidence fixture appends identical e0 and is now a positive reuse case; do not report that stale expected-rejection fixture as still passing. This supplement explicitly tests changed-parent and non-parent duplicate rejection instead.','trust_boundary':'Peer receipt contents still require the root semantic verification described in the original mechanics receipt. Evidence identity/equality is accounting, not scientific correctness.','control_script_sha256':sha(Path(__file__))}
f=O/'evidence-reuse-review-vitamins-v1.json';assert not f.exists();f.write_text(json.dumps(report,indent=2)+'\n');copy=O/'evidence_reuse_controls.py';assert not copy.exists();copy.write_bytes(Path(__file__).read_bytes());print(f,sha(f))
