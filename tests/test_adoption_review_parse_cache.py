"""Native shared-bundle admission and currentness regressions for #1347.

Small synthetic reports exercise the real parser/schema/Markdown contract. They
are not campaign science, and no test uses a timing or memory threshold.
"""

from __future__ import annotations

import copy
import json
import os
from collections import Counter
from pathlib import Path

import pytest
import yaml

from tests import test_stable_id_adoption as adoption_fixture
from tests.test_stable_id_adoption import Fixture, api, command, commit, initialize, write


class ReviewFixture:
    """Two independently checked targets in each of two genuine native bundles."""

    report = Fixture.report
    save_report = Fixture.save_report

    def __init__(self, root, alter=None, disposition="CREATE_DISTINCT_CONCEPT"):
        self.root = root
        initialize(root)
        for name, (raw, _) in api._CAPTURE.files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        self.head = commit(root)
        self.native = api._CAPTURE.script("scripts/record_review.py")
        self.payloads = [
            {"operation_id": f"OP{i}", "synthetic_material": f"distinct material {i}"}
            for i in (1, 2)
        ]
        self.context = {"scope": "two complete synthetic pre-ID questions"}
        self.request = {"review_inputs": {}}
        for key, value in (
            ("context", self.context),
            ("payloads", self.payloads),
            ("eligibility_intake", {"literal_holds": ["unclassified original evidence"]}),
        ):
            name = f"evidence/{key}.json"
            write(root / name, value)
            self.request[key] = {"path": name, "sha256": api.sha((root / name).read_bytes())}
        (root / "primary.txt").write_text("Synthetic inspected evidence.\n")
        self.decisions = [
            {
                "operation_id": p["operation_id"],
                "disposition": disposition,
                "concept_key": p["operation_id"],
                "owner_operation": p["operation_id"],
                "existing_mim_id": "MIM:0000001",
                "identity_holds": [] if disposition != "WITHHOLD_IDENTITY" else ["identity open"],
                "other_holds": ["role remains unreviewed"],
            }
            for p in self.payloads
        ]
        self.targets = [
            {
                "target_id": p["operation_id"],
                "path": self.request["payloads"]["path"],
                "selector": p["operation_id"],
                "kind": "snapshot_row",
                "label": p["synthetic_material"],
                "semantic_digest": {
                    "algorithm": api.CLAIM_ALGORITHM,
                    "sha256": api.digest(p),
                    "description": api.CLAIM_DESCRIPTION,
                },
                "owner_paths": [
                    {
                        "repository": api.REPOSITORY,
                        "path": self.request["payloads"]["path"],
                        "role": "proposed pre-ID concept",
                    }
                ],
            }
            for p in self.payloads
        ]
        self.reports = {}
        for role in ("primary", "skeptic"):
            report = self.report(
                role,
                copy.deepcopy(self.targets),
                [self.request["context"]["path"], self.request["payloads"]["path"], "primary.txt"],
            )
            for row in self.decisions:
                dimensions = {
                    "concept_disposition": disposition,
                    "concept_scope": "complete_source_and_duplicate_boundary",
                    "residual_identity_holds": json.dumps(
                        row["identity_holds"], separators=(",", ":")
                    ),
                    "residual_other_holds": json.dumps(row["other_holds"], separators=(",", ":")),
                    "concept_key": row["concept_key"],
                    "concept_owner_operation": row["owner_operation"],
                    "concept_existing_mim_id": row["existing_mim_id"],
                }
                report["assessments"].append(
                    {
                        "assessment_id": row["operation_id"],
                        "area": "identity",
                        "topic": "Complete synthetic identity boundary",
                        "outcome": "unknown" if disposition == "WITHHOLD_IDENTITY" else "supported",
                        "summary": "Explicit synthetic decision",
                        "target_ids": [row["operation_id"]],
                        "evidence_ids": ["primary"],
                        "dimensions": [
                            {
                                "name": name,
                                "value": value,
                                "definition": "Explicit synthetic reviewed dimension",
                                "evidence_ids": ["primary"],
                            }
                            for name, value in dimensions.items()
                        ],
                    }
                )
                row[role] = {
                    "path": f"reviews/structured/{report['review_id']}/review.yaml",
                    "target_id": row["operation_id"],
                    "assessment_id": row["operation_id"],
                }
            if alter:
                alter(role, report)
            self.reports[role] = report
            path = self.save_report(report)
            for member in (path, path.with_name("review.md")):
                self.request["review_inputs"][str(member.relative_to(root))] = api.sha(
                    member.read_bytes()
                )
        self.request["decisions"] = self.decisions

    def load(self):
        inputs = api.Inputs(self.root)
        api._CAPTURE.bind(inputs)
        return api.Loaded(
            inputs=inputs,
            legacy=api.Inputs(self.root),
            claw=None,
            request=copy.deepcopy(self.request),
            request_path="synthetic-request.json",
            owners={},
            legacy_owners={},
            existing={},
            operations={},
            decisions={r["operation_id"]: copy.deepcopy(r) for r in self.decisions},
            context=copy.deepcopy(self.context),
            payloads=copy.deepcopy(self.payloads),
            head=self.head,
            index=command(self.root, "ls-files", "--stage", "-z"),
            initial_dirty=set(),
        )


