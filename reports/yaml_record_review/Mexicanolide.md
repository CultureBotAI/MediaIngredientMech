# `data/ingredients/mapped/Mexicanolide.yaml`

## Verdict

Pass. The CAS-primary Mexicanolide identity, MeSH parent mapping, expected CAS
and kg-microbe registry companion rows, prefix-specific MeSH validation, and
final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mexicanolide.yaml`.
- Identifier and grounding: `identifier: cas:1915-67-9` with
  `ontology_mapping.ontology_id: mesh:C554989`, label `mexicanolide`, source
  `MESH`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `1915-67-9`; PubChem resolves that CAS to CID
  21596309.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Metronidazole` through `MgO`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH-parent
  CAS-primary record.

## Evidence

- EBI OLS4 MeSH exact search resolves `mesh:C554989` as active
  `mexicanolide`.
- EBI OLS4 ChEBI exact search for `mexicanolide` did not return a same-label
  ChEBI class; the only ChEBI hit was `CHEBI:68370` `trichanolide`, whose text
  mentions a mexicanolide-type skeleton.
- PubChem resolves CAS `1915-67-9` to CID 21596309 with formula `C27H32O7`,
  SMILES, and InChI, supporting the local CAS identity.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` keeps the
  `mesh:C554989` row as a missing-prefix validator coverage issue because the
  prefix-specific OLS query resolves the exact CURIE. It also keeps the
  `cas:1915-67-9` and `kgmicrobe.compound:mexicanolide` rows as expected
  registry identities.
- The final SSSOM publishes a narrow MeSH row plus exact CAS and kg-microbe
  registry rows for `MIM:Mexicanolide`; the exact companion rows carry only
  `CAS:1915-67-9` in `other`.

## Completeness

- The CAS primary identifier, MeSH parent, exact registry companion rows, zero
  occurrence count, and final SSSOM rows are populated and agree.

## Recommended Edits

- None.
