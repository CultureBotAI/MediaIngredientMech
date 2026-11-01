"""Read-only source-ledger and stale-export review of MIM #1025."""
from datetime import datetime, timezone
import csv, hashlib, importlib.util, json, re, subprocess
from pathlib import Path
import yaml
root=Path.cwd(); run=root.parent; out=run/'step1-independent'
path=root/'mappings/unified_mapping_rejections.tsv'
raw=path.read_bytes(); prior=subprocess.check_output(['git','show','HEAD:mappings/unified_mapping_rejections.tsv'])
assert raw.startswith(prior)
rows=list(csv.DictReader(raw.decode().splitlines(),delimiter='\t')); prior_rows=list(csv.DictReader(prior.decode().splitlines(),delimiter='\t'))
held=[row for row in rows if not row['mim_id']]
expected=json.loads((out/'proposed-source-holds.json').read_text())['rows']
assert len(rows)==90 and len(prior_rows)==57 and len(held)==33
assert {(r['ingredient_name'],r['rejected_id']) for r in held}=={(r['ingredient_name'],r['rejected_id']) for r in expected}
cm=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech')
source_checks=[]
for row in held:
    match=re.search(r'https://github.com/CultureBotAI/CultureMech/blob/([0-9a-f]{40})/(\S+) \((\$[^;]+); sha256 ([0-9a-f]{64})\)',row['reason'])
    assert match, row
    revision,relative,selector,digest=match.groups()
    contents=(cm/relative).read_bytes()
    assert hashlib.sha256(contents).hexdigest()==digest,relative
    assert subprocess.check_output(['git','show',f'{revision}:{relative}'],cwd=cm)==contents,relative
    node=yaml.safe_load(contents)
    for key,idx in re.findall(r'\.([A-Za-z_][A-Za-z_0-9]*)|\[(\d+)\]',selector):
        node=node[key] if key else node[int(idx)]
    assert node['preferred_term']==row['ingredient_name'],(selector,row['ingredient_name'],node)
    assert node['term']['id']==row['rejected_id'],(selector,row['rejected_id'],node)
    source_checks.append({'label':row['ingredient_name'],'source':relative,'selector':selector,'source_commit':revision,'sha256':digest,'label_and_id_match':True})
spec=importlib.util.spec_from_file_location('independent_mim_hold_gate',root/'scripts/check_unified_rejections.py'); gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
old_snapshot=run/'step1-evidence/unified-candidate.tsv'
problems=gate.check(old_snapshot,path)
assert problems
for row in held:
    assert any(f": {row['ingredient_name']} republishes rejected " in item for item in problems),row
result={'checked_at':datetime.now(timezone.utc).isoformat(),'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'source_state':'working_tree','input_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,root/'scripts/check_unified_rejections.py',root/'tests/test_unified_source_holds.py',root/'docs/UNIFIED_MAPPING_REJECTIONS.md']},'old_snapshot_sha256':hashlib.sha256(old_snapshot.read_bytes()).hexdigest(),'prior_rows_preserved_as_exact_prefix':len(prior_rows),'added_source_holds':len(held),'source_selectors_verified':len(source_checks),'stale_snapshot_rejection_messages':len(problems),'held_labels_caught_in_stale_snapshot':len(held),'source_checks':source_checks,'stale_snapshot_problems':problems}
(out/'mim-source-hold-probe.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('source_checks','stale_snapshot_problems')},indent=2))
