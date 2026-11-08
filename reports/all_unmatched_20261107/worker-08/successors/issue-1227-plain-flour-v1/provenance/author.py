"""Single immutable proposal correction for filed W08-FINAL-001."""
import copy,datetime,hashlib,json,sqlite3,subprocess
from pathlib import Path
import yaml
from mediaingredientmech.utils.ontology_client import OntologyClient
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ROOT=Path.cwd(); P=ROOT/'.temp/all-unmatched-worker-08/plain-flour-method-v1'
A=ROOT/'reports/all_unmatched_20261107/worker-08'
OLD=A/'successors/issue-1227-v1/final-v2'
OUT=A/'successors/issue-1227-plain-flour-v1'
CASE='KG_CASE:b9a6261315d83792bc02bfbe425cda2032c8833c7a3b6de3aa665fa62a7fc03e'
PID='op1201-plain-flour';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
def ref(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()=='1701ccf2049022866adfcebcc9bba9b6492407c6'
OUT.mkdir(exist_ok=False)
oldp=next(x for x in read(OLD/'proposals.json')['proposals'] if x['proposal_id']==PID)
oldd=next(x for x in read(OLD/'decisions.json')['decisions'] if x['case_id']==CASE)
payload=A/oldp['after_capture']['path'];assert sha(payload)=='aa8390f17f1ed9f9c083fd6b487ee1c40228e754072b7e390b97dfb2fd6eae83'
oldrec=yaml.safe_load(payload.read_text());rec=copy.deepcopy(oldrec)
cap=A/'successors/issue-1201-v1/shared-primary/ols-foodon-00004510.json'
assert sha(cap)=='48c4ece85b7193af6fee377601cc481e86a02b92ae637534a9fd1baf53315c98'
term=read(cap)['_embedded']['terms'][0]
assert term['obo_id']=='FOODON:00004510' and term['label']=='flour' and term['synonyms']==['flour added'] and not term['is_obsolete']
client=OntologyClient();adapter=client._get_adapter('FOODON');label=adapter.label('FOODON:00004510')
assert label=='flour',label
db=Path('/Users/marcin/.data/oaklib/foodon.db')
cx=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True);cx.row_factory=sqlite3.Row
sql="SELECT subject,predicate,object,value FROM statements WHERE predicate IN ('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym','oio:hasBroadSynonym','oio:hasNarrowSynonym') AND lower(value) IN ('flour','plain flour','flour added') ORDER BY subject,predicate,value"
rows=[dict(x) for x in cx.execute(sql)]
meta=[dict(x) for x in cx.execute("SELECT subject,predicate,object,value FROM statements WHERE predicate IN ('owl:versionIRI','owl:versionInfo')")]
cx.close()
assert any(x['subject']=='FOODON:00004510' and x['predicate']=='rdfs:label' and x['value']=='flour' for x in rows)
save(OUT/'research/primary-label-resolution.json',{'at':NOW,'native_adapter_label':label,'target':'FOODON:00004510','adopted_preferred_term':'flour','mapping_grade':'EXACT_MATCH','method':'New native primary-label resolution of the explicitly adopted generic material label; not the historical lookup of raw Plain flour.','database':{'path':str(db),'size':db.stat().st_size,'sha256':sha(db),'metadata':meta},'sql':sql,'rows':rows,'original_primary_capture':ref(cap),'original_primary_accessed_at':'2026-11-08T05:57:13.916914+00:00','raw_source_label_is_established_ontology_synonym':False,'CAS_lookup_performed':False})
scope='The record is reviewed at the generic flour material scope under MAPPING_SEMANTICS section3 step4. The frozen MediaDive ingredient1465 record and its original primary page name Plain flour as a complex substance, without establishing a grain, supplier, catalogue, bleaching/fortification treatment or defined composition. The page flags identifiers as automatically matched; its CAS is not adopted. This agent-assisted material-scope judgment is separate from lexical resolution and grants no product equivalence, owner merge, role or export approval.'
lexical='The archived official FOODON:00004510 response has primary label flour, definition A fine powder made from cereals or other starchy food sources, and captured synonym flour added. A new native label check resolves the adopted preferred_term flour to that primary label. EXACT_MATCH describes this current primary-label resolution under MAPPING_SEMANTICS section0. It does not assert that raw Plain flour was a primary label, a unique ontology synonym, or resolved by CAS; the earlier material-scope judgment was not an exact lexical lookup.'
rec['preferred_term']='flour'
rec['notes'] += '\n\nW08-FINAL-001 correction: '+scope+' '+lexical+' The original Plain flour RAW_TEXT synonym and stable owner filename remain unchanged.'
rec['ontology_mapping']['evidence'][0]['notes']=lexical
rec['ontology_mapping']['evidence'].append({'evidence_type':'LLM_SUGGESTION','source':'https://bacmedia.dsmz.de/ingredients/1465','notes':scope+' Source facts use the original capture from2026-11-08T05:16:12.135246+00:00; no new remote source retrieval is claimed.'})
rec['curation_history'].append({'timestamp':NOW,'curator':'worker08:/root W08-FINAL-001 proposal correction','action':'REVIEW_CORRECTION','changes':'Filed issue1227 comment6719268318 identifies the unsupported earlier EXACT_MATCH method claim for preferred label Plain flour. Preserve that history as history. Reassess the unchanged generic flour material scope under section3 step4, adopt the verified primary label flour, and perform a new native primary-label resolution supporting current EXACT_MATCH under section0. Separate ontology DATABASE_MATCH facts from the explicitly LLM-assisted material-scope judgment; raw Plain flour remains unchanged RAW_TEXT provenance. No synonym lookup of Plain flour, CAS lookup, grain/product specificity, identity-target change, owner merge or role/export approval is claimed. Original source captures, frozen owner beforeimage and all prior source holds remain unchanged.','previous_status':'MAPPED','new_status':'MAPPED','llm_assisted':True,'llm_model':'GPT-6'})
dst=OUT/'payloads/Plain_Flour.yaml';dst.parent.mkdir()
write_validated_ingredient(rec,dst)
assert yaml.safe_load(dst.read_text())==rec
assert rec['curation_history'][:-1]==oldrec['curation_history']
assert rec['synonyms']==oldrec['synonyms'] and rec['identifier']==oldrec['identifier']
proposal=copy.deepcopy(oldp);proposal['after_capture']=ref(dst)
proposal['description']=scope+' Current preferred_term flour has a separately recorded new primary-label resolution; raw Plain flour is preserved and is not claimed as an ontology synonym.'
proposal['evidence_ids'] += ['w08-final001-label-resolution','w08-final001-author-assessment','w08-final001-filed-comment','w08-final001-root-finding']
proposal['publication_review_obligations'].append('W08-FINAL-001: retain stable original owner/filename and source label; no grain/product/role expansion or owner merge. The new preferred flour label and primary-label method require exact successor scientific and skeptical review.')
decision=copy.deepcopy(oldd);decision['reasoning']=proposal['description'];decision['evidence_ids']=proposal['evidence_ids']
decision.setdefault('prior_independent_reviews',[]).append(decision['independent_review'])
decision['independent_review']={'status':'pending','evidence_ids':[]};decision['primary_reviewer']='worker08:/root; W08-FINAL-001 author, not independent approval'
decision['issue_refs'].append('https://github.com/CultureBotAI/MediaIngredientMech/issues/1227#issuecomment-6719268318')
save(OUT/'author/proposal.json',proposal);save(OUT/'author/decision.json',decision)
save(OUT/'author/assessment.json',{'at':NOW,'author':'worker08:/root','finding':'W08-FINAL-001','reviewed_predecessor_head':'1701ccf2049022866adfcebcc9bba9b6492407c6','case_id':CASE,'proposal_id':PID,'original_owner_before_sha256':oldp['before_sha256'],'predecessor_payload':oldp['after_capture'],'successor_payload':ref(dst),'changed_fields':['preferred_term','notes (appended clarification)','ontology_mapping.evidence[0].notes','ontology_mapping.evidence[1] (new LLM_SUGGESTION)','curation_history[5] (new event)'],'unchanged_mapping_quality':'EXACT_MATCH; now supported by a newly recorded primary-label resolution of adopted generic label, not a retroactive claim about Plain flour','scope_assessment':scope,'lexical_assessment':lexical,'preserved_fields':[k for k in oldrec if k not in ['preferred_term','notes','ontology_mapping','curation_history']],'full_record':{'components':'Absent before/after; no composition invented.','roles':'Absent before/after; no source roles approved.','occurrence_statistics':'Original values unchanged; no newly established frequency.','aliases':'Original RAW_TEXT Plain flour and source remain exact.','chemical_properties':'Absent; automated CAS is not imported.','identity':'Same FOODON00004510, same original owner path/beforeimage. No merge.'},'independent_review':'pending','source_evidence_ids':['op-case-180','op-plain-flour-primary','op1201-ols-foodon-00004510'],'scientific_release_approval':False})
save(P/'acceptance.json',{'at':NOW,'head':'1701ccf2049022866adfcebcc9bba9b6492407c6','branch':'review/all-unmatched-w08-source-review-20261107','finding_sha256':sha(P/'inputs/finding-001-plain-flour-method.json'),'filed_comment_sha256':sha(P/'inputs/issue1227-comment6719268318.json'),'predecessor_selection':str(OLD.relative_to(ROOT)),'public_successor':str(OUT.relative_to(ROOT)),'sealed_w06_seal_sha256':sha(ROOT/'.temp/w06-residual-successor-independent-v1/SEAL.json'),'sealed_w06_manifest_sha256':sha(ROOT/'.temp/w06-residual-successor-independent-v1/MANIFEST.json'),'case_scope':[CASE],'proposal_scope':[PID],'new_external_sessions':False,'maintained_edits':False})
print(json.dumps({'payload':ref(dst),'author_assessment':ref(OUT/'author/assessment.json'),'native_label':label,'ontology_query_rows':len(rows)},indent=2))
