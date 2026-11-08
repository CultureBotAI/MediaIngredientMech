import pathlib,json,hashlib,datetime,copy
S=pathlib.Path('.temp/w05-buffer-parts-v1');P=pathlib.Path('reports/all_unmatched_20261107/worker-05/buffer-parts-v1');R=S/'final-assembly-review-v1'
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def oh(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
old=j(P/'control/pre-evidence-envelope-core/evidence.json');new=j(P/'core/evidence.json');adapt=j(P/'control/evidence-envelope-adaptation.json');finding=j(S/'control/evidence-kind-finding-before-fix.json')
assert len(old['evidence'])==len(new['evidence'])==1767
assert old['evidence'][:1627]==new['evidence'][:1627]
expected={'W05-BUFFER-TRIS-ASSESSMENT':'source_review','W05-BUFFER-TRIS-CHRONOLOGY':'provenance_review','W05-BUFFER-TRIS-FILING':'issue_context','W05-PARENTS-TOMBSTONE-BEFORE':'owner_record'}
changed=[]
for a,b in zip(old['evidence'],new['evidence']):
 assert a['evidence_id']==b['evidence_id']
 if a==b:continue
 eid=a['evidence_id'];assert eid in expected and a['kind']==expected[eid]
 c=copy.deepcopy(b);assert c.pop('original_campaign_kind')==a['kind'];assert c['kind']=='source_snapshot';c['kind']=a['kind'];assert c==a
 capture=pathlib.Path('reports/all_unmatched_20261107/worker-05')/b['capture']['path'];assert sha(capture)==b['capture']['sha256']
 change=next(x for x in adapt['changes']if x['evidence_id']==eid);assert change['before']==a and change['after']==b
 changed.append({'evidence_id':eid,'before_object_sha256':oh(a),'after_object_sha256':oh(b),'original_kind':a['kind'],'selected_kind':b['kind'],'capture':b['capture'],'all_other_fields_identical':True,'assessment':'Correct source_snapshot classification for the exact captured author assessment, chronology, filing context or authentic rejected-owner beforeimage. Neither primary scientific authority nor human MappingEvidence is inferred; exact claim, author, locator and available original timestamps are unchanged.'})
assert {x['evidence_id']for x in changed}==set(expected)
assert sha(P/'control/pre-evidence-envelope-core/evidence.json')==finding['reproduction']['core_evidence_sha256']
for name in ['decisions','proposals','proposal-lineage']:
 assert (P/f'core/{name}.json').read_bytes()==(P/f'control/pre-evidence-envelope-core/{name}.json').read_bytes()
out={'reviewer':'/root/final_skeptical','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'finding_id':'W05-ASSEMBLY-EVIDENCE-003','disposition':'RESOLVED_EXACT_FOUR_CANONICAL_ENVELOPES','inputs':[bind(p)for p in [S/'control/evidence-kind-finding-before-fix.json',P/'control/evidence-envelope-adaptation.json',P/'control/pre-evidence-envelope-core/evidence.json',P/'core/evidence.json',S/'review/FINAL-MANIFEST-v1.json']],'entry_reviews':changed,'unchanged_old_evidence_objects':1627,'unchanged_new_other_evidence_objects':136,'unchanged_full_payloads_and_decisions':True,'sealed_author_fragments_preserved':True,'scope':'Canonical report-envelope adaptation only. Main exact21D/35P scientific review remains attributed to its original selected fragment bytes. Final wrapper/native review follows separately; no MappingEvidence/ComponentEvidence enum, payload, source, gate or maintained record change approved.'}
q=R/'evidence-envelope-rereview-v1.json';assert not q.exists();q.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(bind(q)))
