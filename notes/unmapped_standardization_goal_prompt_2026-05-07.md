# Goal Prompt: Standardize Remaining Unmapped Media Ingredients

Continue curation of the remaining unmapped MediaIngredientMech ingredient
records under `data/ingredients/unmapped/`, using individual YAML records as
the source of truth.

## Objective

Reduce unmapped ingredient ambiguity through conservative, evidence-backed
standardization. Make only high-confidence edits that are locally supported by
existing mapped records, local OAK ontology evidence, EBI OLS validation, or
clear source-formulation semantics. Preserve unrelated untracked work and avoid
broad automated remapping.

## Current State

- Mapped individual records: 1855
- Remaining unmapped individual records after the 2026-05-07 duplicate pass: 445
- Heuristic review buckets:
  - Defined media or named formulations: 119
  - Simple chemical, formula, or hydrate cases: 113
  - Rare natural product or ambiguous terms: 104
  - Stock solutions or mixtures: 73
  - Biological extracts or products: 26
  - Commercial products or catalog terms: 10

## Strategy

1. Resolve exact local duplicates first.
   - Search preferred terms and synonyms across `data/ingredients/mapped/`.
   - Merge or retire unmapped records only when the mapped representative
     already carries the same identity or exact synonym evidence.
   - Add absorbed source labels as synonyms and append `curation_history`.
   - Sum occurrence counts only when the unmapped record has nonzero counts.

2. Separate hydrate and salt identity from parent-compound similarity.
   - Use `skos:exactMatch` only when hydrate/salt state matches the ontology
     record or the project already has a documented convention for that exact
     representative.
   - Keep hydrate-specific records unmapped when the only local target is an
     anhydrous or broader parent record.

3. Treat named media, buffers, stocks, vitamin mixes, trace-element solutions,
   seawater preparations, and commercial formulations as formulations unless
   the local record proves a single chemical identity.
   - Do not identity-map these to generic parents.
   - Use `skos:narrowMatch` only with the required kg-microbe registry identity
     row pattern described in `MAPPING_SEMANTICS.md`.

4. For chemical-looking no-hit records, validate candidates with both local OAK
   and EBI OLS before mapping.
   - Prefer CHEBI for single chemicals.
   - Use MESH/NCIT/MICRO only when they are already accepted in local records or
     when CHEBI has no exact equivalent and the term is locally justified.
   - Document any OLS/OAK mismatch in `mappings/`.

5. For remaining ambiguous records, produce review artifacts instead of weak
   mappings.
   - Keep commercial products, catalog labels, source-specific mixes, and
     source-medium references in unmapped with explicit notes or a bucket audit.
   - Do not broaden to generic terms such as `agar`, `vitamin`, `trace element`,
     `medium`, or `seawater` as identity.

## Required Workflow

After YAML curation:

1. Run targeted validation on changed individual YAML records.
2. Regenerate aggregate curated outputs from individual records.
3. Rebuild and validate the SSSOM if mapped records, synonyms, curation history,
   or mapping semantics changed.
4. Publish the SSSOM sharing artifact with the repo's established just/skill
   workflow when the build and review gates pass.
5. Run `just validate-all` and `PYTHONPATH=src pytest -o addopts='' tests/`;
   document known pre-existing failures separately from new failures.
6. Commit and push only tracked files related to this curation pass.

