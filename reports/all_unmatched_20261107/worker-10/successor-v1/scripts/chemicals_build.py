"""Reassess all 22 chemical no-proposal cases into an immutable successor fragment."""
import copy, csv, hashlib, json, re, subprocess, sys, yaml
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); P=ROOT/'reports/all_unmatched_20261107/worker-10'; S=P/'successor-v1'; O=S/'chemicals'
Q=ROOT.parents[2]/'queue/preliminary-v5'; SH=Q/'shards/shard-10.json'
NOW=datetime.now(timezone.utc).isoformat(); IX=json.loads((S/'assigned-no-proposal-cohort.json').read_text())['partitions']['chemicals']
OLD=json.loads((P/'decisions.json').read_text())['decisions']; OE={e['evidence_id']:e for e in json.loads((P/'evidence.json').read_text())['evidence']}; C=json.loads(SH.read_text())['cases']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cap=lambda p:{'root':'artifact','path':str(p.relative_to(P)),'sha256':sha(p)}
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def norm(s):return re.sub(r'[^a-z0-9]+','',s.casefold())
E=[];D=[];PR=[]
def evidence(key,p,kind,loc,claim,url=None,at=None):
 e=dict(evidence_id='sv1-chem-'+key,capture=cap(p),kind=kind,locator=loc,supports_or_contradicts=claim,url=url,accessed_at=at or NOW);E.append(e);return e['evidence_id']

# Python rglob includes ignored/hidden files. Also retain exact rg -uu command/output.
files=sorted((ROOT/'data/ingredients').rglob('*.yaml')); owners=[]
for f in files:
 o=yaml.safe_load(f.read_text()); owners.append((f,o))
li=ROOT/'docs/data/label_index.csv'; index=list(csv.DictReader(li.open()))
patterns={10:r'distilled.*water',14:r'terephthal',15:r'edta|ethylenediamin',27:r'aspart',29:r'distilled.*water',34:r'ore|pyrite|sulfidic|sulfitic',37:r'vanadat|navo3',43:r'penicillin|benzylpenicillin',47:r'ampicillin',52:r'distilled.*water',58:r'nickel.*ammonium|ammonium.*nickel|nh42ni|nickel.*sulf',63:r'ketoglutar|oxoglutar',66:r'distilled.*water',72:r'methoxyacet',74:r'junlon|polyacryl|propenoate|acrylate',76:r'k2hpo4|potassium.*phosph|phosph.*potassium',90:r'k2hpo4|potassium.*phosph|phosph.*potassium',91:r'k2hpo4|potassium.*phosph|phosph.*potassium',95:r'cobalamin|b12|vitamin.b.12',108:r'^acetate$|acetic acid',111:r'edta|ethylenediamin',116:r'aspart'}
look={}; context=[]
for i in IX:
 hits=[]
 for f,o in owners:
  labels=[o.get('identifier',''),o.get('preferred_term',''),o.get('ontology_mapping',{}).get('ontology_label','')]+[x.get('synonym_text','') for x in o.get('synonyms',[])]
  if any(re.search(patterns[i],s,re.I) for s in labels):
   target=O/'owners'/f.name
   if not target.exists():target.parent.mkdir(exist_ok=True);target.write_bytes(f.read_bytes())
   hits.append({'path':str(f.relative_to(ROOT)),'sha256':sha(f),'identifier':o.get('identifier'),'preferred_term':o.get('preferred_term'),'snapshot':cap(target),'matched_labels':[s for s in labels if re.search(patterns[i],s,re.I)]})
 query=C[i]['source_label']; r=subprocess.run(['rg','--no-ignore','--hidden','-n','-i','-F',query,'data/ingredients','docs/data/label_index.csv'],capture_output=True,text=True)
 look[str(i)]={'pattern':patterns[i],'raw_label':query,'candidate_owners':hits,'label_index_matches':[row for row in index if re.search(patterns[i],str(row),re.I)],'raw_rg_command':['rg','--no-ignore','--hidden','-n','-i','-F',query,'data/ingredients','docs/data/label_index.csv'],'raw_rg_exit':r.returncode,'raw_rg_stdout':r.stdout,'raw_rg_stderr':r.stderr}
 cctx=[]
 for occ in C[i]['occurrences']:
  f=Q/occ['full_recipe_snapshot'];assert sha(f)==occ['source_file_sha256'];doc=yaml.safe_load(f.read_text())
  cctx.append({'occurrence_id':occ['occurrence_id'],'recipe_id':occ['recipe_id'],'component_path':occ['component_path'],'snapshot_sha256':sha(f),'snapshot_path':occ['full_recipe_snapshot'],'full_document_keys':list(doc),'raw_component':occ['raw_component']})
 reused=[]
 for key in OLD[i]['evidence_ids']:
  e=OE[key]
  if e['kind'] in ['primary_source','ontology','source_snapshot']:
   root=P if e['capture']['root']=='artifact' else Q;f=root/e['capture']['path'];assert sha(f)==e['capture']['sha256'];f.read_bytes()
   reused.append({'evidence_id':key,'capture':e['capture'],'original_accessed_at':e.get('accessed_at'),'applicability':'Reassessed against this exact case and scope; original bytes/time retained, no inherited scientific approval.'})
 context.append({'case_index':i,'case_id':C[i]['case_id'],'occurrences':cctx,'primary_and_context_reuse':reused})
