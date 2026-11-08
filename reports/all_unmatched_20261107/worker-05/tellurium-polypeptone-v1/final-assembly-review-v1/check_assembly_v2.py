from pathlib import Path
import json,hashlib,datetime
import yaml
r=Path('.temp/w05-tellurium-polypeptone-v1/final-assembly-review-v1');p=Path('reports/all_unmatched_20261107/worker-05/tellurium-polypeptone-v1');b=p.parent/'postseal-source-corrections-v1';C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');B=p.parent
n=Path('reviews/structured/20261108T091207Z-worker05-tellurium-polypeptone-supplement')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def osh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(f):return json.loads(f.read_text())
def bind(f):return {'path':str(f),'sha256':sha(f)}
D=read(p/'core/decisions.json')['decisions'];P=read(p/'core/proposals.json')['proposals'];E=read(p/'core/evidence.json')['evidence'];baseD={x['case_id']:x for x in read(b/'core/decisions.json')['decisions']};baseP={x['proposal_id']:x for x in read(b/'core/proposals.json')['proposals']};baseE={x['evidence_id']:x for x in read(b/'core/evidence.json')['evidence']};dm={d['case_id']:d for d in D};pm={d['proposal_id']:d for d in P};em={d['evidence_id']:d for d in E}
assert len(dm)==len(D)==188;assert len(pm)==len(P)==142;assert len(em)==len(E)==1627;assert set(dm)==set(baseD);assert all(em[k]==v for k,v in baseE.items());assert len(baseE)==1551
peer=read(p/'review/main-review.json');cases={x['case_id']:x for x in peer['case_reviews']};payloads={x['proposal_id']:x for x in peer['payload_reviews']};canonical=[]
for lane,df,pf,ef in [('tellurium','decisions.json','proposals.json','evidence.json'),('polypeptone','decisions-v2.json','proposals-v2.json','evidence-v2.json')]:
 for authored in read(p/lane/df)['decisions']:
  final=dm[authored['case_id']];changed={k for k in final if final[k]!=authored.get(k)};assert changed=={'evidence_ids','independent_review','previous_supplement_independent_review','tellurium_polypeptone_assembly_provenance'}
  assert final['evidence_ids']==authored['evidence_ids']+['W05-TELLURIUM-POLYPEPTONE-INDEPENDENT-REVIEW'];assert final['independent_review']['reviewer']=='/root/final_skeptical';assert final['previous_supplement_independent_review']==baseD[authored['case_id']]['independent_review'];assert osh(authored)==cases[authored['case_id']]['selected_decision_object_sha256'];assert final['tellurium_polypeptone_assembly_provenance']['selected_decision_object_sha256']==osh(authored)
  canonical.append({'case_id':final['case_id'],'authored_sha256':osh(authored),'canonical_sha256':osh(final),'root_changed_fields':sorted(changed),'scientific_fields_exact':True,'authored_scientific_review':cases[final['case_id']]['conclusion']})
 for x in read(p/lane/pf)['proposals']:assert pm[x['proposal_id']]==x;assert osh(x)==payloads[x['proposal_id']]['selected_proposal_object_sha256']
 for x in read(p/lane/ef)['evidence']:assert em[x['evidence_id']]==x
assert sum(d==baseD[d['case_id']]for d in D)==185
holdkeys=['case_input_sha256','source','occurrence_ids','disposition','proposal_ids','owner_records','preserved_downstream_holds','preserved_source_holds']
assert all(all(d.get(k)==baseD[d['case_id']].get(k)for k in holdkeys)for d in D)
assert sum(x['after_capture']==baseP[x['proposal_id']]['after_capture']for x in P)==141
capturechecks=[];cache={}
for x in E:
 cap=x['capture'];f=(B if cap['root']=='artifact' else C)/cap['path'];assert cap['root']in ['artifact','source'];actual=cache.setdefault(str(f),sha(f));assert actual==cap['sha256'],f;capturechecks.append({'evidence_id':x['evidence_id'],'capture':cap,'actual_sha256':actual})
for x in P:
 cap=x['after_capture'];assert sha(B/cap['path'])==cap['sha256']
