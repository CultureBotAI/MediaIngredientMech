#!/usr/bin/env bash
# Engine-A OBO-safety gate for `just validate-terms[-all]` (PR #50 RISK fix).
#
# linkml-term-validator validate-data --labels passes EVERY ontology id in the
# file to OAK's sqlite:obo: adapter. A NON-OBO prefix (cas:, kgmicrobe.compound:,
# kgmicrobe.ingredient:, MICRO: — no bbop-sqlite remote db, or a 0-byte stub)
# makes OAK attempt a futile S3 download and exit 1, crashing the whole recipe
# and blocking the documented Phase-2 `qc` promotion regardless of whether the
# labels are correct. Engine B (scripts/validate_id_label_correspondence.py,
# `just validate-products`) already covers those ids via its prefix allowlist,
# reporting them SKIPPED_NO_ADAPTER / SKIPPED_EMPTY_ADAPTER without downloading.
#
# This helper inspects a single ingredient YAML and exits:
#   0  -> SAFE: every ontology id/term prefix is in the OBO allowlist (or there
#         are no ontology ids at all) -> the caller runs Engine A.
#   1  -> UNSAFE: at least one ontology id uses a non-OBO prefix -> the caller
#         SKIPS Engine A for this file (Engine B will validate it instead).
#
# Usage: scripts/_engine_a_obo_safe.sh <file.yaml> "CHEBI FOODON NCIT ..."
set -uo pipefail

file="${1:?usage: _engine_a_obo_safe.sh <file.yaml> <allowed-prefixes>}"
allowed="${2:?missing allowed-prefixes}"

# Pull the CURIE values bound by the schema for --labels: ontology_id and
# environment_term. Match `  ontology_id: PREFIX:local` (quoted or not) and
# extract the bare prefix. Only these two slots drive Engine A's OAK lookups.
prefixes=$(
    grep -hoE '^[[:space:]]*(ontology_id|environment_term):[[:space:]]*"?[A-Za-z][A-Za-z0-9._]*:' "$file" 2>/dev/null \
        | sed -E 's/^[[:space:]]*(ontology_id|environment_term):[[:space:]]*"?//; s/:$//' \
        | sort -u
)

# No ontology ids -> nothing for OAK to download -> safe to run Engine A.
[ -z "$prefixes" ] && exit 0

# Compare prefixes case-insensitively: the data carries lowercase `mesh:` while
# the allowlist (and OAK's OBO CURIEs) use uppercase `MESH`, so a case-sensitive
# `=` test silently classed every mesh record as UNSAFE and skipped Engine A for
# it — Engine A never validated a single MeSH record despite MESH being in the
# allowlist. nocasematch fixes `[[ ==  ]]` and works on bash 3.2 (macOS) too.
shopt -s nocasematch
while IFS= read -r p; do
    [ -z "$p" ] && continue
    found=1
    for a in $allowed; do
        if [[ "$p" == "$a" ]]; then found=0; break; fi
    done
    # An id whose prefix is NOT in the OBO allowlist would crash OAK -> unsafe.
    [ "$found" -ne 0 ] && exit 1
done <<< "$prefixes"

exit 0
