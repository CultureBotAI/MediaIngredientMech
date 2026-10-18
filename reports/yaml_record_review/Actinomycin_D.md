# `data/ingredients/mapped/Actinomycin_D.yaml`

## Verdict

Needs curation. The exact `CHEBI:27666` identity, CAS-backed chemistry, and
exact ChEBI synonym pass, but the record still carries an unsupported
`SELECTIVE_AGENT` role and a recovered `actinomycin B` raw surface that is not
an exact actinomycin D synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Actinomycin_D.yaml`.
- Identifier and grounding: `identifier: CHEBI:27666` with
  `ontology_mapping.ontology_id: CHEBI:27666`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:27666` to
  `actinomycin D` with formula `C62H86N12O16`, CAS `50-76-0`, SMILES, InChI,
  and InChIKey `RJURFGZVJUQBHK-IIXSONLDSA-N`.
- Local OAK lists the stored long systematic name as an exact ChEBI synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Actinomycin_D.yaml data/ingredients/mapped/Actinomycin_X.yaml data/ingredients/mapped/Actinotiocin.yaml data/ingredients/mapped/Activated_Charcoal.yaml data/ingredients/mapped/Adenine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Actinomycin_D.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27666 CHEBI:16708`:
  returned the expected labels and exact synonyms for actinomycin D and
  adenine.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27666 CHEBI:16708`:
  returned formula and structure metadata for both ChEBI terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS import, official ChEBI record, and local OAK metadata
  support the exact actinomycin D identity and CAS `50-76-0`.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, and InChI.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms `CHEBI:27666`;
  `mappings/ingredient_mappings.sssom.tsv` row 339 maps
  `MIM:Actinomycin_D` to `CHEBI:27666` with the confirmed trailer.
- The `physicochemical_roles.SELECTIVE_AGENT` row is only a name-pattern
  prediction; no inspected source supports actinomycin D as a selective medium
  agent.
- The `actinomycin B` RAW_TEXT synonym is a separate KGX surface recovered by
  `sssom_other_backfill`, not a ChEBI exact synonym of `CHEBI:27666`; keeping it
  on the actinomycin D identity would republish an adjacent antibiotic label in
  the SSSOM `other` column.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, OAK/OLS confirmation row, generated indexes, and ignored
  aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, exact ChEBI synonym, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Actinomycin_D.yaml`, remove or evidence the
  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion.
- Remove the `actinomycin B` raw surface from the `Actinomycin_D` exact identity
  unless a curator can show that it is safe to export as a source surface for
  this record.
- Optionally annotate the stale 2026-05-01 history `changes` prose; the active
  `chemical_properties` fields are already correct.
