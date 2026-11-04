"""Read-only deferred #669 export preflight; all output stays beside this file."""
from pathlib import Path
import csv, datetime, hashlib, importlib.util, io, json, subprocess, sys
import yaml

D = Path(__file__).resolve().parent
W = D.parent.parent / "step8-aliases"
C = D.parent.parent / "step7c-claw"
B = W / "output/next23-native-candidate-v1"
sys.path.insert(0, str(W))
from scripts import validate_sssom_invariants as inv
from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

def sha(raw): return hashlib.sha256(raw).hexdigest()
def read(path):
    path = Path(path)
    assert path.resolve() == path and path.is_file() and not path.is_symlink(), path
    raw = path.read_bytes(); captured[str(path)] = raw
    return raw
def table(raw): return list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))
def sssom(raw): return table(b"".join(l for l in raw.splitlines(keepends=True) if not l.startswith(b"#")))
def tokens(value): return [t.strip() for t in value.split("|") if t.strip()]
def load(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    exec(compile(read(path),str(path),"exec"),mod.__dict__)
    return mod
def git(*args): return subprocess.check_output(["git","-C",str(W),*args]).decode().strip()
def save(name, value):
    with (D/name).open("x") as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write("\n")

captured={}
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
head=git("rev-parse","HEAD")
status=git("status","--short")
policy=load("next23_native_owned_name", C/"src/kg_microbe_utils/owned_name_policy.py")
baseline=table(read(W/"mappings/other_cross_record_baseline.tsv"))
assert len(baseline)==23
selected={(r["subject_id"],r["token"].strip().casefold()) for r in baseline}
assert len(selected)==23
before_raw=read(W/"mappings/ingredient_mappings.sssom.tsv")
current=sssom(before_raw)
candidate=sssom(read(B/"candidate.sssom.tsv"))
candidate_side=table(read(B/"suppressed_aliases.tsv"))
existing_side=table(read(W/"mappings/suppressed_aliases.tsv"))
assert len(existing_side)==11
candidate_index={(r["subject_id"],r["token_key"]):r for r in candidate_side}
existing_index={(r["subject_id"],r["token_key"]):r for r in existing_side}
assert len(candidate_index)==len(candidate_side) and len(existing_index)==11
assert not selected & set(existing_index)
manifest=json.loads(read(B/"candidate.sssom.tsv.manifest.json"))
generation=json.loads(read(B/"generation-receipt.json"))
assert sha(read(B/"candidate.sssom.tsv"))==generation["candidate_sha256"]
assert sha(read(B/"suppressed_aliases.tsv"))==generation["sidecar_sha256"]
assert sha(read(B/"candidate.sssom.tsv.manifest.json"))==generation["native_generation_manifest_sha256"]
assert generation["input_bytes_unchanged"] is True
assert generation["scientific_approval_added"] is False
assert generation["producer_revision"]=="3022b8738dcc9e01c7464a8d5c95aa9be2eef141"
paths=inv._subject_to_path()
assert inv.REPO_ROOT.resolve()==W
records={s:yaml.safe_load(read(p)) for s,p in paths.items()}
# Include ignored and nested YAML in the preservation inventory. Native owner
# selection still uses the existing immediate mapped-directory contract.
all_yaml=[]
for p in sorted((W/"data/ingredients").rglob("*")):
    assert not p.is_symlink(),p
    if p.suffix==".yaml":read(p);all_yaml.append(str(p.relative_to(W)))
for p in sorted((W/"data/curated").glob("*.yaml")):read(p)
for p in (W/"UNIFIED_INGREDIENT_MAPPING.tsv",W/"UNIFIED_INGREDIENT_MAPPING.provenance.json",W/"docs/data/label_index.csv"):
    read(p)
owners=policy.build_owner_index(records)
assert owners==inv._preferred_term_owners()
index_rows=list(csv.DictReader(io.StringIO(read(W/"docs/data/label_index.csv").decode())))
review=json.loads(read(W/"reports/sssom_completion_20260921/review.json"))
assert review["source_sha256"]==sha(before_raw)
decisions={r["source_position"]:r for r in review["decisions"]}
source_inputs={r["path"]:r["sha256"] for r in manifest["source_inputs"]}
source_owner_matches=all(source_inputs[str(p)]==sha(captured[str(p)]) for p in paths.values())
assert source_owner_matches
rows=[]; projection=[dict(r) for r in current]
observed_pairs=set()
for item in baseline:
    subject=item["subject_id"];key=item["token"].strip().casefold()
    holder=owners.get(key)
    assert holder and subject not in holder
    assert holder  # Native owners are authoritative; owned_by remains descriptive text.
    hits=[]
    for pos,row in enumerate(current,1):
        if row["subject_id"]!=subject:continue
        removed=[t for t in tokens(row["other"]) if t.casefold()==key]
        if not removed:continue
        observed_pairs.add((subject,key))
        after=dict(row);after["other"]="|".join(t for t in tokens(row["other"]) if t.casefold()!=key)
        projection[pos-1]=after
        hits.append({"position":pos,"row":row,"row_sha256":sha(json.dumps(row,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()),
                     "removed_spellings":removed,"after_other":after["other"],"current_disposition":decisions[pos]["disposition"],
                     "current_review_evidence":decisions[pos]["review_evidence"],"current_review_reason":decisions[pos]["review_reason"]})
    assert len(hits)==1
    assert not any(r["subject_id"]==subject and key in {t.casefold() for t in tokens(r["other"])} for r in candidate)
    source=records[subject]
    aliases=[{"index":i,"entry":a} for i,a in enumerate(source.get("synonyms",[]) or []) if str(a.get("synonym_text","" )).strip().casefold()==key]
    assert not aliases, (subject,key,"unexpected YAML origin")
    observed=candidate_index.get((subject,key))
    assert observed is None, (subject,key,"unexpected candidate origin")
    if observed:assert json.loads(observed["owner_subject_ids"])==sorted(holder)
    idx=[r for r in index_rows if r["label"].casefold()==key]
    preferred=[r for r in idx if r["match_type"]=="preferred_term"]
    expected_ids={records[s]["identifier"] for s in holder}
    owner_first=bool(idx and idx[0]["identifier"] in expected_ids and idx[0]["match_type"]=="preferred_term")
    assert owner_first,(subject,key,idx)
    rows.append({"subject_id":subject,"token":item["token"],"token_key":key,"disposition":"SUPPRESS",
                 "baseline":item,"source_path":str(paths[subject].relative_to(W)),"source_sha256":sha(captured[str(paths[subject])]),
                 "source_identifier":source["identifier"],"yaml_aliases":aliases,
                 "credited_owners":[{"subject_id":s,"path":str(paths[s].relative_to(W)),"sha256":sha(captured[str(paths[s])]),"identifier":records[s]["identifier"],"preferred_term":records[s]["preferred_term"]} for s in sorted(holder)],
                 "canonical_occurrences":hits,"candidate_suppression":observed,
                 "sidecar_basis":"prior_sssom plus exact candidate origins" if observed else "prior_sssom only; absence from candidate is not chemical refutation",
                 "label_index_matches":idx,"owner_first":owner_first,
                 "approval":"NONE; preserve all YAML and existing identity decisions; changed mapping payloads follow native withholding"})
assert observed_pairs==selected
changed=[i for i,(a,b) in enumerate(zip(current,projection,strict=True),1) if a!=b]
assert all({k for k in current[i-1] if current[i-1][k]!=projection[i-1][k]}=={"other"} for i in changed)
normal_rejects=list(inv.evaluate_rule_k(current))
old_baseline=inv._other_baseline
try:
    inv._other_baseline=lambda:frozenset()
    before_k=list(inv.evaluate_rule_k(current));after_k=list(inv.evaluate_rule_k(projection));candidate_k=list(inv.evaluate_rule_k(candidate))
finally:inv._other_baseline=old_baseline
assert not normal_rejects and not after_k and not candidate_k
assert len(before_k)==len(changed)
proof=verify_mapping_chain(W)
assert len(proof["receipts"])==25 and proof["receipts"][-1]["sequence"]==25
companion=json.loads(read(W/"reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json"))
claims=json.loads(read(W/companion["claims_file"]))["claims"]
selected_claim_overlap=[c["claim_id"] for c in claims if c["kind"]=="mapping" and (c["payload"]["subject_id"] in {r["subject_id"] for r in rows})]
unchanged=all(Path(p).read_bytes()==raw for p,raw in captured.items())
assert unchanged
summary={"scope":"Fresh postmerge read-only preflight for the authorized deferred23 step; not an application, scientific approval, or independent review.",
         "started_at":started,"finished_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"mim_head":head,"mim_head_at_finish":git("rev-parse","HEAD"),
         "status_at_start":status,"status_at_finish":git("status","--short"),
         "counts":{"baseline_pairs":len(baseline),"canonical_rows":len(current),"candidate_rows":len(candidate),"canonical_sidecar_pairs":len(existing_side),
                   "candidate_sidecar_pairs":len(candidate_side),"selected_candidate_sidecar_pairs":sum(r["candidate_suppression"] is not None for r in rows),
                   "selected_prior_only_pairs":sum(r["candidate_suppression"] is None for r in rows),"selected_yaml_backed_pairs":sum(bool(r["yaml_aliases"]) for r in rows),
                   "changed_other_cells":len(changed),"removed_token_occurrences":sum(len(h["removed_spellings"]) for r in rows for h in r["canonical_occurrences"]),
                   "expected_sidecar_pairs":len(existing_side)+len(selected),"expected_baseline_pairs":0,"receipt_prefix":25,
                   "selected_supported_rows":sum(h["current_disposition"]=="SUPPORTED" for r in rows for h in r["canonical_occurrences"]),
                   "selected_withheld_rows":sum(h["current_disposition"]=="WITHHOLD" for r in rows for h in r["canonical_occurrences"]),
                   "ingredient_yaml_preservation_files":len(all_yaml)},
         "native_checks":{"current_rule_k_with_staged_baseline":len(normal_rejects),"current_rule_k_empty_baseline":len(before_k),"projected_rule_k_empty_baseline":len(after_k),"native_candidate_rule_k_empty_baseline":len(candidate_k),
                          "owner_indexes_equal":True,"all_23_credited_owner_sets_derived_natively":True,"all_23_owner_first_in_label_index":True,
                          "all_candidate_record_inputs_equal_current":source_owner_matches,"native_mapping_receipt_chain":"PASS, 25 links",
                          "companion_mapping_subject_overlap":selected_claim_overlap},
         "projection_contract":{"changed_positions":changed,"only_changed_field":"other","row_count_and_order_unchanged":True,
                                "mapping_dates_source_comments_validation_stamps_unchanged":True,"no_YAML_or_unified_writes":True,
                                "next_receipt":26,"next_receipt_conditional":"Recalculate after verified Step7d merge and fresh main; no receipt created here."},
         "input_sha256":{p:sha(raw) for p,raw in sorted(captured.items())},"all_captured_inputs_unchanged":unchanged,
         "candidate_reuse_limit":"Fresh isolated-current-main native generation captured against this exact canonical preimage; bounded projection and independent replay remain required."}
save("pair-preflight-v2.json",rows)
save("preflight-v2.json",summary)
print(json.dumps({k:v for k,v in summary.items() if k not in {"input_sha256","projection_contract"}},indent=2))
