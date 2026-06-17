# Next Tasks — MediaIngredientMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / CommunityMech / TraitMech).

Last reconciled: 2026-06-15.

## 1. Chemical-properties enrichment — enricher repaired, residual is the ceiling

**Done (2026-06-15, `feat/enrich-chemical-properties`)** — the enricher had silently
broken: OLS4 renamed its annotation keys (`formula` → `generalized_empirical_formula`;
SMILES/InChI → `*_string`), so every fetch returned None. Fixed
`chemical_properties_client.py` to read the current keys (legacy fallback kept),
broadened the enricher to target records *missing `molecular_formula`* (not just
those with no `chemical_properties` block) with a gap-filling **merge** (never
clobbers `cas_rn`), and made the `Enriched` counter report net changes. Re-ran:
**3 records gained formula/SMILES** (diaminopimelic acid, sodium L-lactate,
isobutyramide+mass).

The remaining ~83 missing-formula records are the **genuine ceiling** — abstract
CHEBI classes (aromatic compound, bile salt, hydrocarbon), polymers (glycogen,
carboxymethylcellulose, chondroitin sulfate, DNA), proteins (elastin, LL-37),
complexes (kanamycin), and minerals (ferrihydrite) — which legitimately have no
single empirical formula in ChEBI. Not failures; leave them.

- Run again any time with `python scripts/enrich_chemical_properties.py` (idempotent);
  regenerate per-record files with `just export-individual` after.
- Gotcha still live: OLS4 needs **double** URL-encoding of ChEBI IRIs (handled).
- Find remaining: `grep -rL molecular_formula data/ingredients/mapped/*.yaml | xargs grep -l 'ontology_source: CHEBI'`

## 2. Cross-Mech validator pin guard — DONE (4-repo invariant)

