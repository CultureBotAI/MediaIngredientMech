import copy, datetime, hashlib, json, re, subprocess
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event

B=Path('reports/all_unmatched_20261107/worker-04')
S=B/'successors/issue-1201-v1'
F=S/'fragments'; C=S/'captures/chemistry'; P=S/'proposals/chemistry'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
A=json.loads((F/'chemistry-assignment.json').read_text())['cases']
cases={x['index']:x for x in A}
old_e={x['evidence_id']:x for x in json.loads((B/'evidence.json').read_text())['evidence']}
evidence=[]; proposals=[]; decisions={}; specs={}; bindings={}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def cap(p): return {'root':'artifact','path':str(Path(p).relative_to(B)),'sha256':sha(p)}
def dump(p,x): Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ev(key,p,kind,notes,url=None,accessed=None,locator='Complete captured bytes'):
 eid='I1201-CHEM-'+key
 r={'evidence_id':eid,'kind':kind,'capture':cap(p),'locator':locator,'supports_or_contradicts':notes,'url':url}
 if accessed:r['accessed_at']=accessed
 evidence.append(r);return eid
def addnote(n,text,missing=None,changed=False,disposition=None):
 specs[n]={'assessment':text,'missing_fact':missing,'changed':changed,'disposition':disposition}
def propose(key,nums,record,name,description,owner=None,extra_eids=()):
 pid='I1201-CHEM-P-'+key;before=sha(owner) if owner else None
 if owner:
  assert not any(p['owner_path']==owner for p in proposals)
  original=yaml.safe_load(Path(owner).read_text())
 else:original=None
 record_curation_event(record,curator='codex_worker04_chemistry_issue1201',action='CORRECTED' if owner else 'CREATED',changes=description+' Isolated successor proposal only; no maintained surfaces, roles, source bytes or publication holds changed.',previous_status=original['mapping_status'] if original else None,new_status=record['mapping_status'],llm_assisted=True,timestamp=now)
 path=P/(name+'.after.yaml');write_validated_ingredient(record,path)
 peids=list(dict.fromkeys([z for n in nums for z in cases[n]['published_decision']['evidence_ids']]+['I1201-CHEM-lookup-'+str(n) for n in nums]+list(extra_eids)))
 pr={'proposal_id':pid,'supersedes_proposal_ids':[],'case_ids':[cases[n]['frozen_case']['case_id'] for n in nums],'description':description,'evidence_ids':peids,'owner_path':owner or 'data/ingredients/mapped/'+name+'.yaml','kind':'edit_existing_owner' if owner else 'new_owner','after_capture':cap(path),'before_sha256':before,'publication_obligations':['Preserve all inherited source and publication holds.','Withdraw inherited complete-payload support; require independent review of these exact bytes.','Synchronize owner/aggregate/SSSOM only during separately guarded coordinator integration.','For asymmetric mappings emit skos:broadMatch, never identity or subclass; emit mandatory registry rows under Section 2/Rule B1.','Do not resolve rejected raw labels globally or infer recipe doses from stock concentrations.'],'cross_shard_owner_conflict':'Coordinator compares original e000 owner hashes and all published/successor proposals; no last-writer-wins.'}
 if owner:
  cp=C/'owners'/Path(owner).name;cp.parent.mkdir(parents=True,exist_ok=True);cp.write_bytes(Path(owner).read_bytes());pr['evidence_ids'].append(ev('owner-'+Path(owner).stem,cp,'source_snapshot','Exact original e000 baseline owner before this isolated proposal; full history and prior claims preserved.'))
  if '/unmapped/' in owner and record['mapping_status']=='MAPPED':pr['destination_owner_path']=owner.replace('/unmapped/','/mapped/')
 proposals.append(pr)
 for n in nums:bindings.setdefault(n,[]).append(pid)
 return pr
def chemical(ident,label,parent,parentlabel,notes,source,aliases=(),formula=None,cas=None):
 r={'identifier':ident,'preferred_term':label,'mapping_status':'MAPPED','ingredient_type':'SINGLE_INGREDIENT','ontology_mapping':{'ontology_id':parent or ident,'ontology_label':parentlabel or label,'ontology_source':parent.split(':')[0] if parent else ident.split(':')[0],'mapping_quality':'EXACT_MATCH' if parent==ident else 'NARROW_MATCH' if parent else 'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':source,'notes':notes}]},'synonyms':[{'synonym_text':x,'synonym_type':'HYDRATE_FORM' if 'hydrate' in label else 'EXACT_SYNONYM','source':source} for x in aliases],'notes':notes,'curation_history':[]}
 if formula or cas:r['chemical_properties']={'data_source':source,**({'molecular_formula':formula} if formula else {}),**({'cas_rn':cas} if cas else {})}
 return r
