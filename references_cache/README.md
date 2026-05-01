# MIM references cache

Cached PubMed abstracts that back the `pmid` + `snippet` slots on
MIM evidence claims. Populated by
`culturebotai-claw/scripts/fetch_pubmed_abstracts.py` and consumed
by `culturebotai-claw/scripts/validate_evidence_references.py`.

Each file is named `PMID_NNNNNNNN.md` and contains the article
title, authors, journal, year, and full abstract — fetched once
from NCBI E-utilities and committed to the repo so:

- Validation runs offline (CI doesn't hit NCBI on every push).
- Snippets are checked against the *exact* abstract text the
  curator saw at curation time, not whatever NCBI happens to serve
  later (rare, but title revisions and abstract updates do occur).
- Reproducible literature evidence: anyone cloning the repo can
  re-run the validator against the same abstracts.

## When entries get added

`fetch_pubmed_abstracts.py` walks every MIM ingredient YAML, harvests
the `pmid` slots, and fetches any not yet cached. Run it before
`validate-evidence` whenever new PMIDs land.

## When entries get removed

Don't delete entries by hand — they may still be referenced by
historical curation_history records. If a PMID is genuinely retracted
or replaced, fetch a fresh copy by deleting the file and re-running
the fetcher; the new content will reflect NCBI's current state.

## Format

Standard Markdown so reviewers can browse cache entries directly.
The validator's substring match is whitespace- and case-insensitive
(NFKC normalized) so Markdown headers and emphasis don't interfere.
