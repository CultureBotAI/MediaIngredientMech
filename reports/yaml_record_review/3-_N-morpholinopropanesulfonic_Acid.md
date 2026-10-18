# `data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml`

## Verdict

Needs curation, major. The active `CHEBI:44115`
`3-(N-morpholino)propanesulfonic acid` identity, CAS, ChEBI chemistry, buffer
role, occurrence counts, SSSOM row, and aggregate row pass, but exact synonyms
still include `MOPS buffer` and several raw CultureMech role/property strings
that do not denote the pure compound.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:44115` with
  `ontology_mapping.ontology_id: CHEBI:44115`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:44115`
  resolves to `3-(N-morpholino)propanesulfonic acid`, lists formula
  `C7H15NO4S`, carries CAS `1132-61-2`, and matches the record InChI and
  SMILES.
- `ingredient_type: SINGLE_INGREDIENT` is present.
- `kg_microbe_node_id: CHEBI:44115` is consistent with the active identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml data/ingredients/mapped/3-acetylpyridine.yaml data/ingredients/mapped/3-aminobenzoate.yaml data/ingredients/mapped/3-aminobutyrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-_N-morpholinopropanesulfonic_Acid` to `CHEBI:44115` row and carries
  the exact synonyms/catalog surface plus `CAS:1132-61-2` in `other`.

## Evidence

- The direct ChEBI page verifies `CHEBI:44115`, CAS `1132-61-2`, formula,
  InChI, and SMILES, so the old `mappings/record_research_validation.tsv` P1
  rows that asked for direct CHEBI review are stale.
- Supported: the `BUFFER` physicochemical role has database-entry evidence from
  CultureMech imports and 56 distinct CultureMech recipe occurrences after the
  `#337` occurrence refresh.
- Unsupported as exact labels: `MOPS buffer` can denote a pH-adjusted solution
  rather than the pure acid, and the `Role: Buffer; Properties: ...` raw texts
  are annotations, not synonyms. `mappings/record_research_validation.tsv` has
  still-applicable P2 rows for both defects.
- `MOPS buffer (SIGMA)` is lower risk because it is explicitly typed
  `CATALOG_VARIANT` and sourced to one folded CultureMech occurrence instead of
  asserted as an exact synonym.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, synonym-enrichment review, generated docs, CultureMech
  residual alias, and record-research rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS, formula, InChI, and SMILES are populated.
- Occurrence statistics have been refreshed from the `#337` CultureMech
  occurrence table.
- The only consequential gap is synonym scope: buffer/formulation and
  role/property context are still mixed into the label list.

## Recommended Edits

1. In `data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml`, remove
   `MOPS buffer` from `EXACT_SYNONYM` labels or preserve it only in a non-exact
   source-surface field that cannot make the pure compound look identical to a
   formulated buffer.
2. Remove the three `Role: Buffer; Properties: ...` entries from `synonyms`; the
   active `physicochemical_roles.BUFFER` facet already preserves the role.
3. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
