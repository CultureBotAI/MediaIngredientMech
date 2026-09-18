# `data/ingredients/mapped/Acriflavine.yaml`

## Verdict

Pass with minor issues. The CAS-backed identity, PubChem CID, NCIT parent row,
SSSOM registry rows, and aggregate copy pass; one historical PubChem chemistry
change string has truncated structure text.

## Identity

- Reviewed record: `data/ingredients/mapped/Acriflavine.yaml`.
- Identifier and grounding: `identifier: cas:8048-52-0` with
  `ontology_mapping.ontology_id: NCIT:C76253`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- `uv run --frozen runoak -i sqlite:obo:chebi search 'Acriflavine'` returned no
  local ChEBI hits, consistent with the retained CAS primary identifier.
- The PubChem PUG name lookup for CAS `8048-52-0` resolves CID `443101`,
  matching `chemical_properties.pubchem_cid`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `NCIT:C76253` as a prefix-specific OLS exact-CURIE resolution for
  `Acriflavine`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acriflavine.yaml data/ingredients/mapped/Actein.yaml data/ingredients/mapped/Actinohivin.yaml data/ingredients/mapped/Actinomycetin.yaml data/ingredients/mapped/Actinomycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Acriflavine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi search 'Acriflavine'`: passed
  with no local ChEBI hits.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT import supports the source CAS `8048-52-0`.
- PubChem resolves `8048-52-0` to the same CID stored on the record.
- The NCIT parent term is represented with `NARROW_MATCH` in YAML and with
  `skos:narrowMatch` in `mappings/ingredient_mappings.sssom.tsv`; the CAS and
  `kgmicrobe.compound:acriflavine` local identifiers are separate registry
  `skos:exactMatch` rows, as required by Rule B1.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explicitly classifies
  the NCIT row as a historical synonym-review prefix-dispatch miss, and the
  CAS and kg-microbe rows as expected registry identifiers.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, three SSSOM rows, external-prefix OLS validation row, unknown-term
  triage rows, generated indexes, ignored aggregate backups, and stale advisory
  batch rows.
- The only defect is historical: the 2026-05-02
  `AUTO_BACKFILL_PUBCHEM_CHEMISTRY` change string cuts off the SMILES and
  InChI, while `chemical_properties.smiles` and `chemical_properties.inchi`
  retain the full values.

## Completeness

- CAS, PubChem CID, formula, SMILES, InChI, NCIT parent mapping, curation
  history, and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally annotate the stale 2026-05-02 history `changes` prose in
  `data/ingredients/mapped/Acriflavine.yaml`; the active `chemical_properties`
  fields are already populated.