def check_target(loaded, number):
    payload = loaded.payloads[number]
    row = loaded.decisions[payload["operation_id"]]
    return api._reviews(loaded, [row["primary"], row["skeptic"]], payload)


def count_native_parses(monkeypatch):
    calls = Counter()
    original = api._CAPTURE.script

    def script(name):
        native = original(name)
        if name == "scripts/record_review.py":
            parse = native.parse_review_bundle

            def counted(path, *args, **kwargs):
                calls[path] += 1
                return parse(path, *args, **kwargs)

            native.parse_review_bundle = counted
        return native

    monkeypatch.setattr(api._CAPTURE, "script", script)
    return calls


def test_1347_successful_pair_is_parsed_once_but_both_targets_are_admitted(tmp_path, monkeypatch):
    fixture = ReviewFixture(tmp_path / "reviews")
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    before = api.encoded(loaded.request)
    assert api._admitted(loaded) is None
    assert list(calls.values()) == [1, 1]
    assert len(loaded._review_parse_cache) == 2
    assert api.encoded(loaded.request) == before
    # A separate native load has no inherited parse result or scientific outcome.
    fresh = fixture.load()
    assert api._admitted(fresh) is None
    assert list(calls.values()) == [2, 2]
    assert api.encoded(fresh.request) == before
    assert fresh._review_parse_cache is not loaded._review_parse_cache
    for role in ("primary", "skeptic"):
        path = fixture.decisions[0][role]["path"]
        md = str(Path(path).with_name("review.md"))
        direct = fixture.native.parse_review_bundle(
            path,
            (fixture.root / path).read_bytes(),
            (fixture.root / md).read_bytes(),
            fixture.root / "schema/record_review.yaml",
        )
        cached = api._parsed_review(loaded, fixture.native, path, md)
        assert api.encoded(cached) == api.encoded(direct)


def change_dimension(report, name, value):
    next(x for x in report["assessments"][1]["dimensions"] if x["name"] == name)["value"] = value


@pytest.mark.parametrize(
    "change,message",
    [
        ("digest", "review target differs"),
        ("owner", "review owner target differs"),
        ("selector", "review target differs"),
        ("assessment_targets", "single-target"),
        ("disposition", "current concept decision"),
        ("concept_scope", "current concept decision"),
        ("concept_key", "exact concept group"),
        ("concept_owner_operation", "exact concept group"),
        ("residual_identity_holds", "residual hold classification"),
        ("residual_other_holds", "residual hold classification"),
    ],
)
def test_1347_cached_pair_does_not_approve_a_bad_second_target(
    tmp_path, monkeypatch, change, message
):
    def alter(role, report):
        if role != "skeptic":
            return
        if change == "digest":
            report["targets"][1]["semantic_digest"]["sha256"] = "0" * 64
        elif change == "owner":
            report["targets"][1]["owner_paths"][0]["role"] = "not the reviewed owner"
        elif change == "selector":
            report["targets"][1]["selector"] = "DIFFERENT"
        elif change == "assessment_targets":
            report["assessments"][1]["target_ids"] = ["OP1", "OP2"]
        else:
            name = "concept_disposition" if change == "disposition" else change
            change_dimension(
                report, name, '["not agreed"]' if name.startswith("residual_") else "different"
            )

    fixture = ReviewFixture(tmp_path / "reviews", alter)
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    assert check_target(loaded, 0) is None
    assert list(calls.values()) == [1, 1]
    with pytest.raises(ValueError, match=message):
        check_target(loaded, 1)
    assert list(calls.values()) == [1, 1]


