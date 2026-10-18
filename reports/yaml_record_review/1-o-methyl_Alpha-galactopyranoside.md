# `data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml`

## Verdict

Needs curation. The active `CHEBI:55507` grounding and structure are coherent,
but the top-level `notes` still say no CHEBI/NCIT match was available and that
curator review was needed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:55507` with
  `ontology_mapping.ontology_id: CHEBI:55507`, label
  `methyl alpha-D-galactoside`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:55507`
  resolves to `methyl alpha-D-galactoside`, formula `C7H14O6`, the same SMILES
  and InChI stored in `chemical_properties`, and CAS RN `3396-99-4`.
- Source boundary: the preferred term preserves the microbedecoder raw wording,
  while the ontology label names the normalized ChEBI compound. The SSSOM row
  remains `skos:exactMatch` because `CHEBI:55507` denotes the same glycoside.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-naphtylacetic_Acid.yaml data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml data/ingredients/mapped/1-octen-3-ol.yaml data/ingredients/mapped/1-phenazinecarboxamide.yaml data/ingredients/mapped/1-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
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
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` and generated docs contain the
  expected exact `CHEBI:55507` row.

## Evidence

- Current ChEBI verifies the canonical label and the stored formula, SMILES, and
  InChI for `CHEBI:55507`.
- The #213 curation evidence supports the synonym-match promotion: the raw
  `1-o-methyl Alpha-galactopyranoside` label denotes methyl
  alpha-D-galactoside.
- The stale `mappings/record_research_validation.tsv` rows for this slug
  predate the CHEBI resolution or chemical-property backfill. They are
  contradicted by the active YAML and generated products.
- Minor: top-level `notes` still describe the pre-promotion unmapped state.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the expected active YAML/aggregate/SSSOM
  rows, old validation TSV rows, and no duplicate active YAML for
  `CHEBI:55507`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- Formula, SMILES, InChI, and molecular weight are populated and agree with
  current ChEBI.
- Optional: current ChEBI lists CAS RN `3396-99-4`, which could be added on a
  future CAS enrichment pass.

## Recommended Edits

1. Update `notes` in
   `data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml` to describe
   the current `CHEBI:55507` mapped state, then regenerate the aggregate and
   generated products through the maintained recipes.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it or clear the obsolete rows for this slug.
3. Optionally add ChEBI-backed `chemical_properties.cas_rn: 3396-99-4`.
