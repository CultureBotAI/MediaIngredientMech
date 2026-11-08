from pathlib import Path
import json,hashlib,copy,shutil,datetime
W=Path.cwd();C=W.parents[2];R=W/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v5';T=W/'.temp/info004-successor-v1';A=S/'reviewed-draft';A.mkdir(exist_ok=False)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}
now=datetime.datetime.now(datetime.timezone.utc).isoformat();filed=read(T/'coordinator-filing-read-v2.json')[0];assert 'W06-I004-PPG-PROVENANCE-001' in filed['body'];oldfinding=read(T/'linked-final1d62-findings.json');assert 'W08-W06V4-001' in oldfinding['body'] and 'W08-W06-LINEAGE-CTRL-001' in oldfinding['body']
for name in ['coordinator-filing-read-v2.json','linked-final1d62-findings.json']:shutil.copyfile(T/name,S/'inputs'/name)
packets=[]
for dirname in ['w06-ppg-attribution-publication-v1','w06-final-metadata-triage-v1']:
 F=C/'preflight'/dirname;m=read(F/'verified-manifest.json')
 for f in m['files']:assert sha(F/f['path'])==f['sha256'],f
 packets.append({'path':str(F),'manifest_sha256':sha(F/'verified-manifest.json'),'verified_files':len(m['files'])})
 for name in (['verified-manifest.json','comment1201.md','finding.json'] if 'ppg' in dirname else ['verified-manifest.json','root-triage.json','wording-findings.json','control-limitation.json','comment1217.md']):
  out=S/'inputs'/dirname/name;out.parent.mkdir(exist_ok=True);shutil.copyfile(F/name,out)
save(S/'inputs/new-filing-integrity.json',{'verified_at':now,'packets':packets})
DD=read(S/'author-draft/decisions.json');PP=read(S/'author-draft/proposals.json');EE=read(S/'author-draft/evidence.json');D=DD['decisions'];P=PP['proposals'];E=EE['evidence'];by={e['evidence_id']:e for e in E};oldsearch=copy.deepcopy(by['V5-E-PPG-SEARCH']);by['V5-E-PPG-SEARCH']['supports_or_contradicts']='Ignored-inclusive local native catalogues, worker report YAML and enumerated coordinator candidate snapshots contain no matching named PPG owner in the documented scope. This local duplicate search does not establish external ontology or registry absence, supplier procurement, CAS identity, or acceptance of later worker heads.'
index={'collector':'/root/residual_material_review','index_author':'Codex worker06 /root','assembled_at':now,'scope':'Exact official ontology/search retrievals, separate from local dedup. Original raw responses and retrieval times preserved. Failed CAS request is a failed search, never proof of absence. No query hit alone establishes grade identity.','receipt_bindings':[],'queries':[]}
for folder in ['live-ontology-v1','live-terms-v1']:
 q=S/'inputs/ppg'/folder;receipt=read(q/'receipts.json');index['receipt_bindings'].append(cap(q/'receipts.json'))
 for x in receipt['queries']:
  row={k:copy.deepcopy(v) for k,v in x.items() if k not in ['command','body_path']};row['original_body_path']=x.get('body_path');body=q/(x['name']+'.body')
  if body.exists():row['body_capture']=cap(body);assert sha(body)==x.get('sha256',sha(body))
  for ext in ['headers','stderr']:
   f=q/(x['name']+'.'+ext)
   if f.exists():row[ext+'_capture']=cap(f)
  index['queries'].append(row)
