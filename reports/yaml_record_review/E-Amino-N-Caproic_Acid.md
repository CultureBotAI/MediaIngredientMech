# `data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml`

## Verdict

Needs curation. The ChEBI identity, CAS chemistry, aggregate copy, and final
SSSOM identity row agree, but the amino-acid-source role is still a provisional
CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16586` with matching
  `ontology_mapping.ontology_id`, canonical label `6-aminohexanoic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:16586` to
  `6-aminohexanoic acid`.
- PubChem resolved CAS RN `60-32-2` to CID 564 with formula `C6H13NO2` and
  the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml data/ingredients/mapped/Ebselen.yaml data/ingredients/mapped/Econazole_Nitrate_Salt.yaml --out /tmp/mim_e_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  identifier, ontology mapping, CAS RN, formula, InChI, SMILES, and
  `AMINO_ACID_SOURCE` role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:E-Amino-N-Caproic_Acid` to `CHEBI:16586` with `skos:exactMatch`, the
  canonical ChEBI object label, and only `CAS:60-32-2` in `other`; that CAS
  token belongs to the same supplied form.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `CHEBI:16586`, `60-32-2`, and the MIM
  subject found the active YAML, aggregate copy, final SSSOM row, and expected
  row-review TSVs; it did not expose a contradictory active mapping.
- The only role evidence is
  `reference_type: COMPUTATIONAL_PREDICTION` from
  `infer_roles_from_chebi_ancestry`, with a curator note explicitly marking
  the role provisional.

## Completeness

- Identity, CAS RN, formula, InChI, SMILES, mapping history, and SSSOM synonym
  payload are complete for the represented compound.
- Occurrence counts are zero, and no source occurrence list is present; no
  checked row in `mappings` showed a CultureMech recipe occurrence for this
  CAS or MIM subject.

## Recommended Edits

- Major: in `data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml`, either
  replace the provisional `nutritional_roles.AMINO_ACID_SOURCE` evidence with
  claim-level support that 6-aminohexanoic acid is used as an amino acid source
  in MIM media, or remove the role. After changing the per-record YAML, run
  `sync-curated`, rebuild SSSOM if a synonym or identity payload changed, and
  rerun `validate-all`, `qc-sssom`, and the strict validator.
