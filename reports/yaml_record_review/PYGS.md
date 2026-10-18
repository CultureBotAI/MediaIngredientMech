# `data/ingredients/mapped/PYGS.yaml`

## Verdict

Needs curation; major. The local fallback identity and final SSSOM row are
clean, but the asserted starch component overstates the maintained
decomposition row for ambiguous `PYGS`.

## Identity

- Reviewed record: `data/ingredients/mapped/PYGS.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:pygs` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:pygs`, label `PYGS`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 3 MicrobeDecoder `bergey:substrates` occurrences and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` primary record.
- A fresh exact OLS4 search for `PYGS` found no exact public `PYGS` medium term.
- The final SSSOM row was inspected directly and maps `MIM:PYGS` exactly to
  `kgmicrobe.ingredient:pygs` with no `other` tokens.

## Evidence

- The peptone, yeast extract, and glucose components follow the local PYG base
  decomposition, and fresh OLS4 exact component-label lookups resolved
  `MICRO:0000178`, `FOODON:03315426`, and `CHEBI:17234`.
- Fresh OLS4 exact component-label lookup also resolves `CHEBI:28017` as
  `starch`.
- Major: `mappings/microbedecoder_residual_research_decomposition.tsv`
  assigns only `confidence=medium` to `PYGS` and says `S` is usually mineral
  salts but occasionally soluble starch. The YAML asserts `CHEBI:28017` starch
  as the fourth component, so one side of an explicitly ambiguous label was
  promoted to a concrete component.
- The final SSSOM emits a single exact local ingredient row and no unsafe
  synonyms.

## Completeness

- The fallback registry row correctly avoids mapping this ambiguous shorthand
  to the starch component.
- The component list is not complete enough to treat starch as the resolved
  fourth component until the `S` abbreviation is disambiguated.

## Recommended Edits

- Major: in `data/ingredients/mapped/PYGS.yaml`, either replace the starch
  component with a representation of the unresolved mineral-salts-versus-starch
  ambiguity, or split the source labels if MicrobeDecoder has enough context to
  distinguish the two `PYGS` formulations. Keep
  `mappings/microbedecoder_residual_research_decomposition.tsv` synchronized
  with the decision and rerun `scripts/validate_component_partonomy.py`.
