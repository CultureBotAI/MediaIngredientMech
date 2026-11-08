"""2026-11-08: inspect exact official payloads and bind them to frozen owner hints.

This creates a private reference cache, not case decisions, owner selection,
mapping approval or a native record review. All source repositories stay read-only.
"""

from __future__ import annotations

import csv
import datetime
import hashlib
import io
import json
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
C = HERE.parents[1]
W = C.parent / "kgm-unmapped-20261107/worktree"
BASE = "e000d66dd26ab053e9b17ce7bf8d3c873c3dde99"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    with (HERE / name).open("x") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def inspect_record(row):
    path = HERE / row["capture_path"]
    assert sha(path) == row["payload_sha256"]
    payload = json.loads(path.read_text())
    if row["requested_id"].startswith(("CHEBI:", "FOODON:")):
        terms = payload.get("_embedded", {}).get("terms", [])
        assert len(terms) == 1 and terms[0]["obo_id"] == row["requested_id"]
        term = terms[0]
        row["observed"] = {
            key: term.get(key)
            for key in [
                "obo_id",
                "iri",
                "label",
                "description",
                "is_obsolete",
                "term_replaced_by",
                "ontology_name",
                "ontology_iri",
            ]
        }
        row["observed"]["annotation"] = term.get("annotation", {})
        row["observed"]["obo_synonym"] = term.get("obo_synonym", [])
        row["locator"] = "/_embedded/terms/0"
        row["evidence_id"] = "OLS:" + row["requested_id"]
        row["limitations"] = [
            "This is the ontology's exact-ID term record at the stated retrieval time, not an identification of any source ingredient.",
            "Preserve synonym scope; term existence and related synonyms do not approve aliases or supplied forms.",
            "OLS is the official EBI ontology service; this capture does not independently verify every external database cross-reference.",
        ]
    else:
        is_properties = "PropertyTable" in payload
        entries = (
            payload["PropertyTable"]["Properties"]
            if is_properties
            else payload["InformationList"]["Information"]
        )
        assert len(entries) == 1
        entry = entries[0]
        assert isinstance(entry["CID"], int)
        if row["requested_id"].startswith("PUBCHEM:"):
            assert entry["CID"] == int(row["requested_id"].split(":")[1])
        elif not is_properties:
            assert row["requested_id"].removeprefix("cas:") in entry["Synonym"]
        row["observed"] = entry
        row["locator"] = (
            "/PropertyTable/Properties/0" if is_properties else "/InformationList/Information/0"
        )
        suffix = "properties" if is_properties else "synonyms"
        row["evidence_id"] = row["requested_id"] + ":" + suffix
        row["limitations"] = [
            "An official PubChem response for an explicitly recorded owner CID or CAS query; it does not decide source-case identity.",
            "PubChem synonyms aggregate submitted names and may conflict with structural fields; an exact CAS synonym is a lookup cross-reference, not independent CAS Registry certification.",
            "Preserve the returned CID and the exact query; do not infer interchangeable salts, protonation states, hydrates, products or stock solutions.",
        ]
    row["exact_requested_reference_validated"] = True
    row["scientific_case_or_mapping_approval"] = False
    return row


