# `data/ingredients/mapped/Monensin.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:27617` monensin A identity, structure, CAS
provenance, final `CAS:` alias, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Monensin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27617` with
  `ontology_mapping.ontology_id: CHEBI:27617`, label `monensin A`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Modified_Wolfes_Minerals` through `Mono-_And_Disaccharides`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:27617` as active `monensin A` with
  `Monensin` and `monensin` as synonyms.
- The CultureBotHT CAS `17090-79-8` resolves in PubChem to the same
  `C36H62O11` formula and InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Monensin` to
  `CHEBI:27617`; its `other` tokens are the ChEBI IUPAC synonym and
  `CAS:17090-79-8`.

## Completeness

- The active ChEBI target, CAS lookup provenance, formula, InChI, CAS RN, and
  final exact row agree.
- The record does not assert unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
