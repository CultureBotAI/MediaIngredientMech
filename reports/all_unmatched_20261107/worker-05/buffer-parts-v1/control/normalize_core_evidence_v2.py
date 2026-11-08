from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,copy
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';P=W/'reports/all_unmatched_20261107/worker-05/buffer-parts-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text());at=datetime.now(timezone.utc).isoformat()
old=j(P/'core/evidence.json');allowed={'primary_source','source_snapshot','ontology','native_record_review','independent_review','unsuccessful_search','local_validation'};bad=[x for x in old['evidence'] if x['kind'] not in allowed];assert len(bad)==4
f=S/'control/evidence-kind-finding-before-fix.json';assert not f.exists();f.write_text(json.dumps(dict(finding_id='W05-ASSEMBLY-EVIDENCE-003',at=at,reporter='/root',status='confirmed_before_fix',reproduction=dict(core_evidence_sha256=sha(P/'core/evidence.json'),audit_receipt_sha256=sha(P/'validation/final-structural-audit.receipt.json'),audit_stderr_sha256=sha(P/'validation/final-structural-audit.stderr.log')),entries=bad,bounded_fix='Classify four new captured author/context/beforeimage documents as campaign source_snapshot; preserve original_kind/author/capture/claim and all sealed source fragments. No MappingEvidence, primary source, scientific proposal, validator or gate changes.'),indent=2)+'\n')
shutil.copytree(P/'core',P/'control/pre-evidence-envelope-core');V=P/'validation/accounting-attempt-v1';V.mkdir()
for n in ['final-structural-audit.receipt.json','final-structural-audit.stdout.log','final-structural-audit.stderr.log']:shutil.move(P/'validation'/n,V/n)
new=copy.deepcopy(old);changes=[]
for row in new['evidence']:
 if row['kind'] not in allowed:
  before=copy.deepcopy(row);row['original_campaign_kind']=row['kind'];row['kind']='source_snapshot';changes.append(dict(evidence_id=row['evidence_id'],before=before,after=copy.deepcopy(row),scope='Canonical campaign evidence envelope classification only; exact source fragment remains immutable with its authentic author and original type.'))
assert new['evidence'][:1627]==old['evidence'][:1627]
receipt=dict(at=at,compiler='/root',finding_id='W05-ASSEMBLY-EVIDENCE-003',predecessor_evidence=dict(path='control/pre-evidence-envelope-core/evidence.json',sha256=sha(P/'control/pre-evidence-envelope-core/evidence.json')),changes=changes,unchanged_payloads=True,unchanged_case_decisions=True,unchanged_captures_authors_claims=True,no_MappingEvidence_or_ComponentEvidence_changes=True,no_validator_or_gate_change=True)
q=P/'control/evidence-envelope-adaptation.json';assert not q.exists();q.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n');(P/'core/evidence.json').write_text(json.dumps(new,indent=2,ensure_ascii=False)+'\n')
a=j(P/'core/assembly-receipt.json');a['evidence_envelope_adaptation']=dict(path='control/evidence-envelope-adaptation.json',sha256=sha(q),scope='Four new campaign envelope kind corrections; exact source bytes and science unchanged. Separate exact review required.');(P/'core/assembly-receipt.json').write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(changed_entries=len(changes),evidence_sha256=sha(P/'core/evidence.json'),adaptation_sha256=sha(q))))