~~Vendor the id↔label validator into CommunityMech~~ — **DONE** (2026-06-12,
CommunityMech PR #132).

**Done** (2026-06-15): the byte-identical invariant now spans **all four** Mech
repos (CultureMech, MIM, CommunityMech, TraitMech). culturebotai-claw#6 Option 1
extended the pin from the script alone to the full vendored set — the validator
`.py` **plus** the two shared tests — across every repo (CommunityMech's drifted
test copies were resynced + pinned in PR #151); editing a vendored test now fails
CI everywhere. TraitMech joined and enforces too (TraitMech PR #110 Phase 1,
PR #111 Phase 2 blocking gate — 14 wrong CURIEs fixed, gate green). All four pin
the same 3-line manifest (`142bbe1…` / `55a432…` / `f01d22…`).
`conf/id_label_targets.yaml` stays **unpinned by design** — it is intentionally
per-repo (different adapters/targets/exceptions), not a drift risk to fix.

## 3. Hard unmapped residual — dedicated semantic curation (~395 records)

Automated exact/normalized/fuzzy matching is **exhausted** (verified 2026-06-14:
only ~1 clean exact match across all 398). The residual is specialized cobamides,
flavonoids, natural products, element placeholders, and mixtures.

- Use `deep-research-ingredient` (Edison/PaperQA3; `EDISON_PLATFORM_API_KEY` is
  configured) or `mediaingredientmech-agentic-curation` (FutureHouse Falcon) for
  source-backed identity + CHEBI/FOODON grounding, per record.
- **Migration recipe (proven 2026-06-15, NAA promotion):** mapping an unmapped
  record is multi-surface and only partly automated. The working sequence:
  1. In the source collections, move + transform the record:
     `unmapped_ingredients.yaml` (delete record, decrement header counts) →
     `mapped_ingredients.yaml` (add with `ontology_mapping`, `mapping_status: MAPPED`,
     a `PROMOTED_TO_MAPPED` history entry; increment header counts).
  2. `just export-individual` (record file moves unmapped/ → mapped/).
  3. **Hand-add the SSSOM row** — `reconcile_sssom` reports the GAP but won't
     synthesize new-row provenance. One `skos:exactMatch` row to the CHEBI id
     (`obo:chebi.owl`, canonical object_label) suffices for a CHEBI-primary record;
     Rule B1 needs no registry sibling. Insert in the file's sort order (by the
     *decoded* subject label, e.g. between `MIM:1-Kestose` and `MIM:1-Pentanol`).
  4. `just export-lists` (docs). Verify: `reconcile_sssom` GAP 0, SSSOM invariants
     Rules A/B1/B2/B3, `validate-products` (the blocking id↔label gate), validate-strict.
  - **Helper built (2026-06-16): `scripts/promote_resolved_unmapped.py`** automates
    the whole recipe (collection move + canonical-label lookup + SSSOM row inserted in
    sort order + regen + verify), with a **PK-collision guard** that refuses to create
    a duplicate CHEBI primary (redirect those to a merge). `--dry-run` by default.
    Usage: `python scripts/promote_resolved_unmapped.py --identifier UNMAPPED_NNNN
    --to CHEBI:NNN --quality EXACT_MATCH --evidence-source "…" --note "…" --apply`.
    Only handles exact/close (narrow/broad need registry SSSOM rows — hand-curate).
  - Note: the per-record filename sanitiser drifted over time, so a freshly-promoted
    file may get a slightly different slug casing than the old unmapped file — cosmetic.
- **Batch 1 done (2026-06-14, `feat/deep-research-unmapped-batch`)** — 3 records
  deep-researched (Edison/PaperQA3) and **enriched in place** (synonyms / CAS-RN /
  provenance; left UNMAPPED — no risky migration yet):
  - `1-Naphtylacetic Acid` → **MAPPED 2026-06-15** (UNMAPPED_0316 → CHEBI:32918
    "1-naphthaleneacetic acid", EXACT_MATCH) via the migration recipe above. NAA,
    CAS 86-87-3 — a "naphtyl" misspelling string-matching missed. (unmapped 398 → 397)
  - `alpha-ketoglutamate` → **MERGED 2026-06-16** into the existing `CHEBI:30915`
    "alpha-ketoglutaric acid" record (added as a synonym; UNMAPPED_0323 removed).
    `promote_resolved_unmapped.py`'s PK-collision guard caught that CHEBI:30915 (and
    the anion CHEBI:16810) are already mapped — it's a duplicate, not a new mapping.
    (unmapped 397 → 396)
  - `2-methyladeninyl cobamide` (UNMAPPED_0182) → **stays UNMAPPED, confirmed**: a
    specific corrinoid ("Factor A") with no source-backed CHEBI/CAS; do NOT map to
    cobalamin/B12. Validates the prior curator call; enriched with synonyms.
  - Takeaway: deep research resolves identities that string-matching can't, but most
    of the residual is genuinely hard. The 2 "ready to map" records still await the
    multi-surface migration above. Edison reports live under `research/` (gitignored).
- **Batch 2 done (2026-06-16, `feat/deep-research-batch2-enrich`)** — 5 records
  deep-researched (Edison/PaperQA3); **all confirmed UNMAPPED** (0 mappings, 0
  merges) and enriched in place with the findings + provenance:
  - `6-methylnicotinate` — ambiguous (carboxylate/anion vs methyl ester); +synonym
    `6-methylnicotinic acid` (related).
  - `Amphotericin` — spans A/B + formulations; do NOT exact-map to amphotericin B
    (CHEBI:2682); +related synonyms `amphotericin B`/`AmB`.
  - `7,2'-Dimethoxyflavone`, `7,4'-Dimethoxyisoflavone` — specific positional
    isomers, no source-backed CAS/CHEBI; closeMatch to a flavone parent would lose
    isomer specificity.
  - `2',2'-Bisepigallocatechin Digallate` — polyphenol; no CAS/formula/CHEBI;
    naming-variant instability prevents grounding.
  - Confirms the residual is genuinely hard: like the cobamide in batch 1, these
    specialized natural products / ambiguous-form compounds lack clean ontology
    grounding. "Confirmed unmapped + enriched" is the correct, defensible outcome.
  - Remaining candidates for future batches: the cobamide cluster (5-methoxy/
    5-methyl/adeninyl/benzimidazolyl cobamide — likely all confirmed-unmapped).
- **Batch 3 done (2026-06-16, `feat/mim-map-inorganic-batch3`)** — a different angle:
  not deep research but a **mappability triage** of the 396 residual. Most is
  genuinely unmappable (commercial media/broths/agars, trace-element & vitamin
  solutions, sera, extracts, grains, buffers, metal-NTA chelates). The high-yield
  sliver is single compounds automated matching missed via formula/spelling
  variants. **3 mapped** (EXACT_MATCH) via `promote_resolved_unmapped.py`, each
  CHEBI id↔label verified against local OAK before mapping (so the blocking gate
  stays green):
  - `KNO2` (UNMAPPED_0413) → **CHEBI:232610** "potassium nitrite" (formula).
  - `Thioglycollic acid` (UNMAPPED_0539) → **CHEBI:30065** "thioglycolic acid" (spelling).
  - `Pyromelitic acid` (UNMAPPED_0504) → **CHEBI:45165** "pyromellitic acid" (misspelling).
  (unmapped 396 → 393.)
  - **Deferred — `KJ` (UNMAPPED_0412) = potassium iodide (Kaliumjodid):** the
    helper's PK-collision guard caught CHEBI:8346 is **already mapped**, so KJ is a
    duplicate needing a *merge* (add as synonym to the existing KI record + drop
    UNMAPPED_0412), not a promotion — same shape as the alpha-ketoglutamate merge.
  - Left alone (ambiguous, no source CAS to disambiguate): garbled salt-hydrate
    formulae (`MnCl4 x n H2O`, `Na2MoO7 x 2 H2O`, `Na2Se2O3`, …), `Na-tetrathionate`,
    `Sodium crotonate`, `α-D-Glucose monohydrate`. Map only with source confirmation.

## 4. mesh.db refresh → drop the 4 SCR exceptions (low priority)

`conf/id_label_targets.yaml` carries 4 `exceptions` for valid MeSH supplementary-
concept records (avocatin B, cholinium lysinate, sodium glutarate, plicacetin)
absent from the cached `sqlite:obo:mesh`. If a newer mesh.db that includes these
SCRs becomes available, drop the matching `exceptions` entries and re-run
`just validate-products` to confirm they resolve as OK_CANONICAL.