def stock(key,n,label,solute,value,unit,url,notes):
 ident='kgmicrobe.ingredient:'+key
 r={'identifier':ident,'preferred_term':label,'mapping_status':'MAPPED','ingredient_type':'STOCK_SOLUTION','solution_type':'OTHER','ontology_mapping':{'ontology_id':ident,'ontology_label':label,'ontology_source':'kgmicrobe.ingredient','mapping_quality':'FALLBACK_REGISTRY','evidence':[{'evidence_type':'MANUAL_CURATION','source':url,'notes':'Source-qualified stock identity with partial literal component assertion. '+notes}]},'synonyms':[{'synonym_text':cases[n]['frozen_case']['raw_source_label'],'synonym_type':'REJECTED_LABEL','source':url}],'components':[{'component_name':solute,'reference_scope':'UNMAPPED','concentration_value':value,'concentration_unit':unit}],'component_assertion':{'method':'RECIPE_TRANSCRIPTION','completeness':'PARTIAL','evidence':[{'evidence_type':'RECIPE_SOURCE','source':url,'source_record':label,'notes':notes}],'notes':'Unstated solvent and source chemical-form details remain unasserted. Concentration is the stock claim, never the receiving-medium dose.'},'notes':notes,'curation_history':[]}
 if key=='nbrc_1378_fenaedta_stock':
  r.pop('synonyms'); r['notes']+=' Exact raw source label FeNaEDTA is retained as provenance only, not a globally resolving stock alias.'
 return propose(key,[n],r,label.replace(' ','_'),notes)

# Actual ignored-inclusive preflight receipts, plus reinspection integrity of every reused capture.
for x in A:
 n=x['index'];ev('lookup-'+str(n),C/f'lookup-{n:03}.json','source_snapshot','Executed ignored-inclusive baseline owner/label-index and published 63-proposal lookup; all related original case links retained. Not an ontology absence claim.')
verified=[]
for n,x in cases.items():
 for eid in x['published_decision']['evidence_ids']:
  if eid.startswith('independent-'):continue
  e=old_e[eid]; c=e.get('capture')
  if not c:continue
  p=(B if c['root']=='artifact' else Q)/c['path']; got=sha(p);assert got==c['sha256'],(n,eid,p)
  verified.append({'index':n,'evidence_id':eid,'capture':c,'sha256_verified':got})
dump(C/'reused-capture-integrity.json',{'checked_at':now,'captures':verified,'original_retrieval_times_preserved':True})
integrity_id=ev('reused-capture-integrity',C/'reused-capture-integrity.json','source_snapshot','Every reused source, full frozen recipe, owner, ontology and issue capture was read and byte-verified against its published digest; no retrieval time relabeling.')
newid={}
for receipt in ['retrievals.json','retrievals-rsc.json','retrievals-rsc-retry.json','retrievals-rsc-network.json','retrievals-final.json','retrievals-parent.json']:
 if not (C/receipt).exists():continue
 for j,r in enumerate(json.loads((C/receipt).read_text())):
  key=re.sub(r'[^A-Za-z0-9-]','-',r['name'])+'-'+receipt.replace('.json','')
  p=B/r['path'] if 'path' in r else C/receipt
  kind='unsuccessful_search' if 'error' in r else 'ontology' if r['name'].startswith('ols-') else 'primary_source'
  eid=ev(key,p,kind,'Actual retrieval outcome: '+r.get('error','response captured; source claims must be interpreted within the case-specific reasoning.'),r['url'],r['accessed_at'],'Receipt '+receipt+' row '+str(j))
  if 'error' not in r:newid[r['name']]=eid
for name in ['hydrate-searches.json','form-searches.json','source-and-form-searches.json','web-followup.json']:
 if (C/name).exists():ev(name.replace('.json',''),C/name,'unsuccessful_search','Bounded discovery results and failures. Search excerpts are discovery leads, not independently inspected supplier or physical-phase proof.')
mgid=ev('mg-trace',C/'mg-trace/trace.json','source_snapshot','Read-only CultureMech checkout and historical occurrence-output trace: five exact Mg-citrate rows belong to MediaDive404 lineage; separate sixth Magnesium citrate row is BD220908. Current checkout is not claimed live main and old count provenance is not silently rewritten.')
issue655id=ev('issue655-reconciliation',C/'issue655-reconciliation.json','source_snapshot','Fresh issue inventory matches unchanged open issue655 body with zero comments. Alias recommendation is lexical/owner-based and supplies no JCM904-specific sodium-count or L-stereo evidence.')
for p in sorted((C/'mg-trace').glob('*.yaml')):ev('mg-recipe-'+p.stem,p,'source_snapshot','Complete additional local CultureMech recipe context; trace.json identifies provenance and the local checkout revision. Not additional assigned cases.')

