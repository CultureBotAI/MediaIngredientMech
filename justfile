# MediaIngredientMech justfile
# Run `just` to see all available commands

set dotenv-load := true

# Pass recipe arguments to bash as "$@", so quoted arguments keep their quoting.
# Needed by `new-history`, whose --summary/--details are prose; plain `{{args}}`
# interpolation splits them on whitespace. No existing recipe uses $1/$@, so
# enabling this changes nothing else.
set positional-arguments := true

research_dir := "research"
templates_dir := "templates"

# Shared tooling lives in the culturebotai-claw checkout. Override CLAW_SRC when
# claw is not the default sibling directory — CI checks it out elsewhere.
claw_src := env_var_or_default("CLAW_SRC", "../culturebotai-claw/src")
claw_root := parent_directory(claw_src)

# Fail loudly when a shared claw module is missing, rather than running on and
# producing an empty or wrong result. A skip-when-missing variant of this check
# is exactly what let a vendored-sync job pass while verifying nothing
# (CultureMech#112 lane).
_require-claw module:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -d "{{claw_src}}/{{module}}" ]; then
      echo "error: shared module '{{module}}' not found under '{{claw_src}}'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi

# Default recipe - list all commands
default:
    @just --list

# Install package and dependencies
install:
    pip install -e ".[dev]"

# Generate LinkML dataclasses from schema
gen-schema:
    gen-python src/mediaingredientmech/schema/mediaingredientmech.yaml > src/mediaingredientmech/datamodel/mediaingredientmech.py

# Validate schema syntax
validate-schema:
    linkml-validate --schema src/mediaingredientmech/schema/mediaingredientmech.yaml

# Import data from CultureMech
import-data:
    uv run python scripts/import_from_culturemech.py

# Validate all data against schema (both collection and individual files)
validate-all:
    uv run python scripts/validate_all.py --mode both

# Strict closed-schema validation: in-process LinkML validator with
# JsonschemaValidationPlugin(closed=True) so unknown fields are flagged.
# Walks data/ingredients/{mapped,unmapped} and data/curated by default.
# Emits a categorized TSV (reports/instance_validation_failures.tsv) and
# exits non-zero if any ERROR rows were produced.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Inventory YAML-writing scripts under scripts/ and the central curation /
# utils packages. Records whether each writer validates before writing
# and whether it appends a curation_history event. Output:
# reports/pipeline_writers_audit.tsv. Useful for tracking adoption of
# write_validated_ingredient + record_curation_event over time.
audit-writers:
    uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv

# Verify literature snippets in evidence claims appear verbatim in
# cached PubMed abstracts. Anti-hallucination gate. See
# ../culturebotai-claw/.claude/skills/evidence-reference-validation/.
# Exits 2 on SNIPPET_NOT_IN_ABSTRACT (CI blocking).
qc-evidence:
    uv run python {{claw_root}}/scripts/validate_evidence_references.py

# Fetch missing PubMed abstracts referenced by MIM evidence claims.
# Polite (3 req/s, 10 with NCBI_API_KEY env var).
fetch-pubmed *args:
    uv run python {{claw_root}}/scripts/fetch_pubmed_abstracts.py {{args}}

# Validate mappings/ingredient_mappings.sssom.tsv against structural
# invariants (Rule A: auto-classifier token-overlap gate). Rejects are
# written to mappings/needs_curator_review.tsv. Exits 2 on violation
# (CI blocking). See ../culturebotai-claw/.claude/plans/now-focus-on-culturemech-piped-shell.md.
qc-sssom:
    python3 scripts/validate_sssom_invariants.py

schema_path := "src/mediaingredientmech/schema/mediaingredientmech.yaml"

# OBO-resolvable prefixes that linkml-term-validator's `sqlite:obo:` adapter
# can actually download/open. Engine A's --labels passes EVERY ontology_id to
# OAK, so a NON-OBO prefix (cas:, kgmicrobe.compound:, kgmicrobe.ingredient:,
# MICRO: — whose bbop-sqlite .db.gz does not exist / is a 0-byte stub) makes
# OAK attempt a futile S3 download and exit 1, crashing the whole recipe and
# blocking the Phase-2 `qc` promotion regardless of label correctness
# (PR #50 RISK). We pre-filter to these prefixes; everything else is left to
# Engine B (validate-products), which reports it SKIPPED_NO_ADAPTER /
# SKIPPED_EMPTY_ADAPTER instead of downloading. Keep in sync with the OBO
# entries of conf/id_label_targets.yaml `adapters` (MICRO is intentionally
# OMITTED here: sqlite:obo:micro is a 0-byte stub with no remote db).
obo_prefixes := "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"

