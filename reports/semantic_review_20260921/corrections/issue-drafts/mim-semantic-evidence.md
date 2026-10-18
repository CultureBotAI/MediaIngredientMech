Destination: https://github.com/CultureBotAI/MediaIngredientMech/issues
Title: Complete remaining semantic evidence review before approving the full MIM graph

The 2026-09-21 identity-correction batch addressed the 14 identity blockers: 11 were corrected or merged; three unsupported mappings were withdrawn and their records marked AMBIGUOUS. Resolving Artepaulin, 2-tetrachloroethane, and 2-dimethylsuccinic Acid still requires original source identity evidence.

The current full MIM graph retains 670 prediction-only role assertions, 11 roles without evidence, eight cellular roles without organism context, and the prior component-evidence findings, including 51 assertions derived by interpretation or abbreviation expansion. These are not semantically approved merely because structural validation passes.

Resolve findings against original sources, update content-bound review dispositions, regenerate SSSOM/KGX, and require the semantic release gate to pass. Evidence and the remaining backlog are in `reports/semantic_review_20260921/`, with the current snapshot under `corrections/`. Current release verdict: FAIL.
