# `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml`

## Verdict

Needs curation. The September salt-ion repair fixed the material identity by
moving the complete EMIM/lysinate ion pair off the cation-only `CHEBI:61326`
identifier and onto a local `kgmicrobe.compound:` identifier with a narrow
`CHEBI:63895` parent, but the top-level free-text `notes` still describe the
pre-repair unmapped state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine` with
  `ontology_mapping.ontology_id: CHEBI:63895`, label `ionic liquid`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:63895`
  resolves to ChEBI ID `CHEBI:63895`, ChEBI name `ionic liquid`, and a generic
  salt definition. It also lists `1-ethyl-3-methylimidazolium chloride` as a
  child, supporting that `CHEBI:63895` is a whole-substance class rather than
  the bare EMIM cation.
- Exact-vs-parent boundary: `CHEBI:63895` is broader than the target
  EMIM/lysinate pair, so `NARROW_MATCH` is the correct mapping quality and the
  SSSOM builder correctly emits both `skos:narrowMatch CHEBI:63895` and a
  registry `skos:exactMatch` to the local kg-microbe identity.
- Cation boundary: the old `CHEBI:61326` stem match is now retained only in a
  `SUPERSEDED (#315)` evidence note explaining that the ChEBI term denotes
  1-ethyl-3-methylimidazolium alone, not the complete lysinate salt or ion
  pair. The old bare-ion label is a `REJECTED_LABEL`, not an exact synonym.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml data/ingredients/mapped/1-methylphenanthrene.yaml`:
  passed; 3 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed:
  `scripts/validate_strict.py`, `scripts/validate_all.py --mode both`,
  `scripts/validate_sssom_invariants.py`,
  `scripts/check_flat_export_coverage.py`,
  `scripts/audit_duplicate_identifiers.py --check`,
  `scripts/audit_kg_microbe_node_ids.py --check`,
  `scripts/validate_component_partonomy.py`, and
  `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed after ignoring empty default fields that
  are materialized only in the aggregate export.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected two rows:
  `MIM:1-ethyl-3-methylimidazolium_Lysine skos:narrowMatch CHEBI:63895`,
  anchoring this local salt identity to the nearest verified ChEBI parent, and
  `skos:exactMatch kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine`,
  preserving the exact local identity.
- `docs/data/mapped_ingredients.*`, `docs/data/all_ingredients.*`,
  `docs/data/ingredients.json`, and graph/UMAP data expose the local
  `kgmicrobe.compound:` identifier with the `CHEBI:63895` parent label.

## Evidence

- The active identity is supported: the current record keeps the complete
  EMIM/lysinate label, clears cation-only formula/SMILES/InChI values, rejects
  the cation-only CHEBI label as exact synonym text, and records that no exact
  ChEBI term was verified for the complete pair.
- The `CHEBI:63895` parent is directionally correct under
  `MAPPING_SEMANTICS.md`: the local EMIM/lysinate identity is a specific ionic
  liquid, while ChEBI's `ionic liquid` term is a broader class. The registry
  exact row satisfies the narrow-match identity-row pattern.
- The old `mappings/record_research_validation.tsv` P1/P2 rows for this slug
  are stale. They correctly refuted the former cation-only `CHEBI:61326`
  identity and chemical properties, but the live record has already moved to
  `kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine`, points only
  narrowly at `CHEBI:63895`, and no longer publishes the cation structure as
  whole-salt chemistry.
- Minor: top-level `notes` still says the record has "No CAS-RN or CHEBI
  mapping available; curator review needed." That is stale because the record
  now has a verified broader ChEBI parent and a reviewed local identity.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden -n "record_research_validation|1-ethyl-3-methylimidazolium_Lysine|CHEBI:61326|1-methylphenanthrene|CHEBI:35860" . -g '*record_research_validation*' -g '*review*' -g '*.tsv' -g '*.yaml'`
  covered ignored and hidden YAML/TSV/review files. It found the expected stale
  CHEBI:61326 rows in advisory review TSVs and historical backups, the active
  fixed YAML/aggregate/SSSOM rows, and no second active YAML for this exact
  EMIM/lysinate identity.

## Completeness

- Empty `chemical_properties` is correct for now. The cation-only structure was
  removed, and no exact full-salt structure source has been installed.
- Empty component and role slots are acceptable: this is modeled as one defined
  organic salt/ion pair, not as a stock mixture, and no retained source
  supports a narrower nutrient or cellular role.
- The rejected cation label is intentionally preserved so future synonym
  enrichment does not re-promote the old unsafe stem match.

## Recommended Edits

1. Update `notes` in
   `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml` to describe
   the current reviewed state: local EMIM/lysinate identity plus narrow
   `CHEBI:63895` ionic-liquid parent. Then regenerate
   `data/curated/mapped_ingredients.yaml`, SSSOM, and docs through the
   maintained sync/publish recipes.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the old
   cation-overclaim rows for this slug resolved.
3. Do not restore `CHEBI:61326`, the cation-only formula, or the cation-only
   SMILES/InChI fields for this complete salt identity.
