from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess
OUT=Path(__file__).resolve().parent
RUN=OUT.parents[1]
MIM=RUN/'step3-mim'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
writer=load(RUN/'step3-writer-evidence/stable-source.json')
writer.update(load(RUN/'step3-writer-evidence/revision-1036/stable-source.json'))
source={p:v['sha256'] for p,v in writer.items()}
source.update(load(MIM/'output/issue1004-dependency-tests/source-stable.json')['owned_files'])
assert len(source)==17
assert all(sha(MIM/p)==v for p,v in source.items())
prep=load(RUN/'step3-mim-independent/preparation/results.json')
unchanged={p:h for p,h in prep['baseline_inputs'].items() if p not in source}
assert all(sha(MIM/p)==v for p,v in unchanged.items())
protected={p:item['sha256'] for p,item in prep['protected_intel_files'].items()}
assert all(sha(MIM/p)==v for p,v in protected.items())
evidence=MIM/'reports/carnitine_hydrochloride_1004_20261101/sources'
manifest=load(evidence/'manifest.json')
assert sha(evidence/'manifest.json')==prep['source_manifest_sha256']
assert all(sha(evidence/p)==v['sha256'] and (evidence/p).stat().st_size==v['bytes'] for p,v in manifest['files'].items())
logs={}
for name in ['step3-independent-final-writer-dependency-tests','step3-independent-native-boundaries','step3-independent-unified-orchestration-recheck-v2','step3-independent-receipt-orchestration-recheck']:
 receipt=load(RUN/'logs'/f'{name}.json')
 assert receipt['exit_code']==0 and sha(Path(receipt['log']))==receipt['log_sha256']
 logs[name]=receipt
assert '176 passed' in Path(logs['step3-independent-final-writer-dependency-tests']['log']).read_text()
mutations=[]
for folder,key in [(RUN/'step3-writer-evidence/revision-1036','results'),(MIM/'output/issue1004-dependency-tests/mutations','controls')]:
 receipt=load(folder/('mutation-results.json' if key=='results' else 'receipt.json'))
 for item in receipt[key]:
  expected=item['log_sha256']
  possible=[p for p in folder.rglob('*.log') if p.stem==item['name'] or p.name=='run.log' or p.name=='pytest.log']
  matches=[p for p in possible if sha(p)==expected]
  if not matches:matches=[p for p in folder.rglob('*.log') if sha(p)==expected]
  assert matches,(item['name'],expected)
  text=matches[0].read_text()
  assert item['exit_code']==1 and 'failed' in text and 'ERROR collecting' not in text
  mutations.append({'name':item['name'],'log':str(matches[0]),'log_sha256':expected,'attribution':'author-run isolated mutation; independently hash/log checked'})
helpers={name:sha(RUN/name) for name in ['guarded_unified_carnitine.py','make_step3_receipt.py','generate_candidate.py']}
unified=load(RUN/'step3-mim-independent/orchestration-recheck/unified-probe-results.json')
receipt=load(RUN/'step3-mim-independent/orchestration-recheck/receipt-probe-results.json')
assert helpers['guarded_unified_carnitine.py']==unified['orchestration_sha256']
assert helpers['make_step3_receipt.py']==receipt['helper_sha256']
native=load(RUN/'step3-mim-independent/native-boundaries/results.json')
assert native['writer_fixed_sha256']==source['scripts/merge_carnitine_hydrochloride.py']
for p,h in native['production_before_after_identical'].items():assert sha(Path(p))==h
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=MIM,text=True).strip()
assert head==prep['base']
result={'at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_PREAPPLICATION_IMPLEMENTATION','base':head,'final_head_review':False,'production_application_reviewed':False,'scientific_or_release_approval':False,'current_findings':[],
 'source_hashes':source,'source_count':len(source),'source_evidence_manifest_sha256':sha(evidence/'manifest.json'),'source_evidence_files':{p:v['sha256'] for p,v in manifest['files'].items()},'helper_hashes':helpers,'baseline_inputs_unchanged':unchanged,'protected_intel_unchanged':protected,'checks':logs,'author_mutation_logs_independently_verified':mutations,
 'issue_dispositions':[{'issue':1036,'url':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1036','status':'fixed in reviewed source; independent original/fixed native repro'},{'issue':1037,'url':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1037','status':'fixed in reviewed unpublished orchestration; independent original/fixed native publication repro'}],
 'limitations':['No production application, complete generated candidate/canonical products, full post-application QC, final review bundle or committed feature head yet.','Native row-producer dry-run uses actual merged Claw file and real publication code with external fixtures; it is not full-corpus generation.','Unified race fixtures simulate producer/checker subprocesses, Git/settings and caller lock; publication/reservation/native transaction are real. Receipt race fixtures execute actual native maker/publisher but use a minimal synthetic historical chain, not the complete production receipt chain.','Author mutation executions are credited to authors; reviewer checked receipts/log hashes and actual failure summaries.','The 176-test runner uses pinned Claw16fd for validator environment; its SSSOM producer bytes equal merged6a (cc9c38c1d4922e6b167958daa2ce0bd2618e4c122e2de12c8af4ad13505c6c0e). Separate independent native probe explicitly imports merged6a producer.','Old empty Sigma HTML is a failed capture; successful rendered factual extract and original-source CAS caveats remain explicit.']}
