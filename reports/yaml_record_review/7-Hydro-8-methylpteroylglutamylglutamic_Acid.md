# `data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml`

## Verdict

Pass with minor issues. The exact MeSH identity, SSSOM row, and aggregate copy
pass; the record retains a stale import note and a stale generated SSSOM
validation tag from before MeSH prefix-specific checking existed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml`.
- Identifier and grounding: `identifier: mesh:C052093` with
  `ontology_mapping.ontology_id: mesh:C052093`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official NLM MeSH RDF JSON for `C052093` resolves the supplemental
  chemical record, marks it active, and gives the exact label
  `7-hydro-8-methylpteroylglutamylglutamic acid`.
- `identifier` and `ontology_mapping.ontology_id` use the same MeSH record and
  differ only by the source input's term capitalization.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/7-hydroxyflavone.yaml data/ingredients/mapped/72-Dihydroxyflavone.yaml data/ingredients/mapped/8-azaguanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The active MeSH supplemental chemical record supports the exact
  `7-hydro-8-methylpteroylglutamylglutamic acid` identity promoted from
  `UNMAPPED_0590`.
- The duplicate `RAW_TEXT` synonym is the same source surface used for the
  normalized MeSH match and does not introduce a conflicting synonym.
- The SSSOM row maps
  `MIM:7-Hydro-8-methylpteroylglutamylglutamic_Acid` to `mesh:C052093` with
  `skos:exactMatch` and `registry:mesh`.
- The SSSOM validation trailer still says `none|UNKNOWN_TERM|2026-07-07`,
  but `mappings/ingredient_mappings_unknown_term_triage.tsv` records this as a
  missing prefix-validator coverage issue, and the prefix-specific OLS review
  row resolved the exact MeSH CURIE.
- The top-level `notes` field still contains the original import text,
  including `no CAS-RN or CHEBI/NCIT match. Curator review needed.` That is
  stale after the MeSH promotion but does not change the mapped identity.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, external
  prefix review row, unknown-term triage row, and ignored aggregate backups.

## Completeness

- The exact MeSH mapping is populated.
- Formula, CAS, InChI, SMILES, roles, components, source occurrences,
  environmental context, and discussion entries are not required for this MeSH
  registry record.

## Recommended Edits

- Optionally refresh
  `data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml`
  top-level `notes` so it no longer says curator review is needed after the
  successful MeSH promotion.
- On the next SSSOM export refresh, preserve the exact MeSH row but update the
  generated validation trailer so this record no longer carries a stale
  `UNKNOWN_TERM` tag. No identity edit is required.
