# `data/ingredients/mapped/Daidzein.yaml`

## Verdict

Pass. The record is an exact active ChEBI match for daidzein, the CultureBotHT
CAS value resolves to the same formula, there are no unsupported roles, and the
final SSSOM `other` payload contains only the same-subject ChEBI synonym and
structured CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Daidzein.yaml`.
- Identifier and grounding: `identifier: CHEBI:28197` with
  `ontology_mapping.ontology_id: CHEBI:28197`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:28197` to active `daidzein`, formula `C15H10O4`,
  charge `0`, InChIKey `ZQSIJRDFPHDXIC-UHFFFAOYSA-N`, SMILES, and CAS xref
  `486-66-8`.
- PubChem resolves `486-66-8` to `Daidzein`, formula `C15H10O4`, and the same
  InChIKey as ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through the two ChEBI records and then failed on
  `kgmicrobe.compound:danomycin` because local registry targets hit the known
  OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping the two local placeholders.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81430 CHEBI:28197 CHEBI:600103`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:28197`.
- `curl -L ... /compound/name/486-66-8/property/.../JSON`: PubChem resolved the
  CAS value to CID 5281708, `Daidzein`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:28197`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Daidzein`
  to `CHEBI:28197` with `skos:exactMatch`, canonical object label `daidzein`,
  CHEBI object source, and the same-subject tokens
  `7-hydroxy-3-(4-hydroxyphenyl)-4H-chromen-4-one|CAS:486-66-8` in `other`.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record or
  parent-mapping record for `CHEBI:28197`.
- CAS, molecular formula, InChI, SMILES, and the ChEBI exact synonym are
  populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
