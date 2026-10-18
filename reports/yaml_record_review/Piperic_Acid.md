# `data/ingredients/mapped/Piperic_Acid.yaml`

## Verdict

Needs curation; major. The CAS registry identity and MeSH parent row are
internally consistent, but a fresh CHEBI search now finds a plausible
`CHEBI:37316` `(E,E)-piperic acid` promotion candidate that was unavailable
when this record was parked on a CAS primary.

## Identity

- Reviewed record: `data/ingredients/mapped/Piperic_Acid.yaml`.
- Identifier and grounding: `identifier: cas:5285-18-7` with
  `ontology_mapping.ontology_id: mesh:C017637`, label `piperic acid`, source
  `MESH`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `piperic acid` resolves `mesh:C017637`
  `piperic acid` and also returns `CHEBI:37316` `(E,E)-piperic acid` as a
  plausible CHEBI candidate.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C017637` as a resolved exact MeSH CURIE; the older `UNKNOWN_TERM`
  row-review result is a local OAK/OLS coverage artifact.
- A fresh PubChem lookup for the stored CID resolves CAS `5285-18-7` to
  5-(1,3-Benzodioxol-5-yl)-2,4-pentadienoic acid.
- The final SSSOM rows were inspected directly: they preserve the CAS registry
  identity, the local kg-microbe registry identity, and the MeSH parent.

## Evidence

- The CAS primary identifier, mapping target, CAS `5285-18-7`, PubChem CID,
  structured formula, SMILES, and InChI all describe piperic acid.
- The final SSSOM row exports no unsafe `other` tokens except the redundant
  `CAS:5285-18-7` on the exact CAS registry row.
- Major: the curation history says no CHEBI entry existed when this record was
  created, but a fresh CHEBI/MeSH search now finds the plausible
  stereospecific `CHEBI:37316` candidate. The stored PubChem structure lacks
  explicit double-bond stereochemistry, so that promotion needs curator review
  rather than automatic remapping.

## Completeness

- The registry rows are complete enough as a fallback.
- The primary CHEBI promotion remains unresolved while `CHEBI:37316` has not
  been triaged against CAS `5285-18-7`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Piperic_Acid.yaml`, evaluate whether CAS
  `5285-18-7` denotes `(E,E)-piperic acid`; if it does, promote the record from
  the CAS primary to `CHEBI:37316`, otherwise document why the stereospecific
  CHEBI candidate is not exact and keep the registry fallback.
