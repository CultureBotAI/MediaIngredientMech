A further current ChEBI hydration discrepancy was reproduced during worker01 continuation, on **CHEBI:131366, disodium tetraborate decahydrate**. This is distinct from the compounds already listed in this issue.

| Evidence | Content |
| --- | --- |
| Exact frozen source | MediaDive ingredient196, `Na2B4O7 x 10 H2O`;104 media rows across103 media and29 overlapping solution rows. These views overlap and are not summed as observations; the original queue helper count is retained. |
| Original recipes | Inspected DSMZ/JCM recipes retain the printed decahydrate formula. DSMZ770 separately uses1.8mL of a0.1%w/v stock; that occurrence is not the neat hydrate. |
| Current official ChEBI | Name and definition say decahydrate, but formula is `10H2O.H4B4O9.2Na`, mass417.401, with ten explicit water molecules plus the hydroxylated tetraborate structure. |
| Stoichiometric check | The supplied source formula expands to `Na2B4H20O17`; the official term formula expands to `Na2B4H24O19`, a difference of **two H2O**. |
| Current MIM owner | `data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml` uses CHEBI:131366 and the same discrepant chemical formula. Name/CAS agreement does not settle the structural discrepancy. |

Please resolve the ontology formula/structure hydration accounting against authoritative structural evidence and review the MIM chemical properties and exact relation accordingly. Preserve source decahydrate specificity and the separate770 stock context. No silent formula normalization, anhydrous substitution, or full-row approval is proposed by this finding.

Primary authority: [official ChEBI131366](https://www.ebi.ac.uk/chebi/backend/api/public/compound/131366/). Evidence capture and full source applicability are bound in [case175 decision](https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/decisions.fragment.json) and [root_substances/kg26/captures/context-review-ledger.json](https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/root_substances/kg26/captures/context-review-ledger.json). [MIM #718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718) remains the related held-owner curation backlog. This is a tracking comment only; no external source contact or ontology submission was performed.
