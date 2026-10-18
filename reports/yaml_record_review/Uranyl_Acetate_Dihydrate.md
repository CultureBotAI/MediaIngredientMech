# `data/ingredients/mapped/Uranyl_Acetate_Dihydrate.yaml`

## Verdict

Pass. The CAS primary identity, MeSH parent mapping, hydrate-specific registry
SSSOM siblings, aggregate row, and final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Uranyl_Acetate_Dihydrate.yaml`.
- Identifier and grounding: `identifier: cas:6159-44-0` with parent
  `ontology_mapping.ontology_id: mesh:C005460`, label `uranyl acetate`, source
  `MESH`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `6159-44-0`.
- Synonyms: none.
- Occurrences: no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uranyl_Acetate` through `Uridine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  The lower-case `mesh:C005460` parent and CAS registry identity are covered by
  exact OLS/PubChem checks and by the existing unknown-term triage rows that
  classify the final validation stamps as expected local registry or
  missing-prefix-validator coverage.

## Evidence

- Fresh exact OLS4 search for `uranyl acetate` in MeSH returns active
  `mesh:C005460`, supporting the broader parent `skos:narrowMatch` row.
- `reports/hydrate_grounding.tsv` classifies `cas:6159-44-0` as
  `OK_OWN_CAS_ID`, and `mappings/hydrate_review.tsv` keeps the named dihydrate
  as a registered commercial crystal form with a hydrate-specific CAS identity.
- Fresh PubChem lookup for stored CID 114927 returns `Uranyl acetate dihydrate`
  as the first synonym and the same formula, InChI, and SMILES as the YAML.
- The final SSSOM rows correctly publish
  `MIM:Uranyl_Acetate_Dihydrate skos:narrowMatch mesh:C005460` plus exact
  `cas:6159-44-0` and `kgmicrobe.compound:uranyl_acetate_dihydrate` registry
  siblings.

## Issues

None.

## Completeness

- The CAS identity, MeSH parent, hydrate-specific registry rows, aggregate copy,
  and three final SSSOM rows agree.
- The hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found the expected missing-prefix and expected-registry triage rows
  for the MeSH parent, CAS registry row, and `kgmicrobe.compound` sibling.
- PubChem name lookup for `6159-44-0` returned no CID, but the curated CAS is
  covered by the local hydrate review and the stored PubChem CID still resolves
  as uranyl acetate dihydrate.

## Recommended Edits

None.
