# `data/ingredients/mapped/Legionella_Agar_Enrichment.yaml`

## Verdict

Pass. The local stock-solution identity, exact KG-Microbe registry row,
catalog-variant synonym, occurrence count, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Legionella_Agar_Enrichment.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:legionella_agar_enrichment` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Source provenance: extracted from over-conflated `Agar.yaml` synonyms,
  reviewed as an agar enrichment supplement/preparation, and promoted to the
  local registry in #288 because it does not denote a single chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lecithin` through `Leucodin`: exited 0 and wrote zero ERROR rows.
- LinkML term validation was skipped for this local KG-Microbe record because
  the successful batch check covered only the CHEBI-primary records.

## Evidence

- Current exact OLS search across CHEBI, NCIT, MeSH, FOODON, and ENVO found no
  exact external term for `Legionella agar enrichment`; PubChem lookup by the
  same label found no CID.
- The final SSSOM publishes one `skos:exactMatch` row to
  `kgmicrobe.ingredient:legionella_agar_enrichment`; its `other` field contains
  the reviewed catalog label `Legionella agar enrichment (BD-Difco)`.
- The 2/2 occurrence count agrees with the refreshed CultureMech occurrence
  table.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row, the known subject-case regression test, and no sibling MIM record that
  would split the same enrichment-preparation identity.

## Completeness

- The local registry identity, stock-solution classification, occurrence count,
  catalog synonym, aggregate copy, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