@pytest.mark.parametrize("field", ["target_id", "assessment_id"])
def test_1347_cache_hit_keeps_exact_reference_resolution(tmp_path, monkeypatch, field):
    fixture = ReviewFixture(tmp_path / "reviews")
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    check_target(loaded, 0)
    loaded.decisions["OP2"]["skeptic"][field] = "MISSING"
    with pytest.raises(ValueError, match="target differs|single-target"):
        check_target(loaded, 1)
    assert list(calls.values()) == [1, 1]


def test_1347_cache_hit_keeps_exact_bind_existing_decision(tmp_path, monkeypatch):
    def alter(role, report):
        if role == "skeptic":
            change_dimension(report, "concept_existing_mim_id", "MIM:0000002")

    fixture = ReviewFixture(tmp_path / "reviews", alter, "BIND_EXISTING_CONCEPT_ONLY")
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    check_target(loaded, 0)
    with pytest.raises(ValueError, match="select the existing concept"):
        check_target(loaded, 1)
    assert list(calls.values()) == [1, 1]


def second_target_finding(report, status):
    report["findings"].append(
        {
            "finding_id": "identity-open",
            "issue_key": "synthetic-identity-open",
            "category": "identity",
            "severity": "informational",
            "status": status,
            "certainty": "confirmed",
            "title": "Identity requires a decision",
            "description": "Synthetic unresolved second-target obligation",
            "target_ids": ["OP2"],
            "evidence_ids": ["primary"],
            "owner_paths": copy.deepcopy(report["targets"][1]["owner_paths"]),
            **(
                {"disposition_reason": "Explicitly deferred decision"}
                if status == "deferred"
                else {}
            ),
        }
    )


@pytest.mark.parametrize(
    "change", ["failed_check", "not_applicable", "open", "deferred", "unsupported", "no_primary"]
)
def test_1347_later_target_scientific_failures_survive_a_cache_hit(tmp_path, monkeypatch, change):
    def alter(role, report):
        if role != "skeptic":
            return
        if change in {"failed_check", "not_applicable"}:
            check = copy.deepcopy(report["checks"][0])
            check.update(
                check_id="second-target",
                target_ids=["OP2"],
                status="failed" if change == "failed_check" else change,
            )
            report["checks"].append(check)
        elif change in {"open", "deferred"}:
            second_target_finding(report, change)
        elif change == "unsupported":
            report["assessments"][1]["outcome"] = "unknown"
        else:
            evidence = copy.deepcopy(report["evidence"][0])
            evidence.update(evidence_id="context-only", kind="prior_review")
            report["evidence"].append(evidence)
            report["assessments"][1]["evidence_ids"] = ["context-only"]

    fixture = ReviewFixture(tmp_path / "reviews", alter)
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    check_target(loaded, 0)
    with pytest.raises(
        ValueError,
        match="required native check|unresolved concept|unsupported concept|captured primary",
    ):
        check_target(loaded, 1)
    assert list(calls.values()) == [1, 1]


def test_1347_explicit_withhold_keeps_its_native_semantics(tmp_path, monkeypatch):
    def alter(role, report):
        second_target_finding(report, "open")
        check = copy.deepcopy(report["checks"][0])
        check.update(check_id="second-target", target_ids=["OP2"], status="failed")
        report["checks"].append(check)

    fixture = ReviewFixture(tmp_path / "reviews", alter, "WITHHOLD_IDENTITY")
    loaded = fixture.load()
    calls = count_native_parses(monkeypatch)
    assert api._admitted(loaded) is None
    assert list(calls.values()) == [1, 1]
    assert loaded.decisions["OP2"]["identity_holds"] == ["identity open"]
    assert loaded.decisions["OP2"]["other_holds"] == ["role remains unreviewed"]


