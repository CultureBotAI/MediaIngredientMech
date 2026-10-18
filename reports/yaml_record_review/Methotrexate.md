# `data/ingredients/mapped/Methotrexate.yaml`

## Verdict

Needs curation. The exact anhydrous ChEBI identity, formula, structure, and
IUPAC synonym pass, but the YAML and final SSSOM row carry a hydrate CAS value.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methotrexate.yaml`.
- Identifier and grounding: `identifier: CHEBI:44185` with
  `ontology_mapping.ontology_id: CHEBI:44185`, label `methotrexate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: the stored formula `C20H22N8O5`, InChI, and SMILES match
  anhydrous `CHEBI:44185`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methanol` through `Methyl-B-D-galactopyranoside`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:44185` as active `methotrexate` with CAS `59-05-2`,
  formula `C20H22N8O5`, the same InChI and SMILES carried in the YAML, and the
  curated IUPAC synonym.
- PubChem resolves the current YAML CAS `133073-73-1` to a hydrate with formula
  `C20H24N8O6` and an InChI that appends water to the anhydrous methotrexate
  layer.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methotrexate`
  to `CHEBI:44185`; the IUPAC `other` token is an exact ChEBI synonym, but
  `CAS:133073-73-1` does not belong to the anhydrous record.

## Completeness

- `chemical_properties.cas_rn` should identify the same anhydrous substance as
  the ChEBI mapping and structural fields. The current CAS erases a hydrate
  boundary in final SSSOM `other`.

## Recommended Edits

- Replace `chemical_properties.cas_rn: 133073-73-1` with the `CHEBI:44185` CAS
  `59-05-2`, or remove the CAS if the original CultureBotHT row actually meant
  a hydrate.
