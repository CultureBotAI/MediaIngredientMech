# `data/ingredients/mapped/Methylene_Blue.yaml`

## Verdict

Needs curation. The exact `CHEBI:6872` methylene-blue identity, CAS value,
ChEBI/PubChem structure, kg-microbe synonyms, occurrence count, and final SSSOM
row pass, but the `REDOX_INDICATOR` role is still a provisional in-session LLM
assignment with no external source.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylene_Blue.yaml`.
- Identifier and grounding: `identifier: CHEBI:6872` with
  `ontology_mapping.ontology_id: CHEBI:6872`, label `methylene blue`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four CultureMech recipe occurrences.
- Chemical identity: CAS `61-73-4`, formula `C16H18N3S.Cl`, SMILES, and InChI
  for methylene blue.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methylene_Blue` through `Methylxanthoxylin`: exited 0 and wrote zero ERROR
  rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:6872` as active `methylene blue` with CAS
  `61-73-4`, formula `C16H18N3S.Cl`, the same SMILES and InChI carried in the
  YAML, and the kg-microbe aliases as synonyms.
- PubChem resolves CAS `61-73-4` to CID 6099 with the same formula and InChI
  carried in the YAML.
- The OAK/OLS row-review manifest confirmed the identity with no curation
  action.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylene_Blue` to `CHEBI:6872`; its `other` column excludes the raw
  `Properties:` import string and keeps exact aliases plus `CAS:61-73-4`.
- The `physicochemical_roles.REDOX_INDICATOR` evidence is a
  `COMPUTATIONAL_PREDICTION` that explicitly says it came from in-session
  Claude reasoning and recommends review.

## Completeness

- The chemical identity, occurrence count, and final SSSOM synonyms are
  complete enough.

## Recommended Edits

- Major: either replace the provisional `REDOX_INDICATOR` evidence in
  `data/ingredients/mapped/Methylene_Blue.yaml` with a source that directly
  supports methylene blue as a media redox indicator, or remove the role; then
  sync `data/curated/mapped_ingredients.yaml` and rerun role/SSSOM validation.
