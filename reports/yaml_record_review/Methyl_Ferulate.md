# `data/ingredients/mapped/Methyl_Ferulate.yaml`

## Verdict

Pass with minor issues. The CAS-primary methyl ferulate identity, exact ChEBI
row, CAS registry row, local chemistry, and final `other` synonyms pass, but the
generated CAS registry-row comment still describes `CHEBI:67379` as a parent
after the #326 same-formula regrade made it exact.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl_Ferulate.yaml`.
- Identifier and grounding: `identifier: cas:22329-76-6` with
  `ontology_mapping.ontology_id: CHEBI:67379`, label `trans-methylferulate`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `22329-76-6`, PubChem CID 5357283, formula
  `C11H12O4`, SMILES, and trans-configured InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Beta-D-glucopyranoside` through `Methyl_Jasmonate`: exited 0 and
  wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-mapped
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:67379` as active `trans-methylferulate` with formula
  `C11H12O4`, the same InChI carried in the YAML, and `Methyl ferulate` plus
  the curated IUPAC name as synonyms.
- PubChem resolves the YAML CAS `22329-76-6` to CID 5357283 with formula
  `C11H12O4` and the same trans-configured InChI as the YAML and ChEBI target.
- The OAK/OLS row-review manifest confirmed the `CHEBI:67379` row and kept the
  `cas:22329-76-6` row as an expected CAS registry identifier.
- The final SSSOM publishes an exact `CHEBI:67379` row whose `other` contains
  the curated IUPAC name and `CAS:22329-76-6`; it also publishes the expected
  exact CAS registry row.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.
- `find` found no local `compounds_to_cas.csv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for the label and CAS under
  this checkout found only curated records, generated products, backups, row
  reviews, and the #326 regrade script; ignored files were included.

## Recommended Edits

- Minor: update the SSSOM registry-row comment generation for exact
  CAS-primary synonym rows so it no longer says
  `Registry/identity row preserving cas:22329-76-6 alongside parent CHEBI:67379`
  when the companion `CHEBI:67379` row is exact. The maintained owner is the
  sibling `culturebotai-claw/scripts/build_mim_ingredient_sssom.py` builder.
