# `data/ingredients/mapped/Vibriostat.yaml`

## Verdict

Pass. The curated CHEBI synonym match, RAW_TEXT synonym merge, structure
fields, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vibriostat.yaml`.
- Identifier and grounding: `identifier: CHEBI:73908` with matching
  `ontology_mapping.ontology_id`, label
  `2,4-diamino-6,7-diisopropylpteridine`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: two MicrobeDecoder raw labels, `Vibriostat` and
  `Vibriostatic Agent O/129`.
- Chemical fields: formula `C12H18N6` and ChEBI/PubChem SMILES/InChI.
- Occurrences: 16 MicrobeDecoder antibiotic trait occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Veratrine_Hydrochloride` through `Viomycin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Verbascose`, `Vibriostat`, and `Viomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:73908` returns active label
  `2,4-diamino-6,7-diisopropylpteridine`, formula `C12H18N6`, and the same
  SMILES/InChI as the YAML.
- The ChEBI synonym set contains both `vibriostat` and
  `vibriostatic agent O/129`, supporting the two absorbed MicrobeDecoder names
  as the same compound.
- The final SSSOM row correctly maps
  `MIM:Vibriostat skos:exactMatch CHEBI:73908` and exports
  `Vibriostatic Agent O/129` in `other` as a real ChEBI synonym.

## Issues

None.

## Completeness

- The curated CHEBI synonym match, duplicate absorption, structure fields,
  MicrobeDecoder occurrence count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