def main():
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=W, text=True).strip() == BASE
    inputs = json.loads((HERE / "verified-owner-inputs.json").read_text())
    for owner in inputs["owners"]:
        assert sha(W / owner["path"]) == owner["sha256"] == sha(HERE / owner["raw_snapshot"])
    sources = []
    for entry in json.loads((HERE / "reused-captures-v1.json").read_text())["entries"]:
        sources.append(
            inspect_record(
                {
                    "requested_id": entry["requested_id"],
                    "url": entry["url"],
                    "capture_path": entry["capture_path"],
                    "payload_sha256": entry["sha256"],
                    "retrieved_at": entry["accessed_at"],
                    "retrieval": "reused immutable official capture; not freshly fetched",
                    "original_provenance": entry,
                }
            )
        )
    for directory in ["network-attempt-v2", "referenced-cas-attempt-v3"]:
        for entry in json.loads((HERE / directory / "http-results-v1.json").read_text()):
            assert entry["retrieval_succeeded"] and entry["attempts"][-1]["status"] == 200
            sources.append(
                inspect_record(
                    {
                        "requested_id": entry["requested_id"],
                        "url": entry["url"],
                        "capture_path": directory + "/" + entry["capture_path"],
                        "payload_sha256": entry["payload_sha256"],
                        "retrieved_at": entry["attempts"][-1]["completed_at"],
                        "retrieval": "fresh official HTTPS response",
                        "http_provenance": str(
                            (Path(directory) / entry["capture_path"]).with_suffix(".http.json")
                        ),
                    }
                )
            )
    by_id = {row["evidence_id"]: row for row in sources}
    assert len(by_id) == len(sources) == 25
    for cas in ["136-09-4", "68-19-9"]:
        a = by_id["cas:" + cas + ":properties"]["observed"]
        b = by_id["cas:" + cas + ":synonyms"]["observed"]
        assert a["CID"] == b["CID"] and cas in b["Synonym"]

    limitations = {
        "Beta-nad.yaml": "CHEBI:15846 describes oxidized NAD(+). This does not determine a source stock's concentration, redox state, counterion or formulation.",
        "Calcium_Pantothenate.yaml": "The captured calcium salt record and its stereochemical fields do not establish an unspecified source's stereochemistry, hydrate or stock identity.",
        "Distilled_Water.yaml": "The water term does not establish distillation, purity, sterilization, treatment or suitability of a source water preparation.",
        "HOMOPIPES.yaml": "The recorded CID's structure and exact CAS synonym support reference lookup only; no claim of a missing or newly available ChEBI term is made.",
        "Hepes.yaml": "The term describes the specific HEPES acid structure. Do not apply it automatically to a sodium salt or a pH-adjusted stock solution.",
        "Mncl2_X_4_H2o.yaml": "The term explicitly denotes the tetrahydrate; it does not cover anhydrous or other-hydrate material, nor a stock solution without source context.",
        "Na-benzoate.yaml": "The sodium salt reference does not approve a stock formulation, concentration or an acid/salt substitution.",
        "Na-formate.yaml": "The monosodium salt reference does not identify a formic-acid solution or settle source concentration/formulation.",
        "Na-silicate.yaml": "The ontology record's sodium-silicate formula and cross-reference do not determine a commercial silicate ratio, hydration or aqueous product formulation.",
        "Na2co3.yaml": "This reference describes sodium carbonate; it does not merge the separately maintained Sodium_Carbonate_Solution owner or select an owner for shared source labels.",
        "Na2moo4_X_2_H2o.yaml": "The term explicitly denotes the dihydrate; no hydration state or whole-stock identity may be inferred for unmatched source text.",
        "Na2s2o3.yaml": "The sodium-thiosulfate reference does not establish a pentahydrate or a source stock preparation.",
        "Na2wo4_X_2_H2o.yaml": "The term explicitly denotes the dihydrate; anhydrous material and source stock formulations require their own supplied-form evidence.",
        "Sodium_Carbonate_Solution.yaml": "The current owner is a STOCK_SOLUTION. CHEBI:29377 is a solute reference and cannot establish whole-stock composition, concentration, preparation or exact identity.",
        "Soy_Peptone.yaml": "FOODON:03315720 is a hydrolyzed vegetable-protein category. It does not establish equivalence among soybean sources, digestion processes, suppliers, grades or named commercial peptones.",
        "TAPS_Sodium_Salt.yaml": "Keep the owner's CAS identity and NARROW_MATCH parent distinction. CHEBI:191055 describes the acid; the recorded PubChem CID describes the sodium salt. This cache does not approve either relation for a source case.",
        "Thiamine_pyrophosphate.yaml": "Existing WITHHOLD remains. Review source-case supplied forms and the current chloride-bearing properties/aliases; preserve the deliberate CHEBI:9532 decision and the prior conjugate-base ruling. CAS136-09-4 must not be described as chloride from a synonym string.",
        "Vitamin_B12.yaml": "CHEBI:176843 is a cobalamin-vitamer class. The recorded CAS query returns a particular PubChem structure; neither that lookup nor the generic source name selects a source case's vitamer, salt or formulation.",
    }
    owners = []
    for owner in inputs["owners"]:
        row = dict(owner)
        name = Path(owner["path"]).name
        ontology_id = owner["ontology_mapping"]["ontology_id"]
        refs = ["OLS:" + ontology_id] if ontology_id.startswith(("CHEBI:", "FOODON:")) else []
        cid = (owner.get("chemical_properties") or {}).get("pubchem_cid")
        if cid:
            refs.extend([f"PUBCHEM:{cid}:properties", f"PUBCHEM:{cid}:synonyms"])
        if name == "Thiamine_pyrophosphate.yaml":
            refs.extend(["OLS:CHEBI:18290", "cas:136-09-4:properties", "cas:136-09-4:synonyms"])
        if name == "Vitamin_B12.yaml":
            refs.extend(["cas:68-19-9:properties", "cas:68-19-9:synonyms"])
        assert refs and set(refs) <= set(by_id)
        row.update(
            primary_evidence_ids=refs,
            applicability="Reference records for identifiers already present in these exact frozen owner bytes; lexical hints are not identity matches.",
            limitations=limitations[name],
            source_cases_reviewed_by_this_cache=0,
            scientific_approval=False,
        )
        owners.append(row)

    provenance = HERE / "provenance"
    provenance.mkdir()
    refs = []
    for number in [268, 319, 320]:
        source = C / f"preflight/thiamine-issue-{number}-history-v1.json"
        target = provenance / source.name
        shutil.copyfile(source, target)
        refs.append(
            {
                "source_path": str(source),
                "cache_path": str(target.relative_to(HERE)),
                "sha256": sha(target),
                "scope": "Saved coordinator issue-history context; not a primary chemistry source or a new live GitHub query.",
            }
        )
    source = C / "preflight/shared-owner-hints-v1.json"
    shutil.copyfile(source, provenance / source.name)
    dispositions = (
        W
        / "reports/kgm_unmapped_chemicals_20261107/candidate-reviewed-sssom/mapping-dispositions.tsv"
    )
    lines = dispositions.read_text().splitlines(keepends=True)
    table = list(csv.DictReader(io.StringIO("".join(lines)), delimiter="\t"))
    assert len(table) == len(lines) - 1
    owner_paths = {row["path"] for row in owners}
    selected = [
        (index, row)
        for index, row in enumerate(table, 2)
        if row["owner_record"] in owner_paths
    ]
    if not selected:
        raise ValueError("Inspect disposition owner-path field; do not silently drop current holds")
    assert {row["owner_record"] for _, row in selected} == owner_paths
    owner_hashes = {row["path"]: row["sha256"] for row in owners}
    assert all(row["owner_record_sha256"] == owner_hashes[row["owner_record"]] for _, row in selected)
    thiamine_rows = [row for _, row in selected if row["owner_record"].endswith("/Thiamine_pyrophosphate.yaml")]
    assert len(thiamine_rows) == 1 and thiamine_rows[0]["source_position"] == "2792"
    assert thiamine_rows[0]["disposition"] == "WITHHOLD"
    with (provenance / "current-owner-dispositions.tsv").open("x") as stream:
        stream.write(lines[0])
        for line_number, row in selected:
            stream.write(lines[line_number - 1])
    refs.append(
        {
            "source_path": str(dispositions),
            "source_sha256": sha(dispositions),
            "cache_path": "provenance/current-owner-dispositions.tsv",
            "sha256": sha(provenance / "current-owner-dispositions.tsv"),
            "source_line_numbers": [number for number, row in selected],
            "scope": "Exact selected native export lines; historical review wording is not independent chemical evidence.",
        }
    )
    save("provenance.json", refs)
    save("primary-records.json", sources)
    save("owner-reference-index.json", owners)
    save(
        "summary.json",
        {
            "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "source_mim_revision": BASE,
            "owner_hashes_verified": len(owners),
            "official_primary_captures": len(sources),
            "fresh_official_captures": 23,
            "reused_official_captures": 2,
            "captured_ontology_records": sum(
                row["evidence_id"].startswith("OLS:") for row in sources
            ),
            "obsolete_in_captured_ontology_records": [
                row["requested_id"]
                for row in sources
                if row["evidence_id"].startswith("OLS:") and row["observed"]["is_obsolete"]
            ],
            "current_disposition_rows_preserved": len(selected),
            "source_case_decisions_created": 0,
            "owner_changes": 0,
            "mapping_or_release_approvals": 0,
            "initial_failures": "Three web-tool URL failures and 19 bounded initial DNS-failed requests are retained; 23 subsequent official HTTP captures succeeded. No failed lookup is classified as primary evidence.",
            "purpose": "Shared exact-reference evidence, not a substituted shard review, owner-selection decision or scientific approval.",
        },
    )
    print(
        json.dumps(
            {
                "primary_captures": len(sources),
                "owners": len(owners),
                "native_disposition_rows": len(selected),
            }
        )
    )


if __name__ == "__main__":
    main()
