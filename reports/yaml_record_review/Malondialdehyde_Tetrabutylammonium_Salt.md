# `data/ingredients/mapped/Malondialdehyde_Tetrabutylammonium_Salt.yaml`

## Verdict

Pass. The CAS-primary exact identity, PubChem structure, broader ChEBI parent,
registry companion rows, and final SSSOM output all pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Malondialdehyde_Tetrabutylammonium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:100683-54-3` with
  `ontology_mapping.ontology_id: CHEBI:51992`, label
  `tetrabutylammonium salt`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 100683-54-3`, PubChem CID 13707375, formula
  `C19H39NO2`, InChI and SMILES from PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malate` through `Malondialdehyde_Tetrabutylammonium_Salt`: exited 0 and
  wrote zero ERROR rows.
- LinkML term validation was skipped for this CAS-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- PubChem resolves CAS `100683-54-3` to CID 13707375 with formula
  `C19H39NO2` and the same InChI carried in the YAML.
- EBI OLS4 resolves `CHEBI:51992` as active `tetrabutylammonium salt`, a
  broader parent with no exact ChEBI term for malondialdehyde
  tetrabutylammonium salt.
- A current exact OLS search for `Malondialdehyde tetrabutylammonium salt`
  returned no ChEBI hits, so the CAS-primary narrow parent remains justified.
- The final SSSOM publishes the parent `skos:narrowMatch` row to
  `CHEBI:51992`, the exact CAS row to `cas:100683-54-3`, and the exact Rule B1
  local registry row to
  `kgmicrobe.compound:malondialdehyde_tetrabutylammonium_salt`.

## Completeness

- The CAS and local registry rows preserve the exact identity while the ChEBI
  row stays explicitly broader.
- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
