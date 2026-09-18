# `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`

## Verdict

Needs curation, major. The CAS identity and close match to anhydrous
2-oxoglutaric acid are intentionally preserved, but the stored chemistry does
not include hydrate water, a neutral-acid label is exported as an exact `other`
surface, and the carbon-source and energy-source roles remain provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:305-72-6` with
  `ontology_mapping.ontology_id: CHEBI:30915`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- PubChem maps CAS `305-72-6` to CID `31040` with formula `C5H4Na2O5`, the
  stored disodium 2-oxoglutarate InChI, and no water term in the formula.
- The official ChEBI page resolves `CHEBI:30915` to `2-oxoglutaric acid`, the
  anhydrous neutral acid rather than the disodium salt hydrate.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml data/ingredients/mapped/A-Cyclodextrin.yaml data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/AQDS.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected anhydrous-acid label and synonyms for `CHEBI:30915`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected anhydrous-acid formula, structure strings, CAS xref,
  and mass for `CHEBI:30915`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The #342 regrade correctly uses `skos:closeMatch` rather than
  `skos:narrowMatch` to relate this CAS salt/hydrate record to anhydrous
  `CHEBI:30915`.
- `mappings/hydrate_review.tsv` records the remaining hydrate gap: the label
  says only `hydrate`, and the CAS/formula metadata does not establish a
  unique water stoichiometry.
- PubChem CID `31040` confirms the current CAS chemistry is the anhydrous
  disodium salt formula `C5H4Na2O5`; that does not reproduce the hydrate named
  by `preferred_term`.
- `a-Ketoglutaric acid` is the neutral acid, not the disodium salt hydrate, but
  it is stored as an `EXACT_SYNONYM` and exported as a SSSOM `other` value on
  the close-match row.
- The carbon-source and energy-source roles are supported only by provisional
  computational curation notes, not by direct evidence for this hydrate salt.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM CAS and close
  rows, hydrate-review row, unknown-term triage row, and ignored aggregate
  backups.

## Completeness

- The CAS identity, close match to the anhydrous acid, and CAS registry SSSOM
  row are populated.
- Hydrate stoichiometry and role support are unresolved; the record is not
  complete enough for its label and role assertions.

## Recommended Edits

- Inspect the original source or supplier for CAS `305-72-6`; if it supports
  an anhydrous disodium salt rather than a hydrate, remove `hydrate` from
  `preferred_term`.
- Remove `a-Ketoglutaric acid` from exact synonyms, or move it to
  source-occurrence-only provenance that will not be exported as an exact
  `other` surface for the salt.
- Either add direct support for the carbon-source and energy-source roles or
  remove the provisional role facets.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation, the
  hydrate audit, and SSSOM invariants.
