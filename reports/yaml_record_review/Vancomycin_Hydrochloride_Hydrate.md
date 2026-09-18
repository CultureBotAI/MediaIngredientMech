# `data/ingredients/mapped/Vancomycin_Hydrochloride_Hydrate.yaml`

## Verdict

Needs curation. The hydrate-to-parent close match and CAS exact SSSOM rows are
present, but the record still lacks the exact kg-microbe hydrate anchor row
tracked by `reports/hydrate_grounding.tsv` and has a provisional
`SELECTIVE_AGENT` role.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Vancomycin_Hydrochloride_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:123409-00-7` with parent
  `ontology_mapping.ontology_id: CHEBI:9932`, label
  `Vancomycin hydrochloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `123409-00-7`.
- Chemical fields: formula `C66H75Cl2N9O24.HCl`, inherited from the anhydrous
  parent because the unspecified hydrate has no exact CHEBI term.
- Occurrences: 0.
- Role: `SELECTIVE_AGENT` with provisional name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis` through `Vanillin`:
  exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this CAS-primary hydrate row has no OBO adapter for that focused
  check.

## Evidence

- Fresh OLS4 lookup for `CHEBI:9932` returns active label
  `Vancomycin hydrochloride` and no child/descendant hydrate term, which
  supports keeping the CHEBI parent row as `skos:closeMatch` rather than
  `skos:exactMatch` or `skos:narrowMatch`.
- PubChem name lookup for CAS `123409-00-7` returned no CID, and
  `reports/hydrate_grounding.tsv` keeps this record in
  `CAS_MISSING_ANCHOR_ROWS`.
- The final SSSOM has the parent row
  `MIM:Vancomycin_Hydrochloride_Hydrate skos:closeMatch CHEBI:9932` and a CAS
  exact row for `cas:123409-00-7`; a hidden/ignored-inclusive search across the
  worktree found only historic review TSV rows for
  `kgmicrobe.compound:vancomycin_hydrochloride_hydrate`, not a current final
  SSSOM exact row to that local anchor.

## Issues

- Major: the exact kg-microbe hydrate anchor row tracked by
  `reports/hydrate_grounding.tsv` is still missing, leaving the CAS-primary
  hydrate represented by only the close parent and CAS fallback rows.
- Major: `physicochemical_roles.SELECTIVE_AGENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the name-pattern rule is
  provisional and still needs review.

## Completeness

- The CHEBI parent close match, CAS exact row, aggregate copy, and hydrate-audit
  classification agree.
- The hydrate stoichiometry remains unspecified; the local record should not be
  promoted to an exact CHEBI hydrate until a source establishes the exact water
  count or CHEBI adds a matching class.

## Recommended Edits

- Add the missing exact local hydrate anchor for
  `data/ingredients/mapped/Vancomycin_Hydrochloride_Hydrate.yaml` so the final
  SSSOM no longer leaves it in the `CAS_MISSING_ANCHOR_ROWS` bucket; rerun
  `report_hydrate_grounding.py`, SSSOM generation, and the SSSOM invariant
  checks.
- Replace or remove this record's `physicochemical_roles.SELECTIVE_AGENT`; keep
  it only if a maintained source supports vancomycin hydrochloride hydrate as a
  selective agent in the specific media records that use it.
