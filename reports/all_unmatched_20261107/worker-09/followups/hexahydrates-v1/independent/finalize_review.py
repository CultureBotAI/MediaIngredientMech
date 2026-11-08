"""Bind the completed independent two-case review; writes only this directory."""
from pathlib import Path
import json, hashlib, datetime, shutil, subprocess, yaml

HERE=Path(__file__).resolve().parent
FOLLOWUP=HERE.parent
REPO=next(p for p in HERE.parents if (p/'MAPPING_SEMANTICS.md').exists())
ART=FOLLOWUP.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canonical=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
digest=lambda x:hashlib.sha256(canonical(x)).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cases=json.loads((FOLLOWUP/'cases.json').read_bytes())['cases']
decisions=json.loads((FOLLOWUP/'decisions.json').read_bytes())['decisions']
associations=json.loads((FOLLOWUP/'existing-owner-associations.json').read_bytes())['associations']
evs=json.loads((FOLLOWUP/'evidence.json').read_bytes())['evidence']
declared=json.loads((FOLLOWUP/'scientific-payload-hashes.json').read_bytes())
lineage=json.loads((FOLLOWUP/'provenance/source-associations.json').read_bytes())['associations']
assert len(cases)==len(decisions)==len(associations)==2
assert sha(FOLLOWUP/'existing-owner-associations.json')==declared['association_file_sha256']
assert sha(FOLLOWUP/'evidence.json')==declared['evidence_file_sha256_before_peer_attachment']
ev={x['evidence_id']:x for x in evs}
for e in evs:
    assert e['capture']['root']=='artifact'
    p=ART/e['capture']['path']
    assert p.is_file() and not p.is_symlink() and sha(p)==e['capture']['sha256'],e['evidence_id']
for p in [FOLLOWUP/'provenance/PROVENANCE-MANIFEST.json']:
    for x in json.loads(p.read_bytes())['files']:
        f=p.parent/x['path'];assert f.stat().st_size==x['bytes'] and sha(f)==x['sha256']
oldpath='reports/all_unmatched_20261107/worker-09/decisions.json'
oldbytes=subprocess.check_output(['git','show','d74ab6d48f6345260087cf973cadbe7b6269109f:'+oldpath],cwd=REPO)
assert oldbytes==(REPO/oldpath).read_bytes()
old=json.loads(oldbytes)['decisions'];assert len(old)==187
final=HERE/'final-primary-inputs';final.mkdir(exist_ok=True)
for name in ['cases.json','acceptance.json','decisions.json','existing-owner-associations.json','evidence.json','scientific-payload-hashes.json']:
    shutil.copyfile(FOLLOWUP/name,final/name)