# Case-specific reassessments. A retained hold names a chemical/source fact, never unfinished lookup.
addnote(4,'Complete TOGO2692 protocol was reread and compared with the published TOGO2809 TiCl3 stock proposal. The 50 ml recipe is bounded, but TiCl2 precursor and titanium(III) title are a direct oxidation-state contradiction; a registry wrapper would not repair it. The two preparations are not equivalent.', 'Authoritative correction selecting TiCl2 (TiII) or TiCl3 (TiIII) in this 50 ml preparation; no missing stock-volume work remains.')
addnote(6,'Ignored-inclusive search finds only the L-specific potassium glutamate monohydrate owner. Rechecked the manufacturer Raka-Ray218671 formula and DSMZ1047 lineage: neither supplies optical configuration, hydration or a reagent catalogue. Food-additive L-monopotassium examples are not evidence for this product ingredient.', 'Source-specific potassium glutamate salt/hydrate and optical sense. No unspecified-sense exact term was established; do not invent an exact L identity.')
addnote(10,'The recovered JCM401 PDF explicitly supplies 5 mM quinic acid as a stock addition. Its receiving-medium 13 ml/1 ml water inconsistency does not prevent a source-qualified partial stock record. No solvent, stereochemistry or final-medium concentration is invented.', 'Stock solvent and optical form remain unspecified; receiving-medium volume inconsistency remains an independent source correction.',True,'stock_product_mixture_context')
addnote(13,'Re-read all 13 frozen recipe occurrences and the inspected Lovley1988 methods. A shared model mnemonic fe3dcit is not a material specification; Lovley states Fe(III)-citrate, not dicitrate. The cohort spans different papers and cannot be assigned one ligand ratio or one stock. Existing ferric citrate, monohydrate and ferrous owners do not resolve it.', 'Occurrence-specific source material or preparation distinguishing ferric-citrate reagent from modeled iron(3+) dicitrate(3-), including counterions when a salt was supplied.')
addnote(19,'DSMZ403 BSK source retains Na-citrate without sodium stoichiometry. Baseline and published-proposal searches found the mono/di/tri distinctions, rejected duplicate dihydrate owners and the new penta candidate; none supplies source-specific evidence to choose a salt.', 'BSK reagent sodium stoichiometry and hydration; the legacy local ID is not independent evidence.')
for n,source in [(27,'CCAP TAP'),(73,'CCAP Waris-H')]:
 addnote(n,f'{source} primary recipe explicitly specifies Na2EDTA.2H2O. Fresh owner/history inspection shows Na2-edta_X_2_H2o is REJECTED (#321/#360), not a competing active owner. Select existing active Na2edta2h2o CHEBI:64758 for this occurrence; preserve the truncated raw label as source provenance without a global alias or unnecessary owner edit.',None,True,'existing_identity_or_alias')
