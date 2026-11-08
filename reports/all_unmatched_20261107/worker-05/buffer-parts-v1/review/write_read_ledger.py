import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';Q=S/'review';B=R/'reports/all_unmatched_20261107/worker-05'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def j(p):return json.loads(Path(p).read_text())
def bind(p):return {'path':str(Path(p).relative_to(R)),'sha256':h(p)}
def cap(c):
 p=S/c['path'].split('buffer-parts-v1/',1)[1] if c['path'].startswith('buffer-parts-v1/') else B/c['path'];assert h(p)==c['sha256'];return p
entries=[]
for x in j(S/'parents/all-capture-index.json')['captures']:
 p=S/'parents/captures'/x['path'];assert h(p)==x['sha256']
 scope='Complete target term/concept metadata, definition, status, relevant annotations and returned hierarchy entries; no scientific approval of every descendant.'
 if 'search' in p.name:scope='Returned search results and query scope; search presence/absence alone is not identity evidence.'
 if p.name=='foodon-official-owl.json':scope='Full exact FOODON03315306 OWL class, restriction, relation and target class located within complete captured ontology; not a scientific review of all ontology classes.'
 if p.name=='mediadive75.json':scope='Complete ingredient75 response including names/identifiers; generic Soy label and material comparison, no imported catalog/CAS/product equivalence.'
 if p.name=='thermo.pdf':scope='Printed7,26,33 and49 scientific text; generic material definitions and product distinctions, not every page or lot assay.'
 entries.append({'lane':'parents','capture':bind(p),'original_capture_metadata':x,'reviewer':'/root/final_skeptical','actual_read_scope':scope})
md=j(S/'media/primary-read-ledger-v1.json')
for n in md['full_primary_documents']:
 p=S/'media'/n;entries.append({'lane':'media','capture':bind(p),'reviewer':'/root/final_skeptical','actual_read_scope':'Complete two-page manufacturer document: formula, preparation, quantities/basis/footnote, catalogue and supplied form. Independently inspected both rendered pages and extracted text.'})
for x in md['full_ontology_entries']:
 p=S/'media'/x['path'];assert h(p)==x['sha256'];entries.append({'lane':'media','capture':bind(p),'reviewer':'/root/final_skeptical','actual_read_scope':'Full target scientific ontology object: identity, structure/form, definition, synonyms/status and supplied annotations. Candidate used only within per-component applicability assessment.'})
seen=set()
for row in md['source_caption_objects']:
 for x in row['source_evidence']:
  c=x['capture'];p=cap(c)
  if str(p) in seen:continue
  seen.add(str(p));scope='Complete visible ingredient page or full solution JSON; namespace, source recipe, quantity and preparation context independently checked.'
  if p.suffix=='.pdf':scope='Complete PDF text: DSM1619 one page, DSM339 three pages or DSM339a two pages, including supplement and source catalogue scope.'
  if x['evidence_id'].startswith('M1193-SCOPE'):scope='Source-scope metadata/occurrence fields and exact retained captures; not a new primary review of every listed recipe.'
  entries.append({'lane':'media-captions','capture':bind(p),'reviewer':'/root/final_skeptical','evidence_id':x['evidence_id'],'original_capture_time':x.get('original_accessed_at'),'actual_read_scope':scope})
reuse=[]
for p in [B/'final-correction-v1/reviews/media/scientific-review-v2.json',R/'.temp/w05-final-correction-v1/review-media/scientific-review-v2.json',Q/'buffer-review-v1.json',Q/'chemical-report-scientific-review-v1.json',Q/'media-scientific-review-v1.json',Q/'dependencies/main-review.json']:
 if p.exists():reuse.append(bind(p))
v={'reviewer':'/root/final_skeptical','at':datetime.now(timezone.utc).isoformat(),'entries':entries,'complete_payload_scope':'All parent/media selected complete YAMLs and exact preimages were individually read, including historical fields. Later generic/Polypeptone/reference successors require their own exact read receipt.','existing_component_owner_scope':'28 matching existing native owners inspected for identity/mapping/chemistry/supplied-form fields; Agar and Starch complete files read. This is not 28 whole-owner scientific approvals.','frozen_source_scope':'Two Peptone original rows, Soy ingredient75 record and source/negative-hold metadata. All 200 Soy quarantine associations are retained byte-for-byte, not individually freshly approved. Four media caption source scopes are retained with their exact earlier evidence; no claim to a fresh review of hundreds of recipes.','reused_reviews':reuse,'attribution':'Earlier primary and skeptical authors retain their actual work. Current fresh source checks supplement only the declared scopes; unchanged historical interpretations are not silently reauthored.','scope_limit':'Hashes document exact read inputs and preserved reuse, not chemical correctness by themselves. Source acquisition times remain the actual original values; current review time is distinct.'}
p=Q/'parents-media-source-read-ledger-v1.json';assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(h(p),len(entries))
