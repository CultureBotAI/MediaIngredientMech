# `data/ingredients/mapped/Levomenthol.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:15409 levomenthol identity, CAS RN,
PubChem structure, and own-identifier SSSOM row pass, but racemic menthol labels
from `sssom_other_backfill` are attached to this enantiopure record and are
published in the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Levomenthol.yaml`.
- Identifier and grounding: `identifier: CHEBI:15409` with
  `ontology_mapping.ontology_id: CHEBI:15409`, label `(-)-menthol`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `2216-51-5`, molecular formula `C10H20O`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Leupeptin` through `Levomenthol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:15409` as active `(-)-menthol`, lists CAS
  `2216-51-5`, lists `levomenthol` and the YAML IUPAC synonym on that same
  term, and records the same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `2216-51-5` to CID `16666` with formula `C10H20O` and
  the same stereospecific InChI as the YAML record.
- EBI OLS4 resolves the racemic term separately as `CHEBI:76310`
  `(+-)-menthol` with synonyms `DL-menthol`, `rac-menthol`, `racementhol`,
  `racementholum`, and `racementol`; PubChem resolves `DL-menthol` to CID
  `1254`, whose InChI omits the levomenthol stereo layer.
- Major: the YAML `synonyms` list and final SSSOM `other` field publish
  `(+-)-menthol`, `DL-menthol`,
  `rac-(1R,2S,5R)-5-methyl-2-(propan-2-yl)cyclohexan-1-ol`, `rac-menthol`,
  `racementhol`, `racementholum`, and `racementol` as exact same-substance
  labels for enantiopure levomenthol. Those labels belong to the racemate and
  erase the stereochemical boundary that the `CHEBI:15409` mapping preserves.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:15409`; the row
  also carries the valid IUPAC synonym and `CAS:2216-51-5`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, and aggregate
  copy are present and consistent.
- The published synonym surface is incomplete as a safe final product until
  racemic labels are removed from this record or moved to a separate
  `CHEBI:76310` racemic menthol record.

## Recommended Edits

- Major: remove the racemic `sssom_other_backfill` synonyms from
  `data/ingredients/mapped/Levomenthol.yaml` so only true levomenthol synonyms
  remain on this enantiopure record.
- If the raw corpus requires a racemic menthol subject, create or curate a
  separate record grounded to `CHEBI:76310`; do not preserve racemic labels on
  `CHEBI:15409`.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, term, round-trip, component, and SSSOM validation.
