# Resolving the CultureMech ingredient residual

CultureMech resolves recipe ingredient labels against MIM's **literal** label index
(`docs/data/label_index.csv`, vendored in CultureMech at a pinned commit). A surface form
that differs from an indexed label only by punctuation, a vendor tag, a concentration
annotation, or a Unicode codepoint therefore fails to resolve even where MIM already holds
the compound. As of 2026-08-30 that was 6,105 ingredient mentions over 1,911 distinct
labels.

Read as a raw number that looks like ~1,900 compounds needing research. It is not, and
knowing the split is what makes the work tractable.

## Step 1 — triage (read-only)

```
python scripts/triage_culturemech_residual.py \
    --occurrences ../CultureMech/output/ingredient_occurrences.tsv \
    --out reports/culturemech_residual_triage.tsv
```

| bucket | meaning | what it needs |
|---|---|---|
| `ALIAS` | folds onto a MAPPED record | a synonym |
| `UNMAPPED` | folds onto a record that exists but is ungrounded | a synonym, then grounding |
| `AMBIGUOUS` | two or more records publish the label | a merge or granularity decision (#504) |
| `NOISE` | CultureMech parse damage | an upstream fix (CultureMech#387) |
| `RESIDUAL` | genuinely absent from MIM | grounding, then research or a mint |

The fold is comparison-only and deliberately conservative. **It never folds away a
hydration state** — `CaCl2` and `CaCl2 x 2 H2O` are 110.98 and 147.01 g/mol
(`MAPPING_SEMANTICS.md` §3), so treating `(anhydrous)` as decoration lets an anhydrous
surface form inherit a hydrate's identifier. It also never strips a parenthesis that is
part of a formula token: `AlK(SO4)2` must not become `alk 2`.

## Step 2 — apply the alias head (dry-run by default)

```
python scripts/apply_culturemech_aliases.py                 # ALIAS + UNMAPPED
python scripts/apply_culturemech_aliases.py --apply
just sync-curated          # per-record wins; NOT sync-individual
just export-lists
```

Adding a surface form as a synonym asserts no new chemical identity, so this is the
zero-risk head of the work. `sync-individual` is the wrong direction here — it projects
the collection over the per-record tree and reverts these edits.

## Step 3 — propose exact groundings for the rest (read-only)

```
python scripts/propose_residual_groundings.py \
    --sources CHEBI,FOODON,MICRO,ENVO,UBERON,BTO,NCIT --ols-sources MICRO
```

Only *exact* matches are proposed: the query equals the term's label or an exact synonym.
Each hit is routed by whether MIM already holds the CURIE — in MIM the `identifier` IS the
ontology CURIE, so a hit on a held CURIE means the answer is a synonym onto that record,
never a new record (which would be a duplicate by construction).

MICRO is queried over OLS4 because its local semantic-sql build is a 0-byte stub.

## Step 4 — apply

```
python scripts/apply_culturemech_aliases.py --groundings reports/...tsv --apply  # synonyms
python scripts/create_records_from_groundings.py --groundings reports/...tsv --apply  # new records
python scripts/promote_resolved_unmapped.py --identifier UNMAPPED_NNNN --to <CURIE> ...  # promotions
```

`create_records_from_groundings.py` routes a surface form MIM already holds as an UNMAPPED
record to a *promotion* rather than a creation, so the existing record's synonyms,
occurrence statistics and curation history are not stranded.

## Why each guard exists

Every one of these was added after it caught something real. They are the reason the
pipeline can be trusted, and removing one silently re-opens a way to publish a false claim.

| guard | what it caught |
|---|---|
| hydration state is never folded | `CaCl2 (anhydrous)` inheriting a hydrate's identifier |
| a formula's parenthesis is never stripped | `AlK(SO4)2 (anhydrous)` folding to `alk 2` |
| `REJECTED_LABEL` is never promoted | undoing #477 |
| an identifier held by >1 record is skipped | ownership is a merge decision |
| a spelling two records would claim is dropped | an ambiguous index row; CultureMech fails closed on it |
| NCIT and MESH match on the primary label only | `B12` → `TNFAIP1 wt Allele` via a gene-symbol alias |
| names under 3 characters are never matched | `X` → UBERON "area X of ventral lateral nucleus" |
| the matched term must denote a substance | `Dissolve` → NCIT:C64929, a procedure (the #356 class) |
| ontology preference outranks query variants | `Air`→NCIT and `air`→ENVO, decided by capitalisation |
| OLS4 `is_defining_ontology=false` is refused | MicrO's ~1,472 non-round-tripping classes |
| server-side exact matches are trusted | discarding every OLS4 *synonym* match |

## What the pipeline deliberately will not do

- **Force a match.** A wrong grounding is worse than an honest UNMAPPED.
- **Mint.** Where no ontology term exists at any granularity, `MAPPING_SEMANTICS.md` §3
  step 3 mints a `kgmicrobe.ingredient:` term — but that publishes new identifiers and
  belongs in its own reviewed change.
- **Ground a variable-composition mixture** that no ontology models. Staying UNMAPPED is
  the correct outcome for most `UNDEFINED_MIXTURE` records.
