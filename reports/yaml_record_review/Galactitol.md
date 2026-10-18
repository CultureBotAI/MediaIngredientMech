# `data/ingredients/mapped/Galactitol.yaml`

## Verdict

Pass. The MicrobeDecoder galactitol record maps to the exact active ChEBI
chemical, its ChEBI-backed structure fields agree with OLS and PubChem, and the
final SSSOM `Dulcitol (galactitol)` surface is a valid same-substance raw
label.

## Identity

- Reviewed record: `data/ingredients/mapped/Galactitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16813` with matching
  `ontology_mapping.ontology_id`, canonical label `galactitol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:16813` as an active ChEBI term with formula `C6H14O6`,
  InChI `InChI=1S/C6H14O6/c7-1-3(9)5(11)6(12)4(10)2-8/h3-12H,1-2H2/t3-,4+,5+,6-`,
  SMILES `OC[C@@H](O)[C@H](O)[C@H](O)[C@@H](O)CO`, and related synonym
  `Dulcitol`.
- PubChem lookup by ChEBI's CAS xref `608-66-2` resolved to CID 11850 with
  formula `C6H14O6` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml data/ingredients/mapped/GYPS.yaml data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder source occurrence, CultureMech occurrence,
  raw backfilled synonym, structure fields, and ingredient type as the
  per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved this
  exact ChEBI row after OAK resolved the identifier and matched the canonical
  label.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Galactitol` to `CHEBI:16813` with `skos:exactMatch` and exports only
  `Dulcitol (galactitol)` in `other`; both terms inside that raw label resolve
  to the same ChEBI subject.
- The record has no inferred nutritional, physicochemical, component, or
  environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MicrobeDecoder approval row, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact galactitol identity, single-ingredient type, structure fields,
  MicrobeDecoder and CultureMech occurrence counts, raw same-subject surface
  label, and final SSSOM row are populated.
- I found no consequential missing CAS, role, component, environment, or
  synonym payload.

## Recommended Edits

- None.
