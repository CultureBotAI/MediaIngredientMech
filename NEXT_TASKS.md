# Next Tasks — MediaIngredientMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / CommunityMech / TraitMech).

Last reconciled: 2026-06-14.

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

## 2. Cross-Mech validator pin guard covers only the .py (cross-repo)

~~Vendor the id↔label validator into CommunityMech~~ — **DONE** (2026-06-12,
CommunityMech PR #132). All three Mechs now carry the byte-identical
`scripts/validate_id_label_correspondence.py`, in sync at sha `142bbe1…`;
CommunityMech's `just verify-validator-pin` passes.

Remaining cross-repo follow-up: the pin guard pins the **script** byte-for-byte
but NOT the vendored test files or the conf structure, so those can silently
drift. Tracked in culturebotai-claw#6. Also open: whether **TraitMech** should
join the byte-identical trio (it has ontology `(id, label)` pairs but no
validator copy — see TraitMech `NEXT_TASKS.md` item 2). Coordinate any change
across all copies at once.

## 3. Hard unmapped residual — dedicated semantic curation (~395 records)

Automated exact/normalized/fuzzy matching is **exhausted** (verified 2026-06-14:
only ~1 clean exact match across all 398). The residual is specialized cobamides,
flavonoids, natural products, element placeholders, and mixtures.

- Use `deep-research-ingredient` (Edison/PaperQA3; `EDISON_PLATFORM_API_KEY` is
  configured) or `mediaingredientmech-agentic-curation` (FutureHouse Falcon) for
  source-backed identity + CHEBI/FOODON grounding, per record.
- **Migration caveat:** mapping an unmapped record is multi-surface and only
  partly automated — move the record from `unmapped_ingredients.yaml` to
  `mapped_ingredients.yaml`, regenerate both per-record dirs, **hand-add the SSSOM
  row(s)** (`reconcile_sssom` reports the GAP but won't synthesize new-row
  provenance), and regenerate docs. Budget for per-record curation, not a sweep.
- **Batch 1 done (2026-06-14, `feat/deep-research-unmapped-batch`)** — 3 records
  deep-researched (Edison/PaperQA3) and **enriched in place** (synonyms / CAS-RN /
  provenance; left UNMAPPED — no risky migration yet):
  - `1-Naphtylacetic Acid` (UNMAPPED_0316) → identity resolved to **1-naphthaleneacetic
    acid (NAA), CAS 86-87-3, CHEBI:32918** (a "naphtyl" misspelling string-matching
    missed). **Ready to map** — CAS-RN added enables the CAS→CHEBI pipeline.
  - `alpha-ketoglutamate` (UNMAPPED_0323) → resolved to alpha-ketoglutarate /
    2-oxoglutarate; free acid **CHEBI:30915**, anion CHEBI:16810. Ready to map once
    the acid-vs-anion form is chosen.
  - `2-methyladeninyl cobamide` (UNMAPPED_0182) → **stays UNMAPPED, confirmed**: a
    specific corrinoid ("Factor A") with no source-backed CHEBI/CAS; do NOT map to
    cobalamin/B12. Validates the prior curator call; enriched with synonyms.
  - Takeaway: deep research resolves identities that string-matching can't, but most
    of the residual is genuinely hard. The 2 "ready to map" records still await the
    multi-surface migration above. Edison reports live under `research/` (gitignored).
  - Next batch candidates: the cobamide cluster (5-methoxy/5-methyl/adeninyl/
    benzimidazolyl cobamide), `6-methylnicotinate`, `Amphotericin`, flavonoids.

## 4. mesh.db refresh → drop the 4 SCR exceptions (low priority)

`conf/id_label_targets.yaml` carries 4 `exceptions` for valid MeSH supplementary-
concept records (avocatin B, cholinium lysinate, sodium glutarate, plicacetin)
absent from the cached `sqlite:obo:mesh`. If a newer mesh.db that includes these
SCRs becomes available, drop the matching `exceptions` entries and re-run
`just validate-products` to confirm they resolve as OK_CANONICAL.
