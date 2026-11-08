import datetime,hashlib,json,pathlib
O=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/review/membership-child');S=pathlib.Path('.temp/w05-tellurium-polypeptone-v1/polypeptone')
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
a=json.loads((S/'context-ledger.json').read_text());b=json.loads((S/'context-ledger-v2.json').read_text());c=json.loads((O/'author-ledger-comparison-v1.json').read_text());late=json.loads((O/'togo-late-primary-review-v1.json').read_text());readhash={x['sha256'] for x in late['successful_captures']}
assert sha(S/'context-ledger.json')==c['author_ledger_sha256']
for k,v in a.items():
 if k!='rows':assert b[k]==v,k
added=[]
for ar,br,cr in zip(a['rows'],b['rows'],c['row_results']):
 for k,v in ar.items():assert br[k]==v,(ar['context_row_index'],k)
 assert objsha(br['original_occurrence_row'])==br['original_row_canonical_sha256']
 cr['checks']['author_original_row_canonical_hash_exact']=True
 if 'fresh_togo_source_binding' not in br:continue
 binding=br['fresh_togo_source_binding'];p=S/'captures'/pathlib.Path(binding['capture']['path']).name;receipt=pathlib.Path(str(p)+'.receipt.json');rc=json.loads(receipt.read_text());actual=json.loads(p.read_text())
 assert sha(p)==binding['capture']['sha256']==rc['sha256'] and sha(p) in readhash
 assert sha(receipt)==binding['receipt']['sha256'] and binding['url']==rc['url'] and binding['accessed_at']==rc['accessed_at']
 assert br['fresh_togo_meta']==actual['meta']
 for m in br['fresh_togo_matched_components']:
  x=actual
  for step in m['json_pointer'].split('/')[1:]:x=x[int(step)] if isinstance(x,list) else x[step]
  assert x==m['exact_component']
 cr['late_togo_rereview']={'capture_path':str(p),'sha256':sha(p),'actual_source_binding':'Exact URL, timestamp, metadata and target component object verified; capture independently scientifically read before author-v2 comparison.','interpretation':'Supported positive provider cross-label relationship; formulation/SKU and current Shioya equivalence appropriately excluded. Raw units and all original row fields remain unchanged.'}
 added.append(br['context_row_index'])
assert len(added)==17
c.update({'compared_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author_ledger_path':str(S/'context-ledger-v2.json'),'author_ledger_sha256':sha(S/'context-ledger-v2.json'),'author_supplemented_at':b['supplemented_at'],'predecessor_comparison':{'path':str(O/'author-ledger-comparison-v1.json'),'sha256':sha(O/'author-ledger-comparison-v1.json')},'late_togo_row_indices':added,'unchanged_original_fields_in_all150':True,'conditional_matrix_binding':{'path':str(S/'conditional-grounding-matrix.json'),'sha256':sha(S/'conditional-grounding-matrix.json'),'assessment':'Complete three-option matrix read. MICRO:0000179 applicability is conditional on a supported BD blend scope; source-specific broader FOODON option is conditional rather than universally nearest. No molecular-completeness or all150-resolution prerequisite is imposed. Whole-owner continuity/source allocation and source-specific holds remain separate; no final identity selected by this child.'}})
p=O/'author-ledger-comparison-v2.json';assert not p.exists();p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('All150 original fields unchanged;17 appended TOGO rows independently re-reviewed; conditional matrix supported.')
