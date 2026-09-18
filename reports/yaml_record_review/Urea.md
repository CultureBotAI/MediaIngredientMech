# `data/ingredients/mapped/Urea.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, structure fields,
catalog variant, aggregate row, and most final SSSOM synonyms pass, but final
SSSOM `other` exports process-qualified `hydrolysis: urea` text and the
`NITROGEN_SOURCE` role is still provisional in-session evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Urea.yaml`.
- Identifier and grounding: `identifier: CHEBI:16199` with matching
  `ontology_mapping.ontology_id`, label `urea`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `57-13-6`.
- Synonyms: raw CultureMech properties, CHEBI-derived synonyms, one
  process-qualified synonym, and one Sigma catalog variant.
- Occurrences: 72 CultureMech recipe occurrences in 71 media.
- Roles: one `nutritional_roles.NITROGEN_SOURCE` facet at confidence `0.6`.
- KG-Microbe node: `CHEBI:16199`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uranyl_Acetate` through `Uridine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:16199` returns active label `urea`, CAS xref
  `57-13-6`, formula `CH4N2O`, the same InChI and SMILES as the YAML, and the
  exported non-process SSSOM `other` labels as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Urea skos:exactMatch CHEBI:16199` and exports the structured CAS token
  and curated catalog variant in `other`.

## Issues

### Major: final `other` exports process-qualified text

`hydrolysis: urea` describes a process-specific import context, not an exact
synonym for the urea compound. It should not be present in the final published
SSSOM synonym surface.

### Major: `NITROGEN_SOURCE` is provisional in-session LLM evidence

The only role assertion is:

```yaml
nutritional_roles:
- role: NITROGEN_SOURCE
  confidence: 0.6
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Assigned by in-session Claude reasoning (no external API)
    curator_note: Provisional in-session LLM role assignment; review recommended.
```

The exact CHEBI identity does not independently curate the nitrogen-source
role.

## Completeness

- The exact CHEBI identity, CAS RN, structure fields, catalog variant,
  occurrence count, KG-Microbe node, aggregate copy, and own SSSOM row agree
  apart from the noisy process-qualified `other` token.
- Raw `Cross-references:` and `Properties:` CultureMech strings are kept out of
  final SSSOM `other`.

## Recommended Edits

- Mark `hydrolysis: urea` as non-exportable provenance so final SSSOM `other`
  keeps only true urea synonyms, the Sigma catalog variant, and `CAS:57-13-6`.
- Replace the `NITROGEN_SOURCE` computational prediction with curated
  database/literature evidence, or remove `nutritional_roles` until such
  support is added.
