# Occurrence completeness and unknown counts

`occurrence_statistics` continues to describe recorded media usage. Both integer
counts remain required when that structure exists; negative/non-integer values,
nonzero rejected-owner counts, and `media_count > total_occurrences` fail. Existing
recorded counts and non-media `source_occurrences` are not rewritten by export.
The original owner schema and scientific source-successor contract are unchanged.

A missing count is not measured zero. An ingredient without complete statistics
may instead have an explicit, reviewed UNKNOWN declaration in the separate
`mappings/occurrence_coverage.yaml` companion. The standalone schema is
`src/mediaingredientmech/schema/occurrence_coverage.yaml`; it does not extend or
weaken IngredientRecord. Without a valid declaration, absent statistics remain
MISSING and the occurrence audit fails. A present but incomplete statistics object
is invalid and cannot be hidden by a declaration.

Each declaration binds the permanent MIM ID, exact current individual YAML bytes,
and the canonical loaded-record content (sorted compact JSON, UTF-8, no ASCII
escaping). The content binding also checks the aggregate reader. UNKNOWN requires
a specific coverage/attribution reason, nonempty evidence, source revision and
hash, scan time, row count, scope, and a global distinct-media denominator when
that denominator is established. Evidence files are relative to and contained
inside the companion's directory, with verified SHA256 values. Changed owner or
evidence bytes require a fresh declaration and review; a filename or label match
does not preserve support. Unknown never overrides existing recorded counts.

The declaration states an occurrence-coverage limitation, not a chemical identity
or mapping decision. Its actual reasoning and source attribution require an
independent review before publication. The validator checks structure and bindings. Numeric observations additionally
require the native structured YAML/Markdown review pair, native provenance and
current input hashes, distinct primary/skeptical reviewers and skeptical
independence, and a supported quantity assessment whose evidence-linked
`occurrence_claim_sha256` dimension binds the exact owner bytes, source revision
and hash, count, unit and scope. The `observation_claim` helper computes that
digest. A supported assessment cannot cancel a concern, unknown outcome or
refuting evidence for that exact claim. Same-owner quantity holds with missing,
malformed or evidence-free claim bindings also block qualification; a valid
binding to a distinct claim preserves unrelated limitations. Native findings
have no claim dimension, so unresolved same-owner quantity findings (including
accepted risk) block until resolved or rejected. These checks do not reinterpret
identity or role decisions. Review references alone are not approval; actual scientific assessment
and normal source/identity gates remain required. UNKNOWN declarations with no
observations do not require an invented numeric review. Existing source/SSSOM reviews and every
SUPPORTED/WITHHOLD gate remain required.

Qualified source observations belong to a separate list, with explicit units,
source scope and bound primary/skeptical evidence. They are never substituted for
complete media counts or global recipe denominators. Non-media prevalence stays
non-media. Pending/withheld/unsupported attribution cannot support owner-attributed
observations. This implementation supplies no campaign declarations or counts:
assemble them only after the relevant final owner bytes and evidence are ready.

Validate a prepared companion without writing records:

```bash
uv run --frozen python -m mediaingredientmech.occurrence_coverage \
  mappings/occurrence_coverage.yaml --ingredients-root data/ingredients
uv run --frozen python scripts/audit_occurrence_stats.py
```

The second command uses the default companion when present and retains all
numeric checks. `audit_occurrence_stats.py --fix` refuses to infer zeros; qualified
count corrections still use the existing guarded counts-only workflow (#486,
#820). An UNKNOWN declaration does not widen that workflow's editable sections.

Standalone flat readers without a companion do not import the LinkML validator.
A present companion always requires the full `linkml` dependency declared in
`pyproject.toml`, including in the flat-coverage CI environment (#1431).
`linkml-runtime` alone is insufficient. A missing validator raises an error;
the reader never discards the companion or treats it as validated UNKNOWN.

Browser, list, index, visualization and role outputs use nullable numeric values
and explicit `occurrence_statistics_state`, `occurrence_statistics_reason`, and
(for UNKNOWN) `occurrence_statistics_provenance`. States are RECORDED, MEMBERSHIP
(the existing known-count membership route), UNKNOWN (verified declaration), and
MISSING (no valid declaration). Partial membership evidence does not promote an
absent/unknown complete count to a number. Numeric source observations remain in
the provenance structure rather than media count columns.

JSON unknowns are null, CSV unknowns are blank, and displays say Unknown. Known
zero remains numeric zero. Index totals are labeled known-count subtotals and
report owners without known counts. Role ranking puts unknowns after known counts;
plot displays use an explicitly described fixed size for unknowns and exclude
them from numeric scales. Currency checks still compare native producer output;
they do not confer scientific approval. Final publication requires both valid
coverage evidence and the ordinary full gates, not producer freshness alone.

Related: #1431, #486, #196, #820. No merge, public release or KG installation is
implied by this contract.

Duplicate YAML keys and aliased evidence files are refused (#1463/#1464).
Companion YAML also refuses anchors, aliases and explicit tags. Owner YAML uses
the native duplicate-checking loader so ordinary shared evidence sequences from
the guarded serializer remain readable, for selected and unselected owners.
Merge keys, explicit tags, recursive aliases and non-string keys remain refused;
this compatibility does not change an owner or its byte/content binding.
Source names within a declaration select exactly one pinned version. Native
review pairs may be copied unchanged under the companion directory at their
canonical `reviews/structured/<review_id>/review.yaml` paths, with both files
bound as evidence. Their `source.inputs` remain actual repository-relative
inputs and are rechecked against the current owner/source bytes.
