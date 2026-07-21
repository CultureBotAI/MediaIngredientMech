# MediaIngredientMech justfile
# Run `just` to see all available commands

set dotenv-load := true

research_dir := "research"
templates_dir := "templates"

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
    /opt/homebrew/bin/python3.13 ../culturebotai-claw/scripts/validate_evidence_references.py

# Fetch missing PubMed abstracts referenced by MIM evidence claims.
# Polite (3 req/s, 10 with NCBI_API_KEY env var).
fetch-pubmed *args:
    /opt/homebrew/bin/python3.13 ../culturebotai-claw/scripts/fetch_pubmed_abstracts.py {{args}}

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

# Vendored-file manifest: the id-label files byte-identical across the Mech repos
# that must not silently diverge. conf/id_label_targets.yaml is deliberately
# per-repo (different adapters/targets/exceptions) so it is NOT here.
VENDORED_IDLABEL_FILES := "scripts/validate_id_label_correspondence.py scripts/chem_formula.py tests/test_id_label_empty_adapter.py tests/test_id_label_unknown_prefix.py tests/test_id_label_plausibility.py"

# Durability guard: fail if any vendored id-label file (the validator + its two
# shared tests) drifts from its pinned sha256 (vendored byte-identical across the
# Mech repos — see the validator's docstring + culturebotai-claw#6). CI runs this
# so an accidental edit to one copy can't silently diverge. Uses sha256sum on CI
# (ubuntu), shasum -a 256 on macOS.
verify-validator-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum -c scripts/.validate_id_label_correspondence.sha256
    else
        shasum -a 256 -c scripts/.validate_id_label_correspondence.sha256
    fi

# Intentional sync only: re-pin the sha256 manifest to the CURRENT contents of the
# vendored files after a deliberate, all-repos byte-identical update. Run this in
# every Mech copy.
refresh-validator-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    : > scripts/.validate_id_label_correspondence.sha256
    for f in {{VENDORED_IDLABEL_FILES}}; do
        if command -v sha256sum >/dev/null 2>&1; then h=$(sha256sum "$f" | cut -d' ' -f1); else h=$(shasum -a 256 "$f" | cut -d' ' -f1); fi
        printf '%s  %s\n' "$h" "$f" >> scripts/.validate_id_label_correspondence.sha256
        echo "re-pinned $f to $h"
    done

# Durability guard for the shared LinkML module (Discussion + Dataset), vendored
# byte-identical across the Mech repos — see culturebotai-claw#7. The pinned
# sha256 is identical in every Mech; fail if this copy drifts.
SHARED_SCHEMA_MODULE := "src/mediaingredientmech/schema/mech_shared.yaml"
verify-schema-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum -c src/mediaingredientmech/schema/.mech_shared.sha256
    else
        shasum -a 256 -c src/mediaingredientmech/schema/.mech_shared.sha256
    fi

# Intentional sync only: re-pin after a deliberate, all-repos byte-identical update.
refresh-schema-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    f={{SHARED_SCHEMA_MODULE}}
    if command -v sha256sum >/dev/null 2>&1; then h=$(sha256sum "$f" | cut -d' ' -f1); else h=$(shasum -a 256 "$f" | cut -d' ' -f1); fi
    printf '%s  %s\n' "$h" "$f" > src/mediaingredientmech/schema/.mech_shared.sha256
    echo "re-pinned $f to $h"

# Composite QC: schema validation + strict closed-schema check +
# evidence reference validation + SSSOM invariants.
# NOTE: id↔label enforcement (Phase 2) is now BLOCKING, but lives in the
# dedicated `label-correspondence` CI workflow (`just validate-products`), not
# here: it loads the OAK sqlite ontologies (CHEBI ~3.7GB etc.) and that workflow
# already caches them, whereas `qc` is meant to stay fast and OAK-free. Run
# `just validate-products` locally to reproduce the gate; `just report-label-drift`
# writes the full drift TSV. Engine A (`just validate-terms-all`) is a local-only
# LinkML cross-check (one validator process per record → too slow for CI).
qc: validate-all validate-strict qc-evidence qc-sssom

# Render per-ingredient HTML detail pages from data/ingredients/*.yaml
# into pages/ingredient/. Idempotent (skips fresh outputs); --force
# regenerates everything. See
# ../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
gen-ingredient-pages *args:
    /opt/homebrew/bin/python3.13 src/mediaingredientmech/render_ingredient_pages.py {{args}}

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
gen-qc-dashboard:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply`
# (and e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP).
knowledge-gap-scan *args:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_kgscan --config conf/kgscan_config.yaml {{args}}

# Build complete documentation site
build-docs: gen-docs export-browser
    @echo "Documentation built in docs/"
    @echo "Open docs/index.html to view locally"

# Export collection files to individual YAML records
export-individual:
    uv run python scripts/export_individual_records.py

# Aggregate individual files back to collections
aggregate-collections:
    uv run python scripts/aggregate_records.py

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

# Full workflow: export, validate, aggregate
sync-individual:
    just export-individual && just validate-individual && just aggregate-collections

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
gen-discussions-data:
    PYTHONPATH=../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
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
