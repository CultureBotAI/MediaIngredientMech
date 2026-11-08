from pathlib import Path
import json,hashlib,datetime,shutil
R=Path('reports/all_unmatched_20261107/worker-06');S=R/'successor-v2';F=S/'final'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
sel=json.loads((F/'selection.json').read_text());native=[]
for kind in ['stock','merck']:
 n=json.loads((F/f'logs/native-{kind}-save.json').read_text());native.append({k:str(Path(v).relative_to(Path.cwd())) for k,v in n.items()})
oldhash=sha(R/'proposals.json');newhash=sha(F/'proposals.json');b=S/'research-b/final-binding-v2.json'
text=f'''Worker06 successor is ready for coordinator integration review. **Use only [final/selection.json](final/selection.json) and its declared intake paths.** It selects99 proposals for all188 frozen source cases. The published `d5a7613c931d45d057eaca7b5ec15280aca76c9e` bundle, all100 original payloads and every original manifest-bound evidence file remain byte-identical.

This update reconciles `A-P-NBRC1308-TRACE` and `C-P-NBRC1356-TRACE` into `V2-P-NBRC1308-1356-TRACE`, with one proposed registry identity `kgmicrobe.ingredient:nbrc_1308_1356_trace_elements_stock`. Full primary tables establish the same13 specified solutes,1L distilled-water input and NTA→NaOH pH6.5→minerals→stated finalpH7.0 preparation. That comparison established sameness before choosing the joint label/identifier. Recipe numbers, filenames, hashes and metadata encodings were not substance distinctions or winner-selection criteria.

The shared [payload](payloads/nbrc_1308_1356_trace_elements_stock.yaml) preserves15 named preparation inputs, including unquantified NaOH. The1L water is an input, not an asserted final volume. NaOH amount/concentration, any final-pH correction reagent/amount, unspecified child forms and final equilibrium species remain unknown. No global resolving synonym is made from the local starred headings.

| Source case | Exact included occurrence context | Retained source processing |
|---|---|---|
|19, `Trace element solution**` |CultureMech:007471 ingredients/8; primary NBRC1308 |1ml stock; receiving mixture autoclaved underN2/CO2(80/20)|
|133, `Trace element solution****` |CultureMech:007474 ingredients/6; primary NBRC1356 |10ml filter-sterile stock added inN2-handled medium|

Case19's NBRC1020 and824 occurrences remain excluded from the shared stock and retain unchanged `A-P-NBRC1020-824-TRACE`. All four exact occurrence IDs, raw labels, source digests and complete contexts are retained in [final/proposals.json](final/proposals.json), [final/decisions.json](final/decisions.json) and the [primary comparison](research-a/nbrc1308-1356-comparison.json). Nominal formulation equality does not assert identical post-sterilization endpoints.

The [existing-owner search](research-c/existing-owner-search.json) enumerated all2,956 maintained owners including ignored files,156 broad candidates and all100 published proposals. No maintained whole-stock owner was positively established for this formulation; defined nearby NTA stocks differ, while underspecified generic owners remain unverified. No maintained owner was merged or edited. [Lineage](lineage.json) preserves both original author histories, exact payloads, original retrieval timestamps and prior independent reviews.

The required full partonomy check also exposed one inherited Merck108339 reference-label mismatch. The original100 overlay and first99 candidate both reproduced the same failure; the maintained baseline passed. Supplier and ontology evidence independently support using canonical `D-glucose` for the already referenced `CHEBI:17634`, with exact supplier `D(+)Glucose` retained in component evidence. The [final correction](final/partonomy-correction.json) changes only that component name, its provenance explanation and an appended audit event. Chemical identity, product identity,20.0G_PER_L,reference scope, separate agar and historical-lot/form limits are unchanged. The final intake therefore retains97 selected payloads and184 case outcomes unchanged from the published bundle; two stock cases and two Merck cases received distinct-author re-review.

The first99 candidate at `successor-v2/proposals.json` and its [selection](selection.json) are immutable historical evidence of the reconciled stock before the inherited Merck validation failure was corrected. Its failed logs and both earlier reviewer receipts remain intact. **They are superseded for intake by `successor-v2/final/selection.json`.** Neither original stock owner should be installed, and no recursive ingestion of every YAML under this evidence directory is appropriate.

Current authoritative intake, with artifact capture paths resolved against `reports/all_unmatched_20261107/worker-06/`:

- [final/selection.json](final/selection.json): explicit supersession, current paths and hashes.
- [final/decisions.json](final/decisions.json): all188 cases; all310 CultureMech occurrence IDs retained. KG empty occurrence-ID lists still mean that source IDs are not exposed, not zero observations.
- [final/evidence.json](final/evidence.json):1,066 evidence entries, including all1,056 original entries unchanged.
- [final/proposals.json](final/proposals.json):99 selected proposals (75 new-owner proposals;24 existing-owner edits), exact after captures and original before-owner hashes.
- [final/source-holds.json](final/source-holds.json): all88 downstream hold rows and all original source flags unchanged.

Use the same frozen queue as `--source-root`; use the parent worker06 report directory as `--artifact-root`, not `final/`. The original assignment SHA remains `6e5d487b0ffb05a867766fe51bc90074c7aa2e48459335cf983f021720ce2808`, with original base `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99` and explicit PR1158 dependency. This report makes no current-main or PR-merge claim.

Actual authorship is in [final/agent-scopes.json](final/agent-scopes.json). Root authored the successor and label correction; research_a compared primary tables and verified its former Merck source; research_c searched existing owners; research_b separately reviewed both final deltas and all affected outcomes. No additional external session was started. Independent receipts:

- [Stock scientific review](research-b/scientific-review.json): `{sha(S/'research-b/scientific-review.json')}`.
- [Merck label delta review](research-b/merck-label-delta-review.json): `{sha(S/'research-b/merck-label-delta-review.json')}`.
- [Final complete intake binding](research-b/final-binding-v2.json): `{sha(b)}`. Covers188 cases,99 payloads,1,066 captures, all original100 payloads and1,758 original manifest files; no open binding findings.

Final validation receipts:

- [Full-shard structural binding](final/logs/structural-audit.json): PASS188/188. Structural validity does not establish scientific approval.
- [Strict schema](final/logs/schema-command.json): PASS99/99 exact selected payloads.
- [Native partonomy](final/logs/partonomy-successor.log): PASS3,031 records,149 decompositions,1,032 components,zero violations in a private full-catalog overlay. This is validation input, not an installed catalog or downstream rebuild.
- [Invariants](final/logs/invariants.json): PASS, including preserved source holds, exact original before hashes, unchanged historical files, source-case partitions and unique proposed identifiers/paths.
- [Original100 failed partonomy receipt](logs/partonomy-original100.json) and [first99 failed receipt](logs/partonomy-successor.json) remain visible; validation was not weakened.
- Native validate/save/check receipts and exact execution status are in [final/validation-status.json](final/validation-status.json).
- [Final independent diff review](research-a/final-successor-diff-review.json) covers the additions and preservation boundary.

Native scientific category reviews were saved through inspect→validate→save, with explicit author self-review status and distinct skeptical-review evidence:

- Stock reconciliation: [YAML](../../../../{native[0]['review']}) and [Markdown](../../../../{native[0]['markdown']}); five targets.
- Merck reference-label correction: [YAML](../../../../{native[1]['review']}) and [Markdown](../../../../{native[1]['markdown']}); four targets.

The original published review and worker03's read-only snapshot remain valid historical evidence. The coordinator evaluates this successor separately. [Issue1207](https://github.com/CultureBotAI/MediaIngredientMech/issues/1207) and supplement SHA `e309179928a0130bf05fd34f95f501bb5339bc44e4fbfd6f05ac2d6ebc11345a` are preserved as the triggering finding; no issue closure, source-case approval, owner approval or export approval is claimed.

| Proposal ledger | SHA256 |
|---|---|
|Published original100, `../proposals.json`|`{oldhash}`|
|First99 candidate, `proposals.json`|`{sha(S/'proposals.json')}`|
|**Current final99, `final/proposals.json`**|`{newhash}`|

Final selector SHA256: `{sha(F/'selection.json')}`. The [successor SHA256SUMS](SHA256SUMS) binds all new artifacts and both native review pairs; the old manifest is untouched. The final Git head is the ordinary commit enclosing this handoff, reported exactly in the session completion. Branch: `review/all-unmatched-w06-source-review-20261107`.

Coordinator integration remains a separate guarded operation: select one stock payload, retain all raw source/occurrence scopes and both lineages, withdraw inherited support for changed installed owners, and run separate whole-owner/source/export gates. No maintained YAML, mapping, selector or export was changed; no downstream rebuild, force push, PR or merge was performed.
'''
(S/'HANDOFF.md').write_text(text)
(S/'README.md').write_text('Current intake: [final/selection.json](final/selection.json). Read [HANDOFF.md](HANDOFF.md).\n\nThe original published100 selection and the first99 candidate in this directory remain historical. The final99 selection includes the independently reconciled stock and the source-backed Merck component-label correction required by full partonomy validation.\n')
dump(F/'artifact-index.json',{'current_selection':{'path':str(F/'selection.json'),'sha256':sha(F/'selection.json')},'proposal_ledger':{'path':str(F/'proposals.json'),'sha256':newhash},'published_original_ledger':{'path':str(R/'proposals.json'),'sha256':oldhash,'commit':'d5a7613c931d45d057eaca7b5ec15280aca76c9e'},'first_candidate_historical':{'path':str(S/'proposals.json'),'sha256':sha(S/'proposals.json')},'independent_binding':{'path':str(b),'sha256':sha(b)},'native_reviews':native,'handoff':str(S/'HANDOFF.md'),'no_source_owner_export_approval':True})
shutil.copyfile(Path(__file__),F/'validation-scripts/handoff.py');shutil.copyfile(Path('.temp/all-unmatched-worker-06/successor-v2/validate_successor.py'),S/'validation-scripts/validate_successor.py')
print('Prepared handoff; current intake',F/'selection.json')