save(S/'inputs/ppg/official-query-index-v1.json',index)
E.append({'evidence_id':'V5-E-PPG-OFFICIAL-SEARCH','kind':'source_snapshot','capture':cap(S/'inputs/ppg/official-query-index-v1.json'),'locator':'Every exact original official query receipt/body/header/error binding with original accessed_at and result status','supports_or_contradicts':'Bounded exact nominal-grade searches returned no supported exact term; full generic CHEBI:61615 supports only a broader polymer-material parent. Other misleading/generic results and unsuccessful registry access do not establish NBRC procurement, supplier, CAS, fixed structure or universal ontology absence.','url':None,'case_ids':[D[28]['case_id']]})
D[28]['evidence_ids'].append('V5-E-PPG-OFFICIAL-SEARCH');P[-1]['evidence_ids'].append('V5-E-PPG-OFFICIAL-SEARCH')
# New immutable active evidence wording; raw provenance and historical original summaries stay exact.
claim_changes=[]
for eid,i in [('A-E-CAPTURE-078',20),('A-E-CAPTURE-102',38)]:
 e=by[eid];before=copy.deepcopy(e)
 if i==20:e['supports_or_contradicts']='case20: ATCC1775 specifies KOH for pH adjustment during trace-element preparation, without stating supplied form, stock strength, density, carrier or product identity. The separate solution classification is supported by TOGO M2665 in A-E-COMPLETION-09, not by this ATCC capture; it does not identify the whole preparation as pure potassium hydroxide.'
 else:
  prefix=e['supports_or_contradicts'].split('; case38:')[0];e['supports_or_contradicts']=prefix+'; case38: JCM1344 specifies 1 ml of separately sterilized 1% yeast-extract solution. The stock carrier, extract product and percent basis are unspecified; basal water is not stock-carrier evidence.';assert e['supports_or_contradicts'].split('; case38:')[0]==before['supports_or_contradicts'].split('; case38:')[0]
 assert {k:v for k,v in e.items() if k!='supports_or_contradicts'}=={k:v for k,v in before.items() if k!='supports_or_contradicts'}
 claim_changes.append({'evidence_id':eid,'case_index':i,'before':before,'after':copy.deepcopy(e),'only_changed_field':'supports_or_contradicts','raw_capture_and_url_access_time_unchanged':True})
 d=D[i];d['prior_v5_independent_review']=copy.deepcopy(d['independent_review']);d['independent_review']={'status':'pending','evidence_ids':[]};d['evidence_ids'].append('V5-E-STOCK-CLAIM-SUPERSESSION');d['issue_refs']=list(dict.fromkeys(d.get('issue_refs',[])+[oldfinding['html_url']]));d['source_claim_supersession']='W08-W06V4-001: active evidence wording corrected; unchanged supported payload and unchanged scientific source outcome, with all unknowns/holds retained.'
sup={'author':'Codex worker06 /root','llm_assisted':True,'at':now,'finding_id':'W08-W06V4-001','filed_issue':oldfinding['html_url'],'changes':claim_changes,'historical_native_summaries_superseded_claim_only':[{'path':'reviews/structured/20261108T080947Z-w06-successor-v4-residuals/review.yaml','sha256':'b7f505b9eb538ae407b1bfc0a9d6c8bc8fbe1e3d6d1fbba60af5ac1093ee8c17','pointers':['/evidence/17/summary','/evidence/21/summary'],'scope':'Only unsupported ATCC solution attribution and JCM case38 aqueous characterization. Historic report stays byte-identical and remains evidence of the prior review, not current scientific support for those two words.'}],'case27_annotation_retained_exact':True,'payload_changes':0,'no_new_approval':True};save(S/'claim-supersessions.json',sup)
E.append({'evidence_id':'V5-E-STOCK-CLAIM-SUPERSESSION','kind':'source_snapshot','capture':cap(S/'claim-supersessions.json'),'locator':'Exact before/after evidence descriptions and prior native-summary claim pointers; original captures/URLs/times unchanged','supports_or_contradicts':'Filed bounded evidence-scope correction for case20 KOH form attribution and case38 unknown yeast-stock carrier. Existing source-specific stocks, unknown strength/basis/product/carrier and all downstream holds remain; unrelated case27 annotation unchanged.','url':None,'case_ids':[D[20]['case_id'],D[38]['case_id']]})
disp={'finding_id':'W06-I004-PPG-PROVENANCE-001','filed_issue':filed['html_url'],'filing_created_at':filed['created_at'],'correction_at':now,'classification':'bounded evidence attribution; original INFO004 remains informational','original_draft_evidence':{'path':str((S/'author-draft/evidence.json').relative_to(W)),'sha256':sha(S/'author-draft/evidence.json')},'before':oldsearch,'after':by['V5-E-PPG-SEARCH'],'new_binding':cap(S/'inputs/ppg/official-query-index-v1.json'),'payload_sha256_unchanged':sha(S/'payloads/polypropylene_glycol_2000.yaml'),'independent_repaired_binding_review':'pending','linked_stock_summary_finding':'claim-supersessions.json','linked_control_coverage_finding':{'finding_id':'W08-W06-LINEAGE-CTRL-001','filed_issue':oldfinding['html_url'],'disposition':'Original weak negative arms preserved as historical comparisons, not proof of complete validation-path rejection. Additive complete-payload fixture controls will supply any stronger coverage claim.'},'no_role_or_export_approval':True};save(S/'provenance-finding-disposition.json',disp)
for name,obj in [('decisions',DD),('proposals',PP),('evidence',EE)]:save(A/(name+'.json'),obj)
print('New reviewed-draft created after two exact filed comments; no payload changed; original author-draft preserved')