dump(O/'owner-lookup.json',{'at':NOW,'scope':'All maintained individual YAMLs via pathlib rglob (includes ignored/hidden), full label_index, and per-case rg --no-ignore --hidden','record_count':len(files),'label_index_sha256':sha(li),'case_lookups':look})
dump(O/'source-inspection.json',{'at':NOW,'cases':context})
lookid=evidence('owner-lookup',O/'owner-lookup.json','local_validation','case_lookups by exact zero-based shard index','Actual ignored-inclusive owner search and candidate inventory; lexical hits are not identity matches.')
ctxid=evidence('context',O/'source-inspection.json','source_snapshot','cases[].occurrences and primary_and_context_reuse','Complete frozen snapshots parsed and hashed for every assigned occurrence; exact predecessor primary capture bytes and original access times retained.')

# All actual HTTP outcomes, including failed retrievals, remain immutable.
F={}
for p in sorted(O.glob('*-receipts.json')):
 for r in json.loads(p.read_text()):
  if not r['exit_code']:
   f=P/r['path'];assert sha(f)==r['sha256'];F[r['key']]=evidence(r['key'],f,'ontology' if r['key'].startswith(('ols-','live-')) else 'primary_source','Full response; precise inspected fields and limits in each decision', 'Primary reference reassessed only where explicitly bound below; no source-case or export approval.',r['url'],r['accessed_at'])
  else:F[r['key']]=evidence(r['key']+'-failed',p,'unsuccessful_search',r['key'],'Actual public retrieval failed: '+r['stderr'],r['url'],r['accessed_at'])
for p in sorted(O.glob('*search*.json')):
 F[p.stem]=evidence(p.stem,p,'unsuccessful_search','actual search queries and returned snippets','Discovery search retained for transparency; snippets alone do not establish a source-specific purchase or identity.')
F['supplier-web-open']=evidence('supplier-web-open',O/'supplier-web-open.json','primary_source','Web tool parsed primary supplier pages; explicit CAS, formula and material labels','Direct primary supplier page comparison; does not establish that the recipe used these catalogue products. Full curl attempts failed and are preserved separately.')

# B12: inspect full provider solutions rather than stop after the four nested source records.
b12=[]
for j,occ in enumerate(C[95]['occurrences']):
 ids=[x['value'] for x in occ['recipe_source_identifiers']]; link=None
 for sid in ids:
  if sid.startswith('mediadive.medium:'):
   f=P/'chemicals/captures'/('md-medium-'+sid.split(':')[1]+'.json')
   if f.exists():
    doc=json.loads(f.read_text());rows=[{'solution_id':s['id'],'row':r} for s in doc.get('data',{}).get('solutions',[]) for r in s.get('recipe',[]) if r.get('compound_id')==1238]
    if rows: link={'capture':cap(f),'compound_id':1238,'rows':rows}
  if sid.startswith('mediadive.solution:'):
   f=P/'chemicals/captures'/('md-solution-'+sid.split(':')[1]+'.json');doc=json.loads(f.read_text());rows=[r for r in doc.get('data',{}).get('recipe',[]) if r.get('compound_id')==1238]
   if rows:link={'capture':cap(f),'compound_id':1238,'rows':rows}
 b12.append({'occurrence_id':occ['occurrence_id'],'source_identifiers':ids,'source_compound_link':link,'conclusion':'Existing Cyanocobalamin owner; no global B12 alias or quantity approval.' if link else 'Only generic B12 occurrence confirmed in this source. No transfer of MediaDive compound1238 identity across source versions.'})
