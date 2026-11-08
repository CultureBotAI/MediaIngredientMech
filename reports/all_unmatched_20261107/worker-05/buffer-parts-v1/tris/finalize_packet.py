from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1/tris';B=W/'reports/all_unmatched_20261107/worker-05';T=W.parents[2]/'preflight/buffer-source-parts-triage-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
obj=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
j=lambda p:json.loads(p.read_text())
def bind(p):return dict(path=str(p.relative_to(W)) if p.is_relative_to(W) else str(p),sha256=sha(p))
def put(p,x):
 assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
at=datetime.now(timezone.utc).isoformat();science=j(S/'source-assessment.json');sources=j(S/'occurrence-routes.json')['frozen_sources'];D=j(S/'decisions.json')['decisions'][0];PS=j(S/'proposals.json')['proposals'];add=j(S/'evidence.json')['evidence']
assert j(S/'validation/strict-receipt.json')['exit_code']==0
put(S/'local-wrapper-diagnostic.json',dict(at=at,author='/root/buffer_tris',first_attempt='functions.exec JavaScript string parse error before tool execution; no filesystem writes or science affected.',second_attempt='build_packet.py finished captures, source assessment, D/P/E and successful validation, then relative_to(W) failed while indexing two external coordinator files.',disposition='Preserve original helper and its complete scientific outputs. Finalizer writes missing read ledger/summary/handoff/manifest only, using explicit absolute paths for external inputs. No science or payload change; not a curation finding.'))
ledger=[]
for p in [W/'MAPPING_SEMANTICS.md',W/'.claude/skills/add-media/SKILL.md',W/'.claude/skills/curate-yaml-record/SKILL.md',W/'.claude/skills/curate-yaml-record/references/review-checklist.md',W/'src/mediaingredientmech/schema/mediaingredientmech.yaml',W/'src/mediaingredientmech/validation/write_validated.py',B/'final-correction-v1/chemicals/new-tris-components-finding-v1.json',T/'ASSESSMENT.json',T/'new-tris-components-finding-v1.json']:
 ledger.append(dict(**bind(p),scope='Applicable contract or complete finding/assessment inspected; native schema validation performed.'))
for p in sorted((S/'captures').glob('*')):ledger.append(dict(**bind(p),scope='Tris primary source complete text and JCM raw HTML read; NBRC source text context-only. PDF bytes integrity checked against original capture/extraction.'))
for p in sorted((S/'selected-payloads').glob('*')):ledger.append(dict(**bind(p),scope='Complete current selected payload read; no fields changed.'))
for p in sorted((S/'historical-before').glob('*')):ledger.append(dict(**bind(p),scope='Historical before payload parsed and compared, unsupported component/assertion objects read in complete original finding; preserved original history.'))
put(S/'source-read-ledger.json',dict(at=at,scientist='/root/buffer_tris',reads=ledger,frozen_recipe_contexts=sources,capture_acquisition_times=j(S/'inputs/primary-capture-index.json'),scope='Scientific source applicability and current complete-payload assessment; counts imply no admission or release.'))
summary=dict(at=at,author='/root/buffer_tris',status='READY_FOR_INDEPENDENT_REVIEW',base='0bac12cabfd1f67f212631d8eef9aa46379f6b41',selected=dict(decisions=bind(S/'decisions.json'),proposals=bind(S/'proposals.json'),evidence=bind(S/'evidence.json')),case_reviews=[dict(case_id=D['case_id'],selected_decision_object_sha256=obj(D),assessment=science['conclusion'])],payload_reviews=[dict(proposal_id=p['proposal_id'],after_capture=p['after_capture'],selected_proposal_object_sha256=obj(p),assessment='Full retained source-defined Tris stock payload already omits unsupported components and paired assertion. Whole-stock specification, original history and claim-specific LLM provenance remain byte-identical.') for p in PS],changed_payloads=0,changed_proposal_objects=0,changed_decisions=1,additive_evidence=len(add),guarded_validation='PASS',strict_validation='PASS',new_findings=[],chronology=bind(S/'chronology.json'))
put(S/'summary.json',summary)
put(S/'HANDOFF.json',dict(at=at,author='/root/buffer_tris',completion='complete_primary_assessment',independent_review='pending_parent_skeptical_review',summary=bind(S/'summary.json'),selected=summary['selected'],scope=science['scope'],outcome='Both current selected payloads/proposal objects already correct and unchanged; one additive source-decision update with six evidence entries.',no_payload_write_or_history_event=True,chronology=bind(S/'chronology.json'),limits=science['source_and_release_limits'],new_findings=[],manifest='MANIFEST.json inventories this exact packet; root owns review and publication.'))
files=[dict(path=str(p.relative_to(S)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(S.rglob('*')) if p.is_file()]
put(S/'MANIFEST.json',dict(at=at,author='/root/buffer_tris',status='sealed_primary_packet_pending_independent_review',files=files,scope=science['scope']))
print(json.dumps(dict(status='SEALED_PRIMARY',files=len(files),manifest_sha256=sha(S/'MANIFEST.json'),handoff_sha256=sha(S/'HANDOFF.json'),summary_sha256=sha(S/'summary.json'))))