@pytest.mark.parametrize("change", ["same_identity", "self_review", "no_basis", "same_path"])
def test_1347_warm_parses_do_not_replace_separate_skeptical_review(tmp_path, change):
    def alter(role, report):
        if role != "skeptic":
            return
        if change == "same_identity":
            report["reviewer"]["identity"] = "primary"
        elif change == "self_review":
            report["reviewer"]["independence"] = "self_review"

    fixture = ReviewFixture(tmp_path / "reviews", alter)
    loaded = fixture.load()
    for role in ("primary", "skeptic"):
        path = loaded.decisions["OP1"][role]["path"]
        api._parsed_review(loaded, fixture.native, path, str(Path(path).with_name("review.md")))
    if change == "same_path":
        loaded.decisions["OP2"]["skeptic"] = copy.deepcopy(loaded.decisions["OP2"]["primary"])
    elif change == "no_basis":
        # The genuine native schema rejects a missing basis before any success
        # can be cached. A new invalid capture must not hit the warm valid one.
        path = loaded.decisions["OP2"]["skeptic"]["path"]
        report = copy.deepcopy(fixture.reports["skeptic"])
        report["reviewer"].pop("independence_basis")
        (fixture.root / path).write_text(yaml.safe_dump(report, sort_keys=False))
        loaded.inputs.files[path] = api.FrozenFile.capture(fixture.root / path)
    with pytest.raises(
        ValueError, match="independence_basis" if change == "no_basis" else "separate skeptical"
    ):
        check_target(loaded, 1)
    if change == "no_basis":
        assert len(loaded._review_parse_cache) == 2  # Invalid successor was not cached.


def test_1347_mutating_a_returned_report_cannot_change_cached_science(tmp_path):
    fixture = ReviewFixture(tmp_path / "reviews")
    loaded = fixture.load()
    path = loaded.decisions["OP1"]["primary"]["path"]
    md = str(Path(path).with_name("review.md"))
    first = api._parsed_review(loaded, fixture.native, path, md)
    first["assessments"][1]["outcome"] = "unknown"
    first["targets"][1]["semantic_digest"]["sha256"] = "0" * 64
    again = api._parsed_review(loaded, fixture.native, path, md)
    assert again["assessments"][1]["outcome"] == "supported"
    assert again["targets"][1]["semantic_digest"]["sha256"] == api.digest(loaded.payloads[1])
    assert all(isinstance(value, str) for value in loaded._review_parse_cache.values())
    assert check_target(loaded, 1) is None


@pytest.mark.parametrize(
    "value",
    ["retained literal \u00e9", "retained literal \U0001f9ea", "\udca0", "\ud83d", "\ud83d\udc1c"],
    ids=["bmp", "non_bmp", "lone_low_surrogate", "lone_high_surrogate", "adjacent_surrogates"],
)
def test_1347_native_admitted_strings_survive_cache_losslessly(tmp_path, monkeypatch, value):
    def alter(role, report):
        report["assessments"][0]["dimensions"].append(
            {
                "name": "literal_capture_annotation",
                "value": value,
                "definition": "Synthetic optional annotation; not a decision dimension.",
                "evidence_ids": [],
            }
        )

    fixture = ReviewFixture(tmp_path / "reviews", alter)
    loaded = fixture.load()
    path = loaded.decisions["OP1"]["primary"]["path"]
    md = str(Path(path).with_name("review.md"))
    expected = fixture.native.parse_review_bundle(
        path,
        (fixture.root / path).read_bytes(),
        (fixture.root / md).read_bytes(),
        fixture.root / "schema/record_review.yaml",
    )
    calls = count_native_parses(monkeypatch)
    native = api._CAPTURE.script("scripts/record_review.py")
    first = api._parsed_review(loaded, native, path, md)
    again = api._parsed_review(loaded, native, path, md)
    assert first == expected == again
    assert first is not again
    assert calls[path] == 1
    for report in (expected, first, again):
        retained = report["assessments"][0]["dimensions"][-1]["value"]
        assert [ord(char) for char in retained] == [ord(char) for char in value]
    assert api._admitted(loaded) is None
    assert calls[path] == 1
    assert all(isinstance(item, str) for item in loaded._review_parse_cache.values())


