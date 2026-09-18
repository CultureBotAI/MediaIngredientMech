# `data/ingredients/mapped/Sorgoleone.yaml`

## Verdict

Pass. The exact `CHEBI:61117` sorgoleone identity, CultureBotHT source,
structure, curated IUPAC synonym, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sorgoleone.yaml`.
- Identifier and grounding: `identifier: CHEBI:61117` with
  `ontology_mapping.ontology_id: CHEBI:61117`, label `sorgoleone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sorgoleone` through `Soya_Peptone`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:61117` with label `sorgoleone`
  and the curated IUPAC synonym.
- Fresh PubChem lookup for CAS `105018-76-6` resolves to sorgoleone with the
  same formula and InChI as the record.
- Final SSSOM publishes the same-substance IUPAC synonym plus
  `CAS:105018-76-6`.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, active synonym, and final
  exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
