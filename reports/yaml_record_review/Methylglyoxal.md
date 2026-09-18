# `data/ingredients/mapped/Methylglyoxal.yaml`

## Verdict

Needs curation. The exact `CHEBI:17158` methylglyoxal identity, formula,
structure, ChEBI synonym, and final SSSOM predicate pass, but the YAML and final
SSSOM publish the wrong CAS value.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylglyoxal.yaml`.
- Identifier and grounding: `identifier: CHEBI:17158` with
  `ontology_mapping.ontology_id: CHEBI:17158`, label `methylglyoxal`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: formula `C3H4O2`, SMILES, and InChI for methylglyoxal.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methylene_Blue` through `Methylxanthoxylin`: exited 0 and wrote zero ERROR
  rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:17158` as active `methylglyoxal` with formula
  `C3H4O2`, the same SMILES and InChI carried in the YAML, the curated
  `2-Oxopropanal` synonym, and CAS `78-98-8`.
- PubChem resolves CAS `78-98-8` to CID 880 with the same formula and InChI as
  the YAML and ChEBI target.
- PubChem returned no CID for the record's current CAS `79-98-8`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylglyoxal` to `CHEBI:17158`; its `other` column includes the valid
  ChEBI synonym but also exports the bad `CAS:79-98-8` token.

## Completeness

- The record has enough structure and synonym support once the CAS value is
  corrected.

## Recommended Edits

- Major: change `chemical_properties.cas_rn` in
  `data/ingredients/mapped/Methylglyoxal.yaml` from `79-98-8` to `78-98-8`,
  sync `data/curated/mapped_ingredients.yaml`, regenerate the final SSSOM so
  `other` publishes `CAS:78-98-8`, and rerun
  `scripts/validate_sssom_invariants.py`.
