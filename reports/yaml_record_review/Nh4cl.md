# `data/ingredients/mapped/Nh4cl.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:31206` ammonium chloride identity,
CAS-backed structure, source-backed `NITROGEN_SOURCE` role, occurrence count,
and core final row pass, but the record still has a duplicate provisional
nitrogen-source role and final SSSOM publishes malformed, CAS-decorated,
catalog, and role-qualified labels as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4cl.yaml`.
- Identifier and grounding: `identifier: CHEBI:31206` with
  `ontology_mapping.ontology_id: CHEBI:31206`, label `ammonium chloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4665 CultureMech recipe occurrences across 4665 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh4cl` through `Nh4no3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:31206` as active
  `ammonium chloride` with formula `Cl.H4N`, CAS `12125-02-9`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `12125-02-9` resolves to ammonium chloride
  with the same InChI, supporting the chemical block and resolved CAS.
- One `NITROGEN_SOURCE` assertion is supported by imported CultureMech
  `Nitrogen source` role text, and raw `Role:`/`Properties:` labels are
  filtered from final SSSOM.
- Major: the second `NITROGEN_SOURCE` assertion is only a provisional
  `COMPUTATIONAL_PREDICTION` from inorganic-ammonium-salt ancestry; it is
  redundant with the source-backed role and should not remain as active
  evidence.
- Major: final SSSOM `other` still publishes malformed `NH4Cl2`,
  CAS-decorated `NH4Cl(CAS: 12125-02-9)`, vendor/catalog
  `NH4Cl(Fisher A 649-500)`, and role-qualified
  `Ammonium chloride (nitrogen source)`. None is an unconstrained synonym for
  `CHEBI:31206`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 4665/4665 occurrence
  count, and final exact row otherwise agree.
- The remaining consequential gaps are the duplicate provisional role and the
  unsafe final SSSOM synonym tokens.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh4cl.yaml`, remove the duplicate
  CHEBI-ancestry `NITROGEN_SOURCE` role so only the CultureMech
  `DATABASE_ENTRY` role remains.
- Major: in the same maintained YAML, reject or demote `NH4Cl2`,
  `NH4Cl(CAS: 12125-02-9)`, `NH4Cl(Fisher A 649-500)`, and
  `Ammonium chloride (nitrogen source)`, then rebuild final SSSOM so the row
  exports only real ammonium chloride synonyms plus `CAS:12125-02-9`.
