MediaDive ingredient 1944 has a blank name and is reused for three different preparations. A global mapping from `mediadive.ingredient:1944` to yeast extract would also misidentify Trypticase peptone and MES rows. This is a source-identity defect; this review does not establish that the current KG emits a wrong chemical endpoint.

The worker01 canary is bound to MIM base `e000d66dd26ab053e9b17ce7bf8d3c873c3dde99` and dependency [MIM #1158](https://github.com/CultureBotAI/MediaIngredientMech/pull/1158). Its exact source case is `KG_CASE:e431bbfe8e78c226a9a06d038b7944f91e4580b44fe5b9e2c83d0e236c6d23cf`. Frozen `compounds.json` SHA256 is `5401db0bc697249c9b2b0ad0b950fd3c2b7629f0cdd10c7feaf1e40b0a3a4729`; object key `1944` retains `compound: ""`, attribute `w/v) Yeast extract (BD-Difco, 10%`, 5 ml, recipe order 12.

Complete admitted source context and live primary recipes distinguish:

| Recipe / solution / recipe_order | Native attribute | Original recipe meaning |
| --- | --- | --- |
| J935 / 4947 / 12 | `w/v) Yeast extract (BD-Difco, 10%` | 5 ml of a 10% w/v BD-Difco yeast-extract solution |
| J935 / 4947 / 13 | `w/v) Trypticase peptone (BD-BBL, 10%` | 20 ml of a 10% w/v BD-BBL Trypticase-peptone solution |
| J1053 / 5115 / 13 | `w/v) MES (pH 6.0, 20%` | 10 ml of a 20% w/v MES solution at pH 6.0 |

Primary sources: [MediaDive ingredient](https://mediadive.dsmz.de/ingredients/1944), [ingredient JSON](https://mediadive.dsmz.de/download/ingredient/1944/json), [J935 JSON](https://mediadive.dsmz.de/rest/medium/J935), [J1053 JSON](https://mediadive.dsmz.de/rest/medium/J1053), [original JCM 935](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=935), and [original JCM 1053](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1053). Retrieved 2026-11-08 UTC. The two live recipe responses match the retained admitted response bodies byte for byte. The three solution rows repeat the same three recipe rows; they are not six independent occurrences. The queue's `occurrences: 1` is explicitly a helper constant.

The ingredient JSON also gives `chebi_id: 1`. [EBI OLS ChEBI:1](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:1) marks it obsolete with replacement [CHEBI:18357](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18357), `(R)-noradrenaline`. Neither this source cross-reference nor a broad yeast-extract ontology term resolves the incompatible preparations.

Keep a source-scoped hold. No native MIM owner is identified, no alias/ontology/SSSOM edit is proposed, and no existing release hold is removed. Source correction belongs in MediaDive's ingredient/recipe representation or a separately reviewed, source-bound downstream correction that retains original records and uses recipe/solution/list-position identity. A bare component mapping must not replace a stock.

Acceptance for future resolution:

- Obtain corrected MediaDive ingredient identities for each preparation, or an explicit reviewed occurrence-scoped correction with the original source ID and raw fields retained.
- Preserve each recipe's stock concentration, supplier where stated, pH, amount, unit, order, and provenance; do not infer a catalog SKU or an exact supplied chemical form absent from the recipe.
- Reassess any intended MIM stock/ingredient owners independently and pass the normal owner-content and publication gates before releasing mappings.
- Recheck all three source contexts and the erroneous source cross-reference; a correction to the yeast row alone cannot resolve the global blank ID.

This is a bounded source finding from the unmatched-source canary. Related [MIM #1157](https://github.com/CultureBotAI/MediaIngredientMech/issues/1157) addresses five different IDs; [#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), [#811](https://github.com/CultureBotAI/MediaIngredientMech/issues/811) and [#868](https://github.com/CultureBotAI/MediaIngredientMech/issues/868) are broader material/alias queues. [KG-Microbe #1167](https://github.com/Knowledge-Graph-Hub/kg-microbe/issues/1167) and [#1171](https://github.com/Knowledge-Graph-Hub/kg-microbe/issues/1171) concern downstream normalization and occurrence preservation; [#1319](https://github.com/Knowledge-Graph-Hub/kg-microbe/issues/1319) concerns explicit `solution_id` substitution. They do not themselves resolve this shared blank `compound_id`. KG-Microbe #1009 closes a finite instruction/recipe-pair review, rather than this source-ID collision. This follows the read-only source review associated with #1788. Exact-ID and comment searches in both repositories found no existing 1944 finding; broader searches were bounded and are retained in the evidence. Existing issues remain open/closed as observed; no issue closure is requested.