# id↔label gate (Engine A): verify ontology_label is the CANONICAL OBO label
# for ontology_id in one ingredient file. Fails (exit 1) on any label mismatch.
# The schema binds ontology_mapping/environmental_context so --labels fires.
# Skips (exit 0) a file whose ontology ids use a non-OBO prefix — Engine B
# (validate-products) covers those without triggering an OAK download/crash.
validate-terms FILE:
    #!/usr/bin/env bash
    set -uo pipefail
    if scripts/_engine_a_obo_safe.sh "{{FILE}}" "{{obo_prefixes}}"; then
        uv run linkml-term-validator validate-data "{{FILE}}" -s {{schema_path}} -t IngredientRecord --labels
    else
        echo "  - skipping Engine A (non-OBO prefix; covered by validate-products): {{FILE}}"
    fi

# Same, across every per-ingredient record file. NOTE: data/curated/*.yaml is
# intentionally excluded — those are collection/container docs
# (generation_date/total_count/ingredients:[...] or category/count/ingredients)
# not single IngredientRecords, so `-t IngredientRecord` would fail
# structurally. Engine B (validate-products, recursive walk) covers them.
# Records whose ontology_id uses a non-OBO prefix (cas:/kgmicrobe.compound:/
# MICRO:/…) are SKIPPED here to avoid OAK download crashes — Engine B handles
# them as SKIPPED_NO_ADAPTER/SKIPPED_EMPTY_ADAPTER.
validate-terms-all:
    #!/usr/bin/env bash
    set -uo pipefail
    rc=0
    skipped=0
    for file in data/ingredients/mapped/*.yaml data/ingredients/unmapped/*.yaml; do
        [ -e "$file" ] || continue
        if scripts/_engine_a_obo_safe.sh "$file" "{{obo_prefixes}}"; then
            uv run linkml-term-validator validate-data "$file" -s {{schema_path}} -t IngredientRecord --labels || rc=1
        else
            skipped=$((skipped+1))
        fi
    done
    echo "  - Engine A skipped $skipped file(s) with non-OBO ontology prefixes (covered by validate-products)"
    exit $rc

# id↔label gate (Engine B): verify (id,label) pairs in DATA PRODUCTS
# (SSSOM/CSV/review TSVs) correspond to the ontology. canonical_or_synonym
# for product surface labels. Exits 2 on any mismatch / unknown id.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Baseline (non-failing): write a unified id↔label drift report across YAML
# data + products to reports/label_drift.tsv. Use before enforcing.
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# NOTE: the id↔label validator + its shared tests are vendored byte-identical
# across the Mech repos. The old self-generated sha256 pin (verify-/refresh-
# validator-pin) was retired — it only compared a copy to a hash from the SAME
# repo, so all four could pass while diverged. Drift is now caught by the
# shared-reference check: the `vendored-sync` CI job runs
# scripts/check_vendored_sync.sh, which diffs these files against
# CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>. To propagate a change:
# PR into that hub → merge → bump .vendored_canon_ref here.

# NOTE: the shared LinkML module (mech_shared.yaml) is vendored byte-identical
# across the Mech repos (package-namespaced path per repo). Its self-generated
# sha256 pin (verify-/refresh-schema-pin) was retired — same self-referential
# flaw as the id-label pin. It is now covered by the shared-reference drift check
# (scripts/check_vendored_sync.sh diffs src/*/schema/mech_shared.yaml against the
# hub's copy at CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>) plus the
# hub's nightly vendored-fleet-audit.yml.

# Composite QC: schema validation + strict closed-schema check +
# evidence reference validation + SSSOM invariants.
# NOTE: id↔label enforcement (Phase 2) is now BLOCKING, but lives in the
# dedicated `label-correspondence` CI workflow (`just validate-products`), not
# here: it loads the OAK sqlite ontologies (CHEBI ~3.7GB etc.) and that workflow
# already caches them, whereas `qc` is meant to stay fast and OAK-free. Run
# `just validate-products` locally to reproduce the gate; `just report-label-drift`
# writes the full drift TSV. Engine A (`just validate-terms-all`) is a local-only
# LinkML cross-check (one validator process per record → too slow for CI).
qc: validate-all validate-strict qc-evidence qc-sssom qc-roundtrip

