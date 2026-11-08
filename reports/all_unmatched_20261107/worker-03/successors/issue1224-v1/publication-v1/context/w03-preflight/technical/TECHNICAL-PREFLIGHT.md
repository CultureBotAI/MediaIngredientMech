# Worker03 Oxoid successor technical preflight

Reviewer: `/root/oxoid_contract`. This is accounting, capture integrity and implementation guidance, not chemistry or source-case approval. No source/corpus/operator/gate edits, network requests, commits or pushes were made by this reviewer.

The current original report was independently re-read and audited with the original campaign auditor: 188 decisions, 74 proposals, 852 evidence entries, and 806 exact referenced input paths. All 977 original transport-manifest entries match. The original and campaign auditor bytes match. Local HEAD was `1196d5bc3aaba7563b829d5cbe7e54722fccc35d` at the check. Parent separately owns live remote verification. Full receipts and hashes are in the JSON files beside this note.

## Complete successor layout

Place new complete core ledgers under `reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/draft/` (or immutable final successor path), while retaining `--artifact-root` as `reports/all_unmatched_20261107/worker-03`. This keeps every existing capture reference valid without rewriting 73 unrelated proposal objects or 852 original evidence objects. New artifact capture paths start `successors/issue1224-v1/`. Never use traversal or symlinks; the original auditor rejects both.

Retain the original complete reports, indexes, payloads, source captures and reviews. Publish a new explicit selector/HANDOFF; do not overwrite the old selector or reinterpret its claims. The original manifest correctly covers the original publication; the new successor manifest should bind its new inputs and preserved predecessor manifest separately.

Replace exactly one active case proposal reference. The new active stable ID is `w03-oxoid-cm0149-product-1224-v1`, kind `new_owner`, with null `before_sha256` and prospective `data/ingredients/mapped/reinforced_clostridial_medium_oxoid_cm0149.yaml`. Remove `b-proposal-cm0149-form` only from the successor active proposal list, not history. Keep `retired_proposal` and `retired_decision` as their complete exact original objects in retirement.json, plus references to the authentic old before bytes, original after payload and original separate review. `original-origin-binding.json` provides the exact source case and original objects for comparison.

The old mixed RCM `owner_records` is a real frozen current-context reference with SHA256 `7f94183c0d9b070b57c1ffa8beab53817b48791a75278957163619ece7a24c2e`. Keep it unchanged and explain its contextual/historical role. Do not add the prospective new owner to owner_records: the auditor requires actual existing native direct-child bytes there. The new target belongs in proposal.owner_path; null new-owner beforeimage does not replace the authentic old-owner provenance.

Preserve the changed case's original case ID/digest/source object/occurrences, frozen index, owner_records, downstream-hold object, native owner review rows and hold_scope_note. The other 187 case objects and 73 prior proposal objects must remain exactly equal as JSON objects. Preserve all 852 original evidence objects and add distinct IDs for new captures, scope analysis and actual new independent review. Old review capture remains historical evidence, not review of new bytes. The new whole-candidate and changed-case review needs its own real reviewer and reviewed hashes. A pending review is allowed structurally but never publication approval.

## Actual duplicate-search boundary and results

`duplicate-scan.json` hashes every regular file traversed under maintained `data/ingredients/**` and `data/curated/**`, including hidden/ignored files; the derived `docs/data/label_index.csv`; all 981 payload paths in the frozen final-intake ledger; and all 73 YAML files under v4 candidates (37 proposed outputs plus authentic beforeimage files, **not 73 selected candidates**). No credential or unrelated private roots were scanned. There were no skipped symlinks or non-UTF8 files. The 4,035 scanned-path entries include repeated paths by construction and are not a native-owner count.

