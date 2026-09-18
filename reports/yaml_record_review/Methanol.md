# `data/ingredients/mapped/Methanol.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, structure, occurrence
count, and ChEBI-derived synonyms pass, but final SSSOM `other` still exports
asterisked and concentration-qualified raw CultureMech labels as synonyms.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17790` with
  `ontology_mapping.ontology_id: CHEBI:17790`, label `methanol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 251 CultureMech recipes.
- Chemical identity: `cas_rn: 67-56-1`, formula `CH4O`, and InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methanol` through `Methyl-B-D-galactopyranoside`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:17790` as active `methanol` with CAS `67-56-1`,
  formula `CH4O`, the same InChI and SMILES carried in the YAML, and the
  exact synonyms exported in final `other`.
- PubChem resolves CAS `67-56-1` to CID 887 with formula `CH4O` and the same
  InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methanol` to
  `CHEBI:17790`. The ChEBI and CAS `other` tokens pass, but `Methanol*`,
  `Methanol**`, and `Methanol (10%)` are raw source forms rather than exact
  synonyms.

## Completeness

- The raw CultureMech role/property and KEGG cross-reference synonyms remain in
  YAML as provenance but are filtered from final SSSOM.
- The asterisked and 10 percent methanol labels are CultureMech occurrence
  surfaces. They should remain provenance-only and should not be exported as
  same-substance labels in final `other`.

## Recommended Edits

- Mark `Methanol*`, `Methanol**`, and `Methanol (10%)` as non-resolving
  provenance or extend the synonym policy to filter footnote- and
  concentration-qualified raw labels from final SSSOM `other`.
