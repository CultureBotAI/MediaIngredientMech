import pathlib,json,hashlib,copy,datetime
S=pathlib.Path('.temp/w05-buffer-parts-v1');P=pathlib.Path('reports/all_unmatched_20261107/worker-05/buffer-parts-v1');B=P.parent;R=S/'final-assembly-review-v1';C=S/'control/composed-final-v5'
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def oh(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
old=j(P/'control/pre-evidence-envelope-core/evidence.json');middle=j(P/'control/pre-capture-access-core/evidence.json');new=j(P/'core/evidence.json');assert len(old['evidence'])==len(middle['evidence'])==len(new['evidence'])==1767
changes=[]
for oldcore,newcore,ap,fp,expected,mode in [(old,middle,P/'control/evidence-envelope-adaptation.json',S/'control/evidence-kind-finding-before-fix.json',4,'kind'),(middle,new,P/'control/capture-access-adaptation.json',S/'control/evidence-access-finding-before-fix.json',3,'access')]:
 a=j(ap);f=j(fp);dd=[]
 for x,y in zip(oldcore['evidence'],newcore['evidence']):
  assert x['evidence_id']==y['evidence_id']
  if x==y:continue
  e=x['evidence_id'];z=copy.deepcopy(y)
  assert z.pop('original_campaign_kind')==x['kind'];assert z['kind']=='source_snapshot';z['kind']=x['kind']
  if mode=='access':
   assert z.pop('original_source_url')==x['url'];assert z['url'] is None;z['url']=x['url'];assert 'none inferred' in z.pop('capture_access_scope')
  assert z==x
  item=next(v for v in a['changes']if v['evidence_id']==e);assert item['before']==x and item['after']==y
  assert sha(B/y['capture']['path'])==y['capture']['sha256']
  dd.append({'evidence_id':e,'before_object_sha256':oh(x),'after_object_sha256':oh(y),'capture':y['capture'],'assessment':'Exact captured document, claims, locator and actual attribution remain unchanged. Canonical source_snapshot describes retained author/context/beforeimage documents or reused source-document snapshots without claiming new network acquisition. Original type and, where applicable, URL are explicitly preserved. Unknown original acquisition time is not guessed or replaced by failed-shell/local-read time. No MappingEvidence enum, primary interpretation or scientific payload changes.'})
 assert len(dd)==expected and len(a['changes'])==expected
 assert oldcore['evidence'][:1627]==newcore['evidence'][:1627]
 changes.append({'finding_id':f['finding_id'],'disposition':'RESOLVED_EXACT_CANONICAL_METADATA','adaptation':bind(ap),'before_finding':bind(fp),'entry_reviews':dd})
# Complete canonical decisions unwrap exactly to the science-reviewed composition.
science=j(S/'review/main-review.json');sdi={x['case_id']:x for x in science['case_reviews']};cdi={x['case_id']:x for x in j(C/'decisions.json')['decisions']};di={x['case_id']:x for x in j(P/'core/decisions.json')['decisions']};oi={x['case_id']:x for x in j(B/'tellurium-polypeptone-v1/core/decisions.json')['decisions']};ar=j(P/'core/assembly-receipt.json');dchecks=[]
for cid,d in di.items():
 if cid not in sdi:assert d==cdi[cid]==oi[cid];continue
 b=copy.deepcopy(d)
 assert b.pop('previous_consolidated_independent_review')==oi[cid]['independent_review']
 prov=b.pop('consolidated_assembly_provenance');assert prov['selected_decision_object_sha256']==oh(cdi[cid])==sdi[cid]['selected_decision_object_sha256'];assert prov['predecessor_decision_object_sha256']==oh(oi[cid])
 rv=b['independent_review'];assert rv['status']=='complete' and rv['reviewer']=='/root/final_skeptical' and rv['evidence_ids']==['W05-CONSOLIDATED-INDEPENDENT-REVIEW'];assert 'holds' in rv['scope']
 b['independent_review']=cdi[cid]['independent_review'];b['evidence_ids'].remove('W05-CONSOLIDATED-INDEPENDENT-REVIEW');assert b==cdi[cid]
 dchecks.append({'case_id':cid,'scientifically_reviewed_object_sha256':oh(cdi[cid]),'canonical_object_sha256':oh(d),'assessment':'Canonical wrapper adds only exact current peer attribution/evidence and authentic predecessor scope. Complete source fields, occurrences, case disposition and every authored source/owner/role/export limitation equal the independently scientifically reviewed composed object after removing this explicit wrapper.'})
assert len(dchecks)==21 and len(di)==188
for n in ['proposals','proposal-lineage']:
 assert (P/f'core/{n}.json').read_bytes()==(C/f'{n}.json').read_bytes()
peers=[x for x in new['evidence']if x['evidence_id']=='W05-CONSOLIDATED-INDEPENDENT-REVIEW'];assert len(peers)==1
peer=peers[0];assert peer['capture']['sha256']==sha(S/'review/main-review.json')==sha(B/peer['capture']['path']);assert peer['reviewer']==science['reviewer'];assert peer['accessed_at']==science['completed_at'];assert set(peer['case_ids'])==set(sdi)
composed=j(C/'evidence.json')['evidence'];back=copy.deepcopy(new['evidence']);back.pop()
assert len(back)==len(composed)==1766
changed_ids={v['evidence_id']for c in changes for v in c['entry_reviews']}
for x,y in zip(composed,back):assert x==y or x['evidence_id'] in changed_ids
manifest=j(S/'review/FINAL-MANIFEST-v1.json')
for m in manifest['members']:assert sha(S/'review'/m['path'])==m['sha256']
out={'reviewer':'/root/final_skeptical','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verdict':'PASS_EXACT_SEVEN_METADATA_ADAPTATIONS_AND_CANONICAL_WRAPPER','inputs':[bind(P/f'core/{n}.json')for n in ['decisions','proposals','evidence','proposal-lineage','assembly-receipt']]+[bind(S/'review/main-review.json'),bind(S/'review/FINAL-MANIFEST-v1.json')],'finding_dispositions':changes,'canonical_case_reviews':dchecks,'counts':{'cases':188,'wrapped_review_cases':21,'unchanged_other_cases':167,'proposals':155,'scientifically_reviewed_payloads':35,'evidence':1767,'retained_prior_evidence':1627,'canonical_metadata_adaptations':7,'peer_evidence_addition':1},'proposals_and_lineage_exact_science_inputs':True,'sealed74member_science_packet_unchanged':True,'limitation':'This verifies exact scientific-scope and provenance preservation. Final README/register/source-ledger/native saved review and publication controls are reviewed in the final receipt after stable inputs arrive. It is not fresh whole-campaign chemical or owner/export acceptance.'}
q=R/'canonical-wrapper-review-v1.json';assert not q.exists();q.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(bind(q)))
