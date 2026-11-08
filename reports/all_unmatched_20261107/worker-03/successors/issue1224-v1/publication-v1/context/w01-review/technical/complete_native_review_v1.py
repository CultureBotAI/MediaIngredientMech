import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

P=Path(__file__).resolve().parent
W=Path.cwd().resolve()
def bind(p):
    p=Path(p).resolve()
    return {"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def write_json(name,data):
    with (P/name).open("x") as out:
        json.dump(data,out,indent=2,ensure_ascii=False);out.write("\n")
commands=[]
for args,stdout_name,stderr_name in [
    (["validate",str(P/"review-v4.yaml")],"review-validation-v4.stdout","review-validation-v4.stderr"),
    (["render","--content",str(P/"review-v4.yaml")],"review-v4.md","review-render-v4.stderr"),
]:
    cmd=[sys.executable,"-B",str(W/"scripts/record_review.py"),*args]
    with (P/stdout_name).open("x") as out,(P/stderr_name).open("x") as err:
        r=subprocess.run(cmd,cwd=W,stdout=out,stderr=err,check=False)
    commands.append({"argv":cmd,"cwd":str(W),"exit_code":r.returncode,"stdout":bind(P/stdout_name),"stderr":bind(P/stderr_name)})
    assert r.returncode==0,commands[-1]
report=json.loads((P/"REVIEW-v4.json").read_text())
assert report["verdict"]=="NATIVE_GUARD_CHECKS_PASS_RETAINED_WORKER_PROVENANCE_DEFECT_HELD"
assert report["full_projection"]["candidate_rows"]==37
receipt={
    "at":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
    "reviewer":"OpenAI Codex /root/issue_context, independent technical/native/guard/provenance reviewer",
    "active_review":bind(P/"REVIEW-v4.json"),"native_structured_review":bind(P/"review-v4.yaml"),"native_render":bind(P/"review-v4.md"),
    "program":bind(__file__),"native_helper":bind(W/"scripts/record_review.py"),"native_schema":bind(W/"src/mediaingredientmech/schema/record_review.yaml"),
    "commands":commands,"valid_reviews":1,
    "native_guard_verdict":report["verdict"],"structured_verdict":"needs_curation","scientific_approval":False,
    "scope":report["counts"],"all_author_rows_projected":report["full_projection"],"coordinator_metadata_correction":report["evidence_correction"],
    "finding":bind(P/"finding-retained-worker-evidence-1226-v1.json"),
    "hold":"Exactly one confirmed retained worker-proposal MappingEvidence counterexample in TARGET-024 under existing #1226. This is separate from the 13 new coordinator corrections, which pass. No global inherited-evidence conclusion follows; no unqualified whole-candidate acceptance.",
    "preserved_validation_attempts":[{"draft":bind(P/f"review-v{v}.yaml"),"stdout":bind(P/f"review-validation-v{v}.stdout"),"stderr":bind(P/f"review-validation-v{v}.stderr"),"disposition":reason} for v,reason in [(1,"Rejected YAML alias serialization; preserved."),(2,"Rejected slash-bearing finding issue_key as native Token; preserved."),(3,"Rejected missing exact selectors for snapshot-row targets; preserved.")]],
    "limits":["Native review validation verifies the review document, not source freshness; separate pinned-input and maintained-boundary receipts supply that evidence.","No shared native save: its default output path conflicts with the explicit private-only task scope. Actual native inspect, validate and render were used.","No additional broad checks, candidate changes, Git operations, GitHub mutations, external sessions or maintained writes in this completion step.","This local completion receipt is ready for independent skeptical binding and the parent outer seal; it is not a scientific approval or a release decision."]
}
write_json("native-review-completion-v1.json",receipt)
print(json.dumps({"active_review":bind(P/"REVIEW-v4.json"),"native_structured_review":bind(P/"review-v4.yaml"),"native_render":bind(P/"review-v4.md"),"completion":bind(P/"native-review-completion-v1.json")}))
