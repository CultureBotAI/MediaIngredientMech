#!/usr/bin/env python3
"""Diff each ingredient record against its Edison deep-research report.

The sweep exists to *validate* records, not merely to accumulate reports. This
script is the reading end: for every record that has a research bundle, it
extracts what the report actually concluded and compares it with what the record
asserts, emitting a graded discrepancy ledger.

It deliberately does **not** rewrite `ontology_mapping`. #203/#263 are what
happens when a plausible identifier is promoted by a mechanism that never decided
anything, and a report's own recommendations are conservative by design. Every
finding here carries the quoted report line that produced it so a curator can
judge it in one read.

Finding classes, most severe first:

  P1 STATUS_CONFLICT    record is MAPPED; the report recommends UNMAPPED
  P1 CURIE_REFUTED      the report names the record's own CURIE in a "do not map"
                        / "not equivalent" / "broader parent" context
  P1 VERDICT_REFUTES    the report's per-field verdict table marks a populated
                        field REFUTED (template section 0)
  P2 CURIE_ABSENT       the record's CURIE appears nowhere in the report, and the
                        report proposes different ones
  P2 QUALITY_CONFLICT   record says EXACT_MATCH; the report says close/narrow/broad
  P2 CAS_CONFLICT       recorded CAS-RN differs from every CAS-RN in the report
  P3 CAS_AVAILABLE      report supplies a CAS-RN the record lacks (enrichment)
  P4 CONFIRMED          the report endorses what the record says

Usage:
    python scripts/validate_records_against_research.py
    python scripts/validate_records_against_research.py --min-priority P2
    python scripts/validate_records_against_research.py --slug Isophthalate --verbose
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"
RESEARCH = ROOT / "research" / "ingredients"
RESEARCH_CLAUDE = ROOT / "research" / "ingredients-claude"
STATUSES = ("mapped", "unmapped")
DEFAULT_OUT = ROOT / "mappings" / "record_research_validation"

# Prefix matching is case-insensitive for the long, unmistakable prefixes -- the
# corpus writes `mesh:C041783`, `MeSH:D007633` and `MESH:D007633` for the same
# thing. The short ones (GO, PO, CL) stay case-sensitive: lowercased they are
# ordinary English words and `go:1` in prose is not a term reference.
# MeSH locals carry a letter (`C041783`, `D012313`), so the local part allows one.
CURIE_RE = re.compile(
    r"\b(?:(?i:CHEBI|FOODON|NCIT|MESH|ENVO|UBERON|NCBITaxon|BTO|OBI)|GO|PO|CL)"
    r"[:_]([A-Za-z]?\d+)\b")
CURIE_PARTS_RE = re.compile(
    r"\b((?i:CHEBI|FOODON|NCIT|MESH|ENVO|UBERON|NCBITaxon|BTO|OBI)|GO|PO|CL)"
    r"[:_]([A-Za-z]?\d+)\b")
CAS_RE = re.compile(r"\b(\d{2,7}-\d{2}-\d)\b")

# An `ontology_id` in one of these namespaces is a claim about an external
# ontology, and a report that says "no ontology term fits" contradicts it.
ONTOLOGY_PREFIXES = {"chebi", "foodon", "ncit", "mesh", "envo", "uberon",
                     "ncbitaxon", "bto", "obi", "go", "po", "cl", "micro"}
# These are not ontology claims. `kgmicrobe.compound:*` is MIM's deliberate
# FALLBACK_REGISTRY shape for "searched every ontology, none denotes this", and
# `cas:*` is a substance-identity anchor. A report concluding "no ontology term
# fits" *agrees with* such a record rather than contradicting it -- flagging
# those P1 would bury the real conflicts under the convention working correctly.
REGISTRY_PREFIXES = {"kgmicrobe.compound", "kgmicrobe.ingredient", "cas"}

# The report's recommended mapping status. Reports do not use one shape, and the
# shapes are not interchangeable in reliability, so they are tried in order of
# how directly each states a verdict rather than merged into one alternation.
# The one that fired is recorded, so a noisy strategy can be identified from the
# ledger instead of guessed at.
#
# The motivating miss: `## Curation recommendation` followed by
# `**Status: retain \`UNMAPPED\`.**` -- the heading matches "recommend" but the
# verdict token is on a *later* line, so any same-line pattern returns nothing.
STATUS_TOKEN_RE = re.compile(r"\b(MAPPED|UNMAPPED|PENDING_REVIEW)\b")
YAML_STATUS_RE = re.compile(r"^\s*mapping_status:\s*[`'\"]?(\w+)", re.M)
STATUS_LINE_RE = re.compile(
    r"^\s*[-*]?\s*\**(?:Recommended |Curation |Final )?[Ss]tatus\**\s*[:\-][^\n]*", re.M)
RECOMMEND_INLINE_RE = re.compile(
    r"(?:\*\*Recommend(?:ation|ed)?[^*\n]*\*\*|"
    r"\|\s*Recommend(?:ation|ed)?[^|\n]*\||"
    r"^\s*[-*]\s*\*\*Recommend[^\n]*)[^\n]*",
    re.I | re.M)
RECOMMEND_HEADING_RE = re.compile(
    r"^#{2,4}\s*[^\n]*Recommend[^\n]*$", re.I | re.M)

OVERALL_RE = re.compile(r"^\s*[`*_> ]*Overall verdict[`*_ ]*[:\-][`*_ ]*(\w+)", re.I | re.M)

# Language that turns a mention of a CURIE into a refusal of it. Matched against
# the single line the CURIE sits on (a table row or a paragraph line), which is
# the unit reports actually reason in.
REFUTE_MARKERS = (
    "do not map", "do not assert", "should not be mapped", "should not be used",
    "not equivalent", "not an exact", "not identity", "not the same",
    "unsuitable", "avoid mapping", "incorrect", "must not", "reject",
    "would lose", "is wrong", "does not denote", "obsolete", "deprecated",
)
# A recorded EXACT_MATCH that the report downgrades.
NONEXACT_MARKERS = ("closematch", "close match", "narrowmatch", "narrow match",
                    "broadmatch", "broad match", "broader parent", "broader term")

PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}


# --------------------------------------------------------------------------- #
# Report parsing
# --------------------------------------------------------------------------- #

def split_answer(md_path: Path, meta_path: Path) -> str:
    """Return the report body with the echoed prompt removed.

    The `.md` is ``"Question: " + <rendered query> + "\\n\\n" + <answer>``. The
    meta yaml stores that exact query, so stripping it is exact rather than a
    guess at where the prompt ends -- and the prompt contains the record's own
    field values, which would otherwise be mistaken for report claims (every
    record would "confirm" its own CURIE).
    """
    text = md_path.read_text(encoding="utf-8", errors="replace")
    try:
        query = yaml.safe_load(meta_path.read_text(encoding="utf-8", errors="replace")).get("query")
    except Exception:
        query = None
    if query:
        idx = text.find(query)
        if idx != -1:
            return text[idx + len(query):].lstrip()
    # Fall back to the last echoed-template landmark. Better to drop a little
    # answer text than to keep the prompt and validate the record against itself.
    marker = "- Warnings for claims that should not yet be curated into MediaIngredientMech."
    idx = text.rfind(marker)
    return text[idx + len(marker):].lstrip() if idx != -1 else text


CANONICAL_PREFIX = {"chebi": "CHEBI", "foodon": "FOODON", "ncit": "NCIT", "mesh": "MESH",
                    "envo": "ENVO", "uberon": "UBERON", "ncbitaxon": "NCBITaxon",
                    "bto": "BTO", "obi": "OBI", "go": "GO", "po": "PO", "cl": "CL",
                    "micro": "MICRO"}


def norm_curie(prefix: str, local: str) -> str:
    """Fold prefix casing so `mesh:D007633` and `MeSH:D007633` compare equal."""
    return f"{CANONICAL_PREFIX.get(prefix.lower(), prefix)}:{local}"


def split_identifier(identifier: str | None) -> tuple[str, str]:
    """Return (lowercased prefix, canonical CURIE) for a record identifier."""
    if not identifier or ":" not in identifier:
        return "", identifier or ""
    prefix, local = identifier.split(":", 1)
    return prefix.lower(), norm_curie(prefix, local)


def parse_report(body: str) -> dict:
    curies: dict[str, list[str]] = {}
    cas: dict[str, list[str]] = {}
    for line in body.splitlines():
        for m in CURIE_PARTS_RE.finditer(line):
            curies.setdefault(norm_curie(m.group(1), m.group(2)), []).append(line.strip())
        for m in CAS_RE.finditer(line):
            cas.setdefault(m.group(1), []).append(line.strip())

    recommended, rec_source, rec_line = recommended_status(body)

    overall = None
    m = OVERALL_RE.search(body)
    if m:
        overall = m.group(1).upper()

    return {
        "curies": curies,
        "cas": sorted(cas),
        "cas_lines": cas,
        "recommended_status": recommended,
        "recommended_source": rec_source,
        "recommended_line": rec_line,
        "overall_verdict": overall,
        "refuted_fields": parse_verdict_table(body),
    }


def recommended_status(body: str) -> tuple[str | None, str, str]:
    """Return (status, which-strategy-fired, the quoted line).

    Ordered most-explicit first. Each strategy returns the *line* it read the
    token from so the ledger can show a curator exactly what was interpreted --
    a status conflict nobody can trace back to a sentence is not actionable.
    """
    # 1. The `Recommended YAML-oriented updates` fence: the report writing the
    #    field it wants set is as unambiguous as this gets.
    for m in YAML_STATUS_RE.finditer(body):
        tok = STATUS_TOKEN_RE.search(m.group(1).upper())
        if tok:
            return tok.group(1), "yaml-fence", m.group(0).strip()

    # 2. A `Status:` / `Recommended status:` line.
    for m in STATUS_LINE_RE.finditer(body):
        tok = STATUS_TOKEN_RE.search(m.group(0))
        if tok:
            return tok.group(1), "status-line", m.group(0).strip()

    # 3. A bolded/table `Recommend...` run carrying the token inline.
    for m in RECOMMEND_INLINE_RE.finditer(body):
        tok = STATUS_TOKEN_RE.search(m.group(0))
        if tok:
            return tok.group(1), "recommend-inline", m.group(0).strip()

    # 4. A `## ...Recommend...` heading with the token somewhere in its section.
    #    Weakest, because the section may discuss the alternative it rejects --
    #    so it reads only the first token and reports the line it came from.
    for m in RECOMMEND_HEADING_RE.finditer(body):
        section = body[m.end(): m.end() + 1200].split("\n## ")[0]
        tok = STATUS_TOKEN_RE.search(section)
        if tok:
            line = next((ln for ln in section.splitlines()
                         if STATUS_TOKEN_RE.search(ln)), "").strip()
            return tok.group(1), "recommend-heading", line
    return None, "", ""


def parse_claude_report(md_path: Path) -> dict:
    """Parse a Claude-lane report into the same shape as an Edison one.

    No prompt-stripping here: the Claude lane writes only its answer, so unlike
    the Edison `.md` there is no echoed template to mistake for report claims.

    The two lanes answer different questions, so `recommended_status` is derived
    rather than read. The Claude template asks for `Overall verdict:` plus a
    per-field table; a `mapping_status` row marked REFUTES is the closest thing
    it produces to "this record's status is wrong".
    """
    body = md_path.read_text(encoding="utf-8", errors="replace")
    report = parse_report(body)
    if not report["recommended_status"]:
        for field, _was, corrected in report["refuted_fields"]:
            if "mapping_status" in field.lower() or "mapping status" in field.lower():
                tok = STATUS_TOKEN_RE.search(corrected.upper())
                if tok:
                    report["recommended_status"] = tok.group(1)
                    report["recommended_source"] = "claude-verdict-table"
                    report["recommended_line"] = f"{field}: {corrected}"
                break
    return report


EMPTY_RECORDED = {"", "-", "—", "none", "none recorded", "n/a", "na", "null", "not recorded"}

# Fields where a refutation means the record is *wrong*. Everything else
# (chemical_properties, synonyms, ingredient_type, occurrence counts) is a
# completeness gap, which matters much less and should not outrank a bad mapping.
IDENTITY_FIELDS = ("ontology", "mapping_status", "mapping status", "identifier",
                   "curie", "mapping_quality", "mapping quality")


def parse_verdict_table(body: str) -> list[tuple[str, str, str]]:
    """Rows of the section-0 verdict table that read REFUTES/REFUTED.

    Returns (field, recorded, corrected). The `recorded` cell is what separates
    a genuine refutation from a gap: a row refuting `chemical_properties` whose
    recorded value is "None recorded" is not saying the record is wrong, it is
    saying the record is empty. Collapsing those into one severity buried the
    real mapping defects under enrichment noise.

    Only present in reports produced after the template gained section 0; older
    bundles simply yield nothing, which is why the other checks do not depend on
    it.
    """
    out = []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip().strip("*`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if re.fullmatch(r"REFUTE[SD]?", cells[1], re.I):
            recorded = cells[2] if len(cells) > 2 else ""
            corrected = " | ".join(cells[3:]) if len(cells) > 3 else ""
            out.append((cells[0], recorded, corrected))
    return out


# --------------------------------------------------------------------------- #
# Record reading
# --------------------------------------------------------------------------- #

CONVENTION_MARKERS = ("bare anion", "bare-name", "fallback_registry", "#213")


def record_facts(rec: dict) -> dict:
    om = rec.get("ontology_mapping") or {}
    props = rec.get("chemical_properties") or {}
    cas = props.get("cas_number") or props.get("cas_rn") or props.get("cas")
    history = rec.get("curation_history") or []

    # Who last moved this record into MAPPED, and did anyone write down why?
    # A conflict traceable to a named mechanical sweep is triaged very
    # differently from one a curator reasoned through and documented -- the
    # first is a batch to re-examine, the second is a decision already made.
    promoted_by = ""
    for event in reversed(history):
        if str(event.get("new_status", "")) == "MAPPED" or "PROMOTED" in str(event.get("action", "")):
            promoted_by = str(event.get("curator", "") or event.get("action", ""))
            break
    rationale = " ".join(str(e.get("notes", "")) for e in (om.get("evidence") or []))
    documented = any(mk in rationale.lower() for mk in CONVENTION_MARKERS)

    return {
        "promoted_by": promoted_by,
        "documented_rationale": documented,
        "identifier": rec.get("identifier"),
        "preferred_term": rec.get("preferred_term"),
        "mapping_status": rec.get("mapping_status"),
        "ontology_id": om.get("ontology_id"),
        "ontology_label": om.get("ontology_label"),
        "mapping_quality": om.get("mapping_quality"),
        "cas": str(cas) if cas else None,
        "formula": props.get("formula"),
    }


# --------------------------------------------------------------------------- #
# Comparison
# --------------------------------------------------------------------------- #

def compare(status: str, slug: str, facts: dict, report: dict, lane: str = "edison") -> list[dict]:
    findings: list[dict] = []

    def add(priority, kind, detail, evidence=""):
        findings.append({
            "priority": priority, "kind": kind, "lane": lane,
            "status_dir": status, "slug": slug,
            "identifier": facts["identifier"] or "", "preferred_term": facts["preferred_term"] or "",
            "recorded": _recorded_for(kind, facts),
            "mapping_quality": facts["mapping_quality"] or "",
            "promoted_by": facts["promoted_by"],
            "documented_rationale": "yes" if facts["documented_rationale"] else "no",
            "detail": detail, "evidence": _clip(evidence),
        })

    # Whether the record claims *ontology identity* is decided by the primary
    # `identifier`, not by `ontology_mapping.ontology_id`. A cas-primary record
    # carrying a `NARROW_MATCH` to a CHEBI parent (the documented pattern for
    # "CHEBI has no term for this salt") would otherwise be read as asserting
    # that CHEBI term as its identity, and flagged P1 for a claim it never made.
    prefix, _ = split_identifier(facts["identifier"])
    term_prefix, rec_curie = split_identifier(facts["ontology_id"])
    mapped = (facts["mapping_status"] == "MAPPED")
    ontology_claim = prefix in ONTOLOGY_PREFIXES
    # Whether a *specific term* can be checked against the report is a separate
    # question from whether the record claims ontology identity. A cas-primary
    # record still carries a CHEBI term, and a report refuting that term is
    # worth knowing about even though the record never claimed it as identity.
    has_term = term_prefix in ONTOLOGY_PREFIXES

    # The report's recommended status contradicts the record's. How much that
    # matters depends on what the record is claiming: asserting a CHEBI term
    # over "no ontology term fits" is a real conflict, whereas a
    # kgmicrobe.compound / cas record *is* the repo's way of recording exactly
    # that conclusion.
    rs = report["recommended_status"]
    src = report["recommended_source"]
    if mapped and rs == "UNMAPPED":
        if ontology_claim:
            add("P1", "STATUS_CONFLICT",
                f"record asserts ontology term {rec_curie}; report recommends UNMAPPED (via {src})",
                report["recommended_line"])
        elif prefix in REGISTRY_PREFIXES:
            add("P3", "REGISTRY_FALLBACK_AGREES",
                f"report recommends UNMAPPED; record is {prefix}-primary, which already "
                f"encodes 'no ontology term denotes this' (via {src})",
                report["recommended_line"])
        else:
            add("P2", "STATUS_CONFLICT",
                f"record is MAPPED via unrecognised prefix '{prefix}'; report "
                f"recommends UNMAPPED (via {src})",
                report["recommended_line"])
    elif not mapped and rs == "MAPPED":
        add("P2", "STATUS_CONFLICT",
            f"record is UNMAPPED; report recommends MAPPED (via {src})",
            report["recommended_line"])

    # P1 -- the report names this very CURIE and argues against it.
    if has_term:
        lines = report["curies"].get(rec_curie, [])
        refuting = [ln for ln in lines if any(mk in ln.lower() for mk in REFUTE_MARKERS)]
        if refuting:
            add("P1", "CURIE_REFUTED",
                f"report argues against {rec_curie}", refuting[0])
        elif not lines and report["curies"]:
            add("P2", "CURIE_ABSENT",
                f"{rec_curie} never appears in the report; it proposes "
                + ", ".join(sorted(report["curies"])[:5]),
                "")
        elif lines:
            # Only claim confirmation when the report also endorsed the status.
            if not any(f["kind"] == "STATUS_CONFLICT" for f in findings):
                add("P4", "CONFIRMED", f"report cites {rec_curie}", lines[0])

        # P2 -- recorded as exact, described as something weaker.
        if facts["mapping_quality"] == "EXACT_MATCH":
            weak = [ln for ln in lines if any(mk in ln.lower() for mk in NONEXACT_MARKERS)]
            if weak:
                add("P2", "QUALITY_CONFLICT",
                    "recorded EXACT_MATCH; report describes a non-exact relation", weak[0])

    # Explicit per-field refutations from the section-0 verdict table.
    for field, was, corrected in report["refuted_fields"]:
        gap = was.strip().strip("*`").lower() in EMPTY_RECORDED
        identity = any(k in field.lower() for k in IDENTITY_FIELDS)
        if gap:
            add("P3", "FIELD_MISSING",
                f"'{field}' is unset; report supplies a value", corrected)
        elif identity:
            add("P1", "VERDICT_REFUTES",
                f"report refutes identity field '{field}' (recorded: {was})", corrected)
        else:
            add("P2", "VERDICT_REFUTES",
                f"report refutes field '{field}' (recorded: {was})", corrected)

    # CAS. Never auto-applied: a CAS number a report found next to this compound
    # belongs to the neighbouring hydrate or the anhydrous parent often enough
    # that the quoted sentence -- which form it assigns the number to -- is the
    # whole finding. A bare number here would be wrong roughly half the time.
    if report["cas"]:
        if facts["cas"] and facts["cas"] not in report["cas"]:
            add("P2", "CAS_CONFLICT",
                f"recorded {facts['cas']}; report cites " + ", ".join(report["cas"][:4]),
                report["cas_lines"][report["cas"][0]][0])
        elif not facts["cas"] and len(report["cas"]) == 1:
            only = report["cas"][0]
            add("P3", "CAS_AVAILABLE",
                f"report supplies CAS {only}; record has none — confirm the quoted "
                "sentence assigns it to this exact form",
                report["cas_lines"][only][0])

    return findings


def cross_lane(status: str, slug: str, facts: dict,
               edison: dict | None, claude: dict | None) -> list[dict]:
    """Findings that only exist because two independent lanes disagree.

    This is the payoff of running both. The lanes have different blind spots:
    PaperQA3 reads literature but cannot open an ontology page, so it defaults to
    "retain UNMAPPED" whenever it cannot verify a CURIE — which is most of the
    time. The Claude lane resolves the CURIE directly but does not mine primary
    literature. So "Edison says UNMAPPED, Claude resolved the term and confirms
    it" is not a real conflict: it is Edison's known blind spot, and it *clears*
    a P1 rather than adding one. Recording that explicitly is what stops a
    curator re-litigating 50 records the second lane already settled.
    """
    if not edison or not claude:
        return []

    def finding(priority, kind, detail, evidence=""):
        return {"priority": priority, "kind": kind, "lane": "cross",
                "status_dir": status, "slug": slug,
                "identifier": facts["identifier"] or "",
                "preferred_term": facts["preferred_term"] or "",
                "recorded": facts["ontology_id"] or "",
                "mapping_quality": facts["mapping_quality"] or "",
                "promoted_by": facts["promoted_by"],
                "documented_rationale": "yes" if facts["documented_rationale"] else "no",
                "detail": detail, "evidence": _clip(evidence)}

    out = []
    e_status = edison["recommended_status"]
    c_overall = claude["overall_verdict"]
    mapped = facts["mapping_status"] == "MAPPED"

    if mapped and e_status == "UNMAPPED" and c_overall == "CONFIRMED":
        out.append(finding(
            "P3", "LANE_DISAGREEMENT_RESOLVED",
            "Edison recommended UNMAPPED (it could not verify the CURIE); the Claude lane "
            "resolved the term and confirms the record. Treat the Edison P1 as cleared.",
            claude["recommended_line"] or ""))
    elif mapped and e_status == "UNMAPPED" and c_overall == "NEEDS_CORRECTION":
        out.append(finding(
            "P1", "BOTH_LANES_DISPUTE",
            "Both lanes dispute this mapping — Edison recommends UNMAPPED and the Claude "
            "lane marks the record NEEDS_CORRECTION. Strongest signal in the ledger.",
            claude["recommended_line"] or ""))
    elif c_overall == "NEEDS_CORRECTION" and e_status == "MAPPED":
        out.append(finding(
            "P2", "LANE_CONFLICT",
            "Lanes disagree in the opposite direction: Edison endorses a mapping the Claude "
            "lane says needs correction. Read both before acting.",
            claude["recommended_line"] or ""))

    # A CURIE proposed by one lane and contradicted by the other is worth seeing
    # even when the overall verdicts happen to line up.
    e_terms, c_terms = set(edison["curies"]), set(claude["curies"])
    only_claude = c_terms - e_terms
    if facts["ontology_id"] and facts["ontology_id"] not in c_terms and only_claude:
        out.append(finding(
            "P2", "CLAUDE_PROPOSES_OTHER",
            "The Claude lane resolved terms but not the recorded one; it proposes "
            + ", ".join(sorted(only_claude)[:5]), ""))
    return out


def _recorded_for(kind: str, facts: dict) -> str:
    if kind in ("STATUS_CONFLICT",):
        return facts["mapping_status"] or ""
    if kind in ("CAS_CONFLICT", "CAS_AVAILABLE"):
        return facts["cas"] or ""
    if kind == "QUALITY_CONFLICT":
        return facts["mapping_quality"] or ""
    return facts["ontology_id"] or ""


def _clip(text: str, width: int = 300) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= width else text[: width - 1] + "…"


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #

def index_bundles(research_dir: Path, job_short: str = "literature") -> dict[str, Path]:
    suffix = f"-edison-{job_short}-meta.yaml"
    return {p.name[: -len(suffix)].lower(): p for p in research_dir.glob(f"*{suffix}")}


KIND_NOTES = {
    "STATUS_CONFLICT": "The record asserts a mapping its own research report advised against. "
                       "Check `promoted_by`: a conflict produced by a mechanical sweep with no "
                       "`documented_rationale` is the #203/#263 pattern and should be re-decided.",
    "CURIE_REFUTED": "The report names this exact CURIE and argues against using it. Read the "
                     "quoted line — it usually names the correct term or says why none fits.",
    "VERDICT_REFUTES": "The report's per-field verdict table marks a populated field REFUTED and "
                       "supplies a corrected value.",
    "CURIE_ABSENT": "The report proposes CURIEs but never mentions the record's. Weaker than a "
                    "refutation — the report may simply not have restated it.",
    "QUALITY_CONFLICT": "Recorded EXACT_MATCH where the report describes a close/narrow/broad "
                        "relation. Downgrading the quality may be enough; the CURIE can stand.",
    "CAS_CONFLICT": "Recorded CAS-RN is not among those the report found.",
    "CAS_AVAILABLE": "Enrichment opportunity. Confirm from the quoted sentence that the number is "
                     "assigned to *this* hydrate/salt before recording it.",
    "REGISTRY_FALLBACK_AGREES": "Not a defect. The report found no ontology term and the record "
                                "already says so via the registry fallback. Listed for completeness.",
    "CONFIRMED": "The report cites the record's CURIE and did not contradict its status.",
    "BOTH_LANES_DISPUTE": "Both independent lanes dispute this mapping. The strongest signal "
                          "in the ledger — start here.",
    "LANE_CONFLICT": "The lanes disagree about this record. Read both reports before acting.",
    "LANE_DISAGREEMENT_RESOLVED": "Not a defect. Edison could not verify the CURIE and defaulted "
                                  "to UNMAPPED; the Claude lane resolved it and confirms the "
                                  "record. Clears the corresponding Edison P1.",
    "CLAUDE_PROPOSES_OTHER": "The Claude lane resolved ontology terms but not the recorded one.",
    "FIELD_MISSING": "Completeness gap, not a defect: the field is unset and a lane supplied a "
                     "value. Verify against the quoted source before recording it.",
}


def write_summary(path: Path, findings: list[dict], kept: list[dict],
                  seen: int, skipped: int, min_priority: str,
                  lane_counts: dict[str, int] | None = None) -> None:
    """Write the curator-facing triage view of the ledger."""
    # Group by (priority, kind), not kind alone: STATUS_CONFLICT is raised at
    # both P1 and P2, and collapsing them reported every one at P1.
    by_kind: dict[tuple[str, str], list[dict]] = {}
    for f in findings:
        by_kind.setdefault((f["priority"], f["kind"]), []).append(f)

    lines = [
        "# Record-vs-research validation ledger",
        "",
        "Generated by `scripts/validate_records_against_research.py`. Each finding compares an "
        "ingredient record against the Edison deep-research report for that same ingredient.",
        "",
        "**Nothing here has been applied.** A report's recommendation is evidence for a curator, "
        "not an instruction — auto-applying them is how #203/#263 happened. Every row carries the "
        "quoted report line that produced it so a call can be made in one read.",
        "",
        f"- records with a usable research bundle: **{seen}**",
        f"- records with no bundle yet (not evaluated): **{skipped}**",
        f"- findings written to the TSV (>= {min_priority}): **{len(kept)}**",
        "",
    ]
    if lane_counts:
        lines += [
            f"Lane coverage — Edison only: **{lane_counts.get('edison', 0)}**, "
            f"Claude only: **{lane_counts.get('claude', 0)}**, "
            f"both lanes: **{lane_counts.get('both', 0)}**. Only records covered by both "
            "can produce a cross-lane finding.",
            "",
        ]
    lines += [
        "| priority | kind | count | what it means |",
        "|---|---|---|---|",
    ]
    for (priority, kind), group in sorted(
            by_kind.items(), key=lambda kv: (PRIORITY_ORDER[kv[0][0]], -len(kv[1]))):
        lines.append(f"| {priority} | `{kind}` | {len(group)} | {KIND_NOTES.get(kind, '')} |")

    # The most actionable cut: the record makes a *strong* identity claim on an
    # ontology term its own report advised against. EXACT_MATCH and
    # SYNONYM_MATCH assert "this ingredient is that term"; CLOSE/NARROW/BROAD
    # already say the fit is imperfect, so a conservative report disagreeing
    # with one of those is a much weaker signal.
    strong = [f for f in findings
              if f["kind"] == "STATUS_CONFLICT" and f["priority"] == "P1"
              and f["mapping_quality"] in ("EXACT_MATCH", "SYNONYM_MATCH")]
    if strong:
        lines += ["", f"## Priority queue — {len(strong)} strong claims contradicted by their report",
                  "",
                  "Each asserts `EXACT_MATCH`/`SYNONYM_MATCH` to an ontology term whose own "
                  "research report recommended UNMAPPED. Re-decide each: keep with a written "
                  "justification, downgrade the mapping quality, or demote.", "",
                  "| slug | identifier | quality | promoted by | rationale recorded |",
                  "|---|---|---|---|---|"]
        for f in sorted(strong, key=lambda f: f["slug"]):
            lines.append(f"| `{f['slug']}` | `{f['identifier']}` | {f['mapping_quality']} | "
                         f"{f['promoted_by']} | {f['documented_rationale']} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--research-dir", type=Path, default=RESEARCH,
                    help="Edison/PaperQA3 lane bundles.")
    ap.add_argument("--claude-dir", type=Path, default=RESEARCH_CLAUDE,
                    help="Claude lane reports.")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT,
                    help="Output path stem; writes <out>.tsv and <out>.json.")
    ap.add_argument("--slug", help="Validate a single record (debugging).")
    ap.add_argument("--min-priority", choices=("P1", "P2", "P3", "P4"), default="P3",
                    help="Drop findings below this priority from the TSV. Default P3.")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    bundles = index_bundles(args.research_dir)
    findings: list[dict] = []
    seen = skipped = 0
    lane_counts = {"edison": 0, "claude": 0, "both": 0}

    for status in STATUSES:
        for path in sorted((INGREDIENTS / status).glob("*.yaml")):
            if args.slug and path.stem != args.slug:
                continue

            edison_report = None
            meta = bundles.get(path.stem.lower())
            if meta is not None:
                md = meta.parent / meta.name.replace("-literature-meta.yaml", "-literature.md")
                if md.exists() and md.stat().st_size:
                    edison_report = parse_report(split_answer(md, meta))

            claude_report = None
            cmd = args.claude_dir / f"{path.stem}-claude-research.md"
            if cmd.exists() and cmd.stat().st_size:
                claude_report = parse_claude_report(cmd)

            if edison_report is None and claude_report is None:
                skipped += 1
                continue
            seen += 1
            if edison_report and claude_report:
                lane_counts["both"] += 1
            elif edison_report:
                lane_counts["edison"] += 1
            else:
                lane_counts["claude"] += 1

            rec = yaml.safe_load(path.read_text(encoding="utf-8", errors="replace")) or {}
            facts = record_facts(rec)
            found: list[dict] = []
            if edison_report:
                found += compare(status, path.stem, facts, edison_report, lane="edison")
            if claude_report:
                found += compare(status, path.stem, facts, claude_report, lane="claude")
            found += cross_lane(status, path.stem, facts, edison_report, claude_report)
            findings.extend(found)
            if args.verbose:
                print(f"{path.stem}: {[f['kind'] for f in found] or ['no findings']}")

    findings.sort(key=lambda f: (PRIORITY_ORDER[f["priority"]], f["kind"], f["slug"]))
    cutoff = PRIORITY_ORDER[args.min_priority]
    kept = [f for f in findings if PRIORITY_ORDER[f["priority"]] <= cutoff]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["priority", "kind", "lane", "status_dir", "slug", "identifier", "preferred_term",
            "recorded", "mapping_quality", "promoted_by", "documented_rationale",
            "detail", "evidence"]
    with (args.out.with_suffix(".tsv")).open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(kept)
    args.out.with_suffix(".json").write_text(
        json.dumps(findings, indent=2) + "\n", encoding="utf-8")

    write_summary(args.out.with_suffix(".md"), findings, kept, seen, skipped,
                  args.min_priority, lane_counts)

    tally: dict[str, int] = {}
    for f in findings:
        tally[f"{f['priority']} {f['kind']}"] = tally.get(f"{f['priority']} {f['kind']}", 0) + 1
    print(f"records with a usable bundle : {seen}")
    print(f"records without one (skipped): {skipped}")
    for k in sorted(tally, key=lambda k: (PRIORITY_ORDER[k[:2]], -tally[k])):
        print(f"  {k:<26} {tally[k]}")
    print(f"wrote {len(kept)} findings (>= {args.min_priority}) to {args.out.with_suffix('.tsv')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