addnote(30,'DSMZ878 defines the reagent as 0.01 M Fe citrate stock and adds 0.5 ml. The flattened g/L discrepancy belongs to the receiving-medium transcription. A partial source-qualified stock can retain 0.01 M literally while leaving iron valence, citrate ratio and solvent ungrounded.', 'Stock solute oxidation state/ligand ratio and solvent remain unspecified; no mass conversion or molecular exact identity is authorized.',True,'stock_product_mixture_context')
for n in [31,148]:addnote(n,'Original DSMZ906 and ingredient825 preserve five waters. Independent ILO/WHO ICSC1220 explicitly identifies trisodium citrate pentahydrate, CAS6858-44-2 and C6H5Na3O7.5H2O. FAO/JECFA instead says pentahemihydrate and is not corroboration of the five-water identity. Bounded OLS exact-form search has no hit. A distinct CAS owner anchored by ICSC with asymmetric parent mapping completes the work; anhydrous, dihydrate and pentahemihydrate forms remain distinct.',None,True,'new_distinct_ingredient_proposal')
addnote(32,'NBRC1632 itself repeats Mo7O4 rather than Mo7O24. Existing tetrahydrate and orthomolybdate owners and their published proposals were compared. Charge/formula discrepancy is not a missing synonym or ontology lookup.', 'A source erratum or reagent specification resolving O4 versus O24 in the molybdate fragment.')
addnote(47,'JCM904 explicitly prints sodium glutamate·H2O, fixing one water but neither sodium count nor optical configuration. Independent review challenged a draft monosodium registry proposal: both its C5H8NO4.Na.H2O formula and parent CHEBI64220 would add one-sodium specificity absent from the recipe. That draft is withdrawn. The existing CHEBI232425 monohydrate is L-monosodium-specific. Full issue655 recommends adding this alias because a hydrate owner exists, but supplies no source-specific salt/stereo evidence; fresh issue body is unchanged with zero comments. Owner CAS6106-04-3 derives from automated name lookup, not a JCM904 supplier record. The historical recommendation is preserved but does not override unresolved source senses.', 'Source-specific sodium stoichiometry and optical sense are missing; one water is established. No guessed monosodium formula or L-specific CAS is admitted.',True,'unresolved')
addnote(54,'The full TOGO2978 micronutrient context and both molybdate owners were compared. Literal (NH4)6(MO7)24 cannot be turned into heptamolybdate by a spelling alias; uppercase MO and grouping are chemically unresolved.', 'Correct element case, molybdate oxygen count/grouping and hydration from an authoritative reagent specification or source correction.')
addnote(59,'NBRC392,931 and809 explicitly specify Na2WO4·H2O across four frozen occurrences. No competing formula appears in those source recipes. Absence of an exact ontology/CAS and prevalence of dihydrate are not evidence to discard the stated one-water form. Propose its own registry identity with sodium-tungstate parent; report source-stated hydration without claiming a characterized crystal phase.', 'Independent physical-phase or supplier verification remains unasserted, but is not required to preserve this explicit source form; no conversion to common dihydrate.',True,'new_distinct_ingredient_proposal')
for n in [60,150]:addnote(n,'Ignored-inclusive search located existing UNMAPPED0852 Trisodium_Citrate_X_3_H2o, split under #882/#1021 specifically to prevent anhydrous/dihydrate collapse. DSMZ661 explicitly states three waters and five frozen occurrences preserve it. PubChem18421636 structurally represents that formula, but depositor-derived metadata is not supplier proof; attempted RSC primary PDFs failed. Promote the existing distinct form to a registry identity with an asymmetric trisodium-citrate parent, retaining its history and explicit three-water aliases. No new duplicate owner.', 'No measured crystal-phase or supplier certification is claimed; the identity preserves the primary recipe-stated trihydrate and cannot be normalized to dihydrate.',True,'new_distinct_ingredient_proposal')
addnote(62,'Rechecked Lee2009 Table4 row13 and its AAM-minus omission against all three frozen recipes. D-glutamate in the AAM-minus row is contradicted by primary experimental methods; the two Klein1979 recipes remain separately unresolved after the recorded 403 full-text attempt. Existing acid/anion/stereo owners cannot repair the heterogeneous source rows.', 'Correct/remove the Lee2009 AAM-minus D-glutamate entry from source-supported recipe semantics; recover Klein1979 original reagent/table evidence for its two occurrences. No cross-paper stereo extrapolation.')
addnote(63,'Full NBRC1378 defines a named solution and says dissolve alpha-ketoglutamate20mM, filter and store4C; the main recipe adds5ml. The sodium-bearing heading and malformed solute name do not identify what was dissolved. A registry solution wrapper with 20mM as a chemical assertion would conceal the unresolved material. Recorded as a bounded source preparation candidate in evidence, not a ready ingredient identity.', 'Identify the actual solute (ketoglutamate versus ketoglutarate), sodium stoichiometry and hydration. The20mM statement is source text, not a validated chemical concentration.',True,'unresolved')
addnote(80,'Located and inspected the original Hoshino/Satoh1985 S-medium formula. Its succinate/phosphate/ammonium/gelatin/Noble-agar recipe matches the frozen source and prints NaCl0.2g, resolving NaCI as a source transcription error. Select existing sodium-chloride owner for this occurrence; retain NaCI solely as raw source provenance.',None,True,'existing_identity_or_alias')
addnote(87,'Primary NBRC1109 says ammonium tartrate without one/two ammonium ions or stereochemistry. Compared the existing ammonium and diammonium/L terms and live supplier/discovery results. Generic name alone does not select diammonium L-tartrate.', 'Source reagent ammonium stoichiometry and optical sense; no source catalogue or explicit formula establishes them.')
addnote(90,'Fresh primary MediaDiveP5 bytes match the frozen capture and explicitly name Myo-Inositol(B7) separately from Biotin(B8). The chemical-bearing label unambiguously states myo-inositol in its own stock; the vitamin-number annotation is misleading and is not promoted to an alias or role. Select existing myo-inositol owner for this source component only, without adding the complete annotated string globally.',None,True,'existing_identity_or_alias')
addnote(95,'Compared full frozen anaerobic-butyrate RM recipe with ferric, ferrous and dicitrate owners. Retried TOGO3181 successfully: its original quoted method still says Fe-Citrate0.01g, while a GMO enrichment labels it Iron(III)citrate. The same enrichment mislabels MgSO4·7H2O as potassium phosphate dibasic, so that label is not independent source reagent evidence. The original method supplies neither oxidation state nor citrate ratio; medium redox conditions cannot identify the purchased reagent.', 'Original RM iron-citrate reagent or preparation specifying iron valence, ligand ratio/counterions and hydrate form.')
addnote(102,'JCM713 primary trace-mineral formula itself prints Mo7O7·4H2O. Full source and the correctly defined tetrahydrate proposal were compared; the other solution components do not justify changing O7 to O24.', 'A source correction or authenticated reagent formula resolving the oxygen count; not missing owner lookup.')
for n in [107,139]:addnote(n,'DSMZ863 prints NaWO4·6H2O whereas ingredient803 and the frozen labels have Na2WO4·6H2O. This is a primary sodium-count conflict in addition to unusual hydration, unlike the coherent one-water NBRC formulas. Neither existing dihydrate owner nor its published repair can absorb this case.', 'An authoritative DSMZ863 correction or reagent specification resolving sodium stoichiometry and confirming hydration.')
addnote(119,'NBRC943 explicitly specifies (NH4)6Mo7O24·2H2O9.25mg in modified Hutner solution. Formula is chemically coherent and no competing primary recipe formula was found. Exact tetrahydrate term86244 is not an identity match; its own prose says heptahydrate despite four-water formula, so formula/structure take precedence. Preserve a distinct source-stated two-water registry identity without replacing its waters.', 'Physical-phase characterization and catalogue are unasserted; no evidence supports changing the explicit two-water source formula.',True,'new_distinct_ingredient_proposal')
addnote(120,'Full NBRC1378 separately defines FeNaEDTA solution as578mg/L and annotates1.5mM, then adds5ml to medium. Proposed partial stock retains the directly stated mass concentration. The mass/molarity pair must not be used to infer monohydrate; source solute form and the frozen578g/L transcription remain separate unresolved issues.', 'Source ferric-sodium-EDTA hydration and the578mg/L versus1.5mM relationship remain unverified; no molarity conversion or pure-solute exact mapping.',True,'stock_product_mixture_context')
addnote(125,'Original DSMZ1005 says Na2-EDTA0.04g, directly contradicting TOGO2734 Na3EDTA. Compared the published Na3-edta proposal, which is scoped to separate NBRC sources. This case must not join its trisodium alias expansion.', 'Authoritative correction choosing disodium versus trisodium for this source, with supplied hydration if specified.')
addnote(126,'Full TOGO2240 comment identifies50mM Tris-HC1 in the final Mycoplasma medium, not a separately prepared50mM stock. No source URL, acid/base recipe, solvent or premixed-stock definition is present. Existing pure Tris or hydrochloride owners and published HEPES stock cannot supply that missing preparation. Do not create a fictitious50mM stock.', 'The actual supplied buffer preparation (or original paper naming its reagent) and confirmation of HC1/HCl; final-medium50mM/pH7.6 alone do not specify an isolated stock.',True,'stock_product_mixture_context')
for n,ident in [(132,'CHEBI:115156'),(147,'CHEBI:63037'),(151,'CHEBI:131839'),(172,'CHEBI:42334'),(186,'CHEBI:115156')]:addnote(n,'Fresh ignored-inclusive owner, label-index, published-proposal and all188-case comparison confirms the existing '+ident+' identity and source-compatible spelling. No missing alias or second owner is needed. Existing full-payload and source publication holds remain separate from this already-resolved source interpretation.',None)
addnote(138,'Rechecked both sodium-citrate owners and #704. Na2-citrate is already rejected on the trisodium owner; source706 still contradicts its own label through automatic trisodium CAS/formula/molarity. The new penta/tri source-form proposals do not resolve sodium count in706.', 'Source-specific two-versus-three sodium correction; automatic metadata and arithmetic are correlated and not independent reagent proof.')
addnote(154,'Ignored-inclusive baseline/proposal lookup finds Ardacin A/B/C lexical placeholders only; prior exact primary discovery did not establish an authenticated ardacinB structure. A new registry name would duplicate the existing placeholder without resolving identity.', 'A primary isolation/structure or supplier record connecting the originating vocabulary to the exact ardacinB material.')
addnote(157,'Completed actual five-occurrence trace rather than deferring it. Historical/current occurrence outputs and six full local recipes show five exact Mg-citrate rows from DSMZ354/solution694/compound404, including two variants and KOMODO; sixth broader Magnesium citrate row is independently BD220908 with an erroneous hydroxide localID and is excluded. Original DSMZ354 merely says Mg-citrate. Compound404 CAS144-23-0, formula and g/mmol agreement support a source-metadata interpretation of1:1 magnesium hydrogen citrate, but are correlated enrichment rather than independent procurement proof. Prepare distinct CHEBI131389 owner without global Mg-citrate alias; do not reverse #320 or assign all five historical occurrences to it automatically.', 'A source reagent/CAS independent of MediaDive automatic enrichment is still needed before releasing the source404→1:1 claim or reassigning historical occurrences. Existing3:2 owner remains held and unchanged.',True,'new_distinct_ingredient_proposal')
addnote(159,'Rechecked #896/#878 and both sulfite owners. Source1201 label says five waters while CAS7757-83-7,126.043mass and conversion are anhydrous. This direct internal conflict differs from a coherent explicit hydrate with only missing ontology. No source choice is repaired by minting a speculative pentahydrate.', 'Original reagent specification or source correction selecting verified pentahydrate versus anhydrous sodium sulfite; inherited issue896 remains the exact tracker.')
addnote(162,'Re-inspected the saved1955 PubMed bibliographic record and prior original-title/JSTAGE discovery, plus ignored-inclusive Grisamine owner search. Neither source identifies the precise graph-node product or a verified structure. Duplicate lexical registry creation is not progress.', 'Original1955 isolation/structure text or authenticated product specification and a link to this source vocabulary; not a guessed griseofulvin identity.')
addnote(169,'Fresh complete owner history disproves the prior duplicate-owner prerequisite: one64758 owner is already REJECTED and the active survivor is known. Ingredient676 still has a real dihydrate-label versus anhydrousCAS139-33-3/336.206mass conflict; owner deduplication cannot fix that source fact.', 'Verify source676 hydration against an independent reagent specification or correction; recalculate molarity only after the form is established.',True,'unresolved')
addnote(170,'Re-read the complete acid owner history: June16 research-based merge treated alpha-ketoglutamate as alpha-ketoglutarate and then equated it with the acid. Even if typo correction is accepted, CHEBI16810 defines the dianion whereas30915 is the acid; the history is not source2384 procurement proof. Propose changing the ambiguous global alias to rejected provenance while retaining the historical merge event and all role data.', 'Source2384 must specify the corrected chemical name and supplied acid/salt/hydrate before its identity can be released.',True,'unresolved')
for n in [174,184]:addnote(n,'The inspected Welsch1947 original pages identify actinomycetin as crude culture filtrate potentially containing multiple active agents. This is sufficient to repair the existing placeholder owner from auto-classified SINGLE_INGREDIENT to UNDEFINED_MIXTURE now. It is not sufficient to promote a molecular identifier or assert one exact product formulation; both independent source cases remain attached.', 'Particular source preparation/strain or product specification remains needed for formulation-specific identity; the mixture-type correction is independently justified.',True,'stock_product_mixture_context')
addnote(175,'Existing64758 duplicate prerequisite was false because the older record is already rejected; the active disodium dihydrate owner is known. Ingredient890 itself still omits sodium count and conflicts with its anhydrous automaticCAS/mass, so the CCAP27/73 evidence cannot be transferred globally.', 'Source890 sodium stoichiometry and hydration, independently of anhydrous automatic metadata; no remaining owner-consolidation prerequisite.',True,'unresolved')

