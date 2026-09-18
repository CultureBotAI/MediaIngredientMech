# `data/ingredients/mapped/Mezlocillin.yaml`

## Verdict

Pass. The exact `CHEBI:6919` mezlocillin identity, MicrobeDecoder review,
local ChEBI/PubChem structure, ingredient type, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mezlocillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6919` with
  `ontology_mapping.ontology_id: CHEBI:6919`, label `mezlocillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: three MicrobeDecoder source occurrences from
  `BacDive_Antibiotic_sensitivity`.
- Chemical identity: formula `C21H25N5O8S2`, SMILES, InChI, and molecular
  weight.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Metronidazole` through `MgO`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:6919` as active `mezlocillin` and distinguishes it
  from the anion, sodium salt, and sodium monohydrate sibling terms.
- PubChem resolves mezlocillin to CID 656511 with formula `C21H25N5O8S2`,
  molecular weight `539.6`, and the same InChI carried in the YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Mezlocillin.yaml` after confirming the OAK-resolved canonical label matched
  `mezlocillin`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mezlocillin`
  to `CHEBI:6919` with empty `other`.

## Completeness

- The record does not publish unsupported roles, stale CAS values, or
  non-exact synonyms.

## Recommended Edits

- None.
