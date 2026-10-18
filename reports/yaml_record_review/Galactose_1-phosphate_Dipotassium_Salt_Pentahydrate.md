# `data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml`

## Verdict

Needs curation, with major hydrate-structure and unsupported-role issues. The
CAS identity, close parent mapping to alpha-D-galactose 1-phosphate, and final
SSSOM registry row pass, but the stored PubChem structure is the anhydrous
dipotassium salt instead of the named pentahydrate, and `CARBON_SOURCE` is only
a provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml`.
- Identifier and grounding: `identifier: cas:19046-60-7` with
  `ontology_mapping.ontology_id: CHEBI:17973`, canonical label
  `alpha-D-galactose 1-phosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:17973` as active alpha-D-galactose 1-phosphate, the
  intentionally broader anhydrous parent.
- PubChem lookup by CAS RN `19046-60-7` returned CID 2733780 titled
  `alpha-D-Galactose 1-phosphate dipotassium salt pentahydrate` with formula
  `C6H21K2O14P`; the record instead stores CID 87916, formula `C6H11K2O9P`,
  and an InChI for the anhydrous dipotassium salt.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Galactomannan_From_Guar.yaml data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml data/ingredients/mapped/Galacturonate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this CAS-primary registry record
  because Engine A/OBO term validation does not cover CAS registry CURIEs.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same CAS
  identifier, close ChEBI parent, CAS RN, anhydrous PubChem structure,
  provisional carbon role, and ingredient type as the per-record YAML.
- `mappings/hydrate_review.tsv` classifies the CAS identity as a hydrate-specific
  registered commercial crystal form and marks the CAS identity correct.
- The final `mappings/ingredient_mappings.sssom.tsv` output has a
  `skos:closeMatch` parent row to `CHEBI:17973` and an exact CAS registry row;
  both rows publish only `CAS:19046-60-7` in `other`.
- Major: the record name is pentahydrate-specific, but `chemical_properties`
  stores the anhydrous dipotassium salt CID, formula, SMILES, and InChI; the
  PubChem CID matching the named pentahydrate is 2733780.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note; no inspected source in the record supports the
  dipotassium pentahydrate as a medium carbon source.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  rows, hydrate review row, row-review decision, and expected CAS unknown-term
  triage row.

## Completeness

- The CAS RN, exact CAS registry row, close parent mapping, and CultureBotHT
  provenance are populated.
- The water-of-hydration structure fields need correction to match the
  pentahydrate subject.

## Recommended Edits

- Major: replace `pubchem_cid: 87916` and the anhydrous formula, SMILES, and
  InChI in
  `data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml`
  with the PubChem pentahydrate identity, then sync
  `data/curated/mapped_ingredients.yaml`.
- Major: replace the provisional `CARBON_SOURCE` role with source-backed
  evidence or remove it.
- Regenerate final SSSOM and rerun strict validation plus SSSOM invariants.
