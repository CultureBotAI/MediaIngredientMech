# IngredientRecord review checklist

Use this checklist for one ingredient. It does not require every optional slot
to be populated.

## Evidence standard

- An identity source must denote the exact supplied chemical form.
- Stable database IDs, DOI/PMID references, and official source URLs must
  resolve to the inspected record or document.
- Search snippets and research output are discovery aids, not evidence.
- Put evidence on the narrowest role, component, mapping, or context it supports.
- Preserve conflicts and bounded negative results; do not convert uncertainty
  into an exact mapping.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | Identifier and preferred term denote one exact substance or intentionally modeled mixture. | Hydrate, salt, stereo, charge, and generic-parent boundaries are explicit. |
| Mapping | Ontology ID, canonical label, predicate direction, quality, confidence, source, and version agree. | `MAPPED` is used only for a valid mapping and specificity loss is represented honestly. |
| Synonyms | Each synonym truly names this form and carries the right type/provenance. | Rejected or broader labels are not silently promoted to exact synonyms. |
| Supplied form | Formula, charge, hydrate/anhydrous state, solution/solid form, and source wording agree. | The modeled form is reproducible from the source claim. |
| Components | Component IDs, proportions/concentrations, units, and partonomy represent a mixture rather than false identity. | No component is treated as the whole and no mixture is mapped to one component. |
| Chemical properties | Formula, mass, structure-derived values, provenance, and retrieval date describe the same form. | Properties do not combine incompatible registry records. |
| Roles | Nutritional, physicochemical, cellular/metabolic, and community roles have appropriate context and evidence. | Roles are asserted for this substance and scope, not inferred from class alone. |
| Occurrences | Raw label, source record, recipe context, and occurrence count remain traceable. | A curator can recover why this ingredient exists and where it is used. |
| Environment | Environment relation and its direction match the asserted context. | Relevance does not imply natural occurrence without evidence. |
| Discussions/datasets | Each entry is relevant, durable, and actionable. | No generic placeholder or bibliography dump remains. |
| Audit | Status and append-only history match the actual mapping/content decision. | LLM assistance and any status transition are recorded honestly. |

## Synchronized surfaces

A complete edit leaves these consistent where applicable:

- `data/ingredients/{mapped,unmapped}/<slug>.yaml`;
- `data/curated/{mapped,unmapped}_ingredients.yaml`;
- `mappings/ingredient_mappings.sssom.tsv`;
- identifier/label registry and alias surfaces; and
- any generated report refreshed by its maintained recipe.
