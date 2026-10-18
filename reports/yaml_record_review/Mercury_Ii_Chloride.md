# `data/ingredients/mapped/Mercury_Ii_Chloride.yaml`

## Verdict

Pass. The CAS-grounded ChEBI identity, structure, exact synonyms, and final
SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mercury_Ii_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:31823` with
  `ontology_mapping.ontology_id: CHEBI:31823`, label `mercury dichloride`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 7487-94-7`, formula `Cl2Hg`, and InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Menthol` through `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:31823` as active `mercury dichloride` with CAS
  `7487-94-7`, formula `Cl2Hg`, the same InChI and SMILES carried in the YAML,
  and the two exact mercury-chloride synonyms curated in the record.
- PubChem resolves CAS `7487-94-7` to CID 24085 with formula `Cl2Hg` and the
  same InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mercury_Ii_Chloride` to `CHEBI:31823`; the two non-CAS `other` tokens
  are exact ChEBI synonyms and `CAS:7487-94-7` matches
  `chemical_properties.cas_rn`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
