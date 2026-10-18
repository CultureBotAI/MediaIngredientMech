# `data/ingredients/mapped/Glycerol_Mono-oleate.yaml`

## Verdict

Needs curation. The CultureMech exact match to active `CHEBI:75937`
monooleoylglycerol, the same-subject ChEBI synonyms, CAS payload, occurrence
count, and final SSSOM row pass, but `SURFACTANT` remains an unsupported
computational role.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerol_Mono-oleate.yaml`.
- Identifier and grounding: `identifier: CHEBI:75937` with matching
  `ontology_mapping.ontology_id`, canonical label `monooleoylglycerol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `129784-87-8`, formula `C21H40O4`, and the ChEBI
  generic SMILES `*OCC(CO)O*`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycerol_Mono-oleate.yaml data/ingredients/mapped/Glycerol_Monostearate.yaml data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Glycine-NaOH_Buffer.yaml data/ingredients/mapped/Glycine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycerol_Mono-oleate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, synonyms, CAS RN, formula, SMILES, occurrence
  count, singleton type, and provisional surfactant role as the per-record YAML.
- OLS4 resolves `CHEBI:75937` as `monooleoylglycerol` and lists the stored
  final-SSSOM tokens `(9Z-octadecenoyl)-glycerol`, `MG[18:1(omega-9)]`,
  `mono-(9Z)-octadecenoylglycerol`, and `oleoylglycerol` as synonyms.
- PubChem resolves CAS `129784-87-8` to monooleoylglycerol CIDs with formula
  `C21H40O4`, agreeing with the record formula.
- Major: `physicochemical_roles.SURFACTANT` is still backed only by
  `COMPUTATIONAL_PREDICTION` from in-session reasoning and a provisional
  curator note. No inspected CultureMech, database, or literature evidence
  supports that role for this record.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycerol_Mono-oleate` to `CHEBI:75937` by `skos:exactMatch` and exports
  only subject synonyms plus `CAS:129784-87-8` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, ChEBI synonyms, ingredient type,
  occurrence count, and final SSSOM row are populated.
- The surfactant role needs claim-level evidence or removal.

## Recommended Edits

- Major: remove `physicochemical_roles.SURFACTANT` from
  `data/ingredients/mapped/Glycerol_Mono-oleate.yaml`, or replace its
  provisional computational evidence with inspected source evidence that
  specifically supports glycerol mono-oleate functioning as a surfactant in
  this medium-ingredient context.
