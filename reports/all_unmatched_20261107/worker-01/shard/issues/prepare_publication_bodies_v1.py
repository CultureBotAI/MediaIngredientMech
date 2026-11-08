import pathlib,json,re,hashlib,datetime
O=pathlib.Path('reports/all_unmatched_20261107/worker-01/shard/issues');P=O/'publication-v1';P.mkdir(exist_ok=False)
plan=json.loads((O/'continuation-issue-plan-v4.json').read_text())
def prose(s):
 # Protect actual URLs and verbatim code/formula tokens while improving prose spacing.
 bits=re.split(r'(`[^`]*`|https?://[^\s)]+)',s)
 for i,t in enumerate(bits):
  if t.startswith(('`','http://','https://')):continue
  for prefix in ['JCM','DSMZ','NBRC','TOGO']:
   t=re.sub(r'\b'+prefix+r'(?=\d)',prefix+' ',t)
  t=re.sub(r'\bCHEBI(?=\d)','CHEBI:',t)
  t=re.sub(r'\b(case|cases|ingredient|solution|stock|table|all|full)(?=\d)',r'\1 ',t,flags=re.I)
  t=re.sub(r'\bpH(?=\d)','pH ',t)
  t=re.sub(r'(?<=\d)(mg|mL|ml|mM|g|L|M)(?=$|[/\s,;:.|)])',r' \1',t)
  t=re.sub(r'(?<=%)(w/v|v/v)',r' \1',t)
  t=t.replace('Worker01','Worker 01').replace('worker01','worker 01').replace('thiosulfate/numeric','thiosulfate and numeric').replace('all188','all 188')
  bits[i]=t
 return ''.join(bits)
for a in plan['actions']:
 old=pathlib.Path(a['body_file']);s=old.read_text()
 if a.get('issue')==408:
  s=s.replace('source bicarbonate is 8.4 g per 100 mL; sulfide is 12 g Na2S·9H2O per 50 mL.','source bicarbonate lists 8.4 g NaHCO3 plus 100 mL water; sulfide lists 12 g Na2S·9H2O plus 50 mL water. Neither added-water amount is a measured final stock volume.')
  s+='\nCase 14 also needs distinct quantity bases: TOGO M3118 lists 94 mg Na2SeO4·5H2O and 1000 mL added water; it does not establish a final 94 mg/L concentration. Frolov’s thesis independently heads its table in mg/L and gives unhydrated Na2SeO4 at 94 mg/L, with a 1 mL/L receiving-medium dose. Preserve that source/version distinction and the unresolved hydration conflict. [Quantity correction](https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/root_substances/case14-quantity-correction-v7.json).\n'
 if a.get('issue')==718:
  s+='\nThe JCM 151 stock formulation is recovered, but its current MIM ownership is conflicted: UNMAPPED_0553 imports MediaDive 1883; `Trace_Mineral_Solution.yaml` imports MediaDive 897 and combines 151/852 aliases; `4-vinylphenol.yaml` carries incompatible trace-mineral aliases. JCM 265 uses a 1 L aliquot of the prepared JCM 151 stock, not necessarily the complete batch made with 1 L water. The proposed parent preserves that nested stock without a guessed catalog reference or duplicate owner. Reconcile the imported source identities and exact alias scopes using the [full owner records and hashes](https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/named_stocks/quantity-v4/jcm151-owner-conflict.json). Closed [#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861) explicitly left this source-specific identity question open while correcting review certainty; [#587](https://github.com/CultureBotAI/MediaIngredientMech/issues/587) covers different instruction-form suggestions.\n\nFor case 14, the TOGO recipe lists 94 mg reagent plus 1000 mL added water. Only the thesis table explicitly supplies a 94 mg/L concentration basis. The two recipe versions and their different hydration claims remain separate.\n'
 if a['action']=='new_issue':
  oldstart=s.index('Deduplication used live')
  s=s[:oldstart]+'''Deduplication was refreshed on 2026-11-08 at 04:54 UTC. Exact source-ID and water-choice searches found no matching tracker. Full bodies and comments of all thiosulfate/numeric candidates were read: #5/#380 concern Madin pathways, #572 concerns METPO guidance, #788 is a closed mapping re-sync regression, and #1668 concerns a different diagnostic PR. The known #1319 and #1824 scopes are distinguished above. Search results were below the query cap, but indexed searches remain bounded. Ignored files were included in the local issue-inventory search. [Deduplication receipt](https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/issues/publication-dedup-disposition-v2.json).
'''
 s=prose(s)
 fingerprint=('w01-source-mediadive572-stock-quantities,w01-source-mediadive2389-water-choice' if a['action']=='new_issue' else 'w01-continuation-'+a['repository'].split('/')[-1].lower()+'-'+str(a['issue']))
 s+='\n<!-- mim-review-round: all-unmatched-20261107-worker01-continuation; mim-fingerprints: '+fingerprint+' -->\n'
 dest=P/old.name;dest.write_text(s);a['body_file']=str(dest);a['fingerprints']=fingerprint.split(',')
plan['created_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();plan['state']='public_prose_cleaned; final_review_dispositions_and_immutable_commit_links_pending';plan['dedup_receipt']=str(O/'publication-dedup-disposition-v2.json');plan['body_sha256']={pathlib.Path(a['body_file']).name:hashlib.sha256(pathlib.Path(a['body_file']).read_bytes()).hexdigest() for a in plan['actions']};(P/'issue-plan.json').write_text(json.dumps(plan,indent=2)+'\n');print(P/'issue-plan.json')
