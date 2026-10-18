# `data/ingredients/mapped/Α1-Acid_Glycoprotein_From_Bovine_Plasma.yaml`

## Verdict

Needs curation. The record preserves CultureBotHT's CAS fallback for bovine
alpha1-acid glycoprotein and exports only the local CAS identity row, but its
PubChem structure fields point to CID 439212, a small `Glycoprotein` entry with
formula `C28H47N5O18`, not a bovine plasma alpha1-acid glycoprotein.

## Identity

- Reviewed record: same path as the report heading.
- Identifier and grounding: `identifier: cas:66455-27-4` with matching
  `ontology_mapping.ontology_id`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `66455-27-4`.
- Structure: formula `C28H47N5O18`, InChI, SMILES, and PubChem CID `439212`.
- Synonyms: none.
- Occurrences: none recorded, which is coherent for a CultureBotHT-only
  fallback import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 4-file batch:
  exited 0 and wrote zero ERROR rows.
- Focused Engine A label validation was skipped for this record because the
  exact identity is a CAS registry CURIE.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh PubChem lookup by CAS `66455-27-4` returned no CID.
- Fresh PubChem lookup of stored CID `439212` returned title `Glycoprotein` and
  the same small `C28H47N5O18` formula stored in this YAML.

## Evidence

- The final SSSOM correctly preserves the registry identity row:
  the MIM subject exact-matches `cas:66455-27-4`.
- The final SSSOM `other` field exports only matching `CAS:66455-27-4`.
- No current evidence ties PubChem CID `439212` or formula `C28H47N5O18` to the
  CultureBotHT source string for bovine plasma alpha1-acid glycoprotein.

## Issues

- Major: the populated structure fields are a small PubChem `Glycoprotein`
  molecule, not a bovine plasma alpha1-acid glycoprotein preparation, so the
  record should not advertise formula, InChI, SMILES, or CID `439212` as
  chemical properties of `cas:66455-27-4`.

## Completeness

- The CAS fallback identity, aggregate copy, and final SSSOM row agree.
- The PubChem structure backfill needs to be removed or replaced with evidence
  that truly belongs to CAS `66455-27-4`.

## Recommended Edits

- Remove `molecular_formula`, `smiles`, `inchi`, and `pubchem_cid: 439212`
  unless a maintained source ties that CID to CAS `66455-27-4`.
- Consider whether a bovine plasma glycoprotein preparation should remain
  `SINGLE_INGREDIENT` or become an undefined purified protein preparation.
- Rebuild SSSOM and rerun strict validation plus the SSSOM invariant gate.