reviews=[]
for c,d,a,l in zip(cases,decisions,associations,lineage):
    assert c['case_id']==d['case_id']==a['case_id']==l['case_id']
    assert digest(c)==d['case_input_sha256']==a['case_input_sha256']
    assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
    assert a['source_record']==c['original_kg_entry']['source_record']==l['source_row']
    assert a['source_locator']==l['locator']
    assert a['source_response_sha256']==l['body_sha256']
    assert a['association_id']==d['source_association_id']
    assert d['proposal_ids']==[] and a['after_capture'] is None and a['maintained_mutation'] is False
    assert a['global_alias_activation'] is False and a['export_approval'] is False
    assert d['retained_holds']==a['retained_holds'] and d['retained_holds']['whole_owner_export_disposition']=='WITHHOLD'
    assert d['evidence_ids']==a['evidence_ids']
    assert all(c['case_id'] in ev[e]['case_ids'] for e in d['evidence_ids'])
    assert d['disposition']=='existing_identity_or_alias' and d['missing_requirement'] is None
    assert next(z for z in old if z['case_id']==c['case_id'])['disposition']=='unresolved'
    for ow in d['owner_records']:assert sha(REPO/ow['path'])==ow['sha256']
    owner=yaml.safe_load((REPO/a['owner_path']).read_bytes())
    assert sha(REPO/a['owner_path'])==a['before_sha256']
    assert owner['mapping_status']=='MAPPED' and owner['identifier']==a['identifier']
    assert owner['chemical_properties']['cas_rn']==a['cas_rn']
    assert any(s['synonym_text']==c['raw_source_label'] and s['synonym_type']=='RAW_TEXT' for s in owner['synonyms'])
    science=digest({k:v for k,v in d.items() if k!='independent_review'})
    assert science==declared['case_hashes'][c['case_id']]
    cobalt=a['source_id'].endswith(':38')
    reviews.append(dict(case_id=c['case_id'],source_id=c['source_case_id'],raw_source_label=c['raw_source_label'],case_input_sha256=digest(c),scientific_payload_sha256=science,association_id=a['association_id'],association_canonical_sha256=digest(a),review_status='complete',result='supported exact source-specific association with retained gates',scientific_reasoning=('The first producer-selected cobalt row is exactly medium14/SL-4 row6, reconstructed through catalogue order and verified against retained original response bytes. The original recipe witness explicitly names CoCl2 six-water reagent; ChEBI53503 defines cobalt:chloride:water1:2:6 with CAS7791-13-1. Current automatic parent annotations and parent-derived mmol_l do not override that source form. The existing active owner already retains the raw label; its generic hydrate and water1/7 synonyms and provisional role remain outside this source association.' if cobalt else 'The first producer-selected nickel row is exactly medium14/SL-4 row8, reconstructed through catalogue order and verified against retained original response bytes. The original recipe witness explicitly names NiCl2 six-water reagent; ChEBI53542 defines nickel:chloride:water1:2:6 with CAS7791-20-0. Issue344 itself warns that this genuine hydrate can carry anhydrous metadata; the group distribution reinforces that warning without proving a backend mechanism. Existing owner association is supported while the full row, roles and rejected legacy records remain held.'),source_scope=dict(original_response_sha256=l['body_sha256'],original_observed_at=l['observed_at'],original_json_pointer=l['json_pointer_in_original_response'],medium_id=14,solution_id=20,recipe_order=a['source_locator']['recipe_order'],not_all_occurrences_of_ingredient_id=True),evidence_ids_reviewed=d['evidence_ids'],retained_holds=d['retained_holds'],review_findings=['HX-SR-01','HX-SR-02'],export_approval=False,maintained_mutation=False))

for eid,cid in [('hx-ingredient-38',cases[0]['case_id']),('hx-page-38',cases[0]['case_id']),('hx-group-Co',cases[0]['case_id']),('hx-ingredient-40',cases[1]['case_id']),('hx-page-40',cases[1]['case_id']),('hx-group-Ni',cases[1]['case_id'])]:
    assert ev[eid]['case_ids']==[cid]
