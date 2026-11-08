import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

O = Path('.temp/w05-final-correction-v1/review-media')
P = Path('.temp/w05-final-correction-v1/media')
R = Path('.temp/w05-final-correction-v1/remediation')
B = Path('reports/all_unmatched_20261107/worker-05')
def load(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x): return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
def write(name, x):
    p=O/name
    assert not p.exists(), p
    p.write_text(json.dumps(x, indent=2, ensure_ascii=False)+'\n')
def diff(a,b,p=''):
    if type(a)!=type(b): return [[p,a,b]]
    if isinstance(a,dict):
        assert set(a)==set(b)
        return [v for k in a for v in diff(a[k],b[k],p+'/'+k)]
    if isinstance(a,list):
        assert len(a)==len(b)
        return [v for i,(x,y) in enumerate(zip(a,b)) for v in diff(x,y,p+'/'+str(i))]
    return [] if a==b else [[p,a,b]]
def verify_manifest(root, expected):
    assert sha(root/'MANIFEST.json')==expected
    m=load(root/'MANIFEST.json')
    rows=m.get('files',m.get('members'))
    for r in rows: assert sha(root/r['path'])==r['sha256'],r['path']
    return len(rows)

at=datetime.now(timezone.utc).isoformat()
verify_manifest(P,'1bec047dc4c2da4b2cd039f150d978522a40a6e2b6115b1448a2a3bd676bf0a1')
verify_manifest(R/'media-report-v2','594011f10c33e2699e4d5d35c495bc6caf8818f05c3e067d7dd0af06ba06e295')
verify_manifest(R/'media-report-v3','5c70d97cc97b3e84821043435290d0e0a5e9a2c539c189cf2c7bce27a2cc7e9d')
changes=[]
for name,key in [('decisions.json','decisions'),('primary-read-ledger.json','cases')]:
    before=load(R/'media-report-v2'/name);after=load(R/'media-report-v3'/name)
    ds=diff(before,after)
    assert len(ds)==2
    indices={159,174}
    for pointer,old,new in ds:
        i=int(pointer.split('/')[2]);assert after[key][i]['case_index'] in indices
        assert pointer.endswith('/assessment')
        assert '1708' in old and '1708' not in new and '1999' in new
        indices.remove(after[key][i]['case_index'])
    assert not indices
    changes.append(dict(path=name,before_sha256=sha(R/'media-report-v2'/name),after_sha256=sha(R/'media-report-v3'/name),differences=ds))
source=B/'media/captures/8accfcb3006f5d17f6.html'
assert sha(source)=='8d4826c05e6536bd55e98c7f2642eba20feb02d2f8128f175cf610dbaacb4999'
assert 'Ingredient ID: 1999' in source.with_suffix('.txt').read_text()
write('metadata-remediation-rereview-v2.json',dict(reviewer='/root/final_skeptical',metadata_author='/root',at=at,finding_id='W05-FINAL-MEDIA-REVIEW-03',manifest_sha256=sha(R/'media-report-v3/MANIFEST.json'),verdict='resolved_in_exact_immutable_metadata_successor',differences=changes,primary_source=dict(path=str(source),sha256=sha(source)),assessment='The exact ingredient page identifies 1999, and JCM1111 names LB broth powder25g. This is a correction to the case174 source caption and case159 comparator caption only. No supplier or Lennox equivalence follows; their unresolved relationship remains intact.',retained_v2_findings=['W05-FINAL-MEDIA-REVIEW-01','W05-FINAL-MEDIA-REVIEW-02'],sealed_media_members_still_exact=True,payloads_unchanged=True))