dump(O/'b12-occurrence-assessment.json',{'at':NOW,'occurrences':b12,'specific_cyanocobalamin_links':sum(bool(x['source_compound_link']) for x in b12),'remaining_generic':sum(not x['source_compound_link'] for x in b12)})
B12ID=evidence('b12-occurrences',O/'b12-occurrence-assessment.json','source_snapshot','all20 occurrence entries','15 exact provider compound1238 links found; five distinct provider occurrences remain generic. Existing rejected global B12 labels are preserved.')

ASSESS={
10:('existing_identity_or_alias','The exact TOGO2547 row separates distilled water from its 960 ml amount. The complete existing Distilled_Water owner is already the intended identity. Owner lookup is complete; making an amount-bearing synonym or stock record would add no distinct substance.',None,'existing_owner_no_payload_needed',[]),
14:('stock_or_solution','The former decision unnecessarily deferred a source-defined preparation while waiting for a more-specific sodium-salt purchase. NBRC824 explicitly specifies a neutralized, filter-sterilized 0.2 M Na-terephthalate solution. A source-qualified local stock is supported at that nominal preparation scope. The raw chemical table row is not asserted globally equivalent to the whole stock, and no solvent, titrant, sodium stoichiometry, hydrate or final-medium dose is inferred.',None,'bounded_preparation_supported',['ols-na-stock']),
15:('unresolved','Completed owner lookup finds distinct anhydrous and dihydrate disodium-EDTA owners. TOGO2277 SL12 identifies disodium EDTA but not hydration. A primary Bonn laboratory SL12 (10x) protocol explicitly uses EDTA-Na2 dihydrate, while the source SL12 differs in Mn hydration and preparation; this independently used recipe cannot select the weighed form in the assigned source. This case is the individual solute, not a named stock node; inventing a source-local stock would change the reviewed entity.', 'The hydration of the weighed disodium-EDTA solute in TOGO2277 is not established by that recipe or an identified product; the independently used SL12 protocol is not the same formulation.','specific_scientific_fact_missing',['bonn-sl12']),
27:('unresolved','All nine frozen source occurrences remain separately bound. MediaDive compound228 states CAS3792-50-5 but its disodium formula/mass conflict with the primary supplier monosodium L-aspartate specification for that CAS. The supplier product is contrast evidence, not proof of what the DSMZ recipes used. This is an unresolved stoichiometric and form disagreement in an individual chemical input, not missing lookup or downstream units.', 'Authoritative source-specific correction selecting the intended mono/disodium salt and its stereochemical/hydration identity; no assumption from the inconsistent MediaDive calculated fields.','specific_scientific_fact_missing',['sodium-aspartate-monosodium','search4']),
29:('existing_identity_or_alias','The 100 ml phrase denotes the water input to the separately named neutralized-sulfide stock in TOGO3119. Complete owner lookup confirms Distilled_Water already owns the substance. Neither a whole-stock equivalence nor an amount-bearing global alias is needed.',None,'existing_owner_no_payload_needed',[]),
34:('new_distinct_ingredient_proposal','The KOMODO485 primary table defines an ore-material input and gives pyrite only as an example. Bounded owner lookup finds no owner for the source-described material. A local undefined-mixture proposal preserves that source-level ore category, without asserting an individual specimen, pyrite identity, mineralogy or composition. Missing specimen analysis limits specificity but does not prevent retaining the named source-material scope.',None,'bounded_material_supported',['ols-ore','metallosphaera-paper','dsmz-metallosphaera']),
37:('unresolved','The original ATCC1926 CENS PDF has now been retrieved and explicitly retains NaVO3.nH2O in True Blue Trace Elements. DSMZ748 independently retains nH2O. The primary supplier xhydrate listing gives a one-water formula and CAS20740-98-1, illustrating why a generic hydrate name is not independent proof of the source n value. Existing CHEBI132095 owner is a fixed monohydrate. This individual solute has no separately specified treatment or formulation boundary that would justify a stock proposal.', 'Water stoichiometry or a source-specific supplied-material specification for ATCC1926 NaVO3.nH2O; fixed monohydrate cannot replace the variable source notation.','specific_scientific_fact_missing',['atcc-cens','dsmz-cens','sodium-metavanadate-xhydrate']),
43:('stock_or_solution','NBRC823 identifies a filter-sterilized Penicillin G stock addition, but its table says20,000U/ml while its own preparation prose says200,000U/ml. This discrepancy blocks either quantitative strength claim; it does not block a source-qualified filtered Penicillin G stock identity with potency explicitly unresolved. Neither the free-acid owner nor a DRON injection/oral product is an exact stock owner. No salt, carrier or dilution is invented.',None,'bounded_preparation_supported',['ols-penicillin-stock']),
47:('existing_identity_or_alias','The exact DSMZ1144-derived Na-ampicillin input is already owned by Na-ampicillin/CHEBI34535. The parenthetical grants optional omission in a pure culture; it is not an ingredient name or a new preparation. Complete lookup and source review require no owner change.',None,'existing_owner_no_payload_needed',[]),
52:('existing_identity_or_alias','The four frozen recipes use a make-up instruction attached to distilled water. Owner lookup establishes the existing water identity; make-up language and source amounts are retained in the occurrence contexts. No scientific identity fact is missing and no distinct stock or global instructional synonym is justified.',None,'existing_owner_no_payload_needed',[]),
58:('unresolved','Full owner lookup and the primary Huber1986 publisher record/full-text attempt were examined. The accessible publisher abstract does not enumerate the MMS nickel reagent; the PDF request does not supply an inspectable full recipe. MediaDB144 itself gives no hydration. ChEBI86151/86149 distinguish anhydrous versus hexahydrate; both current MIM candidate labels point to86149 and their pre-existing registry concern remains. Molar normalization cannot establish the weighed substance.', 'The MMS original preparation or linked product specification identifying nickel-ammonium-sulfate water content; neither an abstract nor a computed mM value resolves this scientific form distinction.','specific_scientific_fact_missing',['huber-1986','huber-1986-pdf']),
63:('unresolved','NBRC1357 names potassium alpha-ketoglutarate at1g. The named E-MP96 product is the completed agar, not the reagent specification. Actual supplier/ontology searches distinguish a monopotassium purchase but do not tie it to NBRC1357; they do not establish potassium stoichiometry or hydration in the source. This individual weighed chemical is not a prepared stock whose qualitative boundary can be preserved independently.', 'A source-specific mono/dipotassium and hydration specification for the weighed NBRC1357 reagent; no linked product or preparation evidence was recovered.','specific_scientific_fact_missing',['search3','search5']),
66:('existing_identity_or_alias','Both TOGO2378/2618 occurrences denote water with a make-up instruction. The full owner search confirms Distilled_Water. No new ingredient, alias carrying to, fixed addition volume or stock identity is warranted.',None,'existing_owner_no_payload_needed',[]),
72:('unresolved','The bare-anion rule was explicitly reconsidered: CHEBI132097 correctly denotes methoxyacetate(-1), and a missing sodium counterion alone would not bar that named moiety. New primary DSMZ194 evidence, however, identifies Na-methoxyacetate for DSM5193, and the official culture catalogue connects DSM5193 to the archived478 KoMAc1 source. The archived version instead pairs unqualified methoxyacetate10mM with0.9g/L, while current sodium wording retains0.90g/L. These distinct source versions cannot be treated as one validated weighed form or exact formulation. The prior withdrawn anion payload remains withdrawn; no guessed historical acid/sodium form or stock strength is introduced.', 'Which supplied form the archived DSMZ478 source meant, in view of the specifically linked current sodium-salt instruction and incompatible historical molar/mass basis. A historical preparation/product specification or source correction is needed for an exact archived-case owner.','specific_scientific_fact_missing',['dsmz-194','komac1-catalog','komac1-paper','live-132097','live-132096']),
74:('new_distinct_ingredient_proposal','Reinspection of all four MediaDB253-256 complete source recipes and the Hobbs primary publication establishes Junlon PW110 polymer-additive scope; the imported Propenoate label and monomer-based molarity do not establish acrylate. The primary patent identifies the named PW110 trade material as a polyacrylic product; product-specific full composition and neutralization are not supplied. An opaque source-qualified Junlon PW110 preparation owner is now proposed, with no acrylate equivalence, components, invented molecular weight, source dose validation or active Propenoate alias.',None,'bounded_product_supported',['junlon-patent','ols-junlon']),
76:('existing_identity_or_alias','The exact trihydrate is scientifically established. Complete owner comparison finds a CAS16788-57-1 owner and a local trihydrate owner; the verified CAS record is the more-specific stable identifier already present under section3. Prepare the bounded exact-form alias on that existing CAS owner. This does not merge, rename or recertify either owner; the duplicate-owner conflict and all native withholding obligations remain for coordinator integration.',None,'bounded_existing_owner_proposal',[]),
90:('unresolved','The original OTEB supplier formulation and current indexed supplier revisions consistently identify dibasic potassium phosphate without hydration. A fresh historical supplier insert was requested and inspected; current insert URLs failed retrieval and their search captures remain explicitly limited. The anhydrous and trihydrate are distinct individual reagents. No evidence selects one for these3 exact recipe versions, and a complete-medium purchase does not supply the reagent form.', 'Hydration of the potassium dibasic phosphate input in the assigned OTEB/AS603 formulation versions, beyond the supplier term dibasic; no source-linked reagent specification recovered.','specific_scientific_fact_missing',['oteb-v1','oteb-2021','oteb-2025','chemsearch1']),
91:('existing_identity_or_alias','Both ATCC-derived sources explicitly identify the trihydrate. The existing CAS16788-57-1 owner is already the most-specific stable identity supported by the captured PubChem structure. A combined alias proposal also handles case76. The older unresolved owner-collision task does not imply missing scientific form evidence and is not a reason to leave this isolated proposal unfinished. Preserve the anhydrous owner rejected trihydrate label and both actual old owner hashes; no merge or publication release.',None,'bounded_existing_owner_proposal',[]),
95:('unresolved','The complete provider-recipe walk now establishes15 of20 occurrence-specific MediaDive compound1238 links to the existing cyanocobalamin owner, rather than stopping after the four nested solutions. The one KOMODO and four TOGO occurrences do not carry those same compound links, so their generic B12 cannot be automatically transferred to that vitamer. The existing Vitamin_B12 and Cyanocobalamin records already own the generic and specific senses. No owner mutation is needed for these source associations; existing mutual REJECTED_LABEL entries remain intact.', 'For the five explicitly enumerated generic occurrences only: a source-specific vitamer witness. Fifteen explicit provider links are complete and do not await this fact.','partial_existing_owner_associations',[]),
108:('existing_identity_or_alias','TOGO700 names acetate and expressly marks its dose as final concentration. The bare-anion CHEBI30089 owner already exists; neither a salt purchase nor a stock identity is inferred. Owner lookup is complete and the instructional suffix requires no global synonym.',None,'existing_owner_no_payload_needed',[]),
111:('existing_identity_or_alias','The original ATCC37 PDF was recovered. Its Heavy Metal Solution prints the misspelled Ethlyene Diamine Tetraacetate and immediately instructs Dissolve EDTA first, explicitly linking the source spelling to EDTA. The existing Edta owner preserves the repository-reviewed free-acid naming convention and separate disodium owners. A bounded spelling-alias proposal is supported without inventing an EDTA salt, charge state, hydrate, stock equivalence or procurement specification.',None,'bounded_existing_owner_proposal',['atcc-chromatium']),
116:('unresolved','The NBRC1278 primary recipe was searched and reread in full. It independently names Sodium aspartate without stereochemistry, sodium stoichiometry or hydration; the trace-stock KOH adjustment does not identify this separate weighed reagent. Actual primary supplier searches establish multiple distinct purchasable sodium-aspartate forms but none is linked to NBRC1278. Neither MediaDive228 nor its conflicting fields belong to this source.', 'NBRC1278 source-specific sodium stoichiometry, stereochemistry and hydration of the individual reagent; an unrelated supplier CAS or source228 cannot select them.','specific_scientific_fact_missing',['sodium-aspartate-monosodium','search3','search4'])
}
for i in IX:
 d=copy.deepcopy(OLD[i]);dis,why,missing,category,keys=ASSESS[i]
 if dis=='stock_or_solution':dis='stock_product_mixture_context'
 if i in [27,37,116]:keys=keys+['supplier-web-open']
 d.update(disposition=dis,reasoning=why,missing_requirement=missing,no_change_reason=(why if i not in [14,34,43,74,76,91,111] else None),proposal_ids=[],author='Codex /root worker10 successor primary chemical reviewer',independent_review={'status':'pending','evidence_ids':[]})
 d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[lookid,ctxid]+[F[k] for k in keys if k in F]+([B12ID] if i==95 else [])))
 d['completion_reassessment']={'at':NOW,'supersedes_published_head':'dbaf4629f3b93d3bd8a78028e243abfe90c7a922','prior_decision_capture':cap(P/'decisions.json'),'prior_case_index':i,'classification':category,'owner_lookup_evidence_id':lookid,'actual_primary_search_evidence_ids':[F[k] for k in keys if k in F],'bounded_preparation_assessed':True,'more_specific_product_or_quantity_information_separated_from_identity':True,'precise_remaining_scientific_fact':missing,'native_holds':'All inherited WITHHOLD/REJECTED source, owner and export dispositions retained. No source quantity, role or whole-record approval.'}
 D.append(d)

