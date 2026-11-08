"""Independent input binding; does not author or rewrite successor candidates."""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import json, hashlib, re, subprocess, datetime, yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
CAMPAIGN = ROOT.parents[2]
PLAN = CAMPAIGN/'preflight/w01-w09-author-task-planning-v1'
AUDIT = CAMPAIGN/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
canon = lambda v: hashlib.sha256(json.dumps(v, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
read = lambda p: json.loads(p.read_text())

def save(name, value):
    with (OUT/name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

allow = read(PLAN/'w09-eight-entry-allowlist.json')
excepted = read(PLAN/'w09-preserved-historical-exception.json')['rows'][0]
binding = next(w for w in read(PLAN/'current-worker-bindings.json')['workers'] if w['worker'] == 9)
assert sha(PLAN/'w09-author-task-DRAFT.md') == '5b52e6967ef232e3507b8425934c43127549728ce0170d1d621ac5b4d5977fe7'
assert sha(AUDIT/'provenance/entry-provenance-ledger-v1.json') == '98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2'
assert sha(AUDIT/'provenance/native-type-suggestions-v1.json') == '9ca6b04f03fdaabd65dacd90a160cf9f51dc549e607b5f5634616469532f1b33'
audit_rows = {r['flag_index']:r for r in read(AUDIT/'provenance/entry-provenance-ledger-v1.json')['rows']}
current_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
assert current_head == binding['head'] == '77d6beaea5793a0a763957b99e8141ff12b216d2'
selection = []
for r in binding['all_selected_payloads']:
    path = Path(r['path'])
    assert sha(path) == r['sha256']
    raw_at_head = subprocess.check_output(['git', 'show', current_head+':'+str(path.relative_to(ROOT))], cwd=ROOT)
    assert raw_at_head == path.read_bytes()
    selection.append({'entry_id':r['entry_id'], 'path':str(path), 'sha256':sha(path), 'head_blob_equal':True})
assert len(selection) == 32 and len({r['entry_id'] for r in selection}) == 32
effective = Path(binding['effective_decisions']['path'])
assert sha(effective) == binding['effective_decisions']['sha256']
decisions = read(effective)
case_rows = decisions['decisions'] if isinstance(decisions,dict) else decisions
assert len(case_rows) == 187 and len({r['case_id'] for r in case_rows}) == 187
records = []
for row in allow['rows']:
    path = Path(row['current_payload_path'])
    data = yaml.safe_load(path.read_text())
    i = int(re.fullmatch(r'ontology_mapping\.evidence\[(\d+)\]', row['field']).group(1))
    value = data['ontology_mapping']['evidence'][i]
    assert sha(path) == row['payload_sha256']
    assert value == row['full_value'] and canon(value) == row['full_value_sha256']
    assert value['evidence_type'] == 'MANUAL_CURATION'
    audit = audit_rows[row['flag_index']]
    for key in ['full_value','full_value_sha256','payload_sha256','classification','claim_specific_type_basis','human_review_provenance']:
        assert audit[key] == row[key], (row['flag_index'], key)
    assert row['suggested_native_type'] == 'LLM_SUGGESTION'
    for h in row['author_evidence']['added_curation_history']:
        assert h in data['curation_history']
    records.append({'proposal_id':row['proposal_id'], 'flag_index':row['flag_index'], 'field':row['field'],
                    'path':str(path), 'sha256':sha(path), 'full_record':data,
                    'mapping_context_sha256':canon(data['ontology_mapping']),
                    'full_value_sha256':canon(value), 'full_history_sha256':canon(data['curation_history']),
                    'all_top_level_fields':{k:canon(v) for k,v in data.items()},
                    'authorship':row['author_evidence'], 'claim_typing_basis':row['claim_specific_type_basis']})
assert len(records) == 8 and len({r['proposal_id'] for r in records}) == 8
casamino = next(r['full_record'] for r in records if r['proposal_id'] == 'ma-casamino-distinct')
old_object = casamino['ontology_mapping']['evidence'][1]
assert old_object == excepted['full_value'] and canon(old_object) == '172fc3c050e5737dfc774001fa18e3263d7c33242119f5a00aec64fc2fd915c9'
basepath = Path(excepted['baseline_path'])
assert sha(basepath) == excepted['baseline_sha256']
baseline = yaml.safe_load(basepath.read_text())
historical = baseline['ontology_mapping']['evidence'][1]
assert historical == excepted['claim_specific_type_basis']['inherited_baseline_value']
assert old_object['notes'] == excepted['claim_specific_type_basis']['added_prefix']+historical['notes']
contracts = ['AGENTS.md','MAPPING_SEMANTICS.md','docs/record-reviews.md','docs/record-review-profile.md',
             '.claude/skills/review-yaml-record/SKILL.md','src/mediaingredientmech/schema/mediaingredientmech.yaml',
             'scripts/record_review.py','schema/record_review.yaml']
save('baseline-inspection.json', {'reviewer':'Codex /root/provenance1226_reviewer',
     'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'head':current_head, 'scope':'Independent provenance-only successor review; no science, role or export renewal.',
     'scientific_review':False,'status':'PASS','selection':selection,'records':records,
     'effective_decisions_path':str(effective),'effective_decisions_sha256':sha(effective),
     'case_bindings':[{'case_id':r['case_id'],'full_row_sha256':canon(r)} for r in case_rows],
     'exception':{'full_value':old_object,'full_value_sha256':canon(old_object),'baseline_path':str(basepath),
                  'baseline_sha256':sha(basepath),'inherited_assertion':historical,'inherited_assertion_sha256':canon(historical),
                  'verdict':'Preserve full historical wrapper. Agent-authored wrapper does not establish authorship of the inherited assertion.'},
     'input_hashes':[{ 'path':str(f),'sha256':sha(f)} for f in [PLAN/'w09-author-task-DRAFT.md',PLAN/'w09-eight-entry-allowlist.json',PLAN/'w09-preserved-historical-exception.json',PLAN/'current-worker-bindings.json',AUDIT/'provenance/entry-provenance-ledger-v1.json',AUDIT/'provenance/native-type-suggestions-v1.json']]+[{'path':str(ROOT/f),'sha256':sha(ROOT/f)} for f in contracts]})
print(json.dumps({'status':'PASS','cases':len(case_rows),'selection':len(selection),'changed_scope':len(records)}))
