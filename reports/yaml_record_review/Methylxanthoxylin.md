# `data/ingredients/mapped/Methylxanthoxylin.yaml`

## Verdict

Pass with minor issues. The CAS-primary methylxanthoxylin identity, exact ChEBI
row, CAS registry row, local chemistry, and final `other` synonyms pass, but the
generated CAS registry-row comment still describes `CHEBI:169463` as a parent
after the #326 same-formula regrade made it exact.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylxanthoxylin.yaml`.
- Identifier and grounding: `identifier: cas:23121-32-6` with
  `ontology_mapping.ontology_id: CHEBI:169463`, label
  `2'-Hydroxy-4',6'-dimethoxy-3'-methylacetophenone`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `23121-32-6`, PubChem CID 326186, formula `C11H14O4`,
  SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methylene_Blue` through `Methylxanthoxylin`: exited 0 and wrote zero ERROR
  rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-mapped
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:169463` as active
  `2'-Hydroxy-4',6'-dimethoxy-3'-methylacetophenone` with formula `C11H14O4`,
  the same InChI carried in the YAML, and the curated IUPAC synonym.
- PubChem CID 326186 has formula `C11H14O4` and the same InChI as the YAML and
  ChEBI target.
- The OAK/OLS row-review manifest confirmed the `CHEBI:169463` row through
  synonym enrichment and kept the `cas:23121-32-6` row as an expected CAS
  registry identifier.
- The final SSSOM publishes an exact `CHEBI:169463` row whose `other` contains
  the curated IUPAC name and `CAS:23121-32-6`; it also publishes the expected
  exact CAS registry row.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `rg --no-ignore --hidden --glob '!.git'` for the label and CAS under this
  checkout found only curated records, generated products, backups, row reviews,
  and the #326 regrade script; ignored files were included.

## Recommended Edits

- Minor: update the SSSOM registry-row comment generation for exact
  CAS-primary synonym rows so it no longer says
  `Registry/identity row preserving cas:23121-32-6 alongside parent CHEBI:169463`
  when the companion `CHEBI:169463` row is exact. The maintained owner is the
  sibling `culturebotai-claw/scripts/build_mim_ingredient_sssom.py` builder.
