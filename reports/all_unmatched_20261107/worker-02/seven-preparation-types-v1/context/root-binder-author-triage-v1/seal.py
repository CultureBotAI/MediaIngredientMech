from pathlib import Path
import ast
import datetime
import difflib
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
import yaml

R = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech')
C = R / '.temp/all-unmatched-20261107'
W = C / 'workers/w02/worktree'
A = W / 'reports/all_unmatched_20261107/worker-02'
P = A / 'seven-preparation-types-v1'
O = C / 'preflight/w02-binder-author-triage-v1'

def sha(b): return hashlib.sha256(b).hexdigest()
def write(path, data):
    with path.open('xb') as f: f.write(data)
def dump(path, obj): write(path, (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode())
def git(*args): return subprocess.check_output(['git', '-C', str(W), *args])

before_head = git('rev-parse', 'HEAD').decode().strip()
before_status = git('status', '--porcelain=v1')
probe = json.loads((O / 'reproduction.json').read_text())
assert before_head == probe['published_local_head']
assert (O/'live-reads/w02-remote.stdout').read_text().split()[0] == before_head
source_list = [
    'bind_review.py', 'bind_review_v2.py', 'test_review_binding.py',
    'test_review_binding_v2.py', 'build_successor_v2.py',
    'independent/scientific-review-v1.json',
    'technical/finding-actual-author-field-v1.json',
    'technical/technical-review-final-v2.json',
    'technical/binding-preservation-final-v1.json',
    'technical/binding-controls-final-run-v1.json',
    'technical/binding-controls-final-v1.log',
    'technical/binding-controls-final-v1.xml',
    'selected-v1/review-binding.json', 'selected-v2/review-binding.json',
]
copied = []
for rel in source_list:
    src = P/rel; dst = O/'snapshot/seven-preparation-types-v1'/rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = src.read_bytes(); write(dst, data)
    copied.append({'source': str(src.relative_to(W)), 'capture':str(dst.relative_to(O)), 'sha256':sha(data)})
diffs = {}
for a,b in [('bind_review.py','bind_review_v2.py'),('test_review_binding.py','test_review_binding_v2.py')]:
    text=''.join(difflib.unified_diff((P/a).read_text().splitlines(True),(P/b).read_text().splitlines(True),fromfile=a,tofile=b))
    path=O/(a+'.diff');write(path,text.encode());diffs[a]=sha(text.encode())
old_ast=ast.parse((P/'test_review_binding.py').read_text())
new_ast=ast.parse((P/'test_review_binding_v2.py').read_text())
old_tests={x.name:ast.dump(x,include_attributes=False) for x in old_ast.body if isinstance(x,ast.FunctionDef)}
new_tests={x.name:ast.dump(x,include_attributes=False) for x in new_ast.body if isinstance(x,ast.FunctionDef)}
assert all(new_tests[k]==v for k,v in old_tests.items())
new_names=sorted(set(new_tests)-set(old_tests))
assert new_names==['test_actual_current_author_field_refused']
proof=json.loads((P/'independent/scientific-review-v1.json').read_text())
props={x['proposal_id']:x for x in json.loads((P/'review-input-v1/proposals.json').read_text())['proposals']}
authors=[]
for row in proof['proposal_reviews']:
    p=props[row['proposal_id']]; capture=p['after_capture']; target=A/capture['path'];raw=target.read_bytes()
    assert sha(raw)==capture['sha256']; data=yaml.safe_load(raw);event=data['curation_history'][-1]
    assert event['curator']==row['current_correction_author']=='worker02 /root'
    assert event['llm_assisted'] is True
    authors.append({'proposal_id':p['proposal_id'],'after_capture':capture,'final_history_event':event})
dump(O/'actual-author-history-readback.json',authors)
xml=ET.parse(P/'technical/binding-controls-final-v1.xml').getroot()
suite=xml.find('testsuite') if xml.tag!='testsuite' else xml
assert suite is not None
tests=dict(suite.attrib)
assert int(tests['tests'])==29 and int(tests['failures'])==0 and int(tests['errors'])==0
new_tests_report=[x.attrib['name'] for x in suite.findall('testcase') if 'actual_current_author' in x.attrib['name']]
assert len(new_tests_report)==6
legacy_proof=json.loads((O/'published-scientific-review-v2.json').read_text())
fresh_legacy=[x for k in ['case_reviews','proposal_reviews'] for x in legacy_proof[k] if x['status']=='approve_bounded_correction']
preserved_legacy=[x for k in ['case_reviews','proposal_reviews'] for x in legacy_proof[k] if x['status']!='approve_bounded_correction']
assert len(fresh_legacy)==5 and all(x['original_authors']==['worker02 /root'] for x in fresh_legacy)
assert len(preserved_legacy)==1 and preserved_legacy[0]['status']=='preserved_unchanged_context'
dedup={}
for n in ['binder-search','actual-field-search','independence-search']:
    d=json.loads((O/'live-reads'/f'{n}.stdout').read_text())
    dedup[n]={'total_count':d['total_count'],'incomplete_results':d['incomplete_results'],'issues':[{'number':x['number'],'title':x['title']} for x in d['items']]}
assessment={
 'reviewer':'/root/step7d_independent_review',
 'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'CONFIRMED_DRAFT_GUARD_DEFECT_REPAIR_INDEPENDENTLY_REPRODUCED',
 'original_finding_id':'W02-SEVEN-TECH-ACTUAL-AUTHOR-FIELD-002',
 'source_scope':{'local_and_remote_head':before_head,'seven_preparation_paths_in_that_head':0,'earlier_published_binder_git_bytes_verified':probe['published_predecessor_bytes_verified']},
 'defect':'Seven-preparation v1 checks optional original_authors, while actual approved proof rows declare current_correction_author. Six copied case/proposal mutations (self, missing, unexpected actual author) pass.',
 'actual_effect':'The genuine proof names worker02 /root, distinct from /root/final_reviewer. All seven last history events independently match that author and are explicitly LLM-assisted. No actual false independent approval or candidate corruption is evidenced.',
 'repair':{'v2_sha256':sha((P/'bind_review_v2.py').read_bytes()),'exact_code_delta':'Require actual current_correction_author to equal the known worker02 /root author and differ from reviewer; retain all earlier checks; use fresh selected-v2 output.', 'independent_controls':probe['controls'][:16], 'old_test_function_ASTs_identical':len(old_tests),'new_test_functions':new_names,'six_author_negatives_in_actual_29_pass_XML':new_tests_report,'selected_core_hashes_identical':probe['selected_v1_v2_core_hashes_identical'],'binding_receipt_only_changed_field':probe['receipt_delta_fields']},
 'published_predecessor':{'precise_current_field_mismatch':False,'approved_rows':len(fresh_legacy),'correct_author_supplied_on_every_approved_row':True,'explicit_self_author_rejected_for_case_and_proposal':True,'related_gap':'The published filed-followups binder accepts missing or empty original_authors on a newly approved row; independently reproduced. This is related fail-open validation, not evidence the original published proof was self-authored.','preserved_context_row':{'proposal_id':preserved_legacy[0]['proposal_id'],'status':preserved_legacy[0]['status'],'fresh_whole_payload_science_approval':preserved_legacy[0]['fresh_whole_payload_science_approval']},'earlier_final_corrections_binder':'Separately checks explicit bound author routing plus row original_authors; no same field-mismatch finding established.'},
 'chronology':{'draft_finding_reported':'2026-11-08T09:23:26.739788+00:00','worker_v2_recheck_finished':'2026-11-08T09:24:37.490388+00:00','worker_v2_technical_review':'2026-11-08T09:25:20.711959+00:00','issue_status':'This private repair preceded coordinator issue filing. No issue-first claim is made; root owns any filing before final publication.'},
 'issue_recommendation':{'action':'One new bounded issue for the actual-author provenance guard; attach preserved v1 and repaired v2 evidence. Do not reopen chemistry findings or rewrite historical reports.','dedup':dedup,'related_but_distinct':[1165,1220,1247],'search_limit':'Live all-state GitHub keyword searches and direct body/comments of 1247; no exhaustive assertion that no differently-worded issue exists. Local binder searches included ignored files.','historical_code':'Keep archived historical producers immutable. Explicitly select fixed v2 for the new packet. If an older helper is reused, require nonempty known author provenance in an immutable successor before use.'},
 'limits':['Bounded technical triage and validate() counterexamples only; no binder main/publication called by this reviewer.','No new scientific approval, complete final shard acceptance, integrated owner application, release approval or CI claim.','The precise defect is unpublished at observed f0d2be8b; later worker publication requires explicit re-verification.'],
 'copied_source_inputs':copied,'source_diffs':diffs,
}
dump(O/'ASSESSMENT.json',assessment)
after_head=git('rev-parse','HEAD').decode().strip();after_status=git('status','--porcelain=v1')
assert before_head==after_head and before_status==after_status
for x in copied:assert sha((W/x['source']).read_bytes())==x['sha256']
for rel,h in probe['input_hashes'].items():assert sha((W/rel).read_bytes())==h
dump(O/'final-readback.json',{'head':after_head,'status_before':before_status.decode(),'status_after':after_status.decode(),'copied_inputs_unchanged':len(copied),'probe_input_hashes_rechecked':len(probe['input_hashes']),'worker_or_maintained_writes':False})
print(json.dumps({'assessment_sha256':sha((O/'ASSESSMENT.json').read_bytes()),'tests':tests,'copied':len(copied)},indent=2))
