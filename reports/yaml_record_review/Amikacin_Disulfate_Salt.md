# `data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml`

## Verdict

Pass. The CAS-selected `CHEBI:2638` amikacin disulfate identity, exact disulfate
synonym, ChEBI/PubChem chemistry, row-review state, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:2638` with
  `ontology_mapping.ontology_id: CHEBI:2638`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2638` to
  `amikacin disulfate` with formula `C22H43N5O13.2H2O4S`, CAS `39831-55-5`,
  SMILES
  `NCC[C@H](O)C(=O)N[C@@H]1C[C@H](N)[C@@H](O[C@H]2O[C@H](CN)[C@@H](O)[C@H](O)[C@H]2O)[C@H](O)[C@H]1O[C@H]1O[C@H](CO)[C@@H](O)[C@H](N)[C@H]1O.O=S(=O)(O)O.O=S(=O)(O)O`,
  and InChIKey `FXKSEJFHKVNEFI-GCZBSULCSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml data/ingredients/mapped/Amicoumacin_B.yaml data/ingredients/mapped/Amikacin.yaml data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml data/ingredients/mapped/Amino_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned canonical `amikacin disulfate`, `amikacin bis(sulphate)`, and
  `amikacin disulphate` aliases for `CHEBI:2638`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:2638`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The creation history records a CultureBotHT CAS `39831-55-5` import resolved
  to `CHEBI:2638`; local ChEBI also cross-references the same CAS on
  `CHEBI:2638`.
- The `2026-08-24` regrade documents why `CAS_RN_LOOKUP` is preserved as
  mapping provenance while the SSSOM predicate remains `skos:exactMatch`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` says the proposed
  `Amikacin disulfate salt` surface is already represented, and the active YAML
  carries the exact structural disulfate synonym.
- `mappings/ingredient_mappings.sssom.tsv` row 391 maps
  `MIM:Amikacin_Disulfate_Salt` to `CHEBI:2638` with `skos:exactMatch`,
  `CAS:39831-55-5`, and the expected `SYNONYM_ENRICH` trailer.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, row-review files, generated reports, and the
  separate amikacin base record.

## Completeness

- CAS, formula, SMILES, InChI, exact disulfate synonym, mapping evidence,
  curation history, and `ingredient_type` are populated.
- No source occurrence, role, component, environmental context, discussion, or
  dataset entry is needed because the record came from a CultureBotHT CAS
  lookup with no retained recipe occurrence.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
