# `data/ingredients/mapped/13-Hexanediol.yaml`

## Verdict

Pass. The record intentionally uses a CAS-backed local fallback for
`1,3-Hexanediol`, and its PubChem-backed chemistry, aggregate entry, SSSOM row,
and docs row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/13-Hexanediol.yaml`.
- Identifier and grounding: `identifier: cas:21531-91-9`,
  `ontology_mapping.ontology_id: cas:21531-91-9`,
  `ontology_mapping.ontology_label: 1,3-Hexanediol`, source `CAS`, and
  `mapping_quality: FALLBACK_REGISTRY`.
- Registry boundary: no active ontology CURIE is asserted, so the record is not
  pretending that a broader or adjacent OBO term denotes this CAS-specific
  substance.
- PubChem check: PubChem CID `210704` resolves to `1,3-Hexanediol`, includes
  CAS `21531-91-9`, and reports formula `C6H14O2`, canonical SMILES
  `CCCC(CCO)O`, and an InChI matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/13-Butandiol.yaml data/ingredients/mapped/13-Hexanediol.yaml data/ingredients/mapped/13-Propanediol.yaml data/ingredients/mapped/14-B-D-Galactobiose.yaml data/ingredients/mapped/14-Butanediol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/13-Hexanediol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1 with no output because the record intentionally has a `cas:`
  fallback identifier rather than an Engine A OBO CURIE.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:13-Hexanediol` to `cas:21531-91-9` row with
  `validation_status: UNKNOWN_TERM`.

## Evidence

- The active PubChem record confirms the CAS RN and structure-derived formula,
  SMILES, and InChI used in the YAML.
- The local CAS fallback keeps `identifier`, `ontology_mapping`, and
  `registry_info` synchronized around `cas:21531-91-9`.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active fallback YAML,
  aggregate, SSSOM, and docs rows; the remaining research-validation rows are
  stale because a registry fallback now intentionally encodes no external
  ontology term.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- The record has no exact synonyms, which is acceptable for a CAS fallback when
  no supported synonym has been curated.
- Empty component and role slots are acceptable for this single registry
  chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`1,3-Hexanediol` fallback.
