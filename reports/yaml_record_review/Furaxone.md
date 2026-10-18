# `data/ingredients/mapped/Furaxone.yaml`

## Verdict

Needs curation, with a major duplicate-identity issue. `Furaxone` is not an
orphan local compound: PubChem resolves that surface to furazolidone, and this
repository already has an exact `CHEBI:5195` `Furazolidone` record.

## Identity

- Reviewed record: `data/ingredients/mapped/Furaxone.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:furaxone` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem lookup by name resolved `Furaxone` to CID 5323714 titled
  `Furazolidone` with formula `C8H7N3O5`.
- `data/ingredients/mapped/Furazolidone.yaml` already maps the active
  `Furazolidone` record to exact ChEBI term `CHEBI:5195`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml data/ingredients/mapped/Furaltadone_Hydrochloride.yaml data/ingredients/mapped/Furaxone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this local
  `kgmicrobe.compound:` record because the Engine A/OBO prefix scope does not
  cover private KG-Microbe CURIEs.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, fallback registry mapping, MicrobeDecoder source
  occurrence, and stale import note as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Furaxone`
  to `kgmicrobe.compound:furaxone` with `skos:exactMatch` and an empty `other`
  column.
- Major: the local fallback registry identity is no longer justified because
  `Furaxone` resolves to the already active `Furazolidone` / `CHEBI:5195`
  identity.
- `mappings/record_research_validation.tsv` already warned that a CAS supplied
  by one literature pass belonged to nitrofurazone and not to the
  furazolidone/Furaxone identity; that warning does not justify retaining a
  separate local `Furaxone` class.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active Furaxone YAML, aggregate copy,
  final local SSSOM row, MicrobeDecoder source rows, Furazolidone exact record,
  and record-research validation rows.

## Completeness

- The single MicrobeDecoder `Furaxone` occurrence is traceable.
- The missing CAS and structure fields are symptoms of the duplicate local
  fallback identity; they should resolve by merging or redirecting Furaxone to
  the existing Furazolidone record.

## Recommended Edits

- Major: merge or reject `data/ingredients/mapped/Furaxone.yaml` in favor of
  `data/ingredients/mapped/Furazolidone.yaml`, preserving `Furaxone` only as a
  source synonym or alias of the exact `CHEBI:5195` record; sync
  `data/curated/mapped_ingredients.yaml`, regenerate final SSSOM, and rerun
  duplicate-identifier plus SSSOM QC.