@pytest.mark.parametrize("change", ["yaml", "markdown", "utf8", "canonical_id", "scope"])
def test_1347_failed_native_parse_never_becomes_reusable_success(tmp_path, monkeypatch, change):
    fixture = ReviewFixture(tmp_path / "reviews")
    path = fixture.decisions[0]["primary"]["path"]
    yaml_path = fixture.root / path
    md_path = yaml_path.with_name("review.md")
    if change == "yaml":
        yaml_path.write_text("not: [valid YAML\n")
    elif change == "markdown":
        md_path.write_text("Different scientific report\n")
    elif change == "utf8":
        md_path.write_bytes(b"\xff")
    else:
        report = copy.deepcopy(fixture.reports["primary"])
        if change == "canonical_id":
            report["review_id"] = "20260102T000000Z-a-different-id"
            md_path.write_text(fixture.native.render_markdown(report))
        else:
            report["scope"]["reviewed_target_ids"].remove("OP2")
        yaml_path.write_text(yaml.safe_dump(report, sort_keys=False))
    loaded = fixture.load()
    calls = Counter()
    parse = fixture.native.parse_review_bundle

    def counted(*args, **kwargs):
        calls["attempts"] += 1
        return parse(*args, **kwargs)

    monkeypatch.setattr(fixture.native, "parse_review_bundle", counted)
    for _ in range(2):
        with pytest.raises((ValueError, UnicodeDecodeError, yaml.YAMLError)):
            api._parsed_review(loaded, fixture.native, path, str(Path(path).with_name("review.md")))
        assert not loaded._review_parse_cache
    assert calls["attempts"] == 2


@pytest.mark.parametrize("member", ["review.yaml", "review.md"])
def test_1347_changed_pair_capture_never_hits_the_old_success(tmp_path, member):
    fixture = ReviewFixture(tmp_path / "reviews")
    loaded = fixture.load()
    path = fixture.decisions[0]["primary"]["path"]
    md = str(Path(path).with_name("review.md"))
    api._parsed_review(loaded, fixture.native, path, md)
    changed = path if member == "review.yaml" else md
    destination = fixture.root / changed
    destination.write_bytes(b"{}\n" if member == "review.yaml" else b"not matching\n")
    # An explicitly new capture cannot collide with a previous exact-byte entry.
    loaded.inputs.files[changed] = api.FrozenFile.capture(destination)
    with pytest.raises(ValueError):
        api._parsed_review(loaded, fixture.native, path, md)
    assert len(loaded._review_parse_cache) == 1