r=load(O/'scientific-review-v1.json')
assert sha(O/'scientific-review-v1.json')=='c044d5f8e492ace6312682f459337dce96a6e91ebf9bba6f3239ff778d5e4823'
r['at']=at
r['predecessor_review']=dict(path='scientific-review-v1.json',sha256=sha(O/'scientific-review-v1.json'),preserved=True)
r['selected_inputs']['report_metadata_manifests']=[dict(path=str(R/v/'MANIFEST.json'),sha256=sha(R/v/'MANIFEST.json')) for v in ['media-report-v2','media-report-v3']]
del r['selected_inputs']['report_metadata_manifest']
r['selected_inputs']['decisions']=dict(path=str(R/'media-report-v3/decisions.json'),sha256=sha(R/'media-report-v3/decisions.json'))
r['selected_inputs']['report_file_selection']='media-report-v3 decisions/primary-read-ledger; media-report-v2 finding-dispositions/mapping-evidence-typing/SUPERSEDING-MEDIA-REPORT; original sealed media proposals/evidence/payloads unchanged.'
dmap={x['case_id']:x for x in load(R/'media-report-v3/decisions.json')['decisions']}
evidence={x['evidence_id']:x for x in load(P/'evidence.json')['evidence']}
byproposal={x['proposal_id']:x for x in r['payload_reviews']}
extras={97:['MEDIA-ARCHIVE-M2996','M1193-DIRECT-30'],110:['MEDIA-P070','MEDIA-P072'],177:['MEDIA-P070','MEDIA-P072']}
for c in r['case_reviews']:
    d=dmap[c['case_id']]
    c['selected_decision_object_sha256']=objsha(d)
    ids=set(extras.get(c['case_index'],[]))
    for pid in c['proposal_ids']: ids.update(x['evidence_id'] for x in byproposal[pid]['primary_sources'])
    c['primary_sources']=[dict(evidence_id=k,capture=evidence[k]['capture'],url=evidence[k].get('url'),original_accessed_at=evidence[k].get('accessed_at')) for k in sorted(ids)]
for x in r['new_findings']:
    if x['finding_id']=='W05-FINAL-MEDIA-REVIEW-03': x['status']='resolved_by_root_report_metadata_v3'
r['verdict']='all60_cases_and45_complete_payloads_scientifically_reviewed; all3_new_report_findings_fixed_and_rereviewed; no_source_owner_or_export_approval'
for q in r['payload_reviews']: assert sha(B/q['after_capture']['path'])==q['full_payload_sha256']
write('scientific-review-v2.json',r)

read_rows=[json.loads(x) for x in (O/'primary-text/read-index.jsonl').read_text().splitlines()]
unique={}
for row in read_rows:
    key=(row['evidence_id'],row['sha256'],row['text_sha256'])
    assert sha(Path(row['source_path']))==row['sha256']
    assert sha(Path(row['text_path']))==row['text_sha256']
    unique[key]=row
semantic_ids={s['evidence_id'] for c in r['case_reviews'] for s in c['primary_sources']}
assert semantic_ids <= {x['evidence_id'] for x in unique.values()}
authority_paths=[Path('MAPPING_SEMANTICS.md'),Path('.claude/skills/add-media/SKILL.md'),Path('.claude/skills/review-yaml-category/SKILL.md'),Path('docs/record-reviews.md'),Path('docs/record-review-profile.md')]
authority_paths += [B/'final-correction-v1/inputs'/p for p in ['authorization/AUTHOR-TASK.md','authorization/TRIAGE.json','external-w08-review/native/review.yaml','provenance-audit-w02/HANDOFF.md','provenance-audit-w02/provenance/native-type-suggestions-v1.json']]
authority_paths += [P/'captures'/p for p in ['comments-1193.json','comments-1208.json','comments-1226.json']]
write('review-read-ledger-v1.json',dict(reviewer='/root/final_skeptical',at=at,authority_and_review_inputs=[dict(path=str(p),sha256=sha(p)) for p in authority_paths],primary_extractions=list(unique.values()),scientifically_used_evidence_ids=sorted(semantic_ids),metadata_correction_source=dict(path=str(source),sha256=sha(source)),methods=['Read complete selected YAML claims and compared all predecessor changes plus historical prefixes independently.','Read exact frozen raw cases, recipe contexts and selected primary formula/instruction passages; scientific assessments and applicability are per case/payload in scientific-review-v2.json.','Verified every483 original/new referenced capture hash, all45 payload hashes and58 recipe hashes; byte verification by itself is not scientific applicability approval.','PDF/HTML/JSON decoded text supports the actual reads. Entire-book extraction is not a claim that irrelevant book pages were scientifically reviewed.','No new network retrieval, paid provider, maintained-data edit, GitHub write, owner application or export approval was performed.'],counts=dict(extraction_events=len(read_rows),unique_extractions=len(unique),scientifically_used_primary_evidence_ids=len(semantic_ids))))