# Assert data/curated/ and data/ingredients/ still describe the same records (CI blocking)
qc-roundtrip:
    #!/usr/bin/env bash
    set -euo pipefail
    # A per-record edit must not be silently reverted by the next
    # `just export-individual`, which projects the collection OVER the per-record
    # tree. Aggregates into a temp dir rather than data/collections/: comparing
    # against that committed artifact is what let this drift for months -- it was
    # last regenerated in March 2026, so the check kept passing while 55 curation
    # events sat unreconciled (#148).
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
    # Aggregate diagnostics are NOT discarded: a per-record file it cannot load
    # names itself here. (It now also exits 1 and writes nothing rather than
    # dropping the record silently -- see #172 -- but the diagnostic is still
    # what tells you WHICH file.)
    uv run python scripts/aggregate_records.py \
        --ingredients-dir data/ingredients --output-dir "$tmp"
    uv run python scripts/verify_roundtrip.py \
        --original-dir data/curated --aggregated-dir "$tmp"
    # The same byte-level assertion the qc-roundtrip workflow makes, so this
    # recipe also catches serialization drift (key order, quoting, line
    # wrapping) that verify_roundtrip cannot see.
    #
    # Exported into a COPY, for two reasons. (1) This is a check; it must not
    # rewrite 2,257 working-tree files as a side effect, or a failure would
    # already have clobbered the very per-record edits the error tells you to
    # save. (2) CI can compare with `git status` because actions/checkout gives
    # it a pristine tree; locally that measures divergence from HEAD, not
    # "did export change anything" — so uncommitted per-record work would fail
    # this check even right after `just sync-curated` made everything agree.
    tree="$(mktemp -d)"
    trap 'rm -rf "$tmp" "$tree"' EXIT
    cp -R data/ingredients/. "$tree/"
    uv run python scripts/export_individual_records.py \
        --input-dir data/curated --output-dir "$tree" >/dev/null
    if ! diff -r -q data/ingredients "$tree"; then
      echo "" >&2
      echo "error: exporting data/curated does not reproduce data/ingredients." >&2
      echo "The per-record tree is not a clean projection of the collection." >&2
      echo "If the per-record files are the ones you meant to keep, run" >&2
      echo "'just sync-curated' to write them back into data/curated/." >&2
      echo "(Nothing was modified — the export above went to a scratch copy.)" >&2
      exit 1
    fi

# Write per-record edits BACK into data/curated/, then re-export to a fixed point
sync-curated:
    #!/usr/bin/env bash
    set -euo pipefail
    # The missing half of the round trip, and the remediation when qc-roundtrip
    # goes red because a script edited data/ingredients/ directly.
    # apply-role-research-results now runs this itself (#171), so this recipe is
    # for hand edits and for any future writer that forgets to.
    #
    # `sync-individual` is NOT this: it runs export FIRST, overwriting the
    # per-record edits with the collection. (`aggregate-collections` was removed
    # in #169 — it wrote data/collections/, which nothing reads.)
    #
    # The re-export is not redundant. The collection does not carry
    # `discussions`, so the exporter re-attaches it at the END of the record,
    # swapping its position with any field edited after kgscan wrote it. Content
    # is identical either way, but the gate compares bytes -- without the
    # re-export a curator who edited one of the discussions-bearing records would
    # run sync-curated, see qc-roundtrip still fail, and have nothing left to try.
    #
    # The diff is proportional to the change: the aggregator emits records in
    # the existing collection's order (see _order_like in
    # scripts/aggregate_records.py). It did NOT always — it used filename order,
    # so an unchanged tree rewrote ~9,500 lines and a one-record change arrived
    # unreviewable. If you ever see a diff that size again, that ordering has
    # regressed; do not wave it through.
    uv run python scripts/aggregate_records.py \
        --ingredients-dir data/ingredients --output-dir data/curated
    uv run python scripts/export_individual_records.py \
        --input-dir data/curated --output-dir data/ingredients

# Render per-ingredient HTML detail pages from data/ingredients/*.yaml
# into pages/ingredient/. Idempotent (skips fresh outputs); --force
# regenerates everything. See
# ../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
gen-ingredient-pages *args:
    uv run python src/mediaingredientmech/render_ingredient_pages.py {{args}}

# Launch interactive curation CLI
curate:
    uv run python scripts/curate_unmapped.py

# Generate curation progress report
report:
    uv run python scripts/generate_report.py

# Generate HTML documentation from schema
gen-docs:
    gen-doc --directory docs src/mediaingredientmech/schema/mediaingredientmech.yaml

