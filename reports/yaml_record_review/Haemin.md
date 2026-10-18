# `data/ingredients/mapped/Haemin.yaml`

## Verdict

Needs curation. The exact hemin ChEBI identity, CAS RN, structure fields,
occurrence count, and ChEBI-derived synonyms pass, but final SSSOM exports
recipe/vendor labels as exact synonyms and the `COFACTOR_PROVIDER` role is only
an in-session computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Haemin.yaml`.
- Identifier and grounding: `identifier: CHEBI:50385` with
  `ontology_mapping.ontology_id: CHEBI:50385`, label `hemin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `16009-13-5`, formula `C34H32ClFeN4O4`, InChI
  `InChI=1S/C34H34N4O4.ClH.Fe/c1-7-21-17(3)25-13-26-19(5)23(9-11-33(39)40)31(37-26)16-32-24(10-12-34(41)42)20(6)28(38-32)15-30-22(8-2)18(4)27(36-30)14-29(21)35-25;;/h7-8,13-16H,1-2,9-12H2,3-6H3,(H4,35,36,37,38,39,40,41,42);1H;/q;;+3/p-3/b25-13-,26-13-,27-14-,28-15-,29-14-,30-15-,31-16-,32-16-;;`,
  and SMILES
  `C=CC1=C(C)C2=Cc3c(C=C)c(C)c4[n]3[Fe]35([Cl])[N]2=C1C=c1c(C)c(CCC(=O)O)c([n]13)=CC1=[N]5C(=C4)C(C)=C1CCC(=O)O`.
- Occurrence statistics: `total_occurrences: 257` and `media_count: 256`.
- Role facet: `COFACTOR_PROVIDER` with `COMPUTATIONAL_PREDICTION` evidence from
  provisional in-session Claude reasoning.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H3bo3.yaml data/ingredients/mapped/HOMOPIPES.yaml data/ingredients/mapped/Haemin.yaml data/ingredients/mapped/Halomicin.yaml data/ingredients/mapped/Hans_1000x_Minerals.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:50385` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:50385` as active `hemin` with CAS `16009-13-5`, formula
  `C34H32ClFeN4O4`, the same InChI, and the same SMILES.
- The final SSSOM ChEBI-derived synonym tokens all occur as ChEBI synonyms for
  `CHEBI:50385`, and the final `CAS:16009-13-5` token matches
  `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonyms are correctly filtered from
  final SSSOM.
- Major: `Hemin (0.1% in 0.05 N NaOH)` is a concentration-specific prepared
  solution and `hemin (ICN)` is vendor-qualified; neither is an exact synonym
  of hemin, and both are exported in final SSSOM.
- Major: the `COFACTOR_PROVIDER` facet is supported only by
  `reference_type: COMPUTATIONAL_PREDICTION` from an in-session LLM note.
- The final SSSOM otherwise publishes one `skos:exactMatch` row from
  `MIM:Haemin` to `CHEBI:50385`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, exact hemin identity row, and ChEBI-derived synonyms are present
  and consistent.
- The synonym export and role facet remain incomplete until non-exact recipe
  labels and the provisional cofactor role are curated.

## Recommended Edits

- Major: suppress or retype `Hemin (0.1% in 0.05 N NaOH)` and `hemin (ICN)` so
  they no longer appear in final SSSOM as exact synonyms.
- Major: review the `COFACTOR_PROVIDER` facet and either replace the
  provisional in-session evidence with an external source or remove the
  unsupported role.
