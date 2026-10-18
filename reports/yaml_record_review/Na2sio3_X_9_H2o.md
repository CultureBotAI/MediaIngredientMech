# `data/ingredients/mapped/Na2sio3_X_9_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132108` sodium silicate nonahydrate
identity, CAS-backed structure, duplicate merges, occurrence count, and
`MINERAL_SOURCE` role pass, but final SSSOM still publishes anhydrous, typoed,
and catalog-specific labels as nonahydrate synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2sio3_X_9_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:132108` with
  `ontology_mapping.ontology_id: CHEBI:132108`, label
  `sodium silicate nonahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 36 CultureMech recipe occurrences across 36 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2seo35h2o` through `Na2so3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132108` as active
  `sodium silicate nonahydrate`, with formula `9H2O.2Na.O3Si`, CAS
  `13517-24-3`, and an InChI matching the record.
- A fresh PubChem CAS lookup for `13517-24-3` resolves to sodium silicate
  nonahydrate with the same formula and InChI, so the chemical block matches the
  hydrate-specific ChEBI identity.
- The `MINERAL_SOURCE` role is supported by imported CultureMech `Mineral` role
  text on this inorganic mineral salt.
- Major: final SSSOM `other` publishes `Na2SiO3`, which names an anhydrous
  sodium metasilicate surface rather than the nonahydrate, and
  `Na2SiO3 x 9 H20`, whose water formula is typoed with a zero.
- Major: final SSSOM `other` also publishes CAS-decorated and Sigma-catalog
  source labels from CultureMech. Those strings are procurement/context labels,
  not exact synonyms for the nonahydrate.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 36/36 occurrence
  count, duplicate merges, mineral-source role, and exact final SSSOM row
  otherwise agree.
- The remaining consequential gap is cleanup of anhydrous, typoed, and
  catalog-specific labels in the final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2sio3_X_9_H2o.yaml`, demote or reject the
  anhydrous `Na2SiO3`, the typoed `Na2SiO3 x 9 H20`, and the CAS/vendor
  decorated CultureMech raw labels so they no longer publish as exact
  `CHEBI:132108` synonyms. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