# Export ingredients to browser JSON
export-browser:
    uv run python scripts/browser_export.py

# Generate UMAP visualization
generate-umap:
    uv run python scripts/generate_ingredient_umap.py

# QC coverage dashboard (shared kg_microbe_qc generator in culturebotai-claw).
# Reads conf/qc_config.yaml; writes dashboard/index.html + coverage.png.
gen-qc-dashboard: (_require-claw "kg_microbe_qc")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply`
# (and e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP).
knowledge-gap-scan *args: (_require-claw "kg_microbe_kgscan")
    PYTHONPATH={{claw_src}} uv run python -m kg_microbe_kgscan \
      --config conf/kgscan_config.yaml {{args}}

# Build complete documentation site
build-docs: gen-docs export-browser
    @echo "Documentation built in docs/"
    @echo "Open docs/index.html to view locally"

# Export collection files to individual YAML records
export-individual:
    uv run python scripts/export_individual_records.py

# `aggregate-collections` was REMOVED (#169). It ran the aggregator with no
# --output-dir, which defaulted to data/collections/ — a directory nothing in
# this repo reads. So it looked like it kept the collections in sync and did
# not, which is how 55 curation events sat unreconciled (#148). Use
# `just sync-curated` to write per-record edits back into data/curated/, or
# `just qc-roundtrip` to verify the two surfaces agree.

# Validate individual ingredient files only
validate-individual:
    uv run python scripts/validate_all.py --mode individual

# Run FutureHouse Falcon / deep-research-client against an ingredient record
research-ingredient provider status slug *args="":
    uv run --extra dev python scripts/research_ingredient.py \
        --provider {{provider}} \
        --status {{status}} \
        --slug {{slug}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --research-dir {{research_dir}} \
        {{args}}

# List available deep-research-client providers
research-providers:
    uv run --extra dev python scripts/research_ingredient.py --list-providers

# Check availability for one deep-research-client provider
research-provider provider:
    uv run --extra dev python scripts/research_ingredient.py --provider-status {{provider}}

# Edison Scientific deep research (PaperQA3) for one ingredient record.
# target = slug (searched across mapped/ + unmapped/) or YAML path.
# Examples:
#   just research-ingredient-edison yeast_extract
#   just research-ingredient-edison soil --job literature-high
#   just research-ingredient-edison peptone --dry-run
research-ingredient-edison target *args="":
    uv run --extra dev python scripts/research_ingredient_edison.py \
        --target {{target}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --out-dir {{research_dir}}/ingredients \
        {{args}}

# Edison deep research for a batch of ingredients (JSON list of slugs/paths).
research-ingredient-edison-batch batch *args="":
    uv run --extra dev python scripts/research_ingredient_edison.py \
        --batch {{batch}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --out-dir {{research_dir}}/ingredients \
        {{args}}

# Step 7b — Edison deep research for the ROLE facets of one ingredient. Same
# runner as research-ingredient-edison but pinned to the role-research template
# and a separate output directory (research/ingredients/roles/) so identity-
# mapping and role-research runs never clobber each other.
# Examples:
#   just research-ingredient-roles-edison L-cysteine --dry-run
#   just research-ingredient-roles-edison Glucose --job literature-high
research-ingredient-roles-edison target *args="":
    uv run --extra dev python scripts/research_ingredient_roles_edison.py \
        --target {{target}} \
        {{args}}

# Step 7b — Edison role research for a batch of ingredients. Typically driven
# by the CultureMech prioritizer output (`prioritize_role_research_candidates.py`).
research-ingredient-roles-edison-batch batch *args="":
    uv run --extra dev python scripts/research_ingredient_roles_edison.py \
        --batch {{batch}} \
        {{args}}

# Retroactively backfill Edison provenance sidecars (no re-billing).
enrich-edison-response *args="":
    uv run --extra dev python scripts/enrich_edison_response.py {{args}}

# Step 7b — Apply role research results extracted from Edison output.
# Writes the per-record files AND syncs them back into data/curated/, so the two
# surfaces stay consistent and the next export cannot revert the roles (#171).
# Input: JSON batch emitted by CultureMech's `extract_roles_from_edison.py`.
# Writes rich RoleAssignments (with per-role confidence + evidence citations)
# to `data/ingredients/**/*.yaml`. Per-facet never-overwrite guard.
# Examples:
#   just apply-role-research-results reports/edison_role_extraction.json --dry-run
#   just apply-role-research-results reports/edison_role_extraction.json
apply-role-research-results batch *args="":
    uv run python scripts/apply_role_research_results.py {{batch}} {{args}}

# Project data/curated/ onto the per-record tree, validate, and verify they agree
sync-individual:
    # Treats the COLLECTION as the source of truth, so it OVERWRITES anything
    # edited directly under data/ingredients/. `just sync-curated` is the
    # opposite direction and is what you want after a script edited per-record
    # files.
    just export-individual && just validate-individual && just qc-roundtrip

# Create snapshot of current data
snapshot:
    @timestamp=$(date +%Y%m%d_%H%M%S) && \
    mkdir -p data/snapshots/$$timestamp && \
    cp data/curated/*.yaml data/snapshots/$$timestamp/ && \
    echo "Snapshot created: data/snapshots/$$timestamp"

# Run tests
test:
    pytest tests/

# Run tests with coverage report
test-cov:
    pytest tests/ --cov=mediaingredientmech --cov-report=term-missing --cov-report=html

# Format code with black
format:
    black src/ tests/ scripts/

# Lint code with ruff
lint:
    ruff check src/ tests/ scripts/

# Type check with mypy
typecheck:
    mypy src/

# Run all quality checks
check: lint typecheck test

# Clean generated files
clean:
    rm -rf build/ dist/ *.egg-info htmlcov/ .pytest_cache/ .coverage
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Discussions / knowledge-gap browser (shared kg_microbe_discussions in claw).
gen-discussions-data: (_require-claw "kg_microbe_discussions")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions

# =============================================================================
# CURIE standard (docs/CURIE_STANDARD.md, issue #119)
# =============================================================================

# Regenerate the rename alias map from git history. Run after any record rename.
[group('QC')]
curie-aliases:
    uv run python scripts/build_curie_alias_map.py

# Normalise / resolve CURIEs on the command line.
#   just curie-check MIM:Tryptone CHEBI:15377
curie-check *CURIES:
    uv run python -m mediaingredientmech.curie --equivalent {{CURIES}}

# Re-verify every MICRO id used by the SSSOM against OLS4 (catches MicrO's
# malformed-IRI classes, which cannot be detected offline).
[group('QC')]
curie-verify-micro:
    uv run python scripts/verify_micro_ids.py

# Assert the published SSSOM satisfies the CURIE standard.
[group('QC')]
curie-validate:
    uv run python -m pytest tests/test_curie_normalizer.py -q --no-cov

# =============================================================================
# Curation history (append-only provenance)
# =============================================================================
# Records which model, using which tool, changed what, why, and under which
# issue. One file per session per target under history/; never edited after
# write. See history/README.md. The schema is vendored at
# src/mediaingredientmech/schema/history.yaml; the scaffolder lives in claw.

# Scaffold a history record. Prints the path as its last stdout line.
#   just new-history --kind record --slug Tryptone \
#     --target-root data/ingredients/mapped --event EDIT --outcome changed \
#     --summary "..." --details "..." --model <model-id>
new-history *args:
    #!/usr/bin/env bash
    set -euo pipefail
    claw_src="${CLAW_SRC:-../culturebotai-claw/src}"
    if [ ! -d "$claw_src/kg_microbe_history" ]; then
      echo "new-history: kg_microbe_history not found under '$claw_src'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi
    # "$@" not {{args}} — see `set positional-arguments` at the top of this file.
    # `uv run python`, not `python3`: bare python3 is whatever the machine puts
    # first on PATH, which need not be the project venv.
    PYTHONPATH="$claw_src" uv run python -m kg_microbe_history new "$@"

# Validate one history record, or a directory of them. Uses the VENDORED schema,
# so this works with no claw checkout — same as CI.
validate-history target="history":
    #!/usr/bin/env bash
    set -euo pipefail
    target="{{target}}"
    if [ -z "$target" ]; then
      echo "validate-history: empty target. Pass a record path or a directory." >&2
      exit 2
    fi
    if [ ! -e "$target" ]; then
      echo "validate-history: '$target' does not exist." >&2
      exit 2
    fi
    if [ -d "$target" ]; then
      if [ -z "$(find "$target" -name '*.yaml' -print -quit)" ]; then
        echo "No history records under '$target'."
        exit 0
      fi
      find "$target" -name '*.yaml' -print0 \
        | xargs -0 uv run linkml-validate \
            --schema src/mediaingredientmech/schema/history.yaml \
            --target-class HistoryRecord
    else
      uv run linkml-validate \
        --schema src/mediaingredientmech/schema/history.yaml \
        --target-class HistoryRecord "$target"
    fi