rr=json.loads((HERE/'primary-replay-rerun.json').read_bytes())
assert rr['status']=='PASS' and rr['script_sha256']==sha(FOLLOWUP/'provenance/replay_lineage.py')
assert rr['source_associations_sha256']==sha(FOLLOWUP/'provenance/source-associations.json')
own=json.loads((HERE/'independent-lineage-replay.json').read_bytes())
assert own['status']=='PASS' and own['source_associations_sha256']==rr['source_associations_sha256']
initial=HERE/'initial-primary-inputs/evidence.json'
findings=[dict(finding_id='HX-SR-01',severity='P2',scope='Evidence applicability only; scientific decisions and owner associations unchanged',status='resolved',problem='Six element-specific evidence entries declared both case IDs although their captures concerned only cobalt or nickel.',resolution='Primary author narrowed case_ids for ingredient/page/group entries to their corresponding exact case.',rereview='Compared all six final evidence entries and both decision reference lists; no cross-element applicability remains.',initial_evidence_sha256=sha(initial),final_evidence_sha256_before_peer_attachment=sha(FOLLOWUP/'evidence.json')),
dict(finding_id='HX-SR-02',severity='P2',scope='Capture integrity after primary provenance script finalization',status='resolved',problem='The evidence ledger initially pinned the earlier replay-validation receipt after its author finalized source-manifest checks and changed the receipt bytes.',resolution='Primary author refreshed the lineage-validation capture hash after the provenance bundle froze.',rereview='Final capture hashes and complete provenance manifest validated; finalized replay script independently rerun without writes and returned PASS.',final_script_sha256=rr['script_sha256'],final_replay_validation_sha256=sha(FOLLOWUP/'provenance/replay-validation.json'))]
receipt=dict(schema_version=1,review_status='complete',reviewer='/root/materials',primary_scientific_author='/root',primary_provenance_author='/root/antibiotics',completed_at=now,scope='Only the two exact frozen source cases and proposed existing-owner associations; no broader hydrate family, all-use source-ID or whole-owner release assessment',resulting_association_status='SUPPORTED for exact source cases after separate skeptical review; all stated publication and routing gates retained',reviewed_author_draft_status='proposed source associations pending separate skeptical review',author_draft_status_interpretation='Historical primary-author draft status is preserved byte-for-byte; this independent receipt supplies the completed review outcome without rewriting the reviewed association payload.',published_parent='d74ab6d48f6345260087cf973cadbe7b6269109f',input_hashes={n:sha(FOLLOWUP/n) for n in ['cases.json','acceptance.json','decisions.json','existing-owner-associations.json','evidence.json','scientific-payload-hashes.json','provenance/source-associations.json','provenance/PROVENANCE-MANIFEST.json','provenance/replay_lineage.py']},evidence_file_sha256_before_peer_attachment=sha(FOLLOWUP/'evidence.json'),association_file_sha256=sha(FOLLOWUP/'existing-owner-associations.json'),scientific_hash_method='SHA256 canonical JSON sort_keys=True,separators=(comma,colon),ensure_ascii=False,allow_nan=False; excludes only independent_review from each decision',case_reviews=reviews,findings=findings,open_findings=[],owner_mutation_proposal_count=0,source_association_count=2,validation=dict(status='PASS',evidence_capture_count=len(evs),candidate_owner_count=9,all_evidence_hashes_verified=True,all_provenance_manifest_members_verified=True,original187_decisions_byte_identical_to_parent=True,all_case_and_scientific_hashes_verified=True,all_source_association_links_verified=True,final_provenance_script_readonly_rerun=rr,independent_selection_implementation_capture=dict(path='independent/independent-lineage-replay.json',sha256=sha(HERE/'independent-lineage-replay.json'))),independent_work=['Read full issue344 body and both comments, prior published decisions and nine current owner files.','Fresh official ingredient38/40 REST and webpage captures and cobalt/nickel group pages independently verified automatic-matching disclaimer and shared parent annotations.','Fresh official DSMZ14 PDF independently retrieved; exact bytes equal primary author capture and table explicitly states both six-water reagents.','Independently implemented catalogue-first traversal and compared all1214 compound and5442 solution values and insertion order; both selected rows match exact frozen cases and retained original body.','Read producer catalogue/acquisition/extraction code and independently reran final pure-extraction plus manifest/body/ledger validation without --write.','Verified exact ChEBI1:2:6 definitions, CAS numbers and current active owners; kept stock preparation and dissolved-species scope separate.'],limitations=['The recipe asserts supplied reagent form; this is not analytical verification of a physical supplier lot.','The broad/group-level automatic annotation interpretation is an evidence-supported inference; exact backend assignment of each field is not proven.','PDF and provider API are related source-lineage views, not independent chemical replicates.','Identical source row values occur in other recipes; producer ordering, not value matching, reconstructs the selected frozen source provenance.','No full production acquisition validator, SQLite-cache deserialization, downstream rebuild, maintained mutation, alias activation, hold edit or global source-ID routing was performed.','Original source body observed_at remains2026-11-05; fresh PDF and reviewer capture times are separately recorded.','All185 other campaign source decisions and atypical hydrate families are outside this reassessment.'],release_approval=False)
(HERE/'review-final.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(review_final_sha256=sha(HERE/'review-final.json'),scientific_hashes={r['case_id']:r['scientific_payload_sha256'] for r in reviews},association_file_sha256=receipt['association_file_sha256'],evidence_before_peer_sha256=receipt['evidence_file_sha256_before_peer_attachment'],open_findings=0),indent=2))
