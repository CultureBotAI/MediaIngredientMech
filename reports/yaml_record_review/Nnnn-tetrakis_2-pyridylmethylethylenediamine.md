# `data/ingredients/mapped/Nnnn-tetrakis_2-pyridylmethylethylenediamine.yaml`

## Verdict

Needs curation - major. The CAS-backed `CHEBI:88217` tetrakis compound
identity, structure block, reviewed synonym, and final SSSOM row pass, but
`CHELATOR` is still backed only by provisional CHEBI-ancestry inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Nnnn-tetrakis_2-pyridylmethylethylenediamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:88217` with
  `ontology_mapping.ontology_id: CHEBI:88217`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:88217` as active with formula
  `C26H28N6`, CAS `16858-02-9`, and the same InChI and SMILES as the record.
- A fresh PubChem lookup for CAS `16858-02-9` resolves to formula `C26H28N6`
  and the same InChI.
- The final SSSOM row maps the MIM subject exactly to `CHEBI:88217`; its
  `other` values are the reviewed ChEBI synonym plus `CAS:16858-02-9`.
- Major: `physicochemical_roles.CHELATOR` cites only a
  `COMPUTATIONAL_PREDICTION` from CHEBI is_a/has_role closure. The curator
  note marks the role as provisional and recommended for review, so it needs
  inspected source-backed chelation evidence before publication.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final
  SSSOM row otherwise agree.
- Empty CultureMech occurrence statistics are expected for this CultureBotHT
  source record.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Nnnn-tetrakis_2-pyridylmethylethylenediamine.yaml`,
  replace the `CHELATOR` role evidence with inspected source-backed chelation
  evidence, or remove the role until that evidence exists.
