# `data/ingredients/mapped/5-Hydroxyoctanoate.yaml`

## Verdict

Pass, none. The CAS-backed exact ChEBI identity, exact synonym, chemistry,
SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Hydroxyoctanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:180039` with
  `ontology_mapping.ontology_id: CHEBI:180039`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:180039` to `5-hydroxy-octanoic
  acid` with formula `C8H16O3`, SMILES `CCCC(O)CCCC(=O)O`, and the stored
  InChI.
- Local OAK metadata for `CHEBI:180039` carries `cas:17369-50-5`, the stored
  exact synonym `5-hydroxyoctanoic acid`, and the same formula, SMILES, InChI,
  and InChIKey.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Hydroxyoctanoate.yaml data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml data/ingredients/mapped/5-aminovaleric_Acid.yaml data/ingredients/mapped/5-dehydro-D-gluconate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-Hydroxyoctanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the expected label and synonym block for `CHEBI:180039`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the expected ChEBI formula, structure strings, and CAS xref.

## Evidence

- The active ChEBI term, OAK `cas:17369-50-5` xref, stored formula, stored
  SMILES, stored InChI, and exact ChEBI synonym all support the
  5-hydroxyoctanoic-acid identity.
- The SSSOM row maps `MIM:5-Hydroxyoctanoate` to `CHEBI:180039` with
  `skos:exactMatch`, includes `5-hydroxyoctanoic acid|CAS:17369-50-5` in
  `other`, and preserves the `CAS_RN_LOOKUP` provenance as manual curation.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, synonym-enrichment review rows, and ignored aggregate backups; no
  conflicting curated current record for this CAS or ChEBI identity was found.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