hand=f'''Independent media scientific review sealed by /root/final_skeptical.

All 60 assigned cases, 45 complete selected payloads and 59 contextual occurrence bindings are reviewed in scientific-review-v2.json. The actual primary author is /root/media_research; /root authored only the later report-metadata corrections. This reviewer authored neither. The original source head remains 43f7cf6e8681fa617b5d6d3529d94d537ca01f0d.

The three original findings W05-MEDIA-F01/F02/F03 are resolved within the selected report-only scope: Marine active evidence corrected with full prior history preserved; all five EMJH basal quantities/basis/adjustment footnote supported; unrelated EPA bytes retained as unsuccessful evidence and removed from positive links. All 39 new MappingEvidence retypings were independently checked against the exact W02 entry matrix and actual authorship history. Inherited MANUAL_CURATION objects remain unchanged without authenticating their original supplier; ComponentEvidence enums are separate.

Three additional report findings were reported before correction, preserved in new-findings-v1/v2.json, fixed by root and independently rereviewed. Findings01/02 use media-report-v2; finding03 uses media-report-v3. These remove unsupported human attribution, correct the EMJH printed-page locator to302 and correct the LB comparator/source caption to mediadive.ingredient:1999. All 45 YAMLs remain identical to the sealed media packet. Earlier review versions remain immutable.

Exact selected media manifest: 1bec047dc4c2da4b2cd039f150d978522a40a6e2b6115b1448a2a3bd676bf0a1.
Root metadata v2 manifest: 594011f10c33e2699e4d5d35c495bc6caf8818f05c3e067d7dd0af06ba06e295.
Root metadata v3 manifest: 5c70d97cc97b3e84821043435290d0e0a5e9a2c539c189cf2c7bce27a2cc7e9d.
Final scientific receipt SHA256: {sha(O/'scientific-review-v2.json')}.

All source-specific holds, unresolved existing-owner relationships, raw names/occurrences and coordinator reconciliation obligations remain. This accepts the scientific correctness of the report-only media scope with those limits. It grants no whole-owner application, source matching admission or export approval. Root's canonical188-case assembly and full native overlay validation were not supplied to this review and are not claimed to pass. A later assembly review must bind those exact bytes.

Reproduction is in the byte/delta audit, typing audit, owner inventory, per-case/per-payload scientific receipt, exact primary-read ledger and metadata rereviews. MANIFEST.json seals every file under this review directory except itself. Publishable references may be copied byte-for-byte under final-correction-v1/review-media/ relative to reports/all_unmatched_20261107/worker-05. No commits or GitHub changes were made by this reviewer.
'''
assert not (O/'HANDOFF.md').exists()
(O/'HANDOFF.md').write_text(hand)
members=[dict(path=str(p.relative_to(O)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
write('MANIFEST.json',dict(reviewer='/root/final_skeptical',at=at,files=members,scientific_receipt='scientific-review-v2.json',handoff='HANDOFF.md',scope=r['scope']))
print(json.dumps({n:sha(O/n) for n in ['MANIFEST.json','HANDOFF.md','scientific-review-v2.json','metadata-remediation-rereview-v2.json','review-read-ledger-v1.json']},indent=2))
