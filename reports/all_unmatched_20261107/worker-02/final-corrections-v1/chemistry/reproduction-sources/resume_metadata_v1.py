"""Bounded report-only chemistry successors; never writes maintained surfaces."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, sys, yaml, csv

W=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
R=W/'reports/all_unmatched_20261107/worker-02'
S=R/'final-corrections-v1/chemistry'
O=W/'.temp/w02-final-corrections-v1/chemistry'
NOW=yaml.safe_load((S/'after-v1/P-aminobenzoic_Acid.yaml').read_text())['curation_history'][-1]['timestamp']
AUTHOR='/root/research_b'
def sha(raw): return hashlib.sha256(raw).hexdigest()
def canonical(v): return sha(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def readj(p): return json.loads(p.read_text())
def save(p,v):
    if p.exists():
        assert json.loads(p.read_text())==v,p
        return
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def capture(p): return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
oldp=readj(R/'continuation-1201-v1/proposals.json')['proposals']
oldd=readj(R/'continuation-1201-v1/decisions.json')['decisions']
olde=readj(R/'continuation-1201-v1/evidence.json')['evidence']
pi={x['proposal_id']:x for x in oldp}; ei={x['evidence_id']:x for x in olde}
assert len(oldp)==106 and len(oldd)==188
new_e=[]; used_old=set(); payloads=[]; proposals=[]; changes=[]; lineage=[]
def ev(name,p,url,at,kind,locator,claim):
    id='fc-chem-'+name
    new_e.append({'evidence_id':id,'kind':kind,'capture':capture(p),'url':url,'accessed_at':at,'locator':locator,'supports_or_contradicts':claim})
    return id
retr={}
for version in [2,3,4,5]:
    for row in readj(S/f'captures/fetch-v{version}/retrievals.json'):
        kind='unsuccessful_search' if row['status']!=200 else ('ontology' if row['name'].startswith(('ols','nlm')) else 'primary_source')
        retr[row['name']]=ev(row['name'],R/row['path'],row['url'],row['accessed_at'],kind,'Full response; claim-specific use appears in the disposition ledger.','Failed retrievals establish only access limitations. A successful capture is not source-to-owner approval.')
for name in ['abee-cosmobio','ferric-wako']:
    m=readj(S/f'captures/w04-{name}.receipt.json')
    retr[name]=ev(name,S/f'captures/w04-{name}.body',m['url'],m['started_at'],'primary_source','Manufacturer product identity text; retained exact W04 response bytes and original access time.','ABEE is explicitly 4-aminobenzoic acid ethyl ester; Wako explicitly gives variable-n ferric sulfate CAS15244-10-7. Neither source selects historical reagent lots.')
retr['sigma-web']=ev('sigma-malate-web',S/'captures/sigma-malate-web-extract.json','https://www.sigmaaldrich.com/US/en/product/aldrich/233935','2026-11-08T08:05:48+00:00','primary_source','Saved web-tool extraction, not a successful raw HTTP response.','Supplier labels L-disodium malate monohydrate with stereochemical SMILES and CAS207511-06-6; Aladdin COA labels DL material with the same CAS, an unresolved conflict.')
retr['malate-conflict']=ev('malate-stereo-conflict',S/'new-finding-malate-stereo.json',None,NOW,'local_context','Machine finding reported to root before dependent candidate edits.','No registry/supplier winner is selected; properties may be qualified to the stated L form without settling the shared-CAS conflict.')
lookup=O/'catalog-cas-lookup.json';q=S/'captures/catalog-cas-lookup.json';assert q.read_bytes()==lookup.read_bytes()
retr['lookup']=ev('catalog-cas-lookup',q,None,NOW,'local_context','Full byte search across all2956 actual per-record YAML, including ignored paths.','Own CAS15244-10-7 has no current record hit; mapped variable ferric and separate malformed UNMAPPED0385 competition are not resolved by this search. Exact chrome concept has no current owner hit.')
# Freeze the actual downstream occurrence that led to the independently read primary PABA recipe.
occ_path=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech/output/ingredient_occurrences.tsv')
raw=occ_path.read_bytes();rows=[line for line in raw.decode().splitlines() if 'p-aminobenzoic acid (0.3' in line]
save(S/'captures/paba-source-occurrence-search.json',{'accessed_at':NOW,'source_path':str(occ_path),'file_sha256':sha(raw),'search':'Literal p-aminobenzoic acid (0.3; direct file read includes ignored paths. This is current downstream context, not an altered frozen occurrence.','matching_rows':rows})
retr['paba-lookup']=ev('paba-source-occurrence',S/'captures/paba-source-occurrence-search.json',None,NOW,'local_context','Current occurrence row151675, recipeCultureMech009566, solutions/3/composition.','This lookup identifies NBRC1604/TOGO M3052 for primary verification, and does not substitute current rows for frozen case69.')
def use(*ids):
    for id in ids:
        if id in ei:
            c=ei[id]['capture'];p=(R/c['path']) if c['root']=='artifact' else W/c['path']
            assert sha(p.read_bytes())==c['sha256'],id
            used_old.add(id)
        else: assert id in {x['evidence_id'] for x in new_e},id
    return list(ids)
def target(pid,owner,indices,desc,evs,edit,findings):
    current=W/owner;before=current.read_bytes();baseline=yaml.safe_load(before)
    old=pi.get(pid);pre=R/old['after_capture']['path'] if old else current
    prebytes=pre.read_bytes()
    if old:
        assert sha(prebytes)==old['after_capture']['sha256']
        assert sha(before)==old['before_sha256']
    rec=yaml.safe_load(prebytes);original=copy.deepcopy(rec)
    edit(rec)
    assert rec!=original,pid
    if rec.get('notes'): rec['notes']+='\n\n'
    else: rec['notes']=''
    rec['notes']+='Final W02 proposal correction (unapplied): '+desc+' All precise source, role, duplicate-owner and publication holds remain; this claim-specific correction is not whole-owner approval.'
    record_curation_event(rec,curator='codex_worker02_final_corrections_chemistry',action='PROPOSED_CLAIM_CORRECTION',changes=desc+' Original full before/predecessor objects and field lineage are preserved in reports/all_unmatched_20261107/worker-02/final-corrections-v1/chemistry/. No maintained data changed.',previous_status=original.get('mapping_status'),new_status=rec.get('mapping_status'),llm_assisted=True,timestamp=NOW)
    assert rec['curation_history'][:-1]==original.get('curation_history',[])
    out=S/'after-v1'/Path(owner).name;assert yaml.safe_load(out.read_text())==rec
    loaded=yaml.safe_load(out.read_text());assert loaded==rec
    bcap=S/'before'/Path(owner).name;assert bcap.read_bytes()==before
    pcap=S/'predecessor'/Path(owner).name;assert pcap.read_bytes()==prebytes
    cases=list(dict.fromkeys((old['case_ids'] if old else [])+[oldd[i]['case_id'] for i in indices]))
    evs=use(*evs)
    p=copy.deepcopy(old) if old else {'proposal_id':pid,'kind':'edit_existing_owner','owner_path':owner,'before_sha256':sha(before)}
    p.update(case_ids=cases,description=desc,after_capture=capture(out),evidence_ids=list(dict.fromkeys(p.get('evidence_ids',[])+evs)),final_correction_author=AUTHOR,final_correction_findings=findings,selected_predecessor_capture=capture(pcap),authentic_before_capture=capture(bcap),independent_review_status='pending',publication_authorization='None. Report-only proposal; no owner merge, maintained edit, synchronization, downstream rebuild or release is authorized by this artifact.')
    if old:p['supersedes_selected_proposal_object_sha256']=canonical(old)
    proposals.append(p)
    fielddiff=[{'field':k,'before':original.get(k),'after':rec.get(k)} for k in sorted(set(original)|set(rec)) if original.get(k)!=rec.get(k)]
    changes.append({'proposal_id':pid,'baseline_capture':capture(bcap),'predecessor_capture':capture(pcap),'after_capture':capture(out),'field_diffs':fielddiff,'all_original_history_events_preserved':True,'guarded_writer':'PASS','loaded_roundtrip_equal':True})
    # Exact mapping-evidence lineage, including withdrawn relation entries; never match only by position.
    oe=original.get('ontology_mapping',{}).get('evidence',[]);ne=rec.get('ontology_mapping',{}).get('evidence',[]);avail=list(range(len(ne)))
    for i,x in enumerate(oe):
        match=next((j for j in avail if ne[j]==x),None)
        if match is not None:avail.remove(match)
        lineage.append({'proposal_id':pid,'predecessor_pointer':f'/ontology_mapping/evidence/{i}','predecessor_full_value':x,'predecessor_value_sha256':canonical(x),'status':'unchanged' if match is not None else 'superseded_scientifically','successor_pointer':None if match is None else f'/ontology_mapping/evidence/{match}','successor_full_value':None if match is None else ne[match],'reason':desc if match is None else 'Exact unchanged full object retained; no type or approval inference.'})
    for j in avail:lineage.append({'proposal_id':pid,'status':'new_or_revised_scientific_claim','successor_pointer':f'/ontology_mapping/evidence/{j}','successor_full_value':ne[j],'successor_value_sha256':canonical(ne[j]),'revises_predecessor_pointers':[f'/ontology_mapping/evidence/{i}' for i,x in enumerate(oe) if x not in ne]})
    payloads.append((p,desc,evs,findings))
def reject(rec,tokens):
    for token in tokens:
        items=[s for s in rec.get('synonyms',[]) if s['synonym_text']==token];assert len(items)==1,(token,items)
        assert items[0]['synonym_type']!='REJECTED_LABEL';items[0]['synonym_type']='REJECTED_LABEL'
def judgment(rec,notes):
    rec['ontology_mapping'].setdefault('evidence',[]).append({'evidence_type':'LLM_SUGGESTION','source':'W02 final chemistry correction; final-corrections-v1/chemistry/evidence.json','notes':notes})
def alias_edit(tokens,desc):
    def edit(r):reject(r,tokens);judgment(r,desc)
    return edit

paba='ABEE is retained as REJECTED_LABEL: the primary Cosmo Bio GlyScope brochure explicitly identifies the ethyl ester, not CHEBI30753 free acid. The exact concentration token p-aminobenzoic acid (0.3 μg/μL) is also non-resolving: NBRC1604 explicitly adds10uL of that preparation and TOGO M3052 calls it4-aminobenzoic acid solution. No solvent, complete stock recipe, receiving concentration or transfer to an ester owner is inferred. Preserve the supported Paraamino benzoic acid alias. PMID31986050 remains genuine cocrystal context, qualified PARTIAL rather than exact-owner or role support; other charge aliases and provisional roles remain unapproved.'
def edit_paba(r):
    reject(r,['ABEE','p-aminobenzoic acid (0.3 μg/μL)'])
    x=next(e for e in r['ontology_mapping']['evidence'] if e.get('pmid')=='31986050');x['supports']='PARTIAL';x['explanation']='The preserved abstract snippet mentions a ketoconazole/PABA cocrystal. This is adjacent chemical context; it does not independently establish the free-acid owner identity, synonym equivalence, or a medium-specific vitamin role.'
    judgment(r,paba)
target('b-proposal-paba','data/ingredients/mapped/P-aminobenzoic_Acid.yaml',[69],paba,[retr['abee-cosmobio'],retr['nbrc1604'],retr['togoM3052'],retr['paba-lookup'],'b-reference-92a10ac82f682a4e'],edit_paba,['W02-F-PABA-ABEE','W02-F-INHERITED-ALIASES'])
ferric='Promote the variable-n ferric sulfate primary identity to cas:15244-10-7 under MAPPING_SEMANTICS§3: independent Wako product pages explicitly pair that CAS with Fe2(SO4)3·nH2O. Retain CHEBI53438 iron(3+) sulfate as the asymmetric broader grounding (NARROW_MATCH); do not use CHEBI131387 monohydrate as exact, copy anhydrous formula weight, select n, or assert historical lot procurement. The old no-own-CAS rationale is superseded, with its full original preserved in predecessor evidence/history. JCM413→369 and603→592 are available:369 separately autoclaves0.5% variable-ferric-sulfate solution in0.1N H2SO4 (percent basis unspecified);592 includes0.01g variable ferric sulfate in SolutionA alongside distinct ferrous sulfate and ferric citrate. Failed JCM1250 Nothing-found retrieval is not positive source proof; source-specific TOGO evidence is separately bound. The competing UNMAPPED0385 owner and issue873 remain unresolved; no winner or merge is selected.'
def edit_ferric(r):
    r['identifier']='cas:15244-10-7'
    cp=r.setdefault('chemical_properties',{});cp['cas_rn']='15244-10-7';cp['data_source']='FUJIFILM Wako primary n-hydrate product pages; exact capture provenance in final-corrections-v1/chemistry/evidence.json';cp['retrieval_date']=readj(S/'captures/w04-ferric-wako.receipt.json')['started_at']
    r['ontology_mapping']['evidence']=[e for e in r['ontology_mapping']['evidence'] if not (e.get('source')=='MIM curation (#321)' and 'no exact ChEBI term or own CAS' in e.get('notes',''))]
    judgment(r,ferric)
target('w02-v2-ferric-variable-composed','data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml',[0,8,94,124,144],ferric,[retr['ferric-wako'],retr['ols-term-131387'],retr['ols-term-53438'],retr['ols-search-ferric-cas'],retr['ols-search-ferric-hydrate'],retr['cas-ferric'],retr['lookup'],'b-source-6a3627b402c0f276','b-source-5610ec442e836ef2','b-source-55c33e835e2d7cd8','b-source-c8eadd16aad34b82',retr['jcm369'],retr['jcm592']],edit_ferric,['W02-F-FERRIC-CAS','W02-F-FERRIC-AVAILABILITY'])
chrome='Use exact active MeSH concept mesh:M0314280 chrome alum, dodecahydrate, supported by NLM narrower-concept/registry context and the supplier KCr(SO4)2·12H2O/CAS7788-99-0 identity. Preserve CAS7788-99-0 as chemical property. This potassium/chromium double sulfate differs from CHEBI53471 Cr2(SO4)3 in potassium and sulfate stoichiometry as well as water; retire the old active hydrate-only CLOSE_MATCH rationale instead of substituting NARROW_MATCH. Full prior evidence and all history remain preserved. The JCM1033 Nothing-found capture is not original recipe proof; use separately inspected TOGO/MediaDive captures at their stated source/version scope. No quantity normalization or whole-owner release is approved.'
def edit_chrome(r):
    r['identifier']='mesh:M0314280';m=r['ontology_mapping'];m.update(ontology_id='mesh:M0314280',ontology_label='chrome alum, dodecahydrate',ontology_source='MESH',mapping_quality='EXACT_MATCH')
    m['evidence']=[e for e in m['evidence'] if e.get('source') not in ['Edison LITERATURE (PaperQA3) + local CHEBI verification','MIM curation (#342)']];judgment(r,chrome)
target('a-proposal-chrome-alum','data/ingredients/mapped/CrKSO42_X_12_H2O.yaml',[2,18],chrome,[retr['nlm-chrome-json'],retr['nlm-chrome-browser'],retr['nlm-chrome-M0314280'],retr['nlm-chrome-M0074743'],retr['lookup'],'a-primary-chrome-alum','a-ontology-53471'],edit_chrome,['W02-F-CHROME-ALUM-RELATION'])
malate_alias='Retain Na malate, Na-malate and the truncated Sodium Malate And as non-resolving provenance on the exact disodium(S)-malate owner. The generic names do not fix sodium ratio/stereochemistry; source477 database CAS alone is not independent stereo proof where the provider also assigns L identifiers to DL labels. Source1316 explicitly names a20% preparation, independently handled as a stock with unresolved solute stereochemistry. Keep the previously rejected DL tokens and valid explicit L names; do not change the preferred term, identity or select an alternative source form.'
target('c-proposal-reject-dl-aliases-on-l-malate','data/ingredients/mapped/Sodium_Malate.yaml',[157,163],malate_alias,['c-chebi-91261','c-mediadive-477','c-mediadive-1316'],alias_edit(['Na malate','Na-malate','Sodium Malate And'],malate_alias),['W02-F-INHERITED-ALIASES'])
mohr='Retain Iron ammonium sulfate hydrate and Fe(NH4)2(SO4)2 as non-resolving global provenance on the exact hexahydrate owner. The former is only related in CHEBI76181 and omits oxidation/hydration scope; the bare formula has actual anhydrous and seven-water alternative owners. Preserve the supported source-specific MediaDive106 interpretation because its independent CAS7783-85-9 and six-water formula disambiguate that occurrence. A source-qualified interpretation is not an unconditional resolver synonym. Keep all supported explicit six-water aliases and earlier concentration-label rejections.'
target('w02-v2-mohr-hexahydrate-composed','data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml',[149],mohr,['c-chebi-76181','c-mediadive-106'],alias_edit(['Iron ammonium sulfate hydrate','Fe(NH4)2(SO4)2'],mohr),['W02-F-INHERITED-ALIASES'])
nickel='Preserve the literal (NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v) as REJECTED_LABEL on the chemical owner: its explicit concentration denotes preparation-qualified scope, not an unconditional neat-salt identity. No solvent, receiving dose or recipe completion is invented. Exact six-water source interpretations remain supported separately. The duplicated bare/explicit nickel owners and conflicting CAS annotations remain held under1050; no anhydrous identity or owner winner is inferred.'
target('w02-proposal-ammonium-nickel-hexahydrate','data/ingredients/mapped/Nh42ni_So42_X_6_H2o.yaml',[187],nickel,['a-ontology-86149'],alias_edit(['(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)'],nickel),['W02-F-INHERITED-ALIASES'])
target('fc-chem-proposal-nickel-bare-stock-alias','data/ingredients/mapped/Nh42ni_So42.yaml',[136,187],nickel,['a-ontology-86149'],alias_edit(['(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)'],nickel),['W02-F-INHERITED-ALIASES'])
vanadyl='Preserve vanadic sulfate pentahydrate as REJECTED_LABEL rather than an exact vanadyl alias: CHEBI132758 classifies this text only as related, and no inspected primary evidence establishes the ambiguous vanadic oxidation nomenclature as unconditional exact V(IV) identity. Keep the explicit vanadyl pentahydrate identity and valid five-water spellings, both CAS annotations/history, and earlier stock/bare-token rejections. This does not select a different oxidation state or source lot.'
target('c2-proposal-vanadyl-stock-and-bare-aliases','data/ingredients/mapped/Voso4_X_5_H2o.yaml',[185],vanadyl,['c-chebi-132758'],alias_edit(['vanadic sulfate pentahydrate'],vanadyl),['W02-F-INHERITED-ALIASES'])
cobalt='The exact cobalt(2+) sulfate--water(1/7) label belongs to CHEBI91244 heptahydrate, whose definition/formula explicitly include seven waters. Retain that literal as REJECTED_LABEL on anhydrous CHEBI53470; preserve the prior other heptahydrate rejections and all original source credit. No blanket rejection of generic cobalt names is made.'
target('fc-chem-proposal-cobalt-sulfate-alias','data/ingredients/mapped/Coso4.yaml',[31,51],cobalt,['a-ontology-91244'],alias_edit(['cobalt(2+) sulfate--water (1/7)'],cobalt),['W02-F-INHERITED-ALIASES'])
cobaltcl='Retain Cobalt(II) chloride--water (1/7) as REJECTED_LABEL on the exact CHEBI53503 hexahydrate owner. The explicit water ratio1/7 conflicts with the six-water definition, formula and structure. Preserve valid six-water names and the original literal/source/history; this does not infer any source reagent identity from a malformed formula.'
target('fc-chem-proposal-cobalt-chloride-alias','data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml',[64],cobaltcl,[retr['ols-cobalt-chloride6']],alias_edit(['Cobalt(II) chloride--water (1/7)'],cobaltcl),['W02-F-INHERITED-ALIASES'])
mn='Retain MnCl4 x 4 H2O and MnCl4・4H2O as REJECTED_LABEL on manganese(II) chloride tetrahydrate. Both original JCM616 and MediaDiveJ616 preserve the Cl4 text; neither supplies a corrigendum or product identity proving it means Cl2. CHEBI86368 explicitly has two chlorides. Preserve original merge/backfill history and the raw source tokens; the plausible typo is not silently corrected, and case140 remains unresolved pending original author/reagent evidence.'
target('fc-chem-proposal-manganese-chloride-alias','data/ingredients/mapped/Mncl2_X_4_H2o.yaml',[140],mn,['c-chebi-86368','c-mediadive-1828','c-medium-J616','c-jcm-616'],alias_edit(['MnCl4 x 4 H2O','MnCl4・4H2O'],mn),['W02-F-INHERITED-ALIASES'])
brands='Retain the four existing Feromax, Feroritard, Ferro-Gradumet and Fespan tokens as REJECTED_LABEL, with original credit/history. CHEBI75834 explicitly lists each as a related BRAND NAME; this does not establish that the complete commercial product is identical to neat iron(II) sulfate monohydrate. No product composition or replacement product owner is invented. The supported source1735 monohydrate interpretation and its exact CAS remain unchanged.'
target('fc-chem-proposal-ferrous-monohydrate-brands','data/ingredients/mapped/Feso4_X_H2o.yaml',[135],brands,['c-chebi-75834'],alias_edit(['Feromax','Feroritard','Ferro-Gradumet','Fespan'],brands),['W02-F-INHERITED-ALIASES'])
cpco='Replace only the anhydrous InChI/SMILES inherited via CHEBI53470 with the exact seven-water structures directly reported by CHEBI91244. Preserve the heptahydrate formula and CAS10026-24-1; provenance distinguishes the new structure source from unchanged historical fields. This does not correct malformed source rows or approve receiving concentrations.'
def edit_cpco(r):
    ann=readj(R/'a/captures/chebi-91244.json')['_embedded']['terms'][0]['annotation'];cp=r['chemical_properties'];cp['inchi']=ann['inchi_string'][0];cp['smiles']=ann['smiles_string'][0];cp['data_source']='InChI/SMILES: primary CHEBI91244 capture a-ontology-91244; inherited formula/CAS preserved and agree with that exact heptahydrate';cp['retrieval_date']=ei['a-ontology-91244']['accessed_at'];judgment(r,cpco)
target('fc-chem-proposal-cobalt-heptahydrate-properties','data/ingredients/mapped/Coso4_X_7_H2o.yaml',[31,51],cpco,['a-ontology-91244'],edit_cpco,['W02-F-INHERITED-PROPERTIES'])
cpv='Withdraw the fixed-one-water InChI and SMILES from the variable-n vanadyl sulfate owner. CHEBI87020 definition and formula leave n unspecified; the same source contains one-water structures, an internal inconsistency rather than independent support for n=1. Preserve the variable formula, CAS and prior provenance; no replacement fixed structure, hydration count or mass is generated.'
def edit_cpv(r):
    r['chemical_properties'].pop('inchi');r['chemical_properties'].pop('smiles');judgment(r,cpv)
target('fc-chem-proposal-vanadyl-variable-properties','data/ingredients/mapped/Voso4_X_N_H2o.yaml',[167],cpv,['c-chebi-87020'],edit_cpv,['W02-F-INHERITED-PROPERTIES'])
cpm='Correct the property block at the stated L-disodium malate monohydrate scope using directly retrieved PubChemCID16211643: two sodium ions, one water and explicit S stereochemistry, corroborated by Sigma233935 L-form label/structure. Replace the one-sodium, water-free, stereounspecified CID197014/formula/structures. This is not a CAS reassignment or supplier winner: the same CAS207511-06-6 appears on Aladdin D302750C COA labelled DL, a separately recorded unresolved registry/stereo conflict. Keep the stated owner identity provisionally held, no source-lot equivalence and no resolution of case10 acid-versus-anion ambiguity.'
def edit_cpm(r):
    p=readj(S/'captures/fetch-v2/pubchem-malate-properties.body')['PropertyTable']['Properties'][0];cp=r['chemical_properties'];cp.update(molecular_formula=p['MolecularFormula'],smiles=p['SMILES'],inchi=p['InChI'],pubchem_cid=p['CID'],data_source='Formula/InChI/SMILES/CID: PubChem16211643, exact stated L-disodium monohydrate scope corroborated by Sigma233935. CAS preserved, not independently resolved: Aladdin D302750C labels DL material with same CAS; see final-corrections-v1/chemistry/new-finding-malate-stereo.json.',retrieval_date=next(x['accessed_at'] for x in readj(S/'captures/fetch-v2/retrievals.json') if x['name']=='pubchem-malate-properties'));judgment(r,cpm)
target('fc-chem-proposal-l-malate-monohydrate-properties','data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml',[10],cpm,[retr['pubchem-malate-properties'],retr['sigma-web'],retr['aladdin-malate-coa'],retr['malate-conflict'],retr['cas-malate']],edit_cpm,['W02-F-INHERITED-PROPERTIES'])

# Complete successor decisions for every affected original case, preserving source and occurrence bindings.
revised={}; dispositions=[]
for p,desc,evs,findings in payloads:
    for cid in p['case_ids']:
        old=next(x for x in oldd if x['case_id']==cid);d=revised.setdefault(cid,copy.deepcopy(old))
        d['proposal_ids']=list(dict.fromkeys(d.get('proposal_ids',[])+[p['proposal_id']]))
        d['evidence_ids']=list(dict.fromkeys(d.get('evidence_ids',[])+evs))
        d['independent_review']={'status':'pending','evidence_ids':[]}
        d['primary_author']=AUTHOR;d['no_change_reason']=None
        owner={'path':p['owner_path'],'sha256':p['before_sha256']}
        if owner not in d['owner_records']:d['owner_records'].append(owner)
        d.setdefault('final_correction_notes',[]).append({'proposal_id':p['proposal_id'],'finding_ids':findings,'assessment':desc})
    dispositions.append({'proposal_id':p['proposal_id'],'finding_ids':findings,'status':'proposed_bounded_correction_pending_independent_review','description':desc,'evidence_ids':evs,'before_sha256':p['before_sha256'],'selected_predecessor_capture':p['selected_predecessor_capture'],'after_capture':p['after_capture'],'case_ids':p['case_ids']})
for n in [0,8,94,124,144]:
    d=revised[oldd[n]['case_id']]
    d['reasoning']=oldd[n]['reasoning'].replace('Keep the local variable-hydrate primary ID','The prior local primary ID is superseded by the independently supported own CAS15244-10-7; preserve the variable-hydrate scope').replace('local variable-ferric-sulfate-hydrate identity','variable-ferric-sulfate-hydrate identity now proposed as cas:15244-10-7').replace('local owner','owner')
    if n==124:d['reasoning']='The JCM324/368/369/417/419/478/508/523/524/592 recipes specify Fe2(SO4)3·xH2O. JCM413 and603 are also available:413 delegates to369 with final NaCl/NaHCO3 and thiosulfate/gas modifications, while603 delegates to592 with2g/L yeast extract and gas changes. JCM369 explicitly uses separately autoclaved0.5% variable-ferric-sulfate solution in0.1N H2SO4, with percentage basis unspecified;592 lists0.01g variable ferric sulfate in SolutionA beside distinct ferrous sulfate and ferric citrate. These sources support variable hydration, not a fixed n or anhydrous identity. The preparation grouping and unresolved source quantities remain distinct from the solute identity.'
    d['reasoning']+=' Wako primary sources support own CAS15244-10-7 for the variable-n material; CHEBI131387 monohydrate is not exact. The malformed competing UNMAPPED0385 identity under873 is not resolved or merged.'
    d['applicability']='All original frozen occurrence IDs and full recipe contexts are preserved. '+d['reasoning']+' Supplier evidence identifies chemical scope only, not historical procurement, assay or receiving-medium quantities. Old failed JCM1250 capture is unsuccessful access, not positive recipe evidence. Every original source/release hold remains.'
    d['missing_requirement']='Duplicate-owner competition under873 requires independent source/owner reconciliation; no winner is selected. Source-specific unknown reagent lot, fixed water content and any quantity/preparation normalization remain unasserted; no own-CAS absence or JCM413/603 unavailability claim remains.'
for n in [2,18]:
    d=revised[oldd[n]['case_id']]
    if n==2:d['reasoning']='The separately captured TOGO and MediaDive solution5083 records specify CrK(SO4)2·12H2O in the source contexts. The retained JCM1033 route returns Nothing found and is not positive original recipe evidence. Supplier identity/CAS7788-99-0 corroborates potassium chromium double sulfate dodecahydrate. NLM exact narrower concept M0314280 supplies the form-specific identity; the old CHEBI53471 relationship is superseded because its Cr2(SO4)3 formula differs in potassium and sulfate ratio as well as water.'
    else:d['reasoning']=oldd[n]['reasoning']+' Exact active MeSHM0314280 now provides dodecahydrate identity; preserve ownCAS7788-99-0 as a chemical property and retire the incomplete prior CHEBI53471 CLOSE rationale.'
    d['applicability']=oldd[n]['applicability']+' Positive source support excludes the failed JCM1033 response. Exact form mapping does not authorize any source quantity normalization.'
for d in revised.values():
    for k in ['case_id','case_input_sha256','source','occurrence_ids']:
        assert d[k]==next(x for x in oldd if x['case_id']==d['case_id'])[k]

save(S/'proposals.json',{'scope':'Report-only chemistry replacements/additions against published W02 selected106; root composes preparations and evidence typing separately.','author':AUTHOR,'authored_at':NOW,'proposals':proposals})
save(S/'decisions.json',{'scope':'Full successor decisions for affected original cases only; remaining original188 cases unchanged by this author. Root must compose overlapping preparation decisions.','author':AUTHOR,'decisions':sorted(revised.values(),key=lambda d:next(i for i,x in enumerate(oldd) if x['case_id']==d['case_id']))})
save(S/'evidence.json',{'author':AUTHOR,'evidence':new_e,'reused_unchanged_evidence_ids':sorted(used_old)})
save(S/'finding-dispositions.json',{'author':AUTHOR,'authored_at':NOW,'findings':dispositions,'new_conflict':capture(S/'new-finding-malate-stereo.json'),'claim_scope':'Claim-specific corrections only. Unsupported roles are not classified false; original source/owner release holds remain.'})
save(S/'before-after-diffs.json',{'author':AUTHOR,'changes':changes})
save(S/'mapping-evidence-lineage.json',{'author':AUTHOR,'entries':lineage,'rule':'Exact unchanged objects matched first with multiplicity; superseded entries retain full predecessor values and pointer. Root handles historical MANUAL typing only after scientific composition.'})
save(S/'build-receipt.json',{'authored_at':NOW,'author':AUTHOR,'script_path':str(Path(__file__).relative_to(W)),'script_sha256':sha(Path(__file__).read_bytes()),'proposal_count':len(proposals),'decision_count':len(revised),'new_evidence_count':len(new_e),'reused_evidence_count':len(used_old),'guarded_writer_pass':len(proposals),'all_histories_preserved':True,'source_case_occurrence_bindings_preserved':True,'current_baseline_head':'0597d00417be4d7cdfb5a31970043eec9bbc88fe','maintained_mutation':False,'independent_review':'pending','scientific_limit':'Writer success is structural only. No release, merge, fixed hydrate or supplier winner approval.'})
print(json.dumps({'proposals':len(proposals),'decisions':len(revised),'evidence':len(new_e),'guarded_writer':'PASS'}))
