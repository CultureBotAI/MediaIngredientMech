# `data/ingredients/mapped/1-phenazinecarboxamide.yaml`

## Verdict

Pass with minor issues. The CAS-derived exact `CHEBI:62240` identity is
correct and synchronized; only optional synonym enrichment remains.

## Identity

- Reviewed record: `data/ingredients/mapped/1-phenazinecarboxamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:62240` with
  `ontology_mapping.ontology_id: CHEBI:62240`, label
  `phenazine-1-carboxamide`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:62240`
  resolves to `phenazine-1-carboxamide`, records synonym
  `1-Phenazinecarboxamide`, formula `C13H9N3O`, SMILES
  `NC(=O)c1cccc2nc3ccccc3nc12`, the same InChI stored in
  `chemical_properties`, and CAS RN `550-89-0`.
- Mapping-method boundary: `CAS_RN_LOOKUP` is appropriate because the current
  CAS RN was the explicit CultureBotHT-to-ChEBI lookup key. The exact SSSOM
  predicate is still correct under `MAPPING_SEMANTICS.md` Rule D.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-phenazinecarboxamide.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-phenazinecarboxamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:62240` row with `CAS:550-89-0` in `other_label`, and generated docs
  expose the same mapping quality and ChEBI label.

## Evidence

- Current ChEBI confirms `CHEBI:62240` as the same molecule and CAS registry
  target as the live record.
- The August regrade events are coherent: the record no longer overstates the
  match as a primary-label exact match or plain synonym match, and it now
  preserves the CAS lookup method.
- The stale `mappings/record_research_validation.tsv` row for this slug only
  proposes a source-backed `PCN` abbreviation; it does not refute the active
  CAS-grounded identity.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM rows,
  expected row-review TSV rows, and no duplicate active YAML for `CHEBI:62240`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN, formula, SMILES, and InChI are populated and match current ChEBI.
- Optional: the abbreviation `PCN` can be added later if backed by the cited
  phenazinecarboxamide literature.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is meant to be live, regenerate
   it or clear the stale optional-synonym row for this slug.
2. Optionally add `PCN` as a source-backed abbreviation.
3. No ChEBI, CAS RN, formula, SMILES, InChI, SSSOM, aggregate, or docs edit is
   needed for the active identity.