# Bounded stock payloads.
stock('jcm_401_quinic_acid_5mm_stock',10,'JCM 401 quinic acid 5 mM stock','Quinic acid','5','mM','https://bacmedia.dsmz.de/pdf/J401',specs[10]['assessment']+' '+specs[10]['missing_fact'])
stock('dsmz_878_fe_citrate_001m_stock',30,'DSMZ 878 Fe citrate 0.01 M stock','Fe citrate','0.01','M','https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium878.pdf',specs[30]['assessment']+' '+specs[30]['missing_fact'])
stock('nbrc_1378_fenaedta_stock',120,'NBRC 1378 FeNaEDTA stock','FeNaEDTA','578','mg/L','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1378',specs[120]['assessment']+' '+specs[120]['missing_fact'])

# Distinct source-reported forms, never parent exact identity.
notes=specs[31]['assessment']+' Source identity is CAS6858-44-2; the nearest parent CHEBI53258 is not the hydrate identity.'
r=chemical('cas:6858-44-2','Trisodium citrate pentahydrate','CHEBI:53258','sodium citrate',notes,'https://inchem.org/documents/icsc/icsc/eics1220.htm',['Na3-citrate x 5 H2O'],formula='C6H5Na3O7.5H2O',cas='6858-44-2')
propose('trisodium-citrate-pentahydrate',[31,148],r,'Trisodium_Citrate_Pentahydrate',notes,extra_eids=[newid['icsc-citrate-pentahydrate.html'],newid['jecfa-citrate.pdf'],newid['ols-citrate-pentahydrate.json']])
# Withdraw the unreviewed draft identified as over-specific by independent review.
withdrawn=P/'Monosodium_Glutamate_Monohydrate_Unspecified.after.yaml'
cp=C/'withdrawn-drafts'/withdrawn.name
if withdrawn.exists():
 cp.parent.mkdir(parents=True,exist_ok=True);cp.write_bytes(withdrawn.read_bytes());withdrawn.unlink()
