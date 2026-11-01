from pathlib import Path
from datetime import datetime,timezone
import collections,csv,hashlib,io,json,subprocess
OUT=Path(__file__).resolve().parent;RUN=OUT.parents[1];MIM=RUN/'step3-mim';BASE='99fe4b44d78126d78041a69eeb366c52bedf0caa'
sha=lambda b:hashlib.sha256(b).hexdigest();read=lambda p:(MIM/p).read_bytes();load=lambda p:json.loads(read(p));old=lambda p:subprocess.check_output(['git','show',BASE+':'+p],cwd=MIM)
def table(b,*,sssom=False):
 text=b.decode();text='\n'.join(line for line in text.splitlines() if not line.startswith('#')) if sssom else text
 return list(csv.DictReader(io.StringIO(text),delimiter='\t'))
subjects={'MIM:Carnitine_Hydrochloride','MIM:Carnitine_Dl_Hydrochloride','MIM:NLDM_metabolites'}
owners={'data/ingredients/mapped/'+name+'.yaml' for name in ['Carnitine_Hydrochloride','Carnitine_Dl_Hydrochloride','NLDM_metabolites']}
canonical='mappings/ingredient_mappings.sssom.tsv';before=old(canonical);after=read(canonical);assert sha(after)=='d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6'
br,ar=table(before,sssom=True),table(after,sssom=True);assert (len(br),len(ar))==(2986,2982)
unrelated=lambda data:[line for line in data.splitlines(keepends=True) if line.split(b'\t',1)[0].decode(errors='replace') not in subjects]
assert unrelated(before)==unrelated(after)
key=lambda row:(row['subject_id'],row['predicate_id'],row['object_id'])
bi,ai={key(r):r for r in br},{key(r):r for r in ar};assert len(bi)==len(br) and len(ai)==len(ar)
selected=[r for r in ar if r['subject_id'] in subjects];assert len(selected)==2
assert next(r for r in selected if r['subject_id']=='MIM:Carnitine_Hydrochloride')['object_id']=='NCIT:C216679'
mr=load('reports/sssom_completion_20260921/review.json');omr=json.loads(old('reports/sssom_completion_20260921/review.json'))
assert len(mr['decisions'])==len(ar)
decisions={key(ar[r['source_position']-1]):r for r in mr['decisions']};olddecisions={key(br[r['source_position']-1]):r for r in omr['decisions']}
semantic_decision=lambda d:{k:v for k,v in d.items() if k not in ['source_position','evidence_key']}
for k,r in decisions.items():
 if k[0] not in subjects:assert semantic_decision(r)==semantic_decision(olddecisions[k]),k
 else:assert r['disposition']=='WITHHOLD'
for review in [mr,load('reports/semantic_review_20260921/resolution/current-review.json')]:
 for section in ['inputs','record_inputs']:
  for p,h in review[section].items():assert sha(read(p))==h,(section,p)
oldnldm=next(r for r in omr['decisions'] if r['owner_record'].endswith('/NLDM_metabolites.yaml'));newnldm=next(r for r in mr['decisions'] if r['owner_record'].endswith('/NLDM_metabolites.yaml'))
assert oldnldm['disposition']=='SUPPORTED' and newnldm['disposition']=='WITHHOLD'
assert mr['source_sha256']==sha(after)
counts=dict(collections.Counter(r['disposition'] for r in mr['decisions']));assert counts=={'SUPPORTED':1739,'WITHHOLD':1243}
receipt_path='reports/sssom_completion_20260921/mapping_changes/issue1004-carnitine-hydrochloride-merge.json';receipt=load(receipt_path)
assert receipt['sequence']==17 and receipt['before_sha256']==sha(before) and receipt['after_sha256']==sha(after) and receipt['approval'].startswith('NONE:')
assert (receipt['changed_rows'],receipt['removed_rows'],receipt['added_rows'])==(2,4,0)
assert set(receipt['touched_subjects'])==subjects and {r['source_record'] for r in receipt['records']}==owners
for r in receipt['records']:assert sha(read(r['source_record']))==r['after_yaml_sha256'] and sha(old(r['source_record']))==r['before_yaml_sha256']
prior_receipts=[]
for p in sorted((MIM/'reports/sssom_completion_20260921/mapping_changes').glob('*.json')):
 r=json.loads(p.read_bytes())
 if r['sequence']<17:assert p.read_bytes()==old(str(p.relative_to(MIM)));prior_receipts.append(r['sequence'])
