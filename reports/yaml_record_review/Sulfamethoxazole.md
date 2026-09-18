# `data/ingredients/mapped/Sulfamethoxazole.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:9332` identity, CAS, IUPAC synonym,
structure fields, and final SSSOM row pass, but `SELECTIVE_AGENT` is still only
a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfamethoxazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:9332` with
  `ontology_mapping.ontology_id: CHEBI:9332`, label `sulfamethoxazole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `723-46-6`, formula `C10H11N3O3S`, and
  ChEBI-derived InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfamethoxazole` through `Sulfaquinoxaline`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9332` with label
  `sulfamethoxazole`, CAS xref `723-46-6`, formula `C10H11N3O3S`, and
  structure fields matching the YAML.
- The active synonym
  `4-amino-N-(5-methyl-1,2-oxazol-3-yl)benzenesulfonamide` is the OLS exact
  IUPAC synonym for `CHEBI:9332`.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:9332` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:9332` and publishes only the IUPAC
  synonym and `CAS:723-46-6` in `other`; both are true labels for the same
  subject.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The exact CHEBI identity, CAS, active synonym, aggregate row, and final SSSOM
  row agree.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT,
  MicrobeDecoder candidate, aggregate, generated index, final SSSOM, and
  row-review rows, and no second active MIM record for `CHEBI:9332` or CAS
  `723-46-6`.
- No unsupported active synonym, component, or final SSSOM `other` payload was
  found; the only unsupported claim is the provisional selective-agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Sulfamethoxazole.yaml`, or replace the name-pattern
  evidence with an inspected source showing that sulfamethoxazole is acting as
  a selective agent in a culture medium.
