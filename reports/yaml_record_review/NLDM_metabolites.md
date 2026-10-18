# `data/ingredients/mapped/NLDM_metabolites.yaml`

## Verdict

Pass. `NLDM_metabolites` is correctly modeled as a named 64-component stock
solution with a local `kgmicrobe.ingredient` identity, complete component
transcription, two deliberately unresolved child ingredients, supported source
roles, and a final fallback-registry exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/NLDM_metabolites.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:nldm_metabolites` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:nldm_metabolites`, label
  `NLDM_metabolites`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Occurrences: ten CultureBotHT media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-lauroylsarcosine_Sodium_Salt` through
  `NNNN-Tetramethylethylenediamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` is unavailable for this
  non-OBO `kgmicrobe.ingredient` mapping: it exits 1 after loading the empty
  OBO sqlite adapter and finding no `rdfs_label_statement` table. This is the
  expected Engine A failure mode for local registry prefixes; the record is
  instead covered by Engine B and the SSSOM/product validators.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` records the original
  `UNMAPPED_0299` search with no exact OLS hit for `NLDM_metabolites`, and the
  curation history records later promotion to
  `kgmicrobe.ingredient:nldm_metabolites`.
- Google Sheets `Mixes!A786:Z849` contains exactly the 64 CultureBotHT
  component rows now transcribed in YAML, at matching concentrations and `uM`
  units.
- The two unresolved members, `Gamma-Aminobutyric Acid Hydrochloride` and
  `Trimethylglycine`, are preserved with `reference_scope: UNMAPPED`; no unsafe
  free-acid, hydrate, or broader parent substitution was introduced.
- The carbon, nitrogen, sulfur, and phosphate source roles are grounded in the
  same Mixes-tab component list and name concrete supporting constituents.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:NLDM_metabolites` to `kgmicrobe.ingredient:nldm_metabolites` with empty
  `other`.

## Completeness

- The stock-solution identity, 64/64 component transcription, local fallback
  registry mapping, occurrence count, source roles, and final row agree.
- `component_assertion.completeness: COMPLETE` is used for complete source-row
  transcription; it does not incorrectly claim every child ingredient is mapped.

## Recommended Edits

- None.
