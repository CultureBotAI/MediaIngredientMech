# `data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml`

## Verdict

Pass with minor issues. The exact CAS-backed monohydrate identity, exact
registry row, and `skos:closeMatch` parent row to anhydrous `CHEBI:17256` are
all synchronized; only stale pre-#342 advisory rows still describe the old
fallback or narrow-match state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:16373-93-6` with
  `ontology_mapping.ontology_id: CHEBI:17256`,
  `ontology_mapping.ontology_label: 2'-deoxyadenosine`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official parent ChEBI check: the current EMBL-EBI ChEBI page for
  `CHEBI:17256` resolves to the anhydrous parent `2'-deoxyadenosine`, formula
  `C10H13N5O3`, and an anhydrous InChI.
- Exact PubChem check: CAS `16373-93-6` resolves to CID `9549172`,
  `2'-Deoxyadenosine monohydrate`, formula `C10H15N5O4`, the record's
  water-containing SMILES, and an InChI matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxy-D-glucose.yaml data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml data/ingredients/mapped/2-Deoxycytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed for the parent ChEBI CURIE.
- Whole-corpus checks run earlier in this review pass passed, including SSSOM
  invariants for the close parent plus exact registry row; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:closeMatch` row to `CHEBI:17256` plus the exact `cas:16373-93-6`
  registry row.

## Evidence

- PubChem confirms the exact monohydrate CAS RN, formula, SMILES, and InChI.
- ChEBI confirms that `CHEBI:17256` is the anhydrous parent, so the #342
  regrade from `NARROW_MATCH` to `CLOSE_MATCH` is appropriate.
- Stale: `mappings/ingredient_mappings_unknown_term_triage.tsv`,
  `mappings/record_research_validation.tsv`, and older hydrate review rows still
  include pre-anchor or pre-#342 descriptions. The active YAML and SSSOM no
  longer make the old narrowMatch assertion.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, the exact CAS registry row, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, InChI, and PubChem CID are populated for the exact
  monohydrate.
- Empty component and role slots are acceptable for this modeled single
  hydrate.

## Recommended Edits

1. If hydrate review and unknown-term TSVs are intended to be live queues,
   regenerate them so stale `FALLBACK_REGISTRY` and `NARROW_MATCH` rows no
   longer imply pending work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   monohydrate record.
