Title: Do not infer the T. medium TYGVS peptone from a different-species recipe

Adversarial review of #710 found that the proposed TYGVS component correction replaced Trypticase (`MICRO:0000175`) with tryptone (`MICRO:0000182`) using a T. denticola protocol. The actual MicrobeDecoder source row names T. medium; sharing the oral TYGVS acronym does not establish identical recipe composition.

Primary methods provide a concrete counterexample: https://pmc.ncbi.nlm.nih.gov/articles/PMC145376/ calls the T. medium broth Trypticase–yeast extract–gelatin–volatile fatty acids–serum, while https://academic.oup.com/femspd/article/60/3/251/530699 names tryptone for T. denticola.

Restore the original component identity and provisional assertion method/completeness, record the recovered source context and conflict, and keep all four TYGVS component findings open until the original recipe/citation chain is verified. Add a verification that no component or evidence grade was strengthened by the unsupported cross-species inference.
