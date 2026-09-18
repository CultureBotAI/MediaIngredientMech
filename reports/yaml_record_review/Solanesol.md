# `data/ingredients/mapped/Solanesol.yaml`

## Verdict

Pass. The exact `CHEBI:26718` solanesol identity, CultureBotHT CAS support,
structure, curated IUPAC synonym, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Solanesol.yaml`.
- Identifier and grounding: `identifier: CHEBI:26718` with
  `ontology_mapping.ontology_id: CHEBI:26718`, label `solanesol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soil_Extract` through `Sorbose`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:26718` with label `solanesol`,
  CAS `13190-97-1`, and the curated IUPAC synonym.
- Fresh PubChem lookup for CAS `13190-97-1` resolves to solanesol with the same
  formula and InChI as the record.
- Final SSSOM publishes the same-substance IUPAC synonym plus
  `CAS:13190-97-1`.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, active synonym, and final
  exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