@pytest.mark.parametrize(
    "change",
    [
        "source",
        "context",
        "schema",
        "helper",
        "runtime",
        "head",
        "index",
        "inode",
        "symlink",
        "hardlink",
    ],
)
def test_1347_real_loaded_currentness_guards_still_refuse_after_cache_warmup(
    tmp_path, monkeypatch, change
):
    from tests.stable_publication_fixture import materialize_producer

    claw = materialize_producer(tmp_path / "native-claw")
    monkeypatch.setattr(adoption_fixture, "CLAW", claw)
    (tmp_path / "native").mkdir()
    fixture = Fixture(tmp_path / "native", monkeypatch)
    loaded = api._load(fixture.root, fixture.request_path)
    api._admitted(loaded)
    assert len(loaded._review_parse_cache) == 2
    before = {name: (fixture.root / name).read_bytes() for name in loaded.owners}
    if change in {"source", "context"}:
        relative = "primary.txt" if change == "source" else fixture.request["context"]["path"]
        path = fixture.root / relative
        path.write_bytes(path.read_bytes() + b"\n")
    elif change in {"schema", "helper"}:
        relative = "schema/record_review.yaml" if change == "schema" else "scripts/record_review.py"
        path = fixture.root / relative
        path.write_bytes(path.read_bytes() + b"\n")
    elif change == "runtime":
        monkeypatch.setitem(api._CAPTURE.runtime, "python", "0.0.0")
    elif change == "head":
        command(fixture.root, "commit", "--allow-empty", "-m", "Different endpoint")
    elif change == "index":
        path = fixture.root / "staged-unrelated.txt"
        path.write_text("changed index\n")
        command(fixture.root, "add", "staged-unrelated.txt")
    else:
        path = fixture.root / fixture.request["decisions"][0]["primary"]["path"]
        raw = path.read_bytes()
        if change == "inode":
            original = (path.stat().st_dev, path.stat().st_ino)
            replacement = fixture.root / "replacement-report.yaml"
            replacement.write_bytes(raw)
            # Keep the original allocated until the replacement exists (#1347).
            # Unlink/recreate can reuse the same inode on some filesystems.
            distinct = (replacement.stat().st_dev, replacement.stat().st_ino)
            assert distinct != original
            replacement.replace(path)
            assert (path.stat().st_dev, path.stat().st_ino) == distinct
            assert path.read_bytes() == raw
        else:
            path.unlink()
            other = fixture.root / "aliased-report.yaml"
            other.write_bytes(raw)
            if change == "hardlink":
                os.link(other, path)
            else:
                path.symlink_to(other)
    with pytest.raises(ValueError):
        loaded.check()
    assert {name: (fixture.root / name).read_bytes() for name in loaded.owners} == before
    assert not fixture.stage.exists() and not fixture.receipt.exists()


def test_1347_noncanonical_pair_path_cannot_reuse_a_valid_report(tmp_path):
    fixture = ReviewFixture(tmp_path / "reviews")
    loaded = fixture.load()
    path = fixture.decisions[0]["primary"]["path"]
    md = str(Path(path).with_name("review.md"))
    api._parsed_review(loaded, fixture.native, path, md)
    alias = "reviews/noncanonical/review.yaml"
    alias_path = fixture.root / alias
    alias_path.parent.mkdir()
    alias_path.write_bytes((fixture.root / path).read_bytes())
    alias_md = str(Path(alias).with_name("review.md"))
    (fixture.root / alias_md).write_bytes((fixture.root / md).read_bytes())
    with pytest.raises(ValueError, match="canonical structured bundle"):
        api._parsed_review(loaded, fixture.native, alias, alias_md)
    assert len(loaded._review_parse_cache) == 1


def test_1347_native_administrative_bytes_equal_without_parse_reuse(tmp_path, monkeypatch):
    from tests.stable_publication_fixture import materialize_producer

    claw = materialize_producer(tmp_path / "native-claw")
    monkeypatch.setattr(adoption_fixture, "CLAW", claw)
    (tmp_path / "native").mkdir()
    fixture = Fixture(tmp_path / "native", monkeypatch)
    warm = api._load(fixture.root, fixture.request_path)
    cold = api._load(fixture.root, fixture.request_path)
    calls = count_native_parses(monkeypatch)
    api._admitted(warm)
    assert list(calls.values()) == [1, 1]
    for number in range(len(cold.payloads)):
        cold._review_parse_cache.clear()
        check_target(cold, number)
    assert list(calls.values()) == [3, 3]

    def native_bytes(loaded):
        records, moves, plan = api._records(loaded)
        return {
            "records": {
                name: api.serialized(record, fixture.root / api.SCHEMA)
                for name, record in records.items()
            },
            "moves": api.encoded(moves),
            "assignments": api.encoded(plan.assignments),
            "registry": api.dump_registry(plan.registry),
            "lifecycle": api.dump_lifecycle(plan.registry),
        }

    assert native_bytes(warm) == native_bytes(cold)
    warm.check()
    cold.check()
    assert not fixture.stage.exists() and not fixture.receipt.exists()
