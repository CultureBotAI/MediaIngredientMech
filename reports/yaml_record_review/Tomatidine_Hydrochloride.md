# `data/ingredients/mapped/Tomatidine_Hydrochloride.yaml`

## Verdict

Needs curation, major. The `CHEBI:9629` narrow parent repair is correct, but
the record still uses CAS `69004-03-1`, which resolves to toltrazuril instead
of tomatidine hydrochloride.

## Identity

- Reviewed record: `data/ingredients/mapped/Tomatidine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:69004-03-1`, parent
  `ontology_mapping.ontology_id: CHEBI:9629`, label `tomatidine`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `69004-03-1`.
- Synonyms: none.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Titanium_chloride` through `Tomatidine_Hydrochloride`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `tomatidine` confirms `CHEBI:9629` is the free-base
  tomatidine term and is the correct parent direction for a hydrochloride salt.
- Fresh PubChem name lookup for `Tomatidine hydrochloride` resolves to a
  steroidal hydrochloride with formula `C27H46ClNO2`, while CAS `69004-03-1`
  resolves to CID `68591` with formula `C18H14F3N3O4S`.
- PubChem synonym lookup for CID `68591` names that CAS object as toltrazuril
  and carries the old wrong `CHEBI:93130` cross-reference that this record's
  August curation removed from `ontology_mapping`.
- The final SSSOM still emits exact registry rows for `cas:69004-03-1` and
  `kgmicrobe.compound:tomatidine_hydrochloride`; both rows export
  `CAS:69004-03-1` in `other`.

## Issues

### Major: the exact registry identity still points to toltrazuril

The ontology parent was correctly moved from the toltrazuril-like
`CHEBI:93130` term to `CHEBI:9629` tomatidine, but the primary identifier was
left as `cas:69004-03-1`. A fresh PubChem lookup shows that CAS is the same
toltrazuril registry identity as the dropped `CHEBI:93130` structure, so the
two exact registry rows in the final SSSOM are wrong for Tomatidine
Hydrochloride.

## Completeness

- The aggregate row matches the per-record YAML and the specific
  `CHEBI:9629` narrowMatch target is appropriate.
- No final SSSOM free-text synonyms leak.
- The stale CAS primary and dependent exact registry rows still need repair.

## Recommended Edits

- Replace `cas:69004-03-1` with a reviewed registry identifier for tomatidine
  hydrochloride, then rebuild the Rule B1 `kgmicrobe.compound` row so the
  final exact registry outputs no longer preserve the toltrazuril CAS.
