# `data/ingredients/mapped/1-octen-3-ol.yaml`

## Verdict

Needs curation. The CAS-derived `CHEBI:34118` identity is correct and the
record's formula, SMILES, InChI, CAS RN, aggregate copy, docs, and SSSOM row
agree; the live defect is an unattached `kgscan` discussion that is not a
1-octen-3-ol curation question.

## Identity

- Reviewed record: `data/ingredients/mapped/1-octen-3-ol.yaml`.
- Identifier and grounding: `identifier: CHEBI:34118` with
  `ontology_mapping.ontology_id: CHEBI:34118`, label `oct-1-en-3-ol`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:34118`
  resolves to `oct-1-en-3-ol`, records synonym `1-octen-3-ol`, formula
  `C8H16O`, SMILES `C=CC(O)CCCCC`, the same InChI stored in
  `chemical_properties`, and CAS RN `3391-86-4`.
- Mapping-method boundary: `CAS_RN_LOOKUP` is appropriate because the current
  CAS RN was the explicit CultureBotHT-to-ChEBI lookup key. The exact SSSOM
  predicate is still correct under `MAPPING_SEMANTICS.md` Rule D.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-octen-3-ol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-octen-3-ol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  matched after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:34118` row with `CAS:3391-86-4` in `other_label`, and generated docs
  expose the same mapping quality and ChEBI label.

## Evidence

- Current ChEBI confirms `CHEBI:34118` as the same molecule and CAS registry
  target as the live record.
- The August regrade events are coherent: the record first stopped claiming a
  primary-label exact lexical match, then restored `CAS_RN_LOOKUP` so the grade
  reflects the actual lookup method.
- The stale `mappings/record_research_validation.tsv` row only proposes
  optional synonyms and still references the earlier `EXACT_MATCH` grade; it
  does not refute the active CAS-grounded identity.
- Minor: `discussions[0]` contains generic plant-protein, Jiang-shui,
  review-article, and mycorrhizal-VOC gap sentences. Those are not attached to
  an actionable mapping, synonym, CAS, structure, role, or source-occurrence
  question for this record.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM rows,
  expected review TSV rows, and no duplicate active YAML for `CHEBI:34118`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN, formula, SMILES, and InChI are populated and match current ChEBI.
- No exact synonym needs to be added solely for `oct-1-en-3-ol`: that string is
  already exported as the ontology label. Broader names such as `octenol` should
  remain out unless scoped by a source because they can be ambiguous.

## Recommended Edits

1. Remove or replace `kgscan-ca9d598a165f` with a claim-attached,
   1-octen-3-ol-specific discussion if an actual unresolved gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be live, regenerate
   it or mark the optional/stale 1-octen-3-ol row resolved.
3. No ChEBI, CAS RN, formula, SMILES, InChI, SSSOM, aggregate, or docs edit is
   needed for the active identity.
