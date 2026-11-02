#!/usr/bin/env python3
"""Correct only the active di-keto BacDive evidence note (#1111).

The historical creation event and executed source artifacts remain immutable.
Dry-run by default; the CLI holds the native lock and Python callers must do so.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import html
import importlib
import json
import re
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402
from scripts import apply_owned_name_policy as shared  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts import step7a_guarded_publication as publication  # noqa: E402

REPORT = Path("reports/diketo_bacdive_evidence_1111_20261102")
MANIFEST = REPORT / "source-evidence.json"
MANIFEST_SHA = "41defe43ca5fc06502964d155ea58376d5420c0ce2cb8ffe660294c18638d892"
_MANIFEST = shared.regular(ROOT / MANIFEST)
if guarded.digest(_MANIFEST) != MANIFEST_SHA:
    raise ValueError("Reviewed evidence-correction manifest changed")
META = json.loads(_MANIFEST)
OWNER = Path(META["owner"])
OWNERS = (OWNER,)
NAME = "2,5-didehydro-D-gluconate"
CONTROL = "5-dehydro-D-gluconate"
SOURCE_DIRECTORY = Path("reports/step7c_source_labels_313_235_20261102/sources")
HEADERS = ["@ref", "Chebi-ID", "Metabolite", "Production", ""]
OLD_SENTENCE = "The live BacDive production values are blank: no positive production assertion or chemical role is inferred."
NEW_SENTENCE = (
    "The archived BacDive production results for CHEBI:11449 in strains 34 and 58 are explicitly No "
    "(ph-x/text-danger icons, alt=No and title=No). Empty text extraction had omitted those result "
    "attributes. The count of two remains source-field label appearances; neither positive "
    "production nor a chemical role is inferred."
)
VERIFICATION = (
    "Inspected the archived Metabolite production tables at https://bacdive.dsmz.de/strain/34 "
    "and https://bacdive.dsmz.de/strain/58. Headers bind the exact CHEBI:11449/name row to the "
    "Production column; both cells explicitly encode No in icon alt/title attributes and ph-x "
    "classes. Neighboring mono-keto controls encode Yes (ph-check); their original ChEBI links "
    "are retained verbatim without assigning that source link as a new MIM identity. "
    f"Exact headers, row HTML, icon attributes and immutable input hashes: {MANIFEST} "
    f"sha256={MANIFEST_SHA}. Finding {META['issue']}; decision {META['decision']}."
)
CHANGE = (
    "Corrected the active mapping-evidence note's blank-result interpretation to the explicitly "
    "recorded No results for the two archived BacDive di-keto rows. The earlier "
    "CREATED_FROM_ORIGINAL_SOURCE_LABEL event's blank assertion is incorrect and is superseded "
    "by this event; the original event and executed source proofs remain unchanged. Preserved "
    "CHEBI:11449 identity, exact mapping, source-field count 2, zero recipe counts, recovered "
    "RAW_TEXT alias and absence of a production role. No scientific approval is added. "
    + VERIFICATION
)
APPROVAL = META["approval"]
CODE_PATHS = tuple(
    dict.fromkeys(
        (
            Path(__file__),
            Path(shared.__file__),
            Path(publication.__file__),
            *shared.CODE_PATHS,
            ROOT / "MAPPING_SEMANTICS.md",
            ROOT / "src/mediaingredientmech/schema/mech_shared.yaml",
        )
    )
)
_LOADED_CODE = {p: shared.regular(p) for p in CODE_PATHS}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def bound_path(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "Input/receipt path must not be aliased")
    return path


class _Cell(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []
        self.icons = []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == "i":
            self.icons.append(dict(attrs))


def production_result(cell_html):
    """Read boolean result attributes; empty visible text is not absence."""
    cell = _Cell()
    cell.feed(cell_html)
    text = " ".join("".join(cell.text).split())
    if not cell.icons:
        require(text in {"", "No", "Yes"}, "Unrecognized production result text")
        return text or None
    require(len(cell.icons) == 1, "Ambiguous production result icons")
    icon = cell.icons[0]
    value = icon.get("alt")
    require(
        value in {"No", "Yes"} and icon.get("title") == value,
        "Missing or conflicting production icon attributes",
    )
    classes = set(icon.get("class", "").split())
    expected = {"ph-x", "text-danger"} if value == "No" else {"ph-check", "text-success"}
    forbidden = {"ph-check", "text-success"} if value == "No" else {"ph-x", "text-danger"}
    require(
        expected <= classes and not classes & forbidden and text in {"", value},
        "Conflicting production result class/text",
    )
    return value


def production_rows(raw):
    """Bounded extraction of the archived named table, including its headers."""
    tables = re.findall(
        r"<h3>Metabolite production</h3>.*?(<table\b.*?</table>)", raw.decode(), re.S
    )
    require(len(tables) == 1, "Expected one Metabolite production table")

    def clean(value):
        return html.unescape(re.sub(r"<[^>]*>", "", value)).strip()

    headers = [clean(x) for x in re.findall(r"<th\b[^>]*>(.*?)</th>", tables[0], re.S)]
    require(headers == HEADERS, "Production table headers changed")
    selected = {}
    for row in re.findall(r"<tr\b.*?</tr>", tables[0], re.S):
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.S)
        if len(cells) != len(HEADERS):
            require(not cells, "Production row cell count changed")
            continue
        label = clean(cells[2])
        if label not in {NAME, CONTROL}:
            continue
        require(label not in selected, "Duplicate selected production row")
        if label == NAME:
            require("chebiId=CHEBI:11449" in cells[1], "Di-keto source ChEBI identity changed")
        selected[label] = production_result(cells[3])
    require(set(selected) == {NAME, CONTROL}, "Missing selected production row/control")
    return selected


def evidence_inputs(root):
    raw = shared.regular(root / MANIFEST)
    require(raw == _MANIFEST, "Reviewed correction evidence manifest changed")
    result = {root / MANIFEST: raw}
    for name, item in META["files"].items():
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts, "Unsafe evidence path")
        data = shared.regular(root / path)
        require(
            guarded.digest(data) == item["sha256"] and len(data) == item["bytes"],
            f"Frozen correction source/preimage changed: {name}",
        )
        result[root / path] = data
    for sid in (34, 58):
        require(
            production_rows(result[root / SOURCE_DIRECTORY / f"bacdive-{sid}.html"])
            == {NAME: "No", CONTROL: "Yes"},
            "Archived production evidence changed",
        )
    return result


def frozen():
    data = shared.regular(ROOT / META["preimage"])
    require(guarded.digest(data) == META["owner_sha256"], "Reviewed correction preimage changed")
    return data


def propose_sources(original, *, timestamp):
    require(
        set(original) == set(OWNERS) and original[OWNER] == frozen(),
        "Exactly the reviewed di-keto owner preimage is required",
    )
    when = dt.datetime.fromisoformat(timestamp)
    require(
        when.utcoffset() == dt.timedelta(0)
        and when >= dt.datetime.fromisoformat(META["evidence_not_before"]),
        "Timestamp must be UTC after evidence reinterpretation",
    )
    evidence_inputs(ROOT)
    record = copy.deepcopy(yaml.safe_load(original[OWNER]))
    evidence = record["ontology_mapping"]["evidence"]
    require(
        len(evidence) == 1 and evidence[0]["notes"].count(OLD_SENTENCE) == 1,
        "Unexpected active evidence-note preimage",
    )
    evidence[0]["notes"] = (
        evidence[0]["notes"].replace(OLD_SENTENCE, NEW_SENTENCE) + " " + VERIFICATION
    )
    record_curation_event(
        record,
        curator="Codex",
        action="CORRECTED_SOURCE_EVIDENCE_NOTE",
        changes=CHANGE,
        timestamp=timestamp,
        previous_status="MAPPED",
        new_status="MAPPED",
        llm_assisted=True,
        llm_model="gpt-6",
    )
    with tempfile.TemporaryDirectory(prefix="mim-bacdive-1111-render-") as directory:
        target = Path(directory) / OWNER.name
        write_validated_ingredient(record, target)
        return {OWNER: target.read_bytes()}


def verify_complete(current):
    require(set(current) == set(OWNERS), "Exactly one completed di-keto owner is required")
    try:
        stamp = yaml.safe_load(current[OWNER])["curation_history"][-1]["timestamp"]
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete evidence-note correction") from error
    require(
        current == propose_sources({OWNER: frozen()}, timestamp=stamp),
        "Partial or changed evidence-note correction",
    )
    return stamp


def backups(log):
    return {OWNER: log.with_name(log.stem + ".before-" + OWNER.name)}


def source_context(root, current):
    timestamp = verify_complete(current)
    paths = shared.ingredient_paths(root)
    require(root / OWNER in paths, "Reviewed di-keto owner is absent")
    inputs = {p: shared.regular(p) for p in paths} | evidence_inputs(root)
    for path, expected in _LOADED_CODE.items():
        require(shared.regular(path) == expected, "Loaded correction dependency changed")
        inputs[path] = expected
    for name, expected in META["protected_anchors"].items():
        path = root / name
        data = shared.regular(path)
        require(guarded.digest(data) == expected, "Protected publication anchor changed")
        inputs[path] = data
    for name in ("kg_microbe_write", "kg_microbe_write.transaction"):
        path = Path(importlib.import_module(name).__file__).resolve()
        inputs[path] = shared.regular(path)
    historical = inputs | {root / OWNER: frozen()}
    result = {
        "phase": "sources",
        "approval": APPROVAL,
        "timestamp": timestamp,
        "evidence_manifest": str(root / MANIFEST),
        "evidence_manifest_sha256": MANIFEST_SHA,
        "input_sha256": {str(p): guarded.digest(b) for p, b in historical.items()},
        "output_sha256": {str(p): guarded.digest(b) for p, b in current.items()},
        "records": [
            {
                "source_record": str(OWNER),
                "shape": "source_evidence_note_correction",
                "before_yaml_sha256": META["owner_sha256"],
                "after_yaml_sha256": guarded.digest(current[OWNER]),
                "change": CHANGE,
                "verification": VERIFICATION + " " + APPROVAL,
            }
        ],
    }
    shared.validate_scope(root, inputs, paths)
    return inputs, result, paths


def source_receipt(root, log):
    root, log = shared.checked_root(root), bound_path(log)
    current = {OWNER: shared.regular(root / OWNER)}
    inputs, result, paths = source_context(root, current)
    inputs[log] = shared.completed_receipt(log, result, root, changed=set(OWNERS))
    backup = backups(log)[OWNER]
    require(shared.regular(backup) == frozen(), "Completed correction preimage changed")
    inputs[backup] = frozen()
    inputs.update(
        publication.completed_journal(
            root, log, json.loads(inputs[log]), previous={OWNER: frozen()}
        )
    )
    shared.validate_scope(root, inputs, paths)
    return inputs, result


def apply_sources(root, log, *, apply=False):
    root, log = shared.checked_root(root), bound_path(log)
    original = {OWNER: shared.regular(root / OWNER)}
    if original != {OWNER: frozen()}:
        source_receipt(root, log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    current = propose_sources(original, timestamp=dt.datetime.now(dt.timezone.utc).isoformat())
    inputs, result, paths = source_context(root, current)
    return publication.publish(
        root,
        current,
        inputs,
        log,
        {backups(log)[OWNER]: original[OWNER]},
        result,
        apply=apply,
        validate_scope=lambda: shared.validate_scope(root, inputs, paths),
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    root = shared.checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "#1111 bounded BacDive evidence correction"):
        result = apply_sources(root, args.log, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