if cp.exists():
 ev('withdrawn-case47-draft',cp,'source_snapshot','Rejected unreviewed draft; not a proposal or accepted ingredient. Independent review found unsupported monosodium stoichiometry and formula.')
notes=specs[59]['assessment']+' No supplierCAS or crystal-phase measurement is inferred.'
r=chemical('kgmicrobe.compound:sodium_tungstate_monohydrate','Sodium tungstate monohydrate','CHEBI:63940','sodium tungstate',notes,'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=392',['Na2WO4·H2O'],formula='Na2WO4.H2O')
propose('sodium-tungstate-monohydrate',[59],r,'Sodium_Tungstate_Monohydrate',notes)
owner='data/ingredients/unmapped/Trisodium_Citrate_X_3_H2o.yaml';r=yaml.safe_load(Path(owner).read_text());notes=specs[60]['assessment']
r['identifier']='kgmicrobe.compound:trisodium_citrate_trihydrate';r['mapping_status']='MAPPED';r['ontology_mapping']={'ontology_id':'CHEBI:53258','ontology_label':'sodium citrate','ontology_source':'CHEBI','mapping_quality':'NARROW_MATCH','evidence':[{'evidence_type':'MANUAL_CURATION','source':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium661.pdf','notes':notes}]};r['synonyms'].append({'synonym_text':'Na3-citrate x 3 H2O','synonym_type':'HYDRATE_FORM','source':'DSMZ661 / MediaDive650'});r['notes']+=' Successor proposal: '+notes;r['chemical_properties']={'molecular_formula':'C6H5Na3O7.3H2O','data_source':'DSMZ661 explicit source formula; formal transcription, not measured crystallography.'}
propose('trisodium-citrate-trihydrate',[60,150],r,'Trisodium_Citrate_X_3_H2o',notes,owner,extra_eids=[newid['pubchem-citrate-trihydrate.json'],newid['ols-citrate-trihydrate.json']])
notes=specs[119]['assessment']+' No exact ontology term or CAS is asserted; registry identity preserves the stated formula.'
r=chemical('kgmicrobe.compound:hexaammonium_heptamolybdate_dihydrate','Hexaammonium heptamolybdate dihydrate','CHEBI:35505','hydrate',notes+' Bounded exact hexaammonium search finds only the distinct tetrahydrate; CHEBI35505 is the verified general hydrate-class anchor, not a claim of exact parent identity.','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=943',['(NH4)6Mo7O24·2H2O'],formula='(NH4)6Mo7O24.2H2O')
propose('hexaammonium-heptamolybdate-dihydrate',[119],r,'Hexaammonium_Heptamolybdate_Dihydrate',notes,extra_eids=[newid['ols-hydrate-35505.json'],newid['ols-hexaammonium-heptamolybdate.json']])
notes=specs[157]['assessment']+' '+specs[157]['missing_fact']
r=chemical('CHEBI:131389','Magnesium hydrogen citrate (1:1)','CHEBI:131389','magnesium citrate',notes,'https://www.ebi.ac.uk/chebi/CHEBI:131389',[],formula='C6H6MgO7',cas='144-23-0');r['synonyms']=[{'synonym_text':'Mg-citrate','synonym_type':'REJECTED_LABEL','source':'MediaDive404; ambiguous global name retained as provenance'}]
propose('magnesium-hydrogen-citrate',[157],r,'Magnesium_Hydrogen_Citrate',notes,extra_eids=[mgid,newid['dsmz354.pdf']])
owner='data/ingredients/mapped/Actinomycetin.yaml';r=yaml.safe_load(Path(owner).read_text());r['ingredient_type']='UNDEFINED_MIXTURE';r['notes']+=' Primary Welsch1947 pp101–102 defines crude culture filtrate, possibly containing more than one active agent. Correct type only; legacy placeholder identity, source holds and lack of exact formulation remain.'
r['ontology_mapping']['evidence'].append({'evidence_type':'MANUAL_CURATION','source':'Welsch1947, Bacteriological Reviews11:99–148, original pp101–102','notes':'Primary preparation description contradicts automatic SINGLE_INGREDIENT classification; no exact compound or formulation promotion.'})
propose('actinomycetin-mixture-type',[174,184],r,'Actinomycetin',specs[174]['assessment'],owner)
owner='data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml';r=yaml.safe_load(Path(owner).read_text());next(x for x in r['synonyms'] if x['synonym_text']=='alpha-ketoglutamate')['synonym_type']='REJECTED_LABEL';r['notes']=(r.get('notes','')+' Successor review: source2384 does not establish that alpha-ketoglutamate denotes the acid; prior typo interpretation is historical, not proof of protonation/salt identity. Preserve exact original alias/source as rejected provenance.').strip()
propose('ketoglutamate-acid-alias-rejection',[170],r,'Alpha-ketoglutaric_Acid',specs[170]['assessment'],owner)

# Exact source bindings to unchanged owners avoid unnecessary global aliases.
sourcebindings={27:('CHEBI:64758','data/ingredients/mapped/Na2edta2h2o.yaml'),73:('CHEBI:64758','data/ingredients/mapped/Na2edta2h2o.yaml'),80:('CHEBI:26710','data/ingredients/mapped/Nacl.yaml'),90:('CHEBI:17268','data/ingredients/mapped/Myo-inositol.yaml')}
for n,(ident,p) in list(sourcebindings.items()):
 if not Path(p).exists():
  matches=[q for q in Path('data/ingredients').rglob('*.yaml') if yaml.safe_load(q.read_text()).get('identifier')==ident and yaml.safe_load(q.read_text()).get('mapping_status')!='REJECTED'];assert len(matches)==1,(ident,matches);sourcebindings[n]=(ident,str(matches[0]))
reassessments=[]
for n,x in cases.items():
 sp=specs[n];old=x['published_decision'];look=json.loads((C/f'lookup-{n:03}.json').read_text())
 ids=['I1201-CHEM-lookup-'+str(n),integrity_id]
 if n in [31,148]:ids += [newid['icsc-citrate-pentahydrate.html'],newid['jecfa-citrate.pdf']]
 if n in [60,150]:ids += [newid['pubchem-citrate-trihydrate.json'],newid['ols-citrate-trihydrate.json']]
 if n==80:ids += [newid['s-medium-1985.pdf']]
 if n==90:ids += [newid['mediadive-p5.html']]
 if n==157:ids += [mgid,newid['dsmz354.pdf']]
 if n==47:ids += [newid['ols-sodium-glutamate-hydrate.json'],issue655id]
 if n==95 and 'togo-3181.json' in newid:ids += [newid['togo-3181.json']]
 if sp['changed']:
  d=copy.deepcopy(old);d.update(reasoning=sp['assessment'],missing_requirement=sp['missing_fact'],no_change_reason=None if n in bindings or n in sourcebindings else sp['missing_fact'],proposal_ids=bindings.get(n,[]),disposition=sp['disposition'] or old['disposition'],independent_review={'status':'pending','evidence_ids':[]});d['evidence_ids']=list(dict.fromkeys(old['evidence_ids']+ids));d['supersedes_decision_sha256']=digest(old)
  if n in sourcebindings:
   ident,p=sourcebindings[n];d['source_binding']={'identifier':ident,'owner_path':p,'owner_sha256':sha(p),'scope':'Only this exact frozen source case and listed occurrences; no new global synonym.'}
   cp=C/'owners'/Path(p).name;cp.parent.mkdir(parents=True,exist_ok=True);cp.write_bytes(Path(p).read_bytes());eid='I1201-CHEM-binding-owner-'+Path(p).stem
   if not any(e['evidence_id']==eid for e in evidence):ev('binding-owner-'+Path(p).stem,cp,'source_snapshot','Complete active owner bytes checked for this source-specific binding; no alias or owner mutation proposed.')
   d['evidence_ids'].append(eid)
  for pr in proposals:
   if d['case_id'] in pr['case_ids']:
    d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+pr['evidence_ids']))
    if pr['before_sha256'] and not any(z['path']==pr['owner_path'] for z in d['owner_records']):d['owner_records'].append({'path':pr['owner_path'],'sha256':pr['before_sha256']})
  decisions[n]=d
 reassessments.append({'index':n,'case_id':x['frozen_case']['case_id'],'predecessor_decision_sha256':digest(old),'decision_hash_encoding':'canonical JSON sort_keys=True,separators=(comma,colon),ensure_ascii=False UTF-8','outcome':'changed' if sp['changed'] else 'kept','assessment':sp['assessment'],'missing_fact':sp['missing_fact'],'actual_work':{'lookup_capture':cap(C/f'lookup-{n:03}.json'),'commands':look['commands'],'ignored_files_included':True,'returncodes':look['returncodes'],'source_capture_integrity':integrity_id,'published_proposals_compared':look['published_proposal_hits'],'related_original_cases':look['related_original_cases']},'evidence_ids':list(dict.fromkeys(old['evidence_ids']+ids)),'proposal_ids':bindings.get(n,[]),'all_inherited_holds_preserved':True})
assert len(reassessments)==44
for e in evidence:
 e['case_ids']=sorted({d['case_id'] for d in decisions.values() if e['evidence_id'] in d['evidence_ids']}|{r['case_id'] for r in reassessments if e['evidence_id'] in r['evidence_ids']}|{c for p in proposals if e['evidence_id'] in p['evidence_ids'] for c in p['case_ids']})
dump(F/'chemistry-reassessments.json',{'reassessments':reassessments})
dump(F/'chemistry-decisions.json',{'decisions':[decisions[n] for n in sorted(decisions)]})
dump(F/'chemistry-evidence.json',{'evidence':evidence})
dump(F/'chemistry-proposals.json',{'proposals':proposals})
dump(C/'guarded-write-receipt.json',{'written_at':now,'command':'PYTHONPATH=src .temp/all-unmatched-worker-04/venv/bin/python -B '+str(F/'chemistry-successor.py'),'closed_linkml_guard':'mediaingredientmech.validation.write_validated.write_validated_ingredient','payloads':[x['after_capture'] for x in proposals],'all_passed':True,'maintained_files_written':False})
print(json.dumps({'reassessed':len(reassessments),'changed':len(decisions),'proposals':len(proposals),'evidence':len(evidence),'hashes':{p.name:sha(p) for p in F.glob('chemistry-*.json') if 'assignment' not in p.name}},indent=2))
