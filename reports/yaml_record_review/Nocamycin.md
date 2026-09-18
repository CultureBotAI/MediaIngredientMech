# `data/ingredients/mapped/Nocamycin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:219652` nocamycin identity and
structure block pass, but final SSSOM `other` publishes a `produces:` process
phrase as a synonym and `SELECTIVE_AGENT` is only a provisional name-pattern
role.

## Identity

- Reviewed record: `data/ingredients/mapped/Nocamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:219652` with
  `ontology_mapping.ontology_id: CHEBI:219652`, label `Nocamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:219652` as active `Nocamycin` with
  formula `C26H33NO9` and the same InChI and SMILES as the record.
- The final SSSOM row maps `MIM:Nocamycin` exactly to `CHEBI:219652`.
- Major: the final SSSOM row exports `produces: nocamycin` in `other`. That
  process-qualified phrase is not a same-substance synonym for nocamycin; a
  gitignore-independent search across `data`, `src`, `tests`, `mappings`, and
  `scripts` found it only in the active YAML, aggregate/backups, and generated
  SSSOM products.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only the
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` evidence object.
  That name-pattern rule is explicitly provisional and does not independently
  support the selective-agent role.

## Completeness

- The active ChEBI term, formula, structure, and final exact row otherwise
  agree.
- Empty CultureMech occurrence statistics are expected for this
  kg-microbe-derived compound record.
- The remaining consequential gaps are the unsafe final `other` token and the
  unsupported selective-agent role evidence.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nocamycin.yaml`, remove
  `produces: nocamycin` from active synonyms, keep it out of final SSSOM
  `other`, and preserve the raw process text only as non-resolving provenance
  if it needs to remain traceable.
- Major: replace the `SELECTIVE_AGENT` role evidence with inspected
  source-backed evidence, or remove the role until that evidence exists.
