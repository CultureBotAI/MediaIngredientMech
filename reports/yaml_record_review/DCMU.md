# `data/ingredients/mapped/DCMU.yaml`

## Verdict

Pass. The CultureBotHT CAS value resolves to the active ChEBI diuron class, the
record preserves the DCMU lexical synonym, the refreshed 1/1 occurrence count is
traceable, and the final SSSOM `other` payload contains only same-subject
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/DCMU.yaml`.
- Identifier and grounding: `identifier: CHEBI:116509` with
  `ontology_mapping.ontology_id: CHEBI:116509`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:116509` to active `diuron`, formula
  `C9H10Cl2N2O`, charge `0`, InChIKey `XMTQQYYKAHVGBJ-UHFFFAOYSA-N`, and CAS
  xref `330-54-1`.
- The ChEBI related synonyms include `DCMU`, so the preferred term is a
  same-subject synonym for the mapped diuron class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through `D` and then failed on `DAMPA` because its `cas:` fallback
  hit the known OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset after skipping `DAMPA`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65327 CHEBI:37492 CHEBI:75228 CHEBI:116509`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:116509`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 1 row for
  `CHEBI:116509`, matching `occurrence_statistics.media_count: 1` and
  `total_occurrences: 1`.
- The CAS-derived mapping provenance is internally consistent: the record was
  created from `CAS-RN=330-54-1`, ChEBI carries `cas:330-54-1` on
  `CHEBI:116509`, and the August 2026 curation history regraded the mapping to
  `CAS_RN_LOOKUP` to preserve that method.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:DCMU` to
  `CHEBI:116509` with `skos:exactMatch`, canonical object label `diuron`,
  CHEBI object source, and the same-subject tokens
  `3-(3,4-dichlorophenyl)-1,1-dimethylurea|CAS:330-54-1` in `other`.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over `data`, `mappings`,
  `docs`, `reports`, `.claude`, `.github`, `scripts`, `src`, and `tests` found
  no second primary record or parent-mapping record for `CHEBI:116509`; the
  term appears in this record, synchronized/generated projections, and review
  surfaces.
- CAS, molecular formula, InChI, SMILES, and occurrence statistics are
  populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