# Guarded writes land only in private scratch. Exact validated bytes are copied into proposals.
sys.path.insert(0,str(ROOT/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
SCRATCH=ROOT/'.temp/all-unmatched-worker-10/successor-v1/chemicals-guarded';SCRATCH.mkdir(parents=True,exist_ok=True)
def proposal(indices,stem,record=None,existing=None):
 pid='sv1-chem-proposal-'+str(indices[0]); why=' '.join(ASSESS[i][1] for i in indices)
 op=ROOT/'data/ingredients/mapped'/((existing or stem)+'.yaml');before=sha(op) if existing else None
 if existing:
  record=yaml.safe_load(op.read_text())
  for i in indices:record.setdefault('synonyms',[]).append({'synonym_text':C[i]['source_label'],'synonym_type':'RAW_TEXT','source':'CultureMech source-case '+C[i]['case_id']})
 record_curation_event(record,curator='all_unmatched_worker10_successor_source_review',action='ADDED_SYNONYMS' if existing else 'CREATED_FROM_SOURCE_REVIEW',changes=why+' Isolated proposal only; no owner, mapping-output or role release.',new_status='MAPPED',llm_assisted=True)
 f=SCRATCH/(stem+'.yaml');write_validated_ingredient(record,f)
 out=O/'proposed'/f.name;out.parent.mkdir(exist_ok=True);out.write_bytes(f.read_bytes())
 eids=list(dict.fromkeys(e for d in D if d['case_id'] in [C[i]['case_id'] for i in indices] for e in d['evidence_ids']))
 p={'proposal_id':pid,'case_ids':[C[i]['case_id'] for i in indices],'description':why,'evidence_ids':eids,'owner_path':str(op.relative_to(ROOT)),'kind':'edit_existing_owner' if existing else 'new_owner','after_capture':cap(out),'before_sha256':before,'identity_consequences':'Existing identifier and all inherited source evidence/holds retained; spelling alias only.' if existing else 'Distinct bounded source preparation; no exact equivalence to related solute/product or another source preparation.','predicate_consequences':'Existing mapping predicates unchanged; no release of held aliases or owner.' if existing else 'Own local identity registry row only; no new ontology-parent equivalence.','publication_review_obligations':'All source-specific native holds remain. Coordinator must reconcile duplicate owners/cross-shard proposals, revalidate content-bound full synonym/form/identity payload, withdraw inherited approvals on changed bytes, synchronize surfaces and rebuild only in a separately authorized integration stage.','cross_shard_conflict':'Compare this actual frozen before hash and all candidate owners; no cross-worker bytes adopted and no merge performed.'}
 PR.append(p)
 for d in D:
  if d['case_id'] in p['case_ids']:d['proposal_ids']=[pid];d['no_change_reason']=None
 if existing:assert sha(op)==before
def local(stem,label,typ,source,notes,component=None):
 ident='kgmicrobe.ingredient:'+stem.lower();r={'identifier':ident,'preferred_term':label,'mapping_status':'MAPPED','ingredient_type':typ,'ontology_mapping':{'ontology_id':ident,'ontology_label':label,'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':source,'notes':notes}]},'synonyms':[],'curation_history':[]}
 if typ=='STOCK_SOLUTION':r['solution_type']='OTHER'
 if component:
  r['components']=[{'component_name':component,'reference_scope':'UNMAPPED'}]
  r['component_assertion']={'method':'RECIPE_TRANSCRIPTION','completeness':'PARTIAL','evidence':[{'evidence_type':'RECIPE_SOURCE','source':source,'notes':notes+' Named input only; exact supplied salt, carrier/titrant and quantities are not asserted.'}]}
 return r
