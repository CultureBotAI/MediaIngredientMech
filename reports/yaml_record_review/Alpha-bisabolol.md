# `data/ingredients/mapped/Alpha-bisabolol.yaml`

## Verdict

Needs curation. The exact `CHEBI:125` stereospecific `(-)-alpha-Bisabolol`
identity, CAS xref, chemistry, SSSOM row, and aggregate copy pass, but the
generic `Bisabolol` surface is stored and exported as an exact synonym even
though ChEBI treats `bisabolol` only as a related synonym of this term.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-bisabolol.yaml`.
- Identifier and grounding: `identifier: CHEBI:125` with
  `ontology_mapping.ontology_id: CHEBI:125`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:125` to
  `(-)-alpha-Bisabolol` with formula `C15H26O`, CAS `23089-26-1`, SMILES
  `[H][C@@]1([C@@](C)(O)CCC=C(C)C)CC=C(C)CC1`, and InChIKey
  `RGZSQWQPBWRIAQ-CABCVRRESA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-Tocopherol.yaml data/ingredients/mapped/Alpha-aminobutyrate.yaml data/ingredients/mapped/Alpha-bisabolol.yaml data/ingredients/mapped/Alpha-d-glucose.yaml data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-bisabolol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned canonical `(-)-alpha-Bisabolol`; `bisabolol` was present as only a
  related synonym, not an exact synonym.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:125`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` row 7 confirmed the
  old `MIM:~28-~29-alpha-bisabolol` row to `CHEBI:125`; the
  `MIM:Alpha-bisabolol` alias is recorded in `mappings/mim_curie_aliases.tsv`.
- `mappings/ingredient_mappings.sssom.tsv` row 378 maps
  `MIM:Alpha-bisabolol` to `CHEBI:125` with `skos:exactMatch` and CAS
  `23089-26-1`, but exports `Bisabolol` in `other`.
- The exact `(-)-alpha-bisabolol` preferred term and CAS-specific structure are
  supported by ChEBI; the unspecific `Bisabolol` synonym is broader than the
  stereospecific CHEBI ID.
- The ChEBI page and local ChEBI metadata support the stored CAS, formula,
  SMILES, and InChI.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, alias row, OAK/OLS confirmation row,
  generated indexes, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, curation history, and `ingredient_type` are
  populated.
- `occurrence_statistics` is correctly `0/0` because the record comes from
  CultureBotHT rather than from CultureMech recipe membership.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` history event has truncated InChI and
  SMILES prose, but the current `chemical_properties` values are complete.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove `Bisabolol` from
  `data/ingredients/mapped/Alpha-bisabolol.yaml` or demote it to a non-exact
  synonym type that the SSSOM exporter does not publish as `other`.
- Optionally replace the truncated auto-backfill `changes` prose with a
  complete structure summary or a concise non-structural note.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-bisabolol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
