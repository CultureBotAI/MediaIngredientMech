# `data/ingredients/mapped/Xanthan_From_Xanthomonas_Campestris.yaml`

## Verdict

Needs curation. The CAS exact row and local exact registry row are present, but
the parent row maps xanthan gum to the MeSH source organism
`Xanthomonas campestris` instead of a chemical class; `CHEBI:189560` now
provides a better xanthan target.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Xanthan_From_Xanthomonas_Campestris.yaml`.
- Identifier and exact local identity: `cas:11138-66-2`.
- Current parent grounding: `ontology_mapping.ontology_id: mesh:D016959`, label
  `Xanthomonas campestris`, source `MESH`, and
  `mapping_quality: NARROW_MATCH`.
- CAS RN: `11138-66-2`.
- `mapping_status: MAPPED` and `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: zero.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wolfes_Vitamin_Mix` through `Xanthine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this CAS-primary row has no OBO adapter for that focused check.

## Evidence

- The record was backfilled to MeSH by a `stem-substring` parent search in May
  2026, before the adjacent MicrobeDecoder import established
  `CHEBI:189560` for xanthan.
- Fresh OLS4 lookup for `CHEBI:189560` returns active label `xanthan` and
  defines xanthan as the polysaccharide produced by `Xanthomonas campestris`,
  matching the chemistry of this source-qualified record.
- The final SSSOM currently exports
  `MIM:Xanthan_From_Xanthomonas_Campestris skos:narrowMatch mesh:D016959`,
  then preserves CAS and local kg-microbe exact rows alongside that organism
  parent.

## Issues

- Major: the parent `mesh:D016959` row points to the source organism
  `Xanthomonas campestris`, not to a broader chemical class. The exported
  `skos:narrowMatch` asserts a compound-to-organism relationship that should
  be replaced with xanthan chemistry.
- Major: now that `CHEBI:189560` exists for xanthan, the CAS-primary fallback
  is stale and should be re-evaluated against the active CHEBI term.

## Completeness

- The aggregate row and final SSSOM rows agree with the per-record YAML.
- The exact CAS/local identity row prevents complete identity loss, but the
  parent ontology row is wrong.

## Recommended Edits

- Replace the MeSH organism parent with `CHEBI:189560`; use an exact match if
  CAS `11138-66-2` is truly xanthan, or a close parent if the source-qualified
  record must preserve a more specific exact local identity.
- Rebuild SSSOM and rerun strict validation, LinkML term validation where
  applicable, SSSOM invariant validation, and the parent-mapping audit.
