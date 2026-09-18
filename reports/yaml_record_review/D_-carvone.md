# `data/ingredients/mapped/D_-carvone.yaml`

## Verdict

Pass. The CultureBotHT CAS value resolves to active `CHEBI:15399` for
`(+)-carvone`, the stereospecific structure is populated, the ChEBI exact
synonyms are same-subject labels, and the final SSSOM `other` payload contains
only those synonyms plus the structured CAS value.

## Identity

- Reviewed record: `data/ingredients/mapped/D_-carvone.yaml`.
- Identifier and grounding: `identifier: CHEBI:15399` with
  `ontology_mapping.ontology_id: CHEBI:15399`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:15399` to active `(+)-carvone`, formula
  `C10H14O`, charge `0`, stereospecific InChIKey
  `ULDHMXUKGWMISQ-VIFPVBQESA-N`, and CAS xref `2244-16-8`.
- PubChem resolves `2244-16-8` to `Carvone, (+)-`, formula `C10H14O`, and the
  same stereospecific InChIKey as ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/DL_Vitamins.yaml data/ingredients/mapped/DNA_From_Salmon.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed when non-OBO fallback targets were included.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-Tyrosine.yaml data/ingredients/mapped/DL-glyceraldehyde.yaml data/ingredients/mapped/D_-carvone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping the `kgmicrobe.ingredient:` and
  `cas:` fallback records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18186 CHEBI:5445 CHEBI:15399`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:15399`.
- `curl -L ... /compound/name/2244-16-8/property/.../JSON`: PubChem resolved
  the CAS value to CID 16724, `Carvone, (+)-`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:15399`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The CAS-derived mapping provenance is internally consistent: the record was
  created from `CAS-RN=2244-16-8`, ChEBI carries `cas:2244-16-8` on
  `CHEBI:15399`, and the August 2026 curation history regraded the mapping to
  `CAS_RN_LOOKUP` to preserve that method.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D_-carvone` to `CHEBI:15399` with `skos:exactMatch`, canonical object
  label `(+)-carvone`, CHEBI object source, and the same-subject tokens
  `(4S)-p-mentha-1(6),8-dien-2-one|(5S)-2-methyl-5-(prop-1-en-2-yl)cyclohex-2-en-1-one|CAS:2244-16-8`
  in `other`.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `CHEBI:15399`.
- CAS, molecular formula, InChI, SMILES, and the stereospecific ChEBI exact
  synonyms are populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
