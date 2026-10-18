# `data/ingredients/mapped/Sutezolid.yaml`

## Verdict

Pass. The CAS fallback identity, `NCIT:C152482` parent, PubChem structure
fields, aggregate row, and three final SSSOM rows all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sutezolid.yaml`.
- Identifier and grounding: `identifier: cas:168828-58-8` with
  `ontology_mapping.ontology_id: NCIT:C152482`, label `Sutezolid`, source
  `NCIT`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `168828-58-8`, PubChem CID `465951`, formula
  `C16H20FN3O3S`, and PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Supplemented_Seawater` through `Synephrine_Tartrate`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this NCIT parent
  because NCIT is outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `NCIT:C152482` with label `Sutezolid` and
  CAS Registry `168828-58-8`, matching the YAML parent and CAS fallback
  identifier.
- Fresh PubChem lookup for CID `465951` returns formula `C16H20FN3O3S` and the
  same InChI as the YAML; PubChem synonyms include CAS `168828-58-8`.
- The final SSSOM has the expected `skos:narrowMatch` parent row to
  `NCIT:C152482` plus exact CAS and KG-Microbe compound registry sibling rows,
  both publishing only `CAS:168828-58-8` in `other`.

## Completeness

- The CAS fallback identity, NCIT parent, PubChem CID, aggregate row, zero
  occurrence count, final parent row, and final registry sibling rows agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, PubChem,
  NCIT, final SSSOM, row-review, prefix-triage, and generated rows, and no
  second active MIM record for `cas:168828-58-8`.

## Recommended Edits

- None.
