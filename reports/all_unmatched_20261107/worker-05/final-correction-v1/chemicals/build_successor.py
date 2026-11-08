"""Author's private report-only successor. No maintained paths are written."""
from pathlib import Path
from datetime import datetime, timezone
import copy, difflib, hashlib, json, re, yaml, sys
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient

O = Path(__file__).resolve().parent
R = Path('reports/all_unmatched_20261107/worker-05').resolve()
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P = json.loads((O/'input-proposals.json').read_text())
D = json.loads((O/'input-decisions.json').read_text())
E = json.loads((O/'input-evidence.json').read_text())
AUTHOR = 'Codex worker05 /root/chemicals_research final report correction'
NOW = datetime.now(timezone.utc).isoformat()
def sha(x): return hashlib.sha256(x).hexdigest()
def objsha(x): return sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def dump(path, x):
    assert not path.exists(), path
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ref(path): return {'root':'artifact','path':'final-correction-v1/chemicals/'+str(path.relative_to(O)),'sha256':sha(path.read_bytes())}
def event(d,s):
    record_curation_event(d,curator=AUTHOR,action='CORRECTED_REPORT_PROPOSAL',changes=s,previous_status=d['mapping_status'],new_status=d['mapping_status'],llm_assisted=True,llm_model='gpt-6',timestamp=NOW)
def note(d,s): d['notes']=(d.get('notes','').strip()+' '+s).strip()
def evidence(d,url,s): d['ontology_mapping'].setdefault('evidence',[]).append({'evidence_type':'LLM_SUGGESTION','source':url,'notes':s})

