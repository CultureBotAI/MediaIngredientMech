# `data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml`

## Verdict

Pass. The MicrobeDecoder ONPG surface exact-maps to active `CHEBI:90144`, and
the final SSSOM `other` token is the corrected same-substance spelling.

## Identity

- Reviewed record:
  `data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml`.
- Identifier and grounding: `identifier: CHEBI:90144` with
  `ontology_mapping.ontology_id: CHEBI:90144`, label
  `2-nitrophenyl beta-D-galactoside`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: the imported spelling without a trailing `e`, plus curated
  `O-nitrophenyl-beta-D-galactopyranoside` from the SSSOM surface-form
  backfill.
- Occurrences: eight MicrobeDecoder source-column occurrences across
  `BacDive_Metabolite_production` and `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:90144` as active
  `2-nitrophenyl beta-D-galactoside`, lists
  `o-nitrophenyl beta-D-galactopyranoside` as a synonym, and reports formula
  `C12H15NO8`, CAS xref `369-07-3`, and the same InChI and SMILES stored in
  the YAML.
- `mappings/record_research_validation.tsv` still contains stale P1 rows from
  pre-promotion report disagreement, but its cross-lane row records that the
  Edison UNMAPPED recommendation was cleared after the Claude lane confirmed
  `CHEBI:90144`.
- The final SSSOM row maps `MIM:O-nitrophenyl-beta-D-galactopyranosid`
  exactly to `CHEBI:90144`; its single `other` token is the corrected trailing
  `e` spelling already curated in YAML.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, synonym-backed label, formula, structure, and final
  SSSOM synonym agree.
- The only plausible old unresolved local row is the P3 missing-CAS note in
  `mappings/record_research_validation.tsv`; CAS is optional here and the
  record already carries the ChEBI-backed formula, InChI, and SMILES.

## Recommended Edits

- None for this record.
