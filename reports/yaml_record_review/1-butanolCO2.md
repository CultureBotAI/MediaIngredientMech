# `data/ingredients/mapped/1-butanolCO2.yaml`

## Verdict

Needs curation. The record now correctly models the MicrobeDecoder
`1-butanol+CO2` label as a local `kgmicrobe.ingredient:` blend with explicit
`butan-1-ol` and `carbon dioxide` components instead of falsely mapping the
combination to one component. The only current defects are stale provenance
strings that still say one constituent was unresolved, call the type
`DEFINED_MEDIUM`, and leave an old "Curator review needed" note on an already
mapped record.

## Identity

- Reviewed record: `data/ingredients/mapped/1-butanolCO2.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:1_butanol_co2`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:1_butanol_co2`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Source provenance: `occurrence_statistics.source_occurrences[0]` retains the
  MicrobeDecoder `bergey:substrates` occurrence count of `1`.
- Decomposition provenance:
  `mappings/microbedecoder_residual_research_decomposition.tsv` has the
  maintained `UNMAPPED_0735` row for `1-butanol+CO2`, strategy `split`,
  high confidence, and components `CHEBI:28885:butan-1-ol` plus
  `CHEBI:16526:carbon dioxide`.
- Component checks: the current EMBL-EBI ChEBI pages resolve `CHEBI:28885` to
  `butan-1-ol` and `CHEBI:16526` to `carbon dioxide`, matching the two stored
  component names.
- Boundary checked: active local siblings include `1-propanolCO2.yaml`,
  `2-butanolCO2.yaml`, `2-propanolCO2.yaml`, and `CyclopentanolCO2.yaml`; they
  are analogous but distinct alcohol-plus-carbon-dioxide combinations.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml data/ingredients/mapped/1-butanolCO2.yaml`:
  passed; 2 files scanned, 0 ERROR rows.
- Engine A term validation: skipped for this record because
  `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-butanolCO2.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`
  returned non-OBO. The `validate-terms` recipe documents this skip for
  `kgmicrobe.ingredient:` and other private prefixes; running
  `linkml-term-validator` directly tries to fetch a nonexistent
  `kgmicrobe.ingredient.db.gz` adapter.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed the full product id/label gate; this is the documented Engine B
  coverage for non-OBO prefixes skipped by Engine A.
- Whole-corpus `uv run --frozen python scripts/validate_component_partonomy.py`
  passed earlier in this review pass, including this record's
  `MIM_CATALOG`-scoped `CHEBI:28885` and `CHEBI:16526` components.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `1-butanol+CO2` entry.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-butanolCO2 skos:exactMatch kgmicrobe.ingredient:1_butanol_co2`, with
  object label `1-butanol+CO2`, `kgm:ingredient`, and the August 24 component
  partonomy curator stamp.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same local fallback identity; the label index marks `1-butanol+CO2` `unique`.

## Evidence

- The local fallback mapping is appropriate. The source label explicitly names
  two top-level parts, no OBO term can denote that source-level conjunction as
  one molecule, and the private `kgmicrobe.ingredient:1_butanol_co2` ID
  prevents a false exact match to either `CHEBI:28885` or `CHEBI:16526`.
- The component assertion is complete for the label as written:
  MicrobeDecoder supplied `1-butanol+CO2`, and the maintained decomposition row
  independently records the same split as `Alcohol donor + CO2 acceptor`.
- The current `NAMED_MEDIUM` type is consistent with the retired
  `decompose_substrate_combinations.py` rules: every constituent is a defined
  chemical, so the combination should stay named/defined rather than an
  undefined extract, digest, or body-fluid mixture.
- Minor: `ontology_mapping.evidence[0].notes` is stale. It still says only one
  of two constituents resolved, says `1-butanol` carries no `component_id`, and
  says `ingredient_type=DEFINED_MEDIUM`; the current record has two resolved
  `MIM_CATALOG` component IDs and `ingredient_type: NAMED_MEDIUM`.
- Minor: top-level `notes` still carries the original import text
  `Curator review needed` even though the record has since been decomposed,
  promoted, moved to the mapped collection, typed, and exported.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e kgmicrobe.ingredient:1_butanol_co2 -e "1-butanol+CO2" -e 1_butanol_co2 -e CHEBI:28885 -e CHEBI:16526 -e "mappings/microbedecoder_residual_research_decomposition.tsv" -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, the
  maintained MicrobeDecoder decomposition row, component records, analogous
  alcohol-plus-CO2 siblings, and no duplicate active YAML for
  `kgmicrobe.ingredient:1_butanol_co2`.

## Completeness

- The missing concentrations are correctly absent: neither `1-butanol+CO2` nor
  the curated decomposition row states amounts.
- Both components now have IDs and `MIM_CATALOG` scope because
  `data/ingredients/mapped/Butanol.yaml` owns `CHEBI:28885` and
  `data/ingredients/mapped/Carbon_dioxide_gas.yaml` owns `CHEBI:16526`.
- There is no open discussion overlay on this record, and
  `mappings/record_research_validation.tsv` has no queued rows for
  `1-butanolCO2`.

## Recommended Edits

1. Update `ontology_mapping.evidence[0].notes` in
   `data/ingredients/mapped/1-butanolCO2.yaml` so it reflects the current
   post-#369 state: both components resolved, both carry identifiers, and the
   record type is `NAMED_MEDIUM`.
2. Replace the stale top-level `notes` string with a short note that the
   MicrobeDecoder blend has already been reviewed, decomposed to
   `butan-1-ol` plus `carbon dioxide`, and moved to the mapped collection.
3. No identifier, component, `component_assertion`, mapping predicate, SSSOM,
   or docs edit is needed for the active
   `kgmicrobe.ingredient:1_butanol_co2` identity.
