# `data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml`

## Verdict

Needs curation. The August regrounding correctly moved the complete
`0.2% Thiamine pyrophosphate` stock-solution identity off pure ChEBI
`CHEBI:9532` and onto the local
`kgmicrobe.ingredient:0_2_thiamine_pyrophosphate` registry identifier. The
record still carries pure thiamine-pyrophosphate exact synonyms, pure-compound
chemical properties, a stale `kg_microbe_node_id`, and a `SINGLE_INGREDIENT`
classification that no longer matches the solution identity.

## Identity

- Reviewed record: `data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:0_2_thiamine_pyrophosphate` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:0_2_thiamine_pyrophosphate`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Local-registry check: the identifier is a deliberate mint for this full stock
  solution, not an OBO term. The MIM curation event explicitly records
  `CHEBI:9532 -> kgmicrobe.ingredient:0_2_thiamine_pyrophosphate` because the
  label is a `0.2%` stock solution rather than pure
  `thiamine(1+) diphosphate`.
- Source support: `mappings/culturemech_recipe_membership.tsv` has one current
  CultureMech recipe membership row for
  `kgmicrobe.ingredient:0_2_thiamine_pyrophosphate`, matching
  `occurrence_statistics.total_occurrences: 1` and `media_count: 1`.
- Boundary checked: `data/ingredients/mapped/Thiamine_pyrophosphate.yaml` owns
  pure `CHEBI:9532` `thiamine(1+) diphosphate` after the #319/#320 salt repair.
  `02_Thiamine_Pyrophosphate.yaml` is the remaining 0.2% solution record and
  should not publish pure-compound synonyms or chemical properties as exact
  claims about itself.

## Validation

- Whole-corpus strict validation:
  `uv run --frozen python scripts/validate_strict.py` passed across 2,958 YAML
  documents, including all 2,951 per-record files and the seven curated
  collection files, with 0 ERROR rows.
- Engine A term validation:
  `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`
  skips this file by design because `kgmicrobe.ingredient` is not an OBO prefix;
  Engine B `validate-products` is the gate that can reason about local registry
  identifiers.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `0.2% Thiamine pyrophosphate` entry; curation history
  length is `9` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:02_Thiamine_Pyrophosphate skos:exactMatch
  kgmicrobe.ingredient:0_2_thiamine_pyrophosphate`, with object label
  `0.2% Thiamine pyrophosphate`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; local Rule B4 was skipped
  because the sibling kg-microbe ontology transforms are absent.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `kgmicrobe.ingredient:0_2_thiamine_pyrophosphate` identity.

## Evidence

- The maintained identity repair is sound: the preferred term includes a
  concentration qualifier, and the record's #288/#320 curation event says a
  local `kgmicrobe.ingredient:` fallback is the intended home for that stock
  solution.
- Major: the `EXACT_SYNONYM` values `ThDP`, `ThPP`,
  `thiamine-pyrophosphate`, and the three structural names all describe the
  thiamine-pyrophosphate solute, not a `0.2%` stock solution. They are published
  in the SSSOM `other_label` column and in `docs/data/label_index.csv` as exact
  labels for `kgmicrobe.ingredient:0_2_thiamine_pyrophosphate`.
- Major: `chemical_properties` is still a pure-compound block:
  `cas_rn: 154-87-0`, `molecular_formula: C12H19N4O7P2S`, SMILES, and InChI.
  The same record's own MIM curation evidence says that recorded CAS "is the
  chloride's" and was never evidence for the prior ChEBI grounding, so it is not
  evidence for this stock solution either.
- Major: `ingredient_type: SINGLE_INGREDIENT` contradicts the maintained
  identity. The schema has `STOCK_SOLUTION` for pre-mixed solutions of defined
  ingredients, and stock solutions are in scope for `components` partonomy.
- Major: `kg_microbe_node_id: CHEBI:9532` is a stale compatibility copy of the
  pre-regrounding identifier. `uv run --frozen python
  scripts/audit_kg_microbe_node_ids.py --check` reports it as a cross-prefix
  mismatch in `reports/kg_microbe_node_id_mismatches.tsv`.
- `mappings/record_research_validation.tsv` still has stale rows for the old
  `CHEBI:9532` exact-match version. The August curation resolved their main
  objection by minting the local registry identifier, but did not clean up the
  pure-compound fields those rows also called out.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e "kgmicrobe.ingredient:0_2_thiamine_pyrophosphate" -e "MIM:02_Thiamine_Pyrophosphate" -e "0.2% Thiamine pyrophosphate" -e "154-87-0" -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the maintained YAML/aggregate/docs/SSSOM rows, the
  stale local `kg_microbe_node_id` report row, and no second active owner of the
  local stock-solution identifier.

## Completeness

- The pure `Thiamine_pyrophosphate.yaml` sibling is correctly separate and must
  retain the ChEBI grounding and pure-compound synonyms; it is not a duplicate
  of this stock-solution record.
- `components` is materially missing for the stock solution. The record should
  identify the thiamine-pyrophosphate solute and, where supported by the
  maintained CultureMech source label, the solvent and concentration basis.
- `find . -path ./.git -prune -o -iname '*thiamine*' -print` included ignored
  files and found thiamine, thiamine HCl, thiamine monophosphate,
  thiamine-pyrophosphate, stock-solution, and vitamin-solution siblings rather
  than a duplicate of `kgmicrobe.ingredient:0_2_thiamine_pyrophosphate`.

## Recommended Edits

1. In `data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml`, change
   `ingredient_type` from `SINGLE_INGREDIENT` to `STOCK_SOLUTION` and add
   supported `components` for the solute and solvent/concentration details that
   the maintained CultureMech input actually provides.
2. Remove pure thiamine-pyrophosphate exact synonyms from
   `02_Thiamine_Pyrophosphate.yaml` so `ThDP`, `ThPP`, `thiamine-pyrophosphate`,
   and structural solute names continue resolving only through
   `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`.
3. Remove the stale `chemical_properties` block, or replace it with
   formulation-level properties only if a source directly supports them for
   `0.2% Thiamine pyrophosphate`.
4. Replace or delete `kg_microbe_node_id: CHEBI:9532` so downstream exports do
   not carry the pre-regrounding pure-compound node ID.
5. Run `just sync-curated`, `just qc-roundtrip`, `just qc-component-partonomy`,
   `just validate-products`, and the docs/SSSOM export recipes after the
   maintained YAML fix so the pure-compound `other_label` values disappear from
   the stock-solution SSSOM row and docs label index.
