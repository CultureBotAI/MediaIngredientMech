# `data/ingredients/mapped/Mucic_Acid.yaml`

## Verdict

Needs curation. The CAS-backed `CHEBI:30852` galactaric acid identity,
structure, ChEBI synonyms, and final exact row pass, but the carbon-source role
is only a provisional ChEBI-ancestry prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mucic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30852` with
  `ontology_mapping.ontology_id: CHEBI:30852`, label `galactaric acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MreB_Perturbing_Compound_A22` through
  `Mucin_From_Porcine_StomachType_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30852` as active `galactaric acid`;
  the final `other` tokens for the IUPAC form and `meso-galactaric acid` are
  exact ChEBI synonyms for this term.
- A fresh PubChem lookup for CAS `526-99-8` returns formula `C6H10O8` and the
  same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mucic_Acid` to
  `CHEBI:30852` with same-substance synonyms and `CAS:526-99-8` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, ChEBI synonyms, and final row
  agree.
- `CARBON_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI-ancestry closure with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that mucic acid is used as a carbon source
  in media, or remove the provisional `CARBON_SOURCE` role.