suggestions=json.loads((O/'w02-exact-entry-suggestions.json').read_text())
typed={x['proposal_id']:x for x in suggestions}
types=[]; ancestry=[]; alias_dispositions=[]; conditional=[]; out=[]
sources={
 'CHEM-PROP-dextrose': {'Dextrose (BD 215530)':'https://www.bd.com/en-us/products-and-solutions/products/product-page.215530'},
 'CHEM-PROP-iron': {'Iron (powder, 20 - 60 mesh, Nacalai)':'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=673'},
 'CHEM-PROP-formate': {'NaCOOH':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3211'},
 'CHEM-PROP-magnesium-heptahydrate': {'MgSO .7H 0':'https://www.ccap.ac.uk/wp-content/uploads/MR_E27.pdf ; https://www.ccap.ac.uk/wp-content/uploads/MR_E31.pdf ; https://www.ccap.ac.uk/wp-content/uploads/MR_E31_ANT.pdf','MgSO 7H O':'https://www.ccap.ac.uk/wp-content/uploads/MR_TAP.pdf'},
 'CHEM-PROP-sulfur': {'So(Sulfur Powder)':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2553','Ground sulfur powder':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3129'},
 'CHEM-PROP-riboflavin': {'RibofIavin':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3161'},
 'CHEM-PROP-manganese-tetrahydrate': {'MnCI2.4H2O':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3120 ; https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2367 ; https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2277'},
 'CHEM-PROP-niacin': {'Niacin (B3)':'https://mediadive.dsmz.de/medium/P5'},
 'CHEM-PROP-thiamine-hcl': {'Thiamine HCl (B1)':'https://mediadive.dsmz.de/medium/P5'},
 'CHEM-PROP-hepes': {'N-2-hydroxyethylpiperazine-N-2-ethanesulfonic acid (HEPES, Sigma Chemical Co., St. Louis, MO)':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2410'},
 'CHEM-PROP-tpp-stock': {'Thiamine pyrophosphate (0.2% w/v in water)':'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2577'}
}
hepes='NBRC 1221 and NBRC 1474 each name a 1 M HEPES-KOH stock and add 20 ml. The reported pH values 7.14 and 9.0 belong to the receiving media. Stock pH, neutralization ratio and solvent are unreported. These omissions prove neither equality nor difference. The two accessions support the same bounded nominal preparation description; whether one shared nominal owner or a more specific source-supported representation should be installed remains a coordinator decision under #1237. This identifier is retained only as a conditional historical proposal handle, not a selected stable owner. Do not install both candidates as proven distinct substances. Preserve both source and occurrence routes, all component uncertainty and all inherited holds.'
wolfe_acid='JCM 470 and DSMZ 792 describe the same fourteen named salt inputs and quantities in 1000 ml water, acidified to pH 1 with diluted sulfuric acid. JCM writes MnSO4·xH2O while DSMZ specifies the monohydrate; x is not established to differ from 1. This is compatible evidence with unresolved reagent hydration, not proof of different preparations. Source accessions and their occurrence routes remain separate provenance. The identifier is a conditional historical proposal handle; no winning owner, merge, simultaneous installation or complete component grounding is approved. Coordinator reconciliation under #1237 must preserve both source assertions, pH method and all inherited holds.'
wolfe_modified='ATCC 1190/1191 and JCM 221 list the same thirteen non-water input names and amounts, including NTA and cobalt nitrate hexahydrate. ATCC explicitly specifies MnSO4 monohydrate and anhydrous calcium chloride, alum and selenite; JCM uses variable manganese hydration and omits those other hydration qualifiers. Omitted qualifiers do not establish anhydrous identity or a different formulation. Preserve the source-specific fields without reconciling them by assumption. The source-qualified identifiers remain conditional historical proposal handles pending #1237; no winning owner, merge or simultaneous installation as distinct substances is approved. Existing Modified_Wolfes_Minerals has a different documented input list and is a separate comparison dependency. All inherited holds remain.'
ethanol='The source names a nominal 95% ethanol preparation. The percentage basis, solvent balance, denaturants and historical product specification are unreported. Different source accessions or receiving stocks prove neither equal nor different supplied preparations. A shared bounded nominal representation is a possible coordinator outcome; exact historical formulation equality and a final owner choice remain unresolved under #1237. This identifier is retained only as a conditional historical proposal handle. Do not install all four candidates as proven distinct substances. Retain all 17 precise occurrence routes and the original source lineages. CHEBI:16236 grounds the named ethanol component only; NCIT:C185110 is not approved because it specifically requires aqueous 95% by volume. No numerical component percentage, water balance or whole-stock molecular identity is inferred. All inherited holds remain.'
conditional_text={**{p:hepes for p in ['CHEM-C1193-HEPES-1221','CHEM-C1193-HEPES-1474']},**{p:wolfe_acid for p in ['R1193-P-wolfe470','R1193-P-wolfe792']},**{p:wolfe_modified for p in ['R1193-P-wolfe1190','R1193-P-wolfe221']},**{p:ethanol for p in ['CHEM-C1193-ethanol95-atcc_1490','CHEM-C1193-ethanol95-atcc_1257','CHEM-C1193-ethanol95-atcc_1524','CHEM-C1193-ethanol95-dsmz_78']}}
def reject(d, texts, why, eid):
    found=[]
    for s in d.get('synonyms',[]):
        if s['synonym_text'] in texts:
            old=copy.deepcopy(s);s['synonym_type']='REJECTED_LABEL';found.append(s['synonym_text'])
            alias_dispositions.append({'proposal_id':pid,'before':old,'after':copy.deepcopy(s),'disposition':'reviewed_non_identity_on_this_owner','reason':why,'evidence_ids':[eid]})
    assert set(found)==set(texts),(pid,found,texts)
    note(d,why);changes.append(why)

for p0 in P:
    p=copy.deepcopy(p0);pid=p['proposal_id'];path=R/p['after_capture']['path'];before=path.read_bytes();assert sha(before)==p['after_capture']['sha256']
    original=yaml.safe_load(before);d=copy.deepcopy(original);changes=[]
    if p.get('before_sha256'):
        assert sha(Path(p['owner_path']).read_bytes())==p['before_sha256'],p['owner_path']
    if pid in typed:
        s=typed[pid];assert s['payload_sha256']==sha(before)
        idx=int(re.search(r'\[(\d+)\]',s['field'])[1]);e=d['ontology_mapping']['evidence'][idx]
        assert objsha(e)==s['full_value_sha256'];assert e['evidence_type']=='MANUAL_CURATION'
        old=copy.deepcopy(e);e['evidence_type']='LLM_SUGGESTION'
        types.append({'proposal_id':pid,'field':s['field'],'before':old,'after_type':'LLM_SUGGESTION','w02_audit_row_id':s['audit_row_id'],'before_object_sha256':objsha(old)})
        changes.append('Correct only the exact new campaign MappingEvidence entry identified by the W02 provenance audit from MANUAL_CURATION to LLM_SUGGESTION. Preserve inherited evidence and ComponentAssertion evidence types.')
    if pid in sources:
        for text,url in sources[pid].items():
            rows=[s for s in d['synonyms'] if s['synonym_text']==text];assert len(rows)==1,(pid,text)
            old=copy.deepcopy(rows[0]);rows[0]['source']=url
            alias_dispositions.append({'proposal_id':pid,'before':old,'after':copy.deepcopy(rows[0]),'disposition':'preserved_identity_with_exact_primary_provenance','reason':'The linked recipe or manufacturer capture identifies this reagent at its original stock/medium position. The campaign author is recorded in history rather than used as the source of the literal.'})
        changes.append('Replace campaign-only provenance on the newly proposed source aliases with their exact primary recipe or supplier locators; retain the complete labels, types and historical authorship.')
    if pid in conditional_text:
        text=conditional_text[pid]
        # Keep exact source and quantitative fields, replace current scientific inference.
        raw=d.get('notes','').split('Verbatim source-only labels retained as provenance, excluded from globally resolving aliases:')
        preserved=(' Verbatim source-only labels retained as provenance, excluded from globally resolving aliases:'+raw[1]) if len(raw)>1 else ''
        d['notes']=text+preserved
        for e in d.get('ontology_mapping',{}).get('evidence',[]):
            if e['evidence_type']=='LLM_SUGGESTION':e['notes']=text
        if d.get('component_assertion'):
            d['component_assertion']['notes']=text+' The transcribed components are source assertions, not evidence of cross-source disjointness.'
            for e in d['component_assertion'].get('evidence',[]):
                if 'notes' in e:e['notes']=text+' Component inputs and quantities remain transcribed from this entry’s cited source.'
        p['description']=text;p['identity_consequence']='Conditional historical candidate only; coordinator family identity decision pending.'
        p['integration_disposition']='PENDING_COORDINATOR_FAMILY_DECISION'
        p['predicate_consequence']='No family-owner installation or released identity row is approved by this conditional candidate.'
        changes.append('Withdraw unsupported inference of distinct preparation identity from accession number or missing qualifiers. Retain exact candidate/source/occurrence lineage for conditional family reconciliation under #1237.')
        conditional.append({'proposal_id':pid,'before_capture':p0['after_capture'],'owner_path':p['owner_path'],'case_ids':p['case_ids'],'applies_to_occurrence_ids':p.get('applies_to_occurrence_ids',[]),'assessment':text})
    if pid in ['CHEM-C1193-HEPES-1221','CHEM-C1193-HEPES-1474']:
        d.pop('components');d.pop('component_assertion')
        text='W05-FINAL-CHEM-NEW-02 was reported before correction. Withdraw inferred buffer-moiety and potassium-species material partonomy. The source names only the 1 M HEPES-KOH stock; composition remains unknown. Preserve its nominal strength in the whole-stock description. No solvent, free KOH, neutralization ratio or component molarity is inferred. The original component objects are preserved in the immutable finding and prior payload.'
        note(d,text);changes.append(text)
    if pid in ['CHEM-C1193-DSMZ_394_1137-Tris','CHEM-C1193-JCM_1061-Tris']:
        d.pop('components');d.pop('component_assertion')
        text='W05-FINAL-CHEM-NEW-03 was reported before correction. Withdraw inferred Tris-moiety and chloride-species material partonomy. Preserve the source-defined nominal buffer strength and pH as whole-preparation specifications; the source does not enumerate its material inputs. No solvent, free-base/salt ratio, HCl input or component molarity is inferred. Original component objects and historical claims remain available in the immutable finding and prior payload.'
        note(d,text);changes.append(text)
    if pid=='ROOT-P-fatty-stock':
        retired=[s for s in d['synonyms'] if s['synonym_text'] in ['Fatty acid mixture','Fatty acid mixture (see below)']];assert len(retired)==2
        d['synonyms']=[s for s in d['synonyms'] if s not in retired]
        text='JCM 266 specifies four acids at 0.5 g each, 20 ml water and NaOH adjustment to pH 7.5. DSMZ 119 uses the same generic mixture name for a different 23/27/27/27 ml acid input specification with 896 ml water. Therefore the generic labels cannot globally select this JCM 266 stock. Retire these two active resolver aliases without classifying the authentic source strings as chemically false. Preserve their full structured provenance in the alias-disposition ledger and here: '+json.dumps(retired,ensure_ascii=False)+'. The original history is unchanged. All WITHHOLD and source/export obligations remain.'
        d['notes']=text;changes.append(text);evidence(d,'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf',text)
        for s in retired:alias_dispositions.append({'proposal_id':pid,'before':s,'after':None,'disposition':'retired_ambiguous_global_alias_preserved_structured_provenance','reason':text,'evidence_ids':['ROOT-jcm-266','ROOT-dsmz-119']})
        p['description']='Correct the JCM 266 mixture identity and retire two ambiguous generic global resolver aliases; retain their exact provenance and all holds.'
        p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['ROOT-dsmz-119']))
    if pid=='ROOT-P-thiamine-stock':
        old='JCM403 and NBRC1321 footnote***** both define10mgthiamineHCl in100ml25mMsodiumphosphatebufferpH3.4, filter sterilized.'
        new='JCM 403 and NBRC 1321 footnote ***** both define 10 mg thiamine HCl in 100 ml of 25 mM sodium phosphate buffer at pH 3.4. NBRC 1321 and JCM 1125 explicitly specify filter sterilization. JCM 403 does not explicitly specify filtration of this stock, and JCM 1468 has an unexplained asterisk that does not independently establish filtration.'
        def replace(x):
            if isinstance(x,dict):return {k:(v if k=='curation_history' else replace(v)) for k,v in x.items()}
            if isinstance(x,list):return [replace(v) for v in x]
            if isinstance(x,str):return x.replace(old,new)
            return x
        d=replace(d);changes.append('Correct current filtration attribution by source: '+new+' Preserve the earlier historical event verbatim; this event supersedes its overbroad attribution.')
        p['description']='Promote the existing source-bound thiamine stock with its shared buffered composition; attribute filtration only to NBRC 1321 and JCM 1125, preserving all salt and export holds.'
    if pid=='CHEM-PROP-magnesium-heptahydrate':
        reject(d,['MgSO2','MgSO2·7H2O','MgSO2 x 7 H2O'],'The literal MgSO2 formula has two oxygens in the sulfur group and does not denote MgSO4·7H2O. NBRC 406 itself prints MgSO2·7H2O in the main recipe, while its trace-mineral block separately prints MgSO4·7H2O; TOGO enriches the erroneous main string as heptahydrate. That enrichment is not independent primary correction. Preserve the raw typo and original source in REJECTED_LABEL as a non-identity literal on this exact heptahydrate owner; no different chemical reagent is invented.','FINAL-CHEM-mg-nbrc406')
        generic=['.MgSO4','MgSO 4','magnesium sulphate','magnesium(II) sulfate','sulfuric acid magnesium salt','sulphate of magnesia']
        for s in d['synonyms']:
            if s['synonym_text'] in generic:alias_dispositions.append({'proposal_id':pid,'before':copy.deepcopy(s),'after':copy.deepcopy(s),'disposition':'conditional_inherited_alias_preserved','reason':'The inherited sssom_other_backfill row lacks an original recipe or product locator. The literal omits hydration. That omission establishes neither a heptahydrate nor a different form. Its exact historical occurrence-stage hydration must be recovered before affirming global resolver applicability; no new approval or REJECTED_LABEL is assigned.'})
        note(d,'Six inherited hydration-unspecified aliases remain conditional, exactly preserved with their original structured source/type in the alias ledger. The existing backfill source does not identify their original recipe or product; absence of hydration is not positive evidence of anhydrous material. No whole-owner alias approval or hold release follows.')
        p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['FINAL-CHEM-mg-nbrc406','FINAL-CHEM-mg-togo1597']))
    if pid=='CHEM-PROP-riboflavin':
        reject(d,['Riboflavin (0.2 mg/ml)','Riboflavin (0.05 μg/mL)'],'DSMZ 1157 adds 5 ml of filter-sterilized riboflavin at 0.2 mg/ml; NBRC 1604 separately adds 1 ml of riboflavin at 0.05 microgram/ml after autoclaving. These exact concentration-bearing strings denote supplied preparations, not the neat CHEBI:17015 substance. Reject them only as identity aliases on the molecular owner; retain original text/source/history. No solvent or additional stock owner is inferred.','FINAL-CHEM-riboflavin-dsmz1157')
        p['evidence_ids']+=['FINAL-CHEM-riboflavin-dsmz1157','FINAL-CHEM-riboflavin-nbrc1604']
    if pid=='CHEM-PROP-niacin':
        reject(d,['Nicotinate'],'CHEBI:32544 defines nicotinate as the carboxylate conjugate base with charge -1 and formula C6H4NO2. This does not exactly identify neutral nicotinic acid CHEBI:15940. Retain the historical manual source and literal but mark the exact-identity alias REJECTED_LABEL on this neutral-acid owner. This does not reject niacin or infer a supplied nicotinate salt.','FINAL-CHEM-nicotinate-chebi32544')
        p['evidence_ids']+=['FINAL-CHEM-nicotinate-chebi32544']
    if pid=='CHEM-PROP-hepes':
        text='DSMZ 975 lists HEPES (10mM) as a weighed 2.38 g ingredient in 1000 ml water. The 10 mM qualifier describes the receiving medium, unlike an aliquoted stock. Preserve this exact inherited RAW_TEXT alias and its original backfill provenance. Its source-specific applicability is supported by https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium975.pdf; do not convert it to a distinct 10 mM stock or to the 1 M HEPES-KOH candidates.'
        note(d,text);changes.append(text)
        s=next(s for s in d['synonyms'] if s['synonym_text']=='HEPES (10mM)');alias_dispositions.append({'proposal_id':pid,'before':copy.deepcopy(s),'after':copy.deepcopy(s),'disposition':'positively_retained_weighed_reagent_with_final_medium_dose','reason':text,'evidence_ids':['FINAL-CHEM-hepes-dsmz975']});p['evidence_ids']+=['FINAL-CHEM-hepes-dsmz975']
    if pid in ['CHEM-C1193-Tris-HCl-salt','CHEM-C1193-tellurium-dioxide']:
        assert d['ontology_mapping']['mapping_quality']=='BROAD_MATCH';d['ontology_mapping']['mapping_quality']='NARROW_MATCH'
        text=('Filed #1238: the exact CAS 1185-53-1 salt has the broader tris free-base parent CHEBI:9754.' if 'Tris' in pid else 'W05-FINAL-CHEM-NEW-01, reported to the coordinator before this isolated fix: exact CAS 7446-07-3 tellurium dioxide has the broader tellurium molecular entity parent CHEBI:33305. Separate coordinator issue routing remains pending; the Tris issue does not cover this owner.')
        text+=' Set NARROW_MATCH so the pinned native builder emits skos:broadMatch for the parent instead of the previous closeMatch. Preserve the exact CAS display and all source/identity holds. The complete native before/after projection is separately recorded; no global grade replacement is implied.'
        note(d,text);changes.append(text);p['predicate_consequence']='NARROW_MATCH emits skos:broadMatch to the stated parent, with exact CAS display and local registry identity rows; isolated projection is not export approval.'
    if changes:event(d,' '.join(changes)+' Report-only candidate; separate final scientific review and coordinator integration remain required.')
    target=O/'proposed-v1'/Path(p['owner_path']).name
    assert not target.exists();write_validated_ingredient(d,target,target_class='IngredientRecord')
    assert yaml.safe_load(target.read_text())==d
    if d==original:target.write_bytes(before) # preserve unchanged bytes after guarded replay
    assert d.get('curation_history',[])[:len(original.get('curation_history',[]))]==original.get('curation_history',[])
    delta=''.join(difflib.unified_diff(before.decode().splitlines(True),target.read_text().splitlines(True),fromfile=str(path),tofile=str(target)))
    dp=O/'diffs-v1'/(Path(p['owner_path']).stem+'.diff');dp.parent.mkdir(exist_ok=True);dp.write_text(delta)
    p['predecessor_after_capture']=p0['after_capture'];p['after_capture']=ref(target)
    p['final_correction']={'author':AUTHOR,'timestamp':NOW,'changes':changes,'native_guarded_write':'PASS','independent_review':'pending','prior_proposal_object_sha256':objsha(p0),'predecessor_diff':ref(dp)}
    ancestry.append({'proposal_id':pid,'baseline_owner_path':p['owner_path'],'baseline_sha256':p.get('before_sha256'),'predecessor':p0['after_capture'],'after':p['after_capture'],'changed':d!=original,'history_prefix_preserved':True,'guarded_write':'PASS','exact_diff':ref(dp)})
    out.append(p)

