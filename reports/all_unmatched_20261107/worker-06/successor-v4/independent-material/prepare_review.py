from pathlib import Path
import datetime,hashlib,json,subprocess,yaml
O=Path(__file__).resolve().parent;W=O.parents[2];C=W.parents[2];P=C/'preflight/w06-successor-residual-triage-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):
 with (O/name).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert sha(P/'author-correction-task.md')=='8fdc345bbdc41dfeb653461d9ef5590ef36a73f2540b7adad53bf2288ca55524'
assert sha(P/'MANIFEST.json')=='e25ba4e8b80cf8764e2b849087f09852f6d769d68a2fc5d3759d70c3bce5ea2b'
manifest=json.loads((P/'MANIFEST.json').read_text())
for row in manifest['files']:assert sha(P/row['path'])==row['sha256'] and (P/row['path']).stat().st_size==row['bytes']
source=json.loads((P/'actionable-matrix.json').read_text())
refs=source['apple_pectin']['primary_references']+source['ynb']['primary_references']
ontology=next(r for r in json.loads((P/'additional-inputs.json').read_text()) if r.get('role')=='primary_ontology')
refs.append({'evidence_id':'CHEBI17309-primary-ontology','sha256':ontology['sha256'],'url':ontology['url'],'original_accessed_at':ontology.get('original_accessed_at'),'kind':'primary_ontology'})
receipts=[]
for ref in refs:
 p=P/'inputs'/ref['sha256'];assert sha(p)==ref['sha256']
 receipts.append({**ref,'inspected_path':str(p),'local_inspected_at':at,'new_provider_retrieval':False,'read_scope':'Complete selected captured body including full receiving table/steps; source-specific claims assessed, unrelated roles not endorsed.'})
save('primary-read-receipts.json',receipts)
catalog=[];hits=[]
for root in [W/'data/ingredients',C/'integration/worktree/data/ingredients']:
 files=list(root.rglob('*.yaml'));matches=[]
 for p in files:
  text=p.read_text()
  if 'pectin' not in text.casefold():continue
  rec=yaml.safe_load(text)
  if not isinstance(rec,dict):continue
  names=[rec.get('preferred_term',''),rec.get('identifier','')]+[s.get('synonym_text','') for s in rec.get('synonyms',[])]
  if any('pectin' in str(n).casefold() for n in names):matches.append({'path':str(p),'sha256':sha(p),'identifier':rec.get('identifier'),'preferred_term':rec.get('preferred_term'),'names':names,'full_record':rec})
 catalog.append({'root':str(root),'ignored_files_included':True,'files':len(files),'pectin_named_owners':matches,'apple_qualified_identity_matches':[m['path'] for m in matches if any('apple' in str(n).casefold() and 'pectin' in str(n).casefold() for n in m['names'])]})
save('catalogue-scope.json',catalog)
# All worker report YAML includes retained histories and active successors; no inference of active acceptance.
counts=[];scanned=[];apple=[];pectin=[]
for root in sorted((C/'workers').glob('w*/worktree/reports/all_unmatched_20261107/worker-*')):
 paths=list(root.rglob('*.yaml'));counts.append({'root':str(root),'yaml_files':len(paths)})
 for p in paths:
  text=p.read_text();scanned.append({'path':str(p),'sha256':sha(p)})
  if 'pectin' not in text.casefold():continue
  rec=yaml.safe_load(text)
  if not isinstance(rec,dict) or not rec.get('identifier'):continue
  names=[rec.get('preferred_term',''),rec['identifier']]+[s.get('synonym_text','') for s in rec.get('synonyms',[])]
  item={'path':str(p),'sha256':sha(p),'identifier':rec['identifier'],'preferred_term':rec.get('preferred_term'),'names':names}
  if any('pectin' in str(n).casefold() for n in names):pectin.append(item)
  if any('apple' in str(n).casefold() and 'pectin' in str(n).casefold() for n in names):apple.append(item)
coord=[]
for rel in ['preflight/final-intake-candidate-v1/all-active-proposal-entries-v1.json','integration/final-same-target-reconciliation-v2/publication-v4/candidate-summary-v4.json','integration/specific-reconciliations-v1/HANDOFF.json','integration/family-reconciliations-v1/candidate-index.json']:
 p=C/rel;x=json.loads(p.read_text());rows=x if isinstance(x,list) else x.get('groups',x.get('candidates',[]));matched=[]
 for row in rows:
  names=[row.get(k,'') for k in ['identifier','preferred_term','owner_path','destination','candidate_id']]
  if any('pectin' in str(n).casefold() for n in names):matched.append(row)
 coord.append({'path':str(p),'sha256':sha(p),'rows':len(rows),'pectin_identity_matches':matched,'selection_limit':'Historical frozen intake or private coordinator successor, not proof of acceptance of later worker heads.'})
save('proposal-duplicate-search.json',{'at':at,'ignored_files_included':True,'worker_report_yaml_scope':counts,'worker_report_yaml_scanned':scanned,'pectin_named_payloads':pectin,'apple_qualified_named_payloads':apple,'coordinator_surfaces':coord,'interpretation':'Search tests identities/names, not ingredient component mentions. No history or current active intake is silently substituted; final coordinator selection bridge remains required.'})
save('preliminary-science.json',{'at':at,'reviewer':'/root/residual_material_review','independent_of_root_author':True,'worker_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'triage_files_verified':len(manifest['files']),'scope':['W06 case82 apple pectin','W06 case161 YNB three receiving contexts'],'apple':{'established':'M2313 explicitly distinguishes apple-derived pectin from citrus-peel pectin in a one-of list;0.2% basis unspecified. Procurement details not prerequisite for bounded source-qualified material.','limits':['No Malus species, extraction method, dry supplied form, esterification, molar mass, purity, CAS or nutritional role inferred.','CHEBI17309 is generic parent; both apple-related OBO synonyms are related, not exact.','GMO002380 is an explicitly source-qualified annotation, but GMO is not a permitted native OntologySourceEnum. No schema/pin change authorized.','A new report-only material, if authored, needs actual null-before origin and its own full independent review; generic Pectin history/approval cannot transfer.'],'dedup_summary':{'catalogue_apple_matches':sum(len(r['apple_qualified_identity_matches']) for r in catalog),'current_report_apple_named_payloads':len(apple),'all_worker_yaml_count':len(scanned)},'candidate_verdict':'Not yet assessed; root final payload pending.'},'ynb':{'J240':{'known_manufacturer':'BD-Difco','amount':1,'unit':'g','unknown':['catalogue/formulation variant','amino-acid inclusion','ammonium-sulfate inclusion','lot as needed for exact product']},'DSMZ1682':{'amount':6.7,'unit':'g','supplier':'not stated in exact capture'},'DSMZ1837':{'amount':6.7,'unit':'g','supplier':'not stated in exact capture'},'result':'Only the missing-fact partition is corrected; dose and brand do not establish a common variant. Source-specific no-generic-merge hold remains.'},'approval':False,'new_confirmed_findings':[]})
print(json.dumps({'triage_files':len(manifest['files']),'catalogue_counts':[x['files'] for x in catalog],'worker_report_yaml':len(scanned),'apple_identity_hits':len(apple),'coordinator_rows':[x['rows'] for x in coord]}))
