# `data/ingredients/mapped/Maleic_Acid.yaml`

## Verdict

Needs curation. The exact ChEBI identity, corrected CAS number, structure, and
IUPAC synonym pass, but the final SSSOM exports a comma-joined pair of
synonyms as one `other` token.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maleic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18300` with
  `ontology_mapping.ontology_id: CHEBI:18300`, label `maleic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four total occurrences in four CultureMech recipes.
- Chemical identity: `cas_rn: 110-16-7`, formula `C4H4O4`, InChI and SMILES
  copied from ChEBI after the erroneous EC number was corrected in issue 114.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malate` through `Malondialdehyde_Tetrabutylammonium_Salt`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:18300` as active `maleic acid` with CAS
  `110-16-7`, formula `C4H4O4`, and the same InChI and SMILES carried in the
  YAML.
- ChEBI carries `cis-Butenedioic acid` and `toxilic acid` separately as
  related synonyms, and `(2Z)-but-2-enedioic acid` as an exact IUPAC synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Maleic_Acid` to `CHEBI:18300`; its `other` field contains
  `cis-Butenedioic acid, Toxilic acid`, `(2Z)-but-2-enedioic acid`, and
  `CAS:110-16-7`.

## Completeness

- The primary identity, structure, and CAS are exact.
- `(2Z)-but-2-enedioic acid` is a real exact synonym and is safe to publish.
- `cis-Butenedioic acid, Toxilic acid` is a CultureBotHT comma-separated pair
  of two synonyms, not a single surface form for maleic acid. Publishing it as
  one final `other` token violates the final SSSOM synonym contract.

## Recommended Edits

- Split `cis-Butenedioic acid, Toxilic acid` into two synonym entries or reject
  the bundled text so final SSSOM emits only atomic maleic-acid synonyms.
