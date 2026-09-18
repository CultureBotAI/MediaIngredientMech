# `data/ingredients/mapped/HOMOPIPES.yaml`

## Verdict

Needs curation. The CAS fallback identity, PubChem structure, occurrence count,
and local final SSSOM row pass, but the final synonym export includes a
comma-joined synonym and a Sigma catalog variant, and the `BUFFER` role is only
an in-session computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/HOMOPIPES.yaml`.
- Identifier and grounding: `identifier: cas:202185-84-0` with
  `ontology_mapping.ontology_id: cas:202185-84-0`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `202185-84-0`, PubChem CID `4389145`, formula
  `C9H20N2O6S2`, InChI
  `InChI=1S/C9H20N2O6S2/c12-18(13,14)8-6-10-2-1-3-11(5-4-10)7-9-19(15,16)17/h1-9H2,(H,12,13,14)(H,15,16,17)`,
  and SMILES `C1CN(CCN(C1)CCS(=O)(=O)O)CCS(=O)(=O)O`.
- Occurrence statistics: `total_occurrences: 5` and `media_count: 5`.
- Role facet: `BUFFER` with `COMPUTATIONAL_PREDICTION` evidence from
  provisional in-session Claude reasoning.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H3bo3.yaml data/ingredients/mapped/HOMOPIPES.yaml data/ingredients/mapped/Haemin.yaml data/ingredients/mapped/Halomicin.yaml data/ingredients/mapped/Hans_1000x_Minerals.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because this record is a
  CAS-primary fallback outside the OBO subset used in this batch.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- PubChem resolves CAS `202185-84-0` to CID `4389145`, matching this record.
- Fresh OLS4 exact search for `HOMOPIPES` found no ChEBI term, so the
  CAS-primary fallback remains appropriate.
- The final SSSOM preserves one exact CAS registry row from `MIM:HOMOPIPES` to
  `cas:202185-84-0`, and the final `CAS:202185-84-0` token matches
  `chemical_properties.cas_rn`.
- Major: the YAML stores
  `homopiperazine-1,4-bis(2-ethanesulfonic acid), HOMO-PIPES` as one synonym,
  and final SSSOM exports that comma-joined string as a single exact synonym
  instead of two labels.
- Major: `Homo-PIPES (SIGMA)` is a vendor catalog surface form, not an exact
  synonym of the CAS reagent, and it is exported in final SSSOM.
- Major: the `BUFFER` facet is supported only by
  `reference_type: COMPUTATIONAL_PREDICTION` from an in-session LLM note.

## Completeness

- The CAS fallback identifier, CAS RN, PubChem CID, formula, InChI, SMILES, and
  final local SSSOM row are present and consistent.
- The role facet and synonym list remain incomplete until the provisional buffer
  role and non-exact final synonyms are curated.

## Recommended Edits

- Major: split the comma-joined HOMOPIPES synonym into separate exact labels and
  suppress or retype `Homo-PIPES (SIGMA)` so it no longer appears in final SSSOM
  as an exact synonym.
- Major: review the `BUFFER` facet and either replace the provisional in-session
  evidence with an external source or remove the unsupported role.
