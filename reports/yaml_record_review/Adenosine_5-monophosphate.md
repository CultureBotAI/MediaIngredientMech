# `data/ingredients/mapped/Adenosine_5-monophosphate.yaml`

## Verdict

Pass. The exact `CHEBI:16027` identity, AMP raw synonym, MicrobeDecoder source
occurrence, ChEBI chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Adenosine_5-monophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16027` with
  `ontology_mapping.ontology_id: CHEBI:16027`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16027` to
  `adenosine 5'-monophosphate` with formula `C10H14N5O7P`, CAS `61-19-8`,
  SMILES, InChI, and InChIKey `UDMBCSSLTHHNCD-KQYNXXCUSA-N`.
- Local OAK lists `AMP` as a ChEBI alias, matching the retained `Amp` raw
  synonym from MicrobeDecoder.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml data/ingredients/mapped/Adenomycin.yaml data/ingredients/mapped/Adenosine.yaml data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml data/ingredients/mapped/Adenosine_5-monophosphate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenosine_5-monophosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned the expected labels and aliases for the ChEBI targets in this batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned formula and structure metadata for all four ChEBI terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The MicrobeDecoder exact-label import and official ChEBI record support the
  exact `CHEBI:16027` identity.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the manual
  review-ingredients approval that promoted this exact ChEBI label match from
  `PENDING_REVIEW` to `MAPPED`.
- The `Amp` duplicate merge is documented in the 2026-08-06 history entry and
  matches the `AMP` ChEBI alias.
- `mappings/ingredient_mappings.sssom.tsv` row 349 maps
  `MIM:Adenosine_5-monophosphate` to `CHEBI:16027` with `skos:exactMatch` and
  the manual approval trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, MicrobeDecoder approval row, generated indexes, and ignored
  aggregate backups.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation history,
  and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
