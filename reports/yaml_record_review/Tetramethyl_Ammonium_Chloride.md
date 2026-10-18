# `data/ingredients/mapped/Tetramethyl_Ammonium_Chloride.yaml`

## Verdict

Needs curation - major. The local chloride-salt identity, close cation parent,
occurrence count, aggregate row, and final SSSOM rows pass, but the remaining
chemical properties still describe the tetramethylammonium cation rather than
tetramethylammonium chloride.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Tetramethyl_Ammonium_Chloride.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:tetramethyl_ammonium_chloride` with
  `ontology_mapping.ontology_id: CHEBI:46020`, label
  `tetramethylammonium`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: cation-only `InChI=1S/C4H12N...` and cation-only
  molecular weight `74.147`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetracycline` through `Tetramethyl_Ammonium_Chloride`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search confirms `CHEBI:46020` still resolves as
  `tetramethylammonium`; the exact OLS4 term endpoint returned 404 for this
  CHEBI term, but the local Engine A validator also resolves and validates it.
- Fresh PubChem lookup for `Tetramethyl ammonium chloride` resolves CID 6379
  with formula `C4H12ClN`, chloride-salt InChI
  `InChI=1S/C4H12N.ClH...`, and synonym `75-57-0`.
- The final SSSOM correctly publishes a `skos:closeMatch` row to the
  cation-only `CHEBI:46020` and an exact local registry sibling row to
  `kgmicrobe.compound:tetramethyl_ammonium_chloride`.
- Major: the YAML `chemical_properties.inchi` is still the cation-only
  `CHEBI:46020` InChI and omits chloride, even after the record was corrected
  to keep the cation only as a close parent.

## Completeness

- The local chloride-salt identity, CHEBI cation parent, occurrence count,
  aggregate row, and final SSSOM rows agree.
- The chemical-property block is incomplete until it either describes the
  chloride salt or is removed so the record does not publish stale cation
  structure for a local chloride identity.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected salt-ion repair, rejected
  cation-synonym cleanup, aggregate, occurrence-membership, final SSSOM, tests,
  and generated rows.

## Recommended Edits

- Major: replace the cation-only `chemical_properties` in
  `data/ingredients/mapped/Tetramethyl_Ammonium_Chloride.yaml` with
  chloride-salt formula and structure fields, or clear them if no maintained
  salt-specific structure source should be stored.
- Major: synchronize `data/curated/mapped_ingredients.yaml` and regenerate
  docs after the per-record YAML no longer carries cation-only chemistry.
