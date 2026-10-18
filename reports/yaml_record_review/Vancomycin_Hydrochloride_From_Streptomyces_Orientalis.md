# `data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml`

## Verdict

Needs curation. The CAS-backed vancomycin hydrochloride identity, CAS RN,
formula, aggregate row, and CHEBI exact row pass, but the record has a
provisional `SELECTIVE_AGENT` role and the final SSSOM row exports a hydrate
label as `other` on the anhydrous hydrochloride mapping.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml`.
- Identifier and grounding: `identifier: CHEBI:9932` with matching
  `ontology_mapping.ontology_id`, label `Vancomycin hydrochloride`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `1404-93-9`.
- Synonyms: one exact source spelling, `Vancomycin x HCl`.
- Chemical fields: formula `C66H75Cl2N9O24.HCl`.
- Occurrences: two CultureMech recipe occurrences.
- Role: `SELECTIVE_AGENT` with provisional name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis` through `Vanillin`:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI-primary
  subset of this batch exited 0 for this file, `Vancoresmycin`,
  `Vanillic_Acid`, and `Vanillin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:9932` returns active label
  `Vancomycin hydrochloride`, CAS xref `1404-93-9`, and formula
  `C66H75Cl2N9O24.HCl`, matching the exact hydrochloride identity.
- `Vancomycin x HCl` is the absorbed duplicate source spelling and stays within
  the hydrochloride form.

## Issues

- Major: `physicochemical_roles.SELECTIVE_AGENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the name-pattern rule is
  provisional and still needs review.
- Major: the final SSSOM exact row
  `MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis skos:exactMatch
  CHEBI:9932` exports `Vancomycin Hydrochloride Hydrate` in `other`. That text
  names the distinct hydrate sibling, not the anhydrous `CHEBI:9932` term.

## Completeness

- The CAS-backed CHEBI mapping, CAS RN, formula, occurrence count, and
  aggregate copy agree.
- The final SSSOM row needs its cross-record hydrate-family synonym removed so
  the anhydrous exact match does not advertise a hydrate label.

## Recommended Edits

- Replace or remove
  `data/ingredients/mapped/Vancomycin_Hydrochloride_From_Streptomyces_Orientalis.yaml`
  `physicochemical_roles.SELECTIVE_AGENT`; keep it only if a maintained source
  supports vancomycin hydrochloride as a selective agent in the specific media
  records that use it.
- Remove `Vancomycin Hydrochloride Hydrate` from the SSSOM synonym enrichment
  or hydrate-family allowance feeding `MIM:Vancomycin_Hydrochloride_From_Streptomyces_Orientalis`,
  then rerun the SSSOM build and invariant checks.