No native direct-child record holds the exact new registry identifier; the prospective maintained path does not exist. The maintained native lexical hits are `Dehydrated_RCM_Medium.yaml` and `Reinforced_Clostridial_Medium.yaml`. All 981 frozen payload hashes match their selected-entry digests. RCM-family proposal leads include W03's old annotation, W04 Sigma agar, W05 Difco and dehydrated RCM. The intentionally broad `cm0?149` expression also catches JCM149 references; these are recorded false-positive lexical leads, not claims of product overlap. V4 hits are NEW-OXOID-CM0149, TARGET-032 and TARGET-032's authentic beforeimage. These coordinator proposals are not maintained existing owners or accepted integrations. No global absence or identity-equivalence claim follows outside the stated boundary.

## Authoritative structural invocation

Use a NEW receipt path inside the original artifact root, e.g.:

```sh
PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-03/env/bin/python \
  reports/all_unmatched_20261107/worker-03/tools/audit_worker_outcomes_v1.py \
  --shard /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/shards/shard-03.json \
  --decisions reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/draft/decisions.json \
  --proposals reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/draft/proposals.json \
  --evidence reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/draft/evidence.json \
  --artifact-root reports/all_unmatched_20261107/worker-03 \
  --source-root /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5 \
  --mim-root . \
  --output reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/validation/structural-audit-NEW.json
```

Do not supply `--canary-case`; this is full-shard coverage. Original auditor does not authenticate reviewer independence, scientific correctness, or chemistry. It also does not by itself prove preservation relative to the previous complete report.

For that delta proof run `check_successor_preservation.py --original-root reports/all_unmatched_20261107/worker-03 --successor-root reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/draft --retirement reports/all_unmatched_20261107/worker-03/successors/issue1224-v1/retirement.json --output NEW_RECEIPT.json`. The helper checks the original 188/74/852 counts, exact case membership, 187 unchanged cases, 73 unchanged proposals, all 852 original evidence objects, exact retired objects, one unique new origin, old proposal retirement, fixed source/hold context, null new-owner preimage, and assigned coordinator v4 payload digest. Fourteen meaningful control tests passed, including duplicate case, other-case/proposal/evidence drift, missing evidence, forged retirement, active retired origin, fabricated beforeimage, wrong payload and source/hold mutations. These controls use a synthetic modified core in memory, not an approved scientific successor. See retained `helper-controls.log`.

## Native candidate checks without maintained writes

The original `tools/validate_proposals.py` hardcodes its OUT root and assumes the proposal ledger and captures share that root. Running it unchanged validates the old 74-proposal bundle, not a successor ledger elsewhere. Do not report such a run as successor validation. A bounded report-local wrapper can independently accept the successor ledger path and original artifact root, call native `validate_ingredient(record)` for closed-schema errors, then call `validate_component_partonomy` over the full native direct-child catalog with selected proposed payloads overlaid in memory. Preserve the before/after violation sets and newly introduced differences, plus any pre-existing exceptions. Use all selected payloads if claiming complete successor schema/partonomy validity; checking only the new candidate is a narrower claim. No native gate alteration is needed.

Recheck current native owner before hashes, all proposed payload hashes, role fields unchanged on unrelated existing edits, exact new identity collisions across the complete overlay, intended path absence and complete coordinator history prefix. Use native `synonym_policy.is_resolving_synonym` for technical export eligibility, but review actual source applicability independently; a resolving enum is not scientific proof. Partonomy currently accepts all synonym strings when matching component labels; a structural PASS does not prove a label is scientifically appropriate or exported. The new Oxoid payload has no component assertion, so its partonomy validity does not establish historical formulation.

The existing direct-owner formal review is historical; it cannot become a review of a new source-qualified owner merely by rebinding a path. The source-only candidate/case review must bind the new full payload and exact occurrence. Hold removal, supported export and whole-owner/role admission remain coordinator/native obligations. No full corpus rebuild or network ontology/provider refresh is needed for these report-only checks.

Publication remains conditional on the coordinator's communication of completed W01 exact v4 review and disposition, plus fresh independent successor candidate/case/retirement/accounting review. This technical preflight grants none of those approvals.
