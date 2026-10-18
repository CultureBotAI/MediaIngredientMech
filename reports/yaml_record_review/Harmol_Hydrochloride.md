# `data/ingredients/mapped/Harmol_Hydrochloride.yaml`

## Verdict

Pass. The CAS fallback identity, PubChem structure fields, and final local SSSOM
row are internally consistent, and no exact ChEBI term is currently available.

## Identity

- Reviewed record: `data/ingredients/mapped/Harmol_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:40580-83-4` with
  `ontology_mapping.ontology_id: cas:40580-83-4`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `40580-83-4`, PubChem CID `94507`, formula
  `C12H11ClN2O`, InChI
  `InChI=1S/C12H10N2O.ClH/c1-7-12-10(4-5-13-7)9-3-2-8(15)6-11(9)14-12;/h2-6,13-14H,1H3;1H`,
  and SMILES `CC1=C2C(=C3C=CC(=O)C=C3N2)C=CN1.Cl`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Harmol.yaml data/ingredients/mapped/Harmol_Hydrochloride.yaml data/ingredients/mapped/Hcl.yaml data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml data/ingredients/mapped/Hecogenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because this record is a
  CAS-primary fallback outside the OBO subset used in this batch.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- PubChem resolves CAS `40580-83-4` to CID `94507`, matching this record.
- Fresh OLS4 exact search for `Harmol Hydrochloride` found no ChEBI term, so
  the CAS-primary fallback remains appropriate.
- The final SSSOM publishes one exact CAS registry row from
  `MIM:Harmol_Hydrochloride` to `cas:40580-83-4`; the final `CAS:40580-83-4`
  token matches `chemical_properties.cas_rn`.
- The unknown-term row review keeps the CAS registry identifier as the expected
  fallback while no OAK/OLS ontology term exists for the CAS CURIE.

## Completeness

- The CAS fallback identifier, CAS RN, PubChem CID, formula, InChI, SMILES, and
  final CAS registry SSSOM row are present and consistent.

## Recommended Edits

- None.
