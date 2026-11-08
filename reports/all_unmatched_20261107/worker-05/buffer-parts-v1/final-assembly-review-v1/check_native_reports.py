import pathlib,json,yaml,hashlib,datetime,collections
S=pathlib.Path('.temp/w05-buffer-parts-v1');R=S/'final-assembly-review-v1';B=pathlib.Path('reports/all_unmatched_20261107/worker-05');P=B/'buffer-parts-v1';N=pathlib.Path('reviews/structured/20261108T095807Z-worker05-consolidated-source-successor')
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
peer=j(S/'review/main-review.json');pc={x['case_id']:x for x in peer['case_reviews']};pp={x['proposal_id']:x for x in peer['payload_reviews']}
n=j(P/'native-review-preparation/review-content.json');saved=yaml.safe_load((N/'review.yaml').read_text());assert n==saved
assert len(n['targets'])==len(n['assessments'])==n['scope']['population_size']==56
assert n['reviewer']['independence']=='self_review' and n['verdict']=='needs_curation'
src=[]
for x in n['source']['inputs']:
 p=pathlib.Path(x['path']);assert sha(p)==x['sha256'];src.append(x)
evidence=[]
for x in n['evidence']:
 p=pathlib.Path(x['reference']);assert sha(p)==x['snapshot_sha256'];evidence.append(x)
t={x['target_id']:x for x in n['targets']};checks=[]
for a in n['assessments']:
 assert len(a['target_ids'])==1;tid=a['target_ids'][0];target=t[tid];detail=json.loads(a['details'])
 if target['kind']=='snapshot_row':
  assert target['selector'] in pc;expected=pc[target['selector']]
 else:assert tid in pp;expected=pp[tid]
 assert detail==expected and a['summary']==expected['assessment']
 assert a['outcome']=='supported' and 'PEER' in a['evidence_ids']
 checks.append({'target_id':tid,'source_selector':target.get('selector'),'actual_reviewer':expected.get('actual_scientific_reviewer',expected.get('final_composition_reviewer')),'assessment_exact_verbatim':True,'detailed_scientific_receipt_exact':True})
assert {x.get('source_selector')for x in checks if x.get('source_selector')}==set(pc)
assert {x['target_id']for x in checks if x['target_id'] in pp}==set(pp)
assert not n['findings'] and not n['actions']
assert any('No historical structured finding is terminally closed' in x for x in n['limitations'])
ledger=j(P/'source-ledger.json');selector=j(P/'selected-origin-bindings.json')
fragments=[]
for f in ledger['primary_scopes']:
 assert sha(pathlib.Path(f['path']))==sha(pathlib.Path(f['public_path']))==f['sha256']
 fragments.append({'lane':f['lane'],'kind':f['kind'],'actual_author':f['primary_author'],'public_path':f['public_path'],'sha256':f['sha256']})
assert sha(P/ledger['canonical_selector']['path'])==ledger['canonical_selector']['sha256']
assert ledger['actual_scientific_review']['sha256']==sha(S/'review/main-review.json')
for x in ledger['canonical_evidence_envelope_adaptations']:assert sha(P/x['path'])==x['sha256']
fr=j(P/'finding-register.json');old=j(B/'tellurium-polypeptone-v1/finding-register.json')
assert all(fr[k]==v for k,v in old.items() if k not in ['at','compiler'])
assert len(fr['original_findings'])==18 and len({x['finding_id']for x in fr['original_findings']})==18
newids={x['finding_id']for x in fr['consolidated_successor']['new_findings']};assert {'W05-ASSEMBLY-EVIDENCE-003','W05-ASSEMBLY-EVIDENCE-004'}<=newids
for item in fr['consolidated_successor']['scoped_bindings']:
 assert sha(P/item['path'])==item['sha256']
for item in fr['consolidated_successor']['new_findings']:
 for x in item['reproductions']:assert sha(P/x['path'])==x['sha256']
D=j(P/'core/decisions.json')['decisions'];PS=j(P/'core/proposals.json')['proposals'];E=j(P/'core/evidence.json')['evidence'];counts=j(P/'final-counts.json');oldP={x['proposal_id']:x for x in j(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']};oldD={x['case_id']:x for x in j(B/'tellurium-polypeptone-v1/core/decisions.json')['decisions']}
assert counts['cases']==len(D)==188;assert counts['proposals']==len(PS)==155;assert counts['evidence_entries']==len(E)==1767
assert counts['occurrence_memberships']==sum(len(d['occurrence_ids'])for d in D)==388
assert counts['dispositions']==dict(collections.Counter(d['disposition']for d in D))
assert counts['unchanged_prior_payloads']==sum(p['proposal_id']in oldP and p['after_capture']==oldP[p['proposal_id']]['after_capture']for p in PS)==134
assert counts['unchanged_case_objects']==sum(d==oldD[d['case_id']]for d in D)==167
readme=(P/'README.md').read_text();assert '134 prior payloads remain byte-identical' in readme and '21 complete composed decisions and 35 full payloads' in readme
assert 'Seven new campaign evidence envelopes' in readme and 'All 1627 predecessor evidence objects remain exact' in readme
assert 'Root compiles reports and native checks and is not represented as its own independent reviewer' in readme
out={'reviewer':'/root/final_skeptical','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verdict':'PASS_FINAL_REPORT_AND_NATIVE_SCIENTIFIC_SCOPE','exact_inputs':[bind(P/n)for n in ['README.md','source-ledger.json','selected-origin-bindings.json','finding-register.json','final-counts.json','native-review-preparation/review-content.json']]+[bind(N/'review.yaml'),bind(N/'review.md')],'native_source_bindings':src,'native_evidence_bindings':evidence,'native_assessment_reviews':checks,'actual_final_primary_fragments':fragments,'reported_counts_independently_recomputed':counts,'assessments':['Every native assessment text and complete detail object equals the actual sealed peer receipt; twenty-one decisions and thirty-five payloads retain distinct target/byte scopes and actual child attribution.','Compiler is explicitly self_review; scientific support is cited to the independent receipt. needs_curation expresses residual source/owner/application limits, not a new scientific rejection of the bounded report.','Empty supplemental findings/actions do not close historical findings: the native limitation explicitly preserves historical review authority, and every prior register field except new timestamp/compiler remains exact. Original eighteen findings remain present.','The source ledger selects exact final v3/v5/direct-parent fragments and separately binds both canonical adaptations. It does not turn the older source snapshots into current source approval.','README and counts accurately distinguish 188case accounting from the actual21case/35payload review and 155proposal universe.13 authentic dependent origins do not claim new case ownership.','The selected final generic and named preparation identities, source-specific holds and qualified FoodOn interpretation match the actual scientific review; other workers coupled-owner acceptance remains separate.'],'new_findings':[],'limitation':'Retained native bundle check and final preservation receipt are pending at this read; no published commit/head or final application approval claimed.'}
q=R/'native-and-reports-review-v1.json';assert not q.exists();q.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(bind(q)))
