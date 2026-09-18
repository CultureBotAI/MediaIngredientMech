# `data/ingredients/mapped/56-dihydro-5-azathymidine.yaml`

## Verdict

Pass with minor issues. The exact MeSH identity, SSSOM row, and aggregate copy
pass; the record only retains a stale import note that still says curator
review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/56-dihydro-5-azathymidine.yaml`.
- Identifier and grounding: `identifier: mesh:C014480` with
  `ontology_mapping.ontology_id: mesh:C014480`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK metadata resolves `MESH:C014480` to
  `5,6-dihydro-5-azathymidine`.
- The official NLM MeSH RDF JSON for `C014480` reports active identifier
  `C014480` and label `5,6-dihydro-5-azathymidine`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-trimethoxybenzoate.yaml data/ingredients/mapped/56-dihydro-5-azathymidine.yaml data/ingredients/mapped/574-Trimethoxyisoflavone.yaml data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml data/ingredients/mapped/6-Hydroxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/56-dihydro-5-azathymidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:mesh aliases MESH:C014480`:
  returned the expected MeSH label.
- `uv run --frozen runoak -i sqlite:obo:mesh term-metadata MESH:C014480`:
  returned the expected MeSH identifier and label.

## Evidence

- The active MeSH supplemental concept supports the exact
  5,6-dihydro-5-azathymidine identity promoted from `UNMAPPED_0589`.
- The SSSOM row maps `MIM:56-dihydro-5-azathymidine` to `mesh:C014480` with
  `skos:exactMatch`, `registry:mesh`, and lexical curation provenance.
- The top-level `notes` field still contains the original import text, including
  `no CAS-RN or CHEBI/NCIT match. Curator review needed.` That is stale after
  the subsequent MeSH promotion, but it does not change the mapped identity.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, registry triage row confirming the earlier UNKNOWN_TERM finding was only
  missing prefix coverage, and ignored aggregate backups.

## Completeness

- The exact MeSH mapping is populated.
- Formula, CAS, InChI, SMILES, roles, components, source occurrences,
  environmental context, and discussion entries are not required for this MeSH
  registry record.

## Recommended Edits

- Optionally refresh `data/ingredients/mapped/56-dihydro-5-azathymidine.yaml`
  top-level `notes` so it no longer says curator review is needed after the
  successful MeSH promotion. No identity or SSSOM edit is required.
