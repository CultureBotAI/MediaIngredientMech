# `data/ingredients/mapped/Flavomycin.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The CAS-to-ChEBI
bambermycin grounding is documented and the final SSSOM synonyms are exact, but
`physicochemical_roles.SELECTIVE_AGENT` is still only a provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Flavomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28908` with matching
  `ontology_mapping.ontology_id`, canonical label `bambermycin`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `11015-37-5` resolved to CID 11953887 titled
  `Flavomycin` with formula `C69H107N4O35P` and the same InChI recorded under
  `chemical_properties`.
- The #317 curation history documents why `CAS_RN_LOOKUP` preserves the
  mapping method: CAS `11015-37-5` uniquely resolves by ChEBI xref to
  `CHEBI:28908`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Flavensomycin.yaml data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml data/ingredients/mapped/Flavofungin.yaml data/ingredients/mapped/Flavomycin.yaml data/ingredients/mapped/Flavone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flavomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, synonym, ingredient type,
  and provisional role evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Flavomycin` to `CHEBI:28908` with `skos:exactMatch`.
- The final SSSOM `other` column contains the long IUPAC name curated from
  ChEBI and `CAS:11015-37-5`; both denote the same CAS-backed bambermycin
  identity.
- Major: `physicochemical_roles.SELECTIVE_AGENT` was created by
  `infer_roles_from_name_lists` and has only `COMPUTATIONAL_PREDICTION`
  evidence with a curator note calling the name-pattern rule provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, OAK/OLS confirmation, CAS regrade provenance,
  and ignored historical batch reports.

## Completeness

- The exact CAS-backed ChEBI identity, CAS RN, structure fields, ingredient
  type, and final SSSOM synonym payload are populated.
- The record still needs source-backed evidence for the selective-agent role or
  removal of that role.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` in
  `data/ingredients/mapped/Flavomycin.yaml` with source-backed role evidence or
  remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun
  strict validation plus the final SSSOM invariant gates.
