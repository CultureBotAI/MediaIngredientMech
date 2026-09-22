# Trait phrases in ingredient synonyms: issue #703

The reviewed baseline contains 3,018 SSSOM data rows. Exactly 46 complete
activity/assay strings occur in `other` across 39 rows and 39 source records.
Of their source synonym entries, 34 were `RAW_TEXT` and 12 were
`EXACT_SYNONYM`. Each complete string describes an activity, assay response,
or contextual role rather than naming the ingredient.

The correction changes only those 46 `synonym_type` values to
`REJECTED_LABEL` and appends one LLM-assisted curation event per record.
Original text, source metadata, synonym positions, earlier history, mappings,
roles, and all other source fields are preserved. No prefix is stripped to
create a new alias, and no organism trait assertion is inferred.

The exact source and SSSOM observations are in [decisions.json](decisions.json),
including complete original records, their hashes, exact mapping rows, token
positions, original synonym payloads, import/backfill history references, and
individual reasons. [decisions.tsv](decisions.tsv) is the compact per-token
view. The original labels themselves and their source provenance provide the
evidence needed for this bounded non-name classification; this is not a
literature review or certification of the ingredient identities.

All 46 strings are unambiguous non-names. An exhaustive filesystem scan of
individual ingredient YAML, including ignored files, found no additional
strings with these 12 prefixes. Other colons in published `other` included
CAS annotations, chemical stoichiometric ratios, lipid notation, and systematic
names; the trait decisions do not reject these merely for containing colons.

Related unresolved source observations were reported to the parent review,
without edits or approval: `Ferrihydrite` also retains the unprefixed alias
`goethite`; `Lactate` contains both L-lactate and DL-lactate aliases; and
`Hydrogen_gas` contains `H2_CO2` and `H2_methanol` aliases. Rejecting a complete
trait phrase neither resolves nor endorses those separate identity questions.

The reproducible mutator [apply.py](apply.py) validates all original and
proposed records against the closed schema before writing any record, checks
the exact source bytes and identifiers, derives only the reviewed type changes,
and uses the maintained curation-event helper and validated writer. A second
application is idempotent; changed source records fail closed. The default
mode is read-only. On the maintained environment:

```bash
/private/tmp/mim-710-locked/bin/python reports/sssom_completion_20260921/trait_synonyms/apply.py
/private/tmp/mim-710-locked/bin/python reports/sssom_completion_20260921/trait_synonyms/apply.py --apply
/private/tmp/mim-710-locked/bin/python reports/sssom_completion_20260921/trait_synonyms/apply.py --verify
```

The application receipt records the bounded source validation. Aggregate,
SSSOM, label-index, release-hold, and review-artifact synchronization are owned
by the parent task. The source correction is complete only when those generated
surfaces also exclude the rejected strings and their checks pass. The existing
negative release hold for `Aromatic_Compound` must be explicitly replaced with
fresh evidence for the corrected source before that mapping can be released.

Issue: <https://github.com/CultureBotAI/MediaIngredientMech/issues/703>.
