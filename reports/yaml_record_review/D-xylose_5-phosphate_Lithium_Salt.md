# `data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml`

## Verdict

Needs curation. The CAS-backed local identity and `skos:narrowMatch` to the
free-acid `CHEBI:37492` parent are appropriate for the current ontology, and
the companion CAS and kg-microbe exact identity rows are present in SSSOM, but
the final parent row publishes a parent-only synonym that omits the lithium salt
boundary and the `CARBON_SOURCE` role is still only computationally inferred.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:66768-39-6` with
  `ontology_mapping.ontology_id: CHEBI:37492`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:37492` to active `D-xylose 5-phosphate`, formula
  `C5H11O8P`, charge `0`, InChIKey `PPQRONHOSHZGFQ-VPENINKCSA-N`, and exact
  synonym `D-xylose 5-(dihydrogen phosphate)`.
- Live OLS exact searches for `66768-39-6` and
  `D-xylose 5-phosphate lithium salt` returned zero ChEBI hits, supporting the
  existing CAS fallback rather than promotion to a form-specific ChEBI primary.
- PubChem resolves `66768-39-6` to CID 441187, title
  `D-xylose 5-phosphate`, formula `C5H11O8P`, and InChIKey
  `PPQRONHOSHZGFQ-VPENINKCSA-N`, matching the parent ChEBI structure rather
  than adding a lithium counterion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through `D` and then failed on `DAMPA` because its `cas:` fallback
  hit the known OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset after skipping `DAMPA`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65327 CHEBI:37492 CHEBI:75228 CHEBI:116509`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:37492`.
- `curl -L ... q=66768-39-6&ontology=chebi&exact=true`: live OLS returned
  zero ChEBI hits for the CAS value.
- `curl -L ... q=D-xylose%205-phosphate%20lithium%20salt&ontology=chebi&exact=true`:
  live OLS returned zero ChEBI hits for the supplied label.
- `curl -L ... /compound/name/66768-39-6/property/.../JSON`: PubChem resolved
  the CAS value to CID 441187, `D-xylose 5-phosphate`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:66768-39-6`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The `CARBON_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.
- The final `mappings/ingredient_mappings.sssom.tsv` rows include the required
  `skos:narrowMatch` to `CHEBI:37492`, the `skos:exactMatch` registry row for
  `cas:66768-39-6`, and the `skos:exactMatch` kg-microbe identity row required
  for a subject mapped through a broader ChEBI parent.
- The final registry and kg-microbe identity rows publish only the structured
  same-subject token `CAS:66768-39-6` in `other`.
- The final `skos:narrowMatch` row publishes
  `D-xylose 5-(dihydrogen phosphate)` in `other`; that token is a synonym of
  the broader free-acid parent and is not a same-subject synonym for the
  lithium-salt record.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over `data`, `mappings`,
  `docs`, `reports`, `.claude`, `.github`, `scripts`, `src`, and `tests` found
  no second primary record for `cas:66768-39-6`; the CAS appears in this
  record, synchronized/generated projections, and registry review surfaces.
- The parent/child identity loss is represented by `NARROW_MATCH` plus
  companion local identity rows.
- The record has no source occurrences, component decomposition, or
  environmental-context assertions to resolve.

## Recommended Edits

- In `data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml`, remove
  the parent-only `D-xylose 5-(dihydrogen phosphate)` synonym or retype it so
  the final SSSOM builder does not publish it as `other` for the lithium-salt
  subject.
- In the same file, remove the provisional `CARBON_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
