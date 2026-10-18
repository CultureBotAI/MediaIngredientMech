# `data/ingredients/mapped/Trehalose.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, PubChem structure,
CultureMech carbon-source role, aggregate row, and final SSSOM row pass, but
`ENERGY_SOURCE` is still provisional computational evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trehalose.yaml`.
- Identifier and grounding: `identifier: CHEBI:27082` with matching
  `ontology_mapping.ontology_id`, label `trehalose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `52613-20-4`.
- Synonyms: two exact D-trehalose surfaces plus two raw CultureMech role
  strings.
- Occurrences: 15 CultureMech recipe occurrences in 15 media.
- Roles: curated `CARBON_SOURCE` from original CultureMech role text, plus
  provisional `ENERGY_SOURCE`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trans-cinnamic_Acid` through `Trehalose`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `trehalose` returns `CHEBI:27082` with label
  `trehalose`.
- Fresh PubChem lookup for CAS `52613-20-4` returns formula `C12H22O11` and
  the same InChI as the YAML.
- The final SSSOM row has `MIM:Trehalose skos:exactMatch CHEBI:27082`,
  exports only the two exact synonym labels plus `CAS:52613-20-4`, and filters
  the raw `Role:` strings out of `other`.

## Issues

### Major: `ENERGY_SOURCE` is provisional computational evidence

The imported CultureMech `CARBON_SOURCE` role is supported by original
database text, but `ENERGY_SOURCE` was inferred later:

```yaml
- role: ENERGY_SOURCE
  confidence: 0.7
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Canonical energy substrate (catabolised for energy)
    curator_note: Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.
```

That provisional addition needs curation or removal.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count,
  CultureMech-imported carbon-source role, aggregate copy, and final SSSOM row
  agree.
- The only residual issue is the provisional `ENERGY_SOURCE` role evidence.

## Recommended Edits

- Replace the `ENERGY_SOURCE` computational prediction with curated evidence,
  or remove that role and leave the source-backed `CARBON_SOURCE` facet.