assert sorted(prior_receipts)==list(range(1,17))
path='reports/semantic_review_20260921/resolution/assertion-dispositions.tsv';assertions=table(read(path));oldassertions=table(old(path))
assertionkey=lambda r:(r['source_record'],r['assertion_type'],r['source_position'])
aidx,oidx={assertionkey(r):r for r in assertions},{assertionkey(r):r for r in oldassertions}
assert len(aidx)==len(assertions) and len(oidx)==len(oldassertions)
assert {k:v for k,v in aidx.items() if k[0] not in owners and k[1]!='mapping'}=={k:v for k,v in oidx.items() if k[0] not in owners and k[1]!='mapping'}
# Mapping assertion positions and whole-artifact hashes legitimately relocate.
# Compare exact claim digests/status/evidence using the complete canonical triple.
mapassert={key(ar[int(r['source_position'])-1]):r for r in assertions if r['assertion_type']=='mapping'}
oldmapassert={key(br[int(r['source_position'])-1]):r for r in oldassertions if r['assertion_type']=='mapping'}
semantic_assertion=lambda r:{k:v for k,v in r.items() if k not in ['assertion_id','source_position','source_record_sha256']}
for k,r in mapassert.items():
 assert r['source_record_sha256']==sha(after)
 if k[0] not in subjects:assert semantic_assertion(r)==semantic_assertion(oldmapassert[k]),k
 else:assert r['resolution_status']=='OPEN'
nldm='data/ingredients/mapped/NLDM_metabolites.yaml';nd=[r for r in assertions if r['source_record']==nldm];ond=[r for r in oldassertions if r['source_record']==nldm]
assert len(nd)==len(ond)==68 and all(r['resolution_status']=='OPEN' for r in nd) and all(r['resolution_status']=='APPROVED' for r in ond)
payload_changes=[list(k[1:]) for k,r in aidx.items() if k[0]==nldm and r['assertion_sha256']!=oidx[k]['assertion_sha256']]
assert payload_changes==[['component','59']]
assert all(r['source_record_sha256']==sha(read(nldm)) for r in nd)
for r in nd:assert r['source_record_sha256']!=oidx[assertionkey(r)]['source_record_sha256']
semantic=load('reports/semantic_review_20260921/resolution/current-review.json');assert semantic['release_verdict']=='FAIL' and len(semantic['blocking_finding_ids'])==1732 and len(semantic['blocking_assertion_ids'])==2336
path='reports/semantic_review_20260921/resolution/finding-dispositions.tsv';findings=table(read(path));oldfindings=table(old(path))
assert {r['finding_id']:r for r in findings if r['source_record'] not in owners}=={r['finding_id']:r for r in oldfindings if r['source_record'] not in owners}
unified='UNIFIED_INGREDIENT_MAPPING.tsv';uold,unew=table(old(unified)),table(read(unified));ui,oi={r['ingredient_name']:r for r in unew},{r['ingredient_name']:r for r in uold}
assert len(ui)==len(unew)==len(oi)==len(uold)==4170 and ui.keys()==oi.keys();assert sum(int(r['occurrence_count']) for r in unew)==209330
changed=[name for name in ui if ui[name]!=oi[name]];assert changed==['Carnitine Hydrochloride']
assert [line for line in read(unified).splitlines(keepends=True) if not line.startswith(b'Carnitine Hydrochloride\t')]==[line for line in old(unified).splitlines(keepends=True) if not line.startswith(b'Carnitine Hydrochloride\t')]
row=ui[changed[0]];assert row['mim_id']=='NCIT:C216679' and row['cas_rn']=='461-05-2'
assert set(k for k in row if row[k]!=oi[changed[0]][k])=={'mim_id','cas_rn','synonyms'}
assert not any(r['mapping_status']=='REJECTED' and not r['mim_id'] for r in unew)
assert not any(r['mim_id'].startswith('kgmicrobe.compound:') and any(r[c].startswith('CHEBI:') for c in ['culturemech_term_id','chebi_id','kg_microbe_node_id']) for r in unew)
assert sha(read(unified))=='ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5'
hashrows=[r for r in unew if r['ingredient_name'].startswith('#')];assert len(hashrows)==4 and sum(int(r['occurrence_count']) for r in hashrows)==7
assert load('UNIFIED_INGREDIENT_MAPPING.provenance.json')['artifact_sha256']==sha(read(unified))
comp=load('reports/ingredient_bundle_20261101_carnitine1004/review.json');oldcomp=load('reports/ingredient_bundle_20261101_ncit875/review.json');refresh=load('reports/ingredient_bundle_20261101_carnitine1004/dependency-refresh.json')
assert comp['decisions']==oldcomp['decisions'] and comp['record_inputs']==oldcomp['record_inputs'] and len(comp['decisions'])==51 and len(comp['record_inputs'])==20
assert not owners&set(comp['record_inputs']) and refresh['scientific_approval_added'] is False
assert refresh['successor_review_sha256']==sha(read('reports/ingredient_bundle_20261101_carnitine1004/review.json'))
for p,h in refresh['unchanged_input_sha256'].items():assert sha(read(p))==h
assert len(refresh['selected_mapping_evidence_unchanged'])==20
relocations=sum(x['base_decision_locations']['before']!=x['base_decision_locations']['after'] for x in refresh['selected_mapping_evidence_unchanged']);assert relocations==17
for item in refresh['selected_mapping_evidence_unchanged']:
 beforeloc=item['base_decision_locations']['before'];afterloc=item['base_decision_locations']['after']
 prior=omr['decisions'][beforeloc['source_position']-1];current=mr['decisions'][afterloc['source_position']-1]
 assert semantic_decision(prior)==semantic_decision(current)
