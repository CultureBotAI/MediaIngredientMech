from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1/dependencies';V=S/'inputs/w03-peer'
now=datetime.now(timezone.utc).isoformat()
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def ref(p):return {'root':'artifact','path':'buffer-parts-v1/dependencies/'+str(p.relative_to(S)),'sha256':h(p)}
for name in ['evidence.json','case-deltas.json']:
 p=S/name;q=S/'draft-metadata-v1'/name;q.parent.mkdir(parents=True,exist_ok=True);assert not q.exists();shutil.copyfile(p,q)
E=json.loads((S/'evidence.json').read_text());receipts={r['path']:r for r in json.loads((S/'inputs/issues/remaining-capture-receipt.json').read_text())}
for e in E['evidence']:
 if e['kind'] not in {'independent_review','local_validation'}:e['kind']='source_snapshot'
 if e['evidence_id']=='W05-DEP-FILING':e['accessed_at']=receipts['comment6719248666.json']['accessed_at']
 if e['evidence_id']=='W05-DEP-FAB-FILING':e['accessed_at']=receipts['comment6719468092.json']['accessed_at']
put(S/'evidence.json',E)
P=json.loads((S/'proposals.json').read_text())['proposals'];D=json.loads((S/'case-deltas.json').read_text());base=json.loads((S/'inputs/current-core/decisions.json').read_text())['decisions']
for d in D['case_deltas']:
 b=next(x for x in base if x['case_id']==d['case_id']);d['case_input_sha256']=b['case_input_sha256'];d['union_owner_records']=[{'path':p['owner_path'],'sha256':p['before_sha256']} for p in P if d['case_id'] in p['case_ids']]
put(S/'case-deltas.json',D)
plans=[]
for folder in ['final-component-dependency-plan-v1','final-component-dependency-plan-v2','w05-consolidated-remaining-work-v1']:
 root=S/'inputs'/folder;m=json.loads((root/'MANIFEST.json').read_text())
 for r in m['files']:
  p=root/r.get('path',r.get('capture'));assert h(p)==r['sha256'],p
 plans.append({'path':str(root.relative_to(S)),'manifest_sha256':h(root/'MANIFEST.json'),'verified_members':len(m['files'])})
catalog=json.loads((V/'ambiguous/source-evidence-catalog.json').read_text());access=json.loads((V/'ambiguous/access-and-limitations.json').read_text())
direct={r['path']:r for r in access['direct_attempts']};web={r['path']:r for r in access['web_files']}
rows=[]
for c in catalog:
 captures=[]
 for f in c['files']:
  p=V/'ambiguous'/f['path'];assert h(p)==f['sha256']
  a=direct.get(f['path'],{});w=web.get(f['path'],{})
  original=a.get('accessed_at');lim=None
  if f['path']=='captures/w05-direct-151.body':original='2026-11-08T06:22:02.501887+00:00'
  if f['path']=='captures/w05-direct-155.body':original='2026-11-08T06:22:43.890414+00:00'
  if not original:lim='No independent exact network-access timestamp assigned to this artifact; preserve original recorded-file time or receipt, not a reconstructed access time.'
  captures.append({'capture':ref(p),'original_accessed_at':original,'original_recorded_file_at':w.get('recorded_file_at'),'original_direct_receipt':a or None,'timestamp_limitation':lim})
 rows.append({'source_id':c['source_id'],'original_source_urls':c.get('urls',[c.get('url')]),'doi':c.get('doi'),'captures':captures,'original_source_scientist':'/root/peptone_ambiguous_sources','original_source_catalog_recorded_at':c['recorded_at'],'successor_read_by':'/root/buffer_tris','successor_read_at':now,'read_extent':c['read_extent'],'applicability':c['scope'],'source_claim':c['claim'],'preserve_prior_attribution':True})
put(S/'source-read-ledger.json',{'author':'/root/buffer_tris','at':now,'primary_capture_rows':rows,'raw_database':{'archive':ref(V/'other/captures/microbedecoder_database.zip'),'original_acquired_at':None,'reason':'Unavailable in original metadata; no invented timestamp. Exact ZIP and member bytes verified.','reextraction':ref(S/'source-observations.json'),'read_extent':'Complete original rows for all 130 scoped observations mechanically re-extracted and literal fields/taxa/source links independently verified. Five explicit generic label patterns inspected; all 114 PYG rows accounted as source scope, not 114 primary papers newly read.'},'complete_before_and_after_payloads':[{'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'after_capture':p['after_capture']} for p in P],'prior_peer_review':'Exact all-20 source claim peer report and actual reviewers preserved; no transfer of approval to new payloads.','contracts':['MAPPING_SEMANTICS.md §3 and §6','add-media and curate-yaml-record skills','ComponentAssertion/ComponentEvidence/StockComponent current schema','OUTCOME-CONTRACT-v1'], 'plans_verified':plans,'actual_new_network_fetches':0,'new_source_research_method':'Own applicability reassessment of immutable supplied primary captures and current complete payloads; prior real searches/access failures retained with original attribution.','unread_materials':access['unread_materials'],'scope_limitations':['Only relevant original-paper passages and original publisher abstracts inspected as explicitly recorded; no claim entire papers or all recipe bodies were accessible.','Captured publisher access errors and search previews are limitations, not chemistry evidence.','GYPS original source-specific Bacto negative control unchanged; Marine/RCM and other-worker consumers remain outside this editing lane.']})
put(S/'local-diagnostics.json',{'at':now,'items':['Read helper attempting BeautifulSoup failed because bs4 is unavailable; reran source HTML inspection using Python standard HTMLParser successfully. No payload affected.','Metadata inspection initially treated a list receipt as a dict; corrected read inspected complete list. No scientific mutation.','Two attempted path reads had no file at requested location; complete assigned contract and correct metadata were subsequently located/read. No absence claim based on those failures.','Initial unsealed evidence metadata used noncontract evidence-kind strings and local read times for issue captures. Native outcome contract reread prompted correction before peer seal; initial metadata preserved in draft-metadata-v1. Final source_snapshot enum and exact original GH access timestamps retained.','Additive case deltas now explicitly union actual child owner_records so constructor backlinks can verify each real beforeimage. No owner or source-case fabrication.'],'scientific_findings_added':0})
print(json.dumps({'final_evidence_sha256':h(S/'evidence.json'),'case_deltas_sha256':h(S/'case-deltas.json'),'source_read_ledger_sha256':h(S/'source-read-ledger.json'),'plan_verifications':plans},indent=2))
