# Next Tasks — MediaIngredientMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / CommunityMech / TraitMech).

Last reconciled: 2026-06-14.

## 1. Chemical-properties enrichment (89 CHEBI records missing `molecular_formula`)

89 CHEBI-mapped records have no `molecular_formula` (and likely no SMILES/InChI).
Run the existing enricher to backfill from ChEBI OLS4 + PubChem:

```bash
python scripts/enrich_chemical_properties.py        # auto-fetches formula/SMILES/InChI
```

- Source of truth is `data/curated/mapped_ingredients.yaml`; regenerate per-record
  files with `just export-individual` after.
- Watch the known ceiling: abstract CHEBI classes (e.g. "phosphatidylinositol",
  added in #55), polymers, proteins, and obsolete terms legitimately have no
  formula — don't treat those as failures.
- Gotcha (fixed before, keep an eye out): OLS4 needs **double** URL-encoding of
  ChEBI IRIs; obsolete terms return the IRI fragment as `label`.
- Find them: `grep -rL molecular_formula data/ingredients/mapped/*.yaml | xargs grep -l 'ontology_source: CHEBI'`

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
- A first batch is being run in `feat/deep-research-unmapped-batch`.

## 4. mesh.db refresh → drop the 4 SCR exceptions (low priority)

`conf/id_label_targets.yaml` carries 4 `exceptions` for valid MeSH supplementary-
concept records (avocatin B, cholinium lysinate, sodium glutarate, plicacetin)
absent from the cached `sqlite:obo:mesh`. If a newer mesh.db that includes these
SCRs becomes available, drop the matching `exceptions` entries and re-run
`just validate-products` to confirm they resolve as OK_CANONICAL.