proposal([14],'Nbrc_824_neutralized_0_2_m_na_terephthalate_stock',local('Nbrc_824_neutralized_0_2_m_na_terephthalate_stock','NBRC824 neutralized 0.2 M Na-terephthalate stock','STOCK_SOLUTION','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=824',ASSESS[14][1],'Na-terephthalate (supplied salt form unspecified)'))
proposal([34],'Komodo_485_ore_material',local('Komodo_485_ore_material','KOMODO485 ore material (pyrite given as example)','UNDEFINED_MIXTURE','https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=485',ASSESS[34][1]))
proposal([43],'Nbrc_823_filtered_penicillin_g_stock',local('Nbrc_823_filtered_penicillin_g_stock','NBRC823 filter-sterilized Penicillin G stock (potency unresolved)','STOCK_SOLUTION','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=823',ASSESS[43][1],'Penicillin G (supplied salt form unspecified)'))
jun=local('Junlon_pw110_hobbs_source','Junlon PW110 (Hobbs source product)','UNDEFINED_MIXTURE','https://link.springer.com/article/10.1007/BF00258408; https://patents.google.com/patent/US5010120A/en',ASSESS[74][1]);jun['synonyms']=[{'synonym_text':'Propenoate','synonym_type':'REJECTED_LABEL','source':'MediaDB253-256 imported monomer annotation; polymer source context contradicts exact monomer identity'}]
proposal([74],'Junlon_pw110_hobbs_source',jun)
proposal([76,91],'Potassium_Phosphate_Dibasic_Trihydrate',existing='Potassium_Phosphate_Dibasic_Trihydrate')
proposal([111],'Edta',existing='Edta')
dump(O/'decisions.json',{'schema_version':1,'worker_slot':10,'shard_sha256':sha(SH),'phase':'shard','decisions':D})
dump(O/'evidence.json',{'schema_version':1,'evidence':E})
dump(O/'proposals.json',{'schema_version':1,'proposals':PR})
dump(O/'guarded-write-receipt.json',{'at':NOW,'python':sys.version,'writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','destination':'private scratch only; exact validated bytes copied into immutable successor proposals','proposals':[{'proposal_id':p['proposal_id'],'payload':p['after_capture'],'before_sha256':p['before_sha256']} for p in PR]})
print(json.dumps({'decisions':len(D),'proposals':len(PR),'proposed_cases':sum(bool(d['proposal_ids']) for d in D),'evidence':len(E),'owners_scanned':len(files),'b12_specific':sum(bool(x['source_compound_link']) for x in b12)}))