(OUT/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
text=f'''Pre-application implementation review: PASS, with no remaining confirmed in-scope finding at {result['at']}. This permits root to proceed with the already-authorized guarded application using the exact reviewed bytes. It is not final-head approval, scientific mapping approval, or approval of generated products that do not exist yet.

The reviewer independently executed 176 focused tests (13 warnings, no skips), plus six native writer/receipt-binding cases. The old cc83 writer reproduced #1036 by returning an unchanged result after all three owner timestamps diverged from the completed receipt. Writer2598 rejects that state and tampered transaction/input bindings. Both valid original and repaired controls accept the exact completed execution. Actual merged Claw row generation returns the two selected survivor/NLDM claims; the native dry-run promotion preserves the canonical file and reports two changed/four removed rows. Reservation replacement, precommit ignored/nested owner collision, changed input and complete/no-op boundaries passed through the real native transaction in the focused suite.

The 17 source/test/fixture hashes, 19 primary evidence files and their frozen manifest, reviewed helper hashes, retained baseline inputs and protected Intel files are bound in receipt.json. Source proposal checks preserve all old history/evidence, record exact old free-substance chemistry in the tombstone history/preimage, preserve both rejected aliases with attribution, move only the historical 14 recipe/count pairs, and add only the two exact normalized source-label overrides. Native future 15/15 and 14/15 cohort checks avoid a permanent quota. The NLDM component reference alone changes payload; all 68 inherited component/role approvals and its mapping approval must withdraw through native paths. No Step6 equivalence or supersession bypass is introduced.

For #1037, the original run-owned unified wrapper allowed unchecked candidate replacement and an input-path addition; the original receipt helper allowed changed generated approval bytes and a competing sequence17 receipt. These were reported before root's fixes. The repaired unified wrapper passed its control and rejected five checker/publication-boundary faults; the repaired receipt helper passed its control and rejected staged receipt, chain-set and code-input drift. Canonical bytes remained unchanged on every unified refusal; the receipt helper left no new output/audit on refusal and preserved the competing chain file. These fixtures stub generation/checker/settings only where expressly documented; they do not claim complete production chain validation. generate_candidate.py received source review only; full native candidate generation remains root's next execution step.

Nine writer and six dependency mutation controls were run by the authors. This reviewer independently verified their source receipts, log hashes and assertion-failure outcomes; they are not represented as reviewer-run mutations. The independent 176-test environment intentionally retains the validator pin at Claw16fd; its SSSOM builder bytes are identical to merged6a, and the separate native row/dry-promotion probe imports the actual merged6a path explicitly.

The initial orchestration recheck invocation failed before execution because its relative path was interpreted under the runner's worktree cwd. That diagnostic log is retained; the corrected absolute-path run passed. Earlier pre-fix harness import diagnostics are retained separately and are not software findings.

Required later work remains actual guarded application, source/aggregate/generated export verification, complete mapping receipt17 replay and owner-approval withdrawal, companion refresh, full QC, truthful durable-main native review capture and exact committed-head review. The NCIT mapping remains WITHHOLD until an actual mapping review; full semantic release status must be reported as observed. Sigma evidence is the retained rendered-page field extract, not successful raw HTML; the raw CultureBotHT CSV is hash-bound local data rather than a commit-attested blob. No production data/source was edited by this reviewer.
'''
(OUT/'review.md').write_text(text)
refs=[OUT/'receipt.json',OUT/'review.md',OUT/'freeze_review.py',RUN/'step3-mim-independent/native-boundaries/probe.py',RUN/'step3-mim-independent/native-boundaries/results.json',RUN/'step3-mim-independent/orchestration-preliminary/probe_unified.py',RUN/'step3-mim-independent/orchestration-preliminary/unified-probe-results.json',RUN/'step3-mim-independent/orchestration-preliminary/probe_receipt.py',RUN/'step3-mim-independent/orchestration-preliminary/receipt-probe-results.json',RUN/'step3-mim-independent/orchestration-recheck/probe_unified.py',RUN/'step3-mim-independent/orchestration-recheck/unified-probe-results.json',RUN/'step3-mim-independent/orchestration-recheck/probe_receipt.py',RUN/'step3-mim-independent/orchestration-recheck/receipt-probe-results.json']
for name in logs:refs.extend([RUN/'logs'/f'{name}.log',RUN/'logs'/f'{name}.json'])
(OUT/'inventory.json').write_text(json.dumps({str(p.relative_to(RUN)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in refs},indent=2)+'\n')
print(json.dumps({'verdict':result['verdict'],'source_count':len(source),'unchanged_baseline_count':len(unchanged),'author_mutations_checked':len(mutations),'files':{p.name:sha(p) for p in [OUT/'review.md',OUT/'receipt.json',OUT/'inventory.json']}},indent=2))
