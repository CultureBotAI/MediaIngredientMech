# `data/ingredients/mapped/Licl.yaml`

## Verdict

Needs curation. The CultureMech CHEBI:48607 anhydrous lithium chloride identity,
CAS RN, PubChem structure, CultureMech mineral role, and occurrence count pass,
but hydrate-form labels are published as exact synonyms in the final SSSOM
`other` field.

## Identity

- Reviewed record: `data/ingredients/mapped/Licl.yaml`.
- Identifier and grounding: `identifier: CHEBI:48607` with
  `ontology_mapping.ontology_id: CHEBI:48607`, label `lithium chloride`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7447-41-8`, molecular formula `Cl.Li`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Levorin` through `Lignin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Levulinic_Acid.yaml`, `Lichenan_Icelandic_Moss.yaml`, `Licl.yaml`, and
  `Lignin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:48607` as active `lithium chloride`, lists `LiCl`,
  `Lithiumchlorid`, `chlorure de lithium`, `cloruro de litio`, and
  `lithii chloridum` as synonyms, lists CAS `7447-41-8`, and records the same
  formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `7447-41-8` to CID `433294` with formula `ClLi` and
  the same InChI as the YAML record.
- PubChem resolves `Lithium chloride hydrate` to CID `23681138` with formula
  `ClH2LiO` and a water-containing InChI, so it is not a synonym for anhydrous
  `CHEBI:48607`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:48607`.
- Major: the final SSSOM `other` field publishes `Lithium chloride hydrate` and
  `LiCl.H O` as exact synonyms for anhydrous lithium chloride. The first token
  crosses the hydrate boundary; the second appears to be a malformed hydrate
  label from `sssom_other_backfill`.
- The `nutritional_roles.MINERAL_SOURCE` facet is supported by the original
  CultureMech `Role: Mineral` database entry and the #128 correction that
  intentionally avoided over-asserting `TRACE_ELEMENT`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  15-recipe occurrence count, and true anhydrous final synonyms are present and
  consistent.
- The published synonym surface is incomplete as a safe final product until
  hydrate labels are removed from this anhydrous record.

## Recommended Edits

- Major: remove the `LiCl.H O` `sssom_other_backfill` synonym from
  `data/ingredients/mapped/Licl.yaml` and prevent `Lithium chloride hydrate`
  from being emitted into the final `CHEBI:48607` SSSOM row.
- If the raw corpus needs a hydrated lithium chloride identity, curate it as a
  separate hydrate record instead of flattening it onto anhydrous LiCl.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, term, round-trip, component, and SSSOM validation.
