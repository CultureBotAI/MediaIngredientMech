# `data/ingredients/mapped/DETANO.yaml`

## Verdict

Pass. The CultureBotHT CAS value resolves to active `CHEBI:50154`, the chemical
properties match the ChEBI structure, no unsupported roles are asserted, and the
final SSSOM row publishes only the same-subject CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/DETANO.yaml`.
- Identifier and grounding: `identifier: CHEBI:50154` with
  `ontology_mapping.ontology_id: CHEBI:50154`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:50154` to active
  `1,1-bis(2-aminoethyl)-2-hydroxy-3-oxotriazane`, formula `C4H13N5O2`,
  charge `0`, InChIKey `HMRRJTFDJAVRMR-UHFFFAOYSA-N`, SMILES, and CAS xref
  `146724-94-9`.
- PubChem resolves `146724-94-9` to DETA NONOate records with formula
  `C4H13N5O2`, matching the mapped ChEBI structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:77707 CHEBI:50154 CHEBI:37023 CHEBI:35621 CHEBI:27389`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:50154`.
- `curl -L ... q=DETANO&ontology=chebi&exact=true`: live OLS returned zero
  exact ChEBI hits for the compact subject slug, but the source CAS already
  resolves by ChEBI xref.
- `curl -L ... /compound/name/146724-94-9/property/.../JSON`: PubChem
  resolved the CAS value to DETA NONOate records.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `CHEBI:50154`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The CAS-derived mapping provenance is internally consistent: the record was
  created from `CAS-RN=146724-94-9`, ChEBI carries `cas:146724-94-9` on
  `CHEBI:50154`, and the August 2026 curation history regraded the mapping to
  `CAS_RN_LOOKUP` to preserve that method.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:DETANO` to
  `CHEBI:50154` with `skos:exactMatch`, canonical object label
  `1,1-bis(2-aminoethyl)-2-hydroxy-3-oxotriazane`, CHEBI object source, and
  only `CAS:146724-94-9` in `other`.
- The record does not assert nutritional roles, environmental contexts,
  synonyms, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record or
  parent-mapping record for `CHEBI:50154`.
- CAS, molecular formula, InChI, and SMILES are populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