reg=read(p/'finding-register.json');oldreg=read(b/'finding-register.json');assert reg['original_findings']==oldreg['original_findings'];assert len(reg['original_findings'])==18
native=yaml.safe_load((n/'review.yaml').read_text());assert native['verdict']=='needs_curation';assert native['scope']['population_size']==5;assert len(native['targets'])==5;assert len(native['assessments'])==5
for x in native['source']['inputs']:assert sha(Path(x['path']))==x['sha256']
for x in native['evidence']:assert sha(Path(x['reference']))==x['snapshot_sha256']
for x in native['assessments']:
 details=json.loads(x['details']);target=x['target_ids'][0];expect=cases[details['case_id']]if target.startswith('CASE-')else payloads[target];assert details==expect;assert x['summary']==expect['assessment']
f=native['findings'][0];assert len(native['findings'])==1 and f['finding_id']=='POLYPEPTONE-001'and f['status']=='open'and f['severity']=='major';assert f['issue_key']=='polypeptone-registry-proposal-omits-supported-parent';assert f['target_ids']==['W05-FINAL-MAT-030']
overlay=read(p/'validation/full-overlay/native-validation.json');assert overlay['status']=='PASS';assert overlay['candidate_payloads']==142;assert overlay['overlay_records']==3029;assert not overlay['errors'];assert sha(p/'core/proposals.json')==sha(p/'validation/input-proposals.json')==overlay['inputs']['proposals']['sha256'];assert len(overlay['guarded_payloads'])==142
for i,x in enumerate(overlay['guarded_payloads']):
 assert x['selected_capture']==pm[x['proposal_id']]['after_capture']
 gf=p/'validation/full-overlay/guarded-readback'/f"{i:03d}-{Path(x['destination_owner_path']).name}"
 assert sha(gf)==x['guarded_readback_sha256'];assert yaml.safe_load(gf.read_text())==yaml.safe_load((B/x['selected_capture']['path']).read_text())
strict=read(p/'validation/full-strict/receipt.json');assert strict['exit_code']==0 and strict['payloads']==142
struct=read(p/'validation/final-structural-audit.json');assert struct['structural_accounting']=='PASS';assert not struct['out_of_scope_shard_case_ids'];assert struct['accounted_case_count']==188
rows=read(p/'validation/native-row-projections.json');ownpoly=read(p/'review/independent-polypeptone-native-v1.json');owntel=read(p/'review/independent-tellurium-native-v1.json')
print('root projection element keys',[(x.get('proposal_id'),list(x))for x in rows['reviewed_projections']])
out={'reviewer':'/root/final_skeptical','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_CURRENT_ASSEMBLY_BINDINGS','scope':'Exact compiled scientific field preservation, full evidence/payload hashes, native assessment attribution and source-scope checks. Full scientific review remains separately sealed; final preservation child and retained native-check completion still pending at this receipt.','canonical_files':[bind(p/x)for x in ['core/decisions.json','core/proposals.json','core/evidence.json','core/proposal-lineage.json','core/assembly-receipt.json','finding-register.json','final-counts.json','source-ledger.json','README.md']],'native_files':[bind(n/'review.yaml'),bind(n/'review.md')],'canonical_case_reviews':canonical,'counts':{'cases':len(D),'occurrence_memberships':sum(len(x['occurrence_ids'])for x in D),'proposals':len(P),'evidence':len(E),'old_evidence_objects_exact':len(baseE),'unchanged_decisions':185,'unchanged_payloads':141,'original_finding_objects_retained':18},'all_case_source_hold_objects_exact':True,'all_selected_fragments_preserved_exactly_except_documented_case_review_envelope':True,'all1627_evidence_capture_bindings':capturechecks,'all142selected_payload_hashes_verified':True,'native_scope':'Exactly3case snapshot rows and2complete payloads. Every assessment summary/details equals the separately authored skeptical receipt; root identified self_review compiler, not independent scientist. Open major POLYPEPTONE001 targets onlyMAT030; no wholeunion supersession. UnchangedHipolypepton projection is context only.','native_checks':'Reviewed root complete142 guarded/strict3029 path-keyed overlay and exactinputP byteequality; no newpartonomy, filename or identifiercollisions; no schema success translated into scientific admission.','readme_assessment':'Complete README read. Counts independently agree. Current Tellurium versus historical projection, nested stock quantities, conditional MICRO/FOODON source scope, historical135versus150context distinction and actual scientist attributions are accurate. Finalpublishedhead correctly deferred to postpushhandoff.','open_report_index_finding':'W05-TELLURIUM-POLYPEPTONE-ASSEMBLY-001 awaiting appended selected-origin clarification; no canonical scientific defect identified.'}
f=r/'assembly-checks-v1.json';assert not f.exists();f.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('receipt',sha(f))
