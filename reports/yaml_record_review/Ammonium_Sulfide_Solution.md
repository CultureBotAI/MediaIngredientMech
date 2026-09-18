# `data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml`

## Verdict

Needs curation. The CAS-primary identity, broader `mesh:C027711` MeSH parent,
exact CAS and local SSSOM rows, and aggregate copy agree, but the active record
has an unsupported provisional `REDUCING_AGENT` role and a stale PubChem CID
whose synonym set no longer matches the CAS identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml`.
- Identifier and grounding: `identifier: cas:12135-76-1` with
  `ontology_mapping.ontology_id: mesh:C027711`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  prefix-specific EBI OLS lookup resolves `mesh:C027711` exactly as
  `ammonium sulfide`; the `UNKNOWN_TERM` trailer came from earlier validator
  prefix coverage rather than a mapping defect.
- PubChem resolves CAS `12135-76-1` to CID `25519`, formula `H8N2S`, canonical
  SMILES `[NH4+].[NH4+].[S-2]`, and synonyms including ammonium sulfide
  solution, diammonium sulfide, and the CAS string itself.
- The YAML stores `pubchem_cid: 21842493` with the same `H8N2S` formula, but
  that CID's synonyms name an ammonia and hydrogen sulfide association and do
  not include `12135-76-1`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium_Sulfamate.yaml data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml data/ingredients/mapped/Amoxicillin.yaml data/ingredients/mapped/Amphomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` rows 404-406 export the expected
  `skos:narrowMatch` row to `mesh:C027711`, the exact CAS registry row, and
  the exact `kgmicrobe.compound:ammonium_sulfide_solution` companion row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the MeSH
  `UNKNOWN_TERM` trailer as missing prefix coverage, and classifies the CAS and
  kg-microbe companion rows as expected registry identifiers.
- The only role is a `REDUCING_AGENT` computational prediction inferred from a
  curated name-pattern rule; no medium or source claim demonstrates that this
  record was curated as a reducing agent.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active record, aggregate copy, SSSOM identity rows,
  row-review rows, and no `culturemech_recipe_membership.tsv` rows for
  `cas:12135-76-1`.

## Completeness

- CAS, formula, SMILES, InChI, parent MeSH mapping, exact CAS and local SSSOM
  rows, curation history, and `ingredient_type` are populated.
- No component, synonym, environmental context, discussion, or dataset entry is
  needed.
- The unsupported reducing-agent role and stale PubChem CID remain active gaps.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the provisional role and stale CID.

## Recommended Edits

- In `data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml`, replace the
  `REDUCING_AGENT` computational prediction with source-backed evidence, or
  remove it.
- Reconcile `chemical_properties.pubchem_cid` and the derived structure against
  the CAS-resolved PubChem identity, or document why the neutral
  ammonia/hydrogen sulfide representation is preferred for `cas:12135-76-1`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