new_specs=[('FINAL-CHEM-P-thiamine-dihydrate-cas','Thiamine-hcl_X_2_H2o.yaml',61,'FINAL-CHEM-cas13465-05-9-pubchem'),('FINAL-CHEM-P-ki-stock-alias','Ki.yaml',56,'FINAL-CHEM-ki-dsmz792b'),('FINAL-CHEM-P-ferric-stock-alias','Fe_Iii_Citrate.yaml',63,'FINAL-CHEM-ferric-togo565')]
for pid,name,di,eid in new_specs:
    owner=Path('data/ingredients/mapped')/name;before=owner.read_bytes();d=yaml.safe_load(before);original=copy.deepcopy(d);changes=[]
    if 'thiamine' in pid:
        assert sha(before)=='482d71b94bd51f56bf1cb9ec5ced824709d7f99e0e849749b124b366864574b3'
        assert d['chemical_properties']['cas_rn']=='13465-05-9';del d['chemical_properties']['cas_rn']
        for k in ['data_source','retrieval_date']:d['chemical_properties'].pop(k,None)
        text='Withdraw the active CAS 13465-05-9 and its CAS-retrieval metadata. The direct PubChem name query resolves it to CID 21899424, formula ClH5O2 and InChI=1S/ClH.2H2O/h1H;2*1H2, which lacks the thiamine skeleton. No replacement CAS is established or inserted. Preserve CHEBI:132751, the dihydrate formula/structure, all original history, source labels and WITHHOLD obligations. This repairs the documented false CAS claim under #268 without granting whole-owner or export approval.'
        note(d,text);changes.append(text);evidence(d,'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/13465-05-9/property/MolecularFormula,InChI/JSON',text)
    elif 'ki-' in pid:reject(d,['KI (0.01% w/v)'],'DSMZ 792b explicitly doses 0.50 ml KI (0.01% w/v) into solution A. This is an aliquoted supplied stock, not neat potassium iodide CHEBI:8346. Mark only this stock label REJECTED_LABEL on the chemical owner, preserving its raw text, source and history. Do not infer stock solvent or use this to settle the separate ambiguous KJ source case.','FINAL-CHEM-ki-dsmz792b')
    else:reject(d,['Ferric citrate (0.1%, w/v)'],'TOGO M565, linked to JCM 561, explicitly doses 5 ml Ferric citrate (0.1%, w/v). The literal names a supplied stock, not a neat iron(III) citrate molecule. Mark only this stock label REJECTED_LABEL on CHEBI:144421 and preserve its raw text/source/history. This does not settle the separate Eisencitrat oxidation, stoichiometry or hydration uncertainty or approve other inherited labels.','FINAL-CHEM-ferric-togo565')
    event(d,' '.join(changes)+' Report-only isolated correction; all inherited holds remain.')
    target=O/'proposed-v1'/name;assert not target.exists();write_validated_ingredient(d,target,target_class='IngredientRecord');assert yaml.safe_load(target.read_text())==d
    bp=O/'before'/name;bp.parent.mkdir(exist_ok=True);bp.write_bytes(before)
    bid='FINAL-CHEM-BEFORE-'+Path(name).stem
    E.append({'evidence_id':bid,'kind':'source_snapshot','capture':ref(bp),'locator':str(owner),'observation':'Authentic complete baseline owner; exact bytes verified before creating this isolated successor.'})
    dp=O/'diffs-v1'/(Path(name).stem+'.diff');dp.write_text(''.join(difflib.unified_diff(before.decode().splitlines(True),target.read_text().splitlines(True),fromfile=str(owner),tofile=str(target))))
    p={'proposal_id':pid,'case_ids':[D[di]['case_id']],'description':' '.join(changes),'evidence_ids':[eid,bid],'owner_path':str(owner),'kind':'edit_existing_owner','before_sha256':sha(before),'after_capture':ref(target),'identity_consequence':'Preserve existing identity; withdraw only the demonstrated false CAS or stock-to-solute alias claim.','predicate_consequence':'Existing ontology mapping is retained; false CAS or rejected alias no longer contributes its display/resolution claim. All row holds remain.','publication_obligations':'Coordinator must inspect the exact integrated owner and all dependencies before any application or release.','final_correction':{'author':AUTHOR,'timestamp':NOW,'native_guarded_write':'PASS','independent_review':'pending','baseline_capture':ref(bp),'predecessor_diff':ref(dp)}}
    out.append(p);D[di]['proposal_ids'].append(pid);D[di]['evidence_ids'] += [eid,bid];D[di]['no_change_reason']=None;D[di]['disposition']='curation_proposal'
    D[di]['reasoning']+=' Final correction: '+' '.join(changes)
    ancestry.append({'proposal_id':pid,'baseline_owner_path':str(owner),'baseline_sha256':sha(before),'predecessor':ref(bp),'after':ref(target),'changed':True,'history_prefix_preserved':d['curation_history'][:-1]==original['curation_history'],'guarded_write':'PASS','exact_diff':ref(dp)})

