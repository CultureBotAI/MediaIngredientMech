# `data/ingredients/mapped/H3bo3.yaml`

## Verdict

Needs curation. The exact boric-acid ChEBI identity, CAS RN, structure fields,
CultureMech trace-element role, occurrence count, and ChEBI-derived synonyms
pass, but malformed and catalog-decorated duplicate labels are exported as
final SSSOM exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/H3bo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:33118` with
  `ontology_mapping.ontology_id: CHEBI:33118`, label `boric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `10043-35-3`, formula `H3BO3`, InChI
  `InChI=1S/BH3O3/c2-1(3)4/h2-4H`, and SMILES `[H]OB(O[H])O[H]`.
- Occurrence statistics: `total_occurrences: 4216` and `media_count: 4212`.
- Role facet: `TRACE_ELEMENT` with `DATABASE_ENTRY` evidence from CultureMech
  `Mineral source` annotations.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H3bo3.yaml data/ingredients/mapped/HOMOPIPES.yaml data/ingredients/mapped/Haemin.yaml data/ingredients/mapped/Halomicin.yaml data/ingredients/mapped/Hans_1000x_Minerals.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:33118` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:33118` as active `boric acid` with CAS `10043-35-3`,
  formula `H3BO3`, the same InChI, and the same SMILES.
- The final SSSOM ChEBI-derived synonym tokens `B(OH)3`, `[B(OH)3]`,
  `boron trihydroxide`, `orthoboric acid`, and `trihydroxidoboron` all occur
  as ChEBI synonyms, and the final `CAS:10043-35-3` token matches
  `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonyms are correctly filtered
  from final SSSOM.
- Major: final SSSOM exports `H3BO`, `H3BO3(Baker 0084)`, and `H BO` as
  exact synonyms. Those are a truncated duplicate label, a Baker catalog
  variant, and a malformed spaced formula rather than real boric-acid
  synonyms.
- The final SSSOM otherwise publishes one `skos:exactMatch` row from
  `MIM:H3bo3` to `CHEBI:33118`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, CultureMech role facet, and exact boric-acid identity row are
  present and consistent.
- The synonym export is incomplete until absorbed duplicate aliases are filtered
  to real synonyms.

## Recommended Edits

- Major: suppress or delete `H3BO`, `H3BO3(Baker 0084)`, and `H BO` so the
  final SSSOM `other` column contains only genuine boric-acid synonyms and the
  CAS token.
