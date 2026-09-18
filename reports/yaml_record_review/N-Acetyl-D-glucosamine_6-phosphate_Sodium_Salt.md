# `data/ingredients/mapped/N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt.yaml`

## Verdict

Needs curation. `CHEBI:15784` is active and the structure currently copied from
ChEBI matches that free acid, but the CultureBotHT label is a sodium salt and
is therefore not exact to the mapped ChEBI target.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:15784` with
  `ontology_mapping.ontology_id: CHEBI:15784`, label
  `N-acetyl-D-glucosamine 6-phosphate`, source `CHEBI`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Myo-inositol` through `N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt`:
  exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:15784` as active
  `N-acetyl-D-glucosamine 6-phosphate`; the exact ChEBI synonym on that term is
  also the free acid.
- A fresh PubChem lookup for `N-Acetyl-D-glucosamine 6-phosphate sodium salt`
  resolves a sodium-containing record with formula `C8H16NNaO9P`, distinct from
  the current ChEBI-derived `C8H16NO9P` formula in this record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-Acetyl-D-glucosamine_6-phosphate_Sodium_Salt` to the saltless ChEBI
  acid and carries a saltless ChEBI synonym in `other`.

## Completeness

- The current ChEBI target and structure agree with each other but not with the
  supplied sodium-salt form named by CultureBotHT.
- The source record has no CAS RN; the 2026-05-02 upgrade was only a stem match
  from the sodium salt label to the free-acid ChEBI term.

## Recommended Edits

- Major: re-ground the sodium salt as a distinct local
  `kgmicrobe.compound` identity, or replace `CHEBI:15784` with a
  form-specific ontology term if one becomes available.
- Major: preserve the `CHEBI:15784` free acid only as a broader parent, if the
  repository wants the sodium salt anchored to the parent acid, and remove the
  free-acid synonym from final SSSOM `other`.