for folder in ['new-captures-v2','new-captures-v3']:
    for row in json.loads((O/folder/'retrievals.json').read_text()):
        x=copy.deepcopy(row);x['kind']='ontology' if 'chebi' in x['evidence_id'] else 'primary_source';x['locator']=x['url']
        if 'jcm1145' in x['evidence_id']:x['kind']='unsuccessful_search';x['observation']='HTTP 200 response says Nothing found; no formulation claim is supported.'
        elif 'dsmz1145' in x['evidence_id']:x['observation']='Successful comparator retrieval but unrelated MS-medium; it does not support the ferric-citrate alias.'
        else:x['observation']='Direct primary response captured for the claim-specific final correction; applicability is recorded in the alias and case review ledgers.'
        E.append(x)

for d in D:
    old=next(x for x in json.loads((O/'input-decisions.json').read_text()) if x['case_id']==d['case_id'])
    linked=[p for p in out if d['case_id'] in p['case_ids']]
    d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[e for p in linked for e in p['evidence_ids']]))
    conditional_p=[p for p in linked if p.get('integration_disposition')]
    if conditional_p:
        texts=list(dict.fromkeys(conditional_text[p['proposal_id']] for p in conditional_p))
        d['reasoning']=' '.join(texts);d['applicability']='Preserve exact source and occurrence routes. These full candidate bytes are conditional report artifacts; no family winner, merger or simultaneous installation is selected.'
        d['missing_requirement']='Coordinator must choose and independently review the bounded preparation identity convention and owner reconciliation without using missing formulation facts as proof of equality or difference.'
    if 'ROOT-P-thiamine-stock' in d['proposal_ids']:
        d['reasoning']+=' Filtration attribution is source-specific: explicit in NBRC 1321 and JCM 1125, not explicitly stated for the stock in JCM 403 or established by the unexplained JCM 1468 asterisk.'
    d['prior_independent_review']=d.get('independent_review');d['independent_review']={'status':'pending','evidence_ids':[]}
    d['final_correction_review']={'author':AUTHOR,'timestamp':NOW,'prior_decision_sha256':objsha(old),'scope':'Complete assigned case and complete linked payload review; original case/occurrence/owner hashes and holds are retained. See read ledger for exact primary capture scope.','proposal_ids':[p['proposal_id'] for p in linked],'conditional_proposal_ids':[p['proposal_id'] for p in conditional_p],'whole_owner_approval':False}

dump(O/'proposals-v1.json',out);dump(O/'decisions-v1.json',D);dump(O/'evidence-v1.json',E)
dump(O/'ancestry-v1.json',ancestry);dump(O/'alias-dispositions-v1.json',alias_dispositions);dump(O/'mapping-evidence-corrections-v1.json',types);dump(O/'conditional-candidates-v1.json',conditional)
dump(O/'guarded-write-receipt-v1.json',{'author':AUTHOR,'timestamp':NOW,'target_class':'IngredientRecord','proposal_count':len(out),'case_count':len(D),'mapping_evidence_changes':len(types),'all_guarded_and_roundtrip_equal':True,'input_hashes':{n:sha((O/n).read_bytes()) for n in ['input-decisions.json','input-proposals.json','input-evidence.json']},'outputs':{n:sha((O/n).read_bytes()) for n in ['decisions-v1.json','proposals-v1.json','evidence-v1.json','ancestry-v1.json']}})
print('Guarded report candidates:',len(out),'cases:',len(D),'MappingEvidence corrections:',len(types),'conditional candidates:',len(conditional))