for p in ['.github/workflows/qc-evidence.yaml','.vendored_canon_ref']:
 assert read(p)==old(p)
labels=list(csv.DictReader(io.StringIO(read('docs/data/label_index.csv').decode())))
saltlabels=[r for r in labels if r['preferred_term'] in ['Carnitine Hydrochloride','Carnitine (Dl) Hydrochloride']]
assert saltlabels and all(r['identifier']==r['ontology_id']=='NCIT:C216679' for r in saltlabels)
assert not any(r['label'] in ['DL-carnitine','3-hydroxy-4-(trimethylammonio)butanoate','4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride'] for r in saltlabels)
browser=load('docs/data/ingredients.json')['ingredients'];saltbrowser=[r for r in browser if r['preferred_term'] in ['Carnitine Hydrochloride','Carnitine (Dl) Hydrochloride']]
assert len(saltbrowser)==2 and all(r['id']==r['ontology_id']=='NCIT:C216679' for r in saltbrowser)
assert sorted((r['mapping_status'],r['media_count'],r['total_occurrences']) for r in saltbrowser)==[('MAPPED',14,14),('REJECTED',0,0)]
for r in saltbrowser:assert '461-06-3' not in r['searchable'] and 'kgmicrobe.compound:carnitine_hydrochloride' not in r['searchable']
result={'checked_at':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_BOUNDED_ACTUAL_PRODUCT_AND_WITHDRAWAL_AUDIT','canonical_sha256':sha(after),'canonical_rows':len(ar),'unrelated_sssom_lines_exact':True,'receipt17_sha256':sha(read(receipt_path)),'prior16_receipts_unchanged':True,'mapping_counts':counts,'unrelated_mapping_decisions_equal_except_native_location':True,'nldm_withdrawn':69,'nldm_nonmapping_payloads_unchanged':67,'nldm_payload_changes':payload_changes,'unrelated_nonmapping_assertion_rows_exact':True,'unrelated_mapping_assertion_payload_status_evidence_equal_after_native_relocation':True,'unrelated_finding_rows_exact':True,'full_semantic_status':{'verdict':semantic['release_verdict'],'blocking_findings':len(semantic['blocking_finding_ids']),'blocking_assertions':len(semantic['blocking_assertion_ids'])},'unified':{'sha256':sha(read(unified)),'rows':len(unew),'occurrences':sum(int(r['occurrence_count']) for r in unew),'changed':changed,'before':oi[changed[0]],'after':row,'hash_prefixed_rows':hashrows,'unrelated_bytes_exact':True},'companion':{'claims':51,'owners':20,'mapping_relocations':relocations,'decisions_and_owner_hashes_exact':True},'salt_label_rows':saltlabels,'browser_rows':saltbrowser,'protected_qc_and_pin_unchanged':True,'scientific_or_release_approval':False,'final_head_audit':False,'production_writes':False}
(OUT/'product-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
