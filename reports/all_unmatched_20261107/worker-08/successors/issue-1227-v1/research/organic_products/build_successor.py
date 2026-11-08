"""Bounded issue1227 organic successor; no maintained or predecessor writes."""
import copy, datetime, hashlib, json, pathlib, sqlite3, sys
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient

B=pathlib.Path('reports/all_unmatched_20261107/worker-08')
O=B/'successors/issue-1227-v1/research/organic_products'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):
    with pathlib.Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def dump(name,x):
    p=O/name
    if p.exists():raise RuntimeError('Refusing to overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
A=json.loads((O/'assignment.json').read_text())
E={x['evidence_id']:x for x in json.loads((B/'successors/issue-1201-v1/evidence.json').read_text())['evidence']}
R=json.loads((B/'successors/issue-1227-v1/inputs/external-review/assessment.json').read_text())
RR={x['proposal_id']:x for x in R['proposal_accounting']}
CR={x['case_id']:x for x in R['case_accounting']}
CASE={x['case_id']:x for x in json.loads((B/'provenance/shard-08.json').read_text())['cases']}
P=copy.deepcopy(A['proposals']);D=copy.deepcopy(A['decisions']);dm={x['case_id']:x for x in D}

# These are individual classifications of the actual new assertions, not token replacement.
CATEGORIES={
 'op-ethane-new':('DATABASE_MATCH','The cited ChEBI entry directly identifies ethane; source gas delivery is a separately bounded applicability claim.'),
 'op-nalidixic-new':('DATABASE_MATCH','ChEBI directly identifies the acid. NBRC1301 supplies independent stock context; the unread NBRC1314 occurrence is explicitly held.'),
 'op-glycine-betaine-new':('DATABASE_MATCH','The exact ChEBI compound and supplier contrast establish the zwitterion and its trimethylglycine synonym, excluding hydrochloride and hydrates.'),
 'op-methanethiol-new':('DATABASE_MATCH','The cited ChEBI database identifies methanethiol; gas-dose transcription does not establish a stock or atmosphere identity.'),
 'op-sodium-nicotinate-new':('CAS_RN_CROSS_REFERENCE','NIST CAS54-86-4 establishes the sodium salt. The broader acid anchor remains an explicitly agent-authored form relation, not exact salt identity.'),
 'op1201-glycine-naoh-stock':('LLM_SUGGESTION','An agent proposes a source-qualified registry stock from the JCM906 preparation; the recipe remains the primary evidence and no human confirmation is claimed.'),
 'op1201-indicator-stock':('LLM_SUGGESTION','An agent interprets the exact TOGO comment as one combined indicator preparation and proposes its registry identity.'),
 'op1201-toluene-stock':('LLM_SUGGESTION','An agent proposes a distinct registry preparation from JCM600; unreported phase conditions and solvent grade remain unknown.'),
 'op1201-usb-peptic-pepton':('LLM_SUGGESTION','An agent proposes an opaque source-qualified USB material from NBRC19; no inferred digestion substrate or catalog identity.'),
 'op1201-sulfide-ore':('LLM_SUGGESTION','An agent chooses a generic ore registry scope from DSMZ88; the example pyrite is not a universal constituent.'),
 'op1201-cereal-leaves':('LLM_SUGGESTION','An agent promotes the existing leaf-material record at its source-supported generic scope; no species or extract identity is inferred.'),
 'op1201-homopipes-stock':('LLM_SUGGESTION','An agent proposes the concentration-qualified source preparation, distinct from the existing molecular solute.'),
 'op1201-dl-asparagine-monohydrate':('CAS_RN_CROSS_REFERENCE','The manufacturer SDS establishes the DL monohydrate CAS. The parent relation and exclusion of the L hydrate remain explicit decisions with LLM history.'),
 'op1201-laminarin-scope':('LLM_SUGGESTION','This new assertion is an agent naming/supplied-form decision based on ChEBI scope; the inherited database CAS lookup remains unchanged.'),
 'op1201-bbl-fluid-thioglycollate':('LLM_SUGGESTION','The registry-product choice is an agent interpretation of the ATCC/BD evidence, including a cross-provider recipe comparison.'),
 'op1201-r2a-medium':('DATABASE_MATCH','The official ontology directly provides the generic liquid R2A concept; exact FEBA applicability remains a bounded source comparison.'),
 'op1201-r2a-agar-provenance':('LLM_SUGGESTION','The new source-specific agar interpretation was authored by the agent. The unchanged inherited human-supplied MIM curation entry is preserved.'),
 'op1201-racemic-sodium-sulfolactate':('LITERATURE','The exact Denger2010-to-Roy2003 methods citation chain supports the racemic sodium-salt preparation. LLM assistance is preserved in history.'),
 'op1201-trypticase-soy-broth':('DATABASE_MATCH','MICRO0000113 supplies the exact Trypticase soy broth synonym and canonical tryptic soy broth label.'),
 'op1201-sodium-lactate-alias-boundary':('LLM_SUGGESTION','This assertion records an agent alias-scope decision; it is not evidence supplied by a human reviewer.'),
 'op1201-plain-flour':('DATABASE_MATCH','FoodOn directly supplies the generic flour concept. The source supplies no narrower grain/material specification.'),
 'op1201-amphotericin-stock':('LLM_SUGGESTION','The registry stock is an agent proposal from an unresolved source compound and concentration descriptor, not a human identity confirmation.'),
 'op1201-ferric-pyrophosphate-label':('LLM_SUGGESTION','This assertion records the agent naming/rejected-label repair from exact ferric-pyrophosphate chemistry while retaining the malformed source hold.')
}
ledger=[];assessments=[];changes={};guards=[]
for p in P:
    pid=p['proposal_id'];oldpath=B/p['after_capture']['path'];old=yaml.safe_load(oldpath.read_text())
    assert sha(oldpath)==p['after_capture']['sha256']
    before=yaml.safe_load(pathlib.Path(p['owner_path']).read_text()) if p['before_sha256'] else None
    if before:assert sha(p['owner_path'])==p['before_sha256']
    x=copy.deepcopy(old);actions=[];findings=[]
    oldev=before.get('ontology_mapping',{}).get('evidence',[]) if before else []
    for j,e in enumerate(x.get('ontology_mapping',{}).get('evidence',[])):
        same=e in oldev;prev=copy.deepcopy(e);reason='Unchanged inherited evidence: original source and category are preserved; no fresh human confirmation is asserted.'
        if pid in CATEGORIES and e['evidence_type']=='MANUAL_CURATION' and not same:
            typ,reason=CATEGORIES[pid];e['evidence_type']=typ
            actions.append(f'Correct ontology_mapping.evidence[{j}] from MANUAL_CURATION to {typ}: {reason}')
            findings.append('W08-IR-001')
        ledger.append({'proposal_id':pid,'json_pointer':f'/ontology_mapping/evidence/{j}','old_entry':prev,'old_entry_sha256':digest(prev),'inherited_identical_to_frozen_beforeimage':same,'new_entry':copy.deepcopy(e),'disposition':'corrected' if prev!=e else 'preserved','reason':reason})
    if pid=='op-l-asn-hydrate-alias':
        x['identifier']='NCIT:C87433';x['ontology_mapping']['mapping_quality']='CAS_RN_LOOKUP'
        for e in x['ontology_mapping']['evidence']:
            e['notes']='[HISTORICAL: superseded by the exact NCIT CAS/form adjudication below; retained as import provenance.] '+e['notes']
        x['ontology_mapping']['evidence'].append({'evidence_type':'CAS_RN_CROSS_REFERENCE','source':'https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT:C87433','notes':'Explicit CAS lookup: the record CAS5794-13-8 uniquely matches NCIT:C87433 in the read-only local NCIt database. The official term response also records CAS5794-13-8, C4H8N2O3.H2O and exact synonym L-Asparagine Monohydrate. This is the exact L hydrate, not a generic parent or the distinct DL hydrate CAS69833-18-7. Native canonical-label resolution returns Asparagine Monohydrate. The mapping was established by this CAS lookup and is graded CAS_RN_LOOKUP.'})
        x['notes']=(x.get('notes','')+'\n\n'+'Issue1227 exact-form adjudication: NCIT:C87433 replaces the historical CAS-primary/parent treatment under MAPPING_SEMANTICS section3. CAS5794-13-8, original source alias and all history remain. The inherited non-isomeric SMILES encodes connectivity and hydration but does not specify stereochemistry; it is retained as that limited representation, not as evidence of a racemate. The separate stereo-specific InChI and exact L-hydrate primary evidence establish the L form. No replacement structure, role approval or source-hold release is inferred.').strip()
        actions.append('Adopt exact NCIT:C87433 identity with explicit CAS_RN_LOOKUP, preserve historical CAS/form evidence and clarify the non-isomeric SMILES limitation.');findings.append('W08-IR-012')
        p['description']='Retain the source-bound L-Asparagine*H2O alias and correct the complete L-monohydrate owner to exact NCIT:C87433, established by CAS5794-13-8 lookup. Preserve CAS, source, history, structure limitations and roles.'
        p['identity_predicate_alias_consequences']='Primary identity changes cas:5794-13-8 to exact NCIT:C87433. Mapping quality CAS_RN_LOOKUP records the explicit unique CAS lookup; own-identifier predicate is skos:exactMatch. The historical NCIT parent broadMatch and obsolete CAS-primary registry rows require synchronized retirement on approved integration, not an additional active identity. The CAS remains a chemical property/export synonym. No active selected-payload or maintained component references use the old ID; generated surfaces are inventoried for later regeneration. DL hydrate remains distinct.'
    if pid=='op-nalidixic-new':
        x['ontology_mapping']['evidence'][0]['notes']='ChEBI:100147 directly identifies nalidixic acid, distinct from its sodium salt. Readable NBRC1301 primary composition names a 30 mg/ml nalidixic-acid solution, separately filtered. NBRC1314 and TOGO M2023 could not be read; the frozen 100 mg/ml occurrence is preserved but its primary-source applicability remains held. This proposal identifies the acid component only, not either whole stock.'
        x['notes']='NBRC1301 supports nalidixic acid in its 30 mg/ml stock. Source occurrence CM_OCC:9b9a89f81c52463d464c370ab10bd2fe099e86ab4d2b17ceab5073aaf22c3cdd (NBRC1314 / TOGO M2023) remains source-held pending readable exact primary evidence. The normalized source note is not substituted for independent primary verification. No occurrence, stock quantity or sodium-salt identity is altered.'
        actions.append('Limit primary-source applicability to readable NBRC1301; explicitly hold the NBRC1314 occurrence without rejecting the supported acid identity.');findings.append('W08-IR-007')
    if pid in ['op1201-r2a-medium','op1201-amphotericin-stock']:
        x['component_assertion']['completeness']='UNKNOWN'
        why='The liquid-medium definition enumerates these six constituents but establishes neither closure nor an omitted constituent. The separate agar annotation is excluded.' if pid=='op1201-r2a-medium' else 'The source concentration label names amphotericin but establishes neither all ingredients nor a concrete omitted constituent. Congener, counterion and carrier remain unknown.'
        x['component_assertion']['notes']+=' Completeness UNKNOWN: '+why
        actions.append('Correct source-relative membership completeness PARTIAL to UNKNOWN. '+why);findings.append('W08-IR-006')
    if pid=='op1201-trypticase-soy-broth':
        x['ontology_mapping']['mapping_quality']='SYNONYM_MATCH';actions.append('Correct mapping quality to SYNONYM_MATCH because Trypticase soy broth is an exact synonym of canonical tryptic soy broth; identity and exact own-ID relation are unchanged.');findings.append('W08-IR-009')
    # Three new referrals were routed by root before these bounded corrections.
    if pid=='op-soy-flour-alias':
        x['ontology_mapping']['mapping_quality']='SYNONYM_MATCH';actions.append('Resolve OP1227-REF-001 after coordinator routing: inherited evidence established the Soy flour name by exact synonym of canonical soybean flour. Set SYNONYM_MATCH; identity and source alias are unchanged.');findings.append('OP1227-REF-001')
    if pid=='op1201-r2a-medium':
        c=x['components'][5];assert c=={'component_name':'Pyruvate','reference_scope':'UNMAPPED'}
        c.update(reference_scope='MIM_CATALOG',component_id='CHEBI:15361')
        x['component_assertion']['evidence'][0]['notes']='The literal liquid-medium definition names these six constituents without amounts. Its separate agar-formula source annotation is excluded. Pyruvate is linked to the active CHEBI:15361 named anion entity at definition scope; no sodium counterion, purchased salt, amount or stock preparation is inferred. Casamino acids remain named and ungrounded because the catalog generic FOODON owner collapses a broader milk-protein hydrolysate class and the separate vitamin-assay record is a narrower grade.'
        actions.append('Resolve OP1227-REF-002 after coordinator routing: ground only the definition-level named pyruvate part to CHEBI:15361, preserving unknown counterion, amounts and formulation closure.');findings.append('OP1227-REF-002')
    if actions:
        record_curation_event(x,curator='worker08 /root/organics issue1227 bounded correction',action='REVIEW_CORRECTION',changes=' '.join(actions)+' Isolated successor proposal only; all inherited source, role and export holds remain. Historical evidence and predecessor files are immutable.',previous_status=x['mapping_status'],new_status=x['mapping_status'],llm_assisted=True,llm_model='GPT-6',timestamp=NOW)
        path=O/'proposed_owners'/pathlib.Path(p['owner_path']).name
        if path.exists():raise RuntimeError('Refusing overwrite '+str(path))
        write_validated_ingredient(x,path)
        p['after_capture']={'root':'artifact','path':str(path.relative_to(B)),'sha256':sha(path)}
        guards.append({'proposal_id':pid,'guard':'write_validated_ingredient','errors':[],'path':str(path.relative_to(B)),'sha256':sha(path)})
    else:
        assert not validate_ingredient(x)
        guards.append({'proposal_id':pid,'guard':'validate_ingredient; unchanged original bytes retained by reference','errors':[],'path':str(oldpath.relative_to(B)),'sha256':sha(oldpath)})
    for row in ledger:
        if row['proposal_id']==pid:
            j=int(row['json_pointer'].rsplit('/',1)[1]);row['new_entry']=copy.deepcopy(x['ontology_mapping']['evidence'][j])
            if row['disposition']=='preserved' and row['old_entry']!=row['new_entry']:
                row['disposition']='historical_provenance_qualified_for_IR012'
                row['reason']='Original database category and complete original text retained under an explicit historical/superseded prefix after exact NCIT adjudication.'
    changes[pid]={'proposal_id':pid,'findings':sorted(set(findings)),'actions':actions,'old_capture':A['proposals'][len(assessments)]['after_capture'],'new_capture':p['after_capture'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'case_ids':p['case_ids']}
    assessments.append({'proposal_id':pid,'case_ids':p['case_ids'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'selected_input_after_sha256':sha(oldpath),'final_after_sha256':p['after_capture']['sha256'],'complete_owner_read':True,'inherited_history_preserved':x['curation_history'][:len(old.get('curation_history',[]))]==old.get('curation_history',[]),'inherited_roles_preserved':all(x.get(k)==old.get(k) for k in ['nutritional_roles','environmental_roles','biological_roles','metabolic_roles','application_roles','roles']),'source_evidence_ids':p['evidence_ids'],'prior_external_assessment':RR[pid]['independent_reasoning'],'author_correction_appraisal':' '.join(actions) if actions else 'Complete payload retains the source/form boundary described in the prior external assessment. No bounded correction is required here; historical notes, roles and unresolved family/alias claims are not newly approved.','findings_addressed':sorted(set(findings)),'independent_review':'pending; this is author assessment only'})

# Record native exact CAS lookup without fabricating online ontology absence.
db=pathlib.Path('/Users/marcin/.data/oaklib/ncit.db');con=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True)
casrows=con.execute("select subject,predicate,value from statements where value='5794-13-8'").fetchall();con.close();assert casrows==[('NCIT:C87433','NCIT:P210','5794-13-8')]
dump('cas-lookup.json',{'at':NOW,'database':str(db),'database_sha256':sha(db),'query':"select subject,predicate,value from statements where value='5794-13-8'",'rows':casrows,'unique_term':'NCIT:C87433','scope':'Bounded exact local NCIt snapshot; official OLS term CAS/formula/exact synonym corroborates the supported L hydrate.'})
dump('category-correction-ledger.json',{'schema_version':1,'at':NOW,'scope':'Every mapping-evidence entry in all31 selected organic payloads. Inherited evidence is not recategorized by blanket token replacement. ComponentEvidenceTypeEnum is a different contract and is unchanged.','entries':ledger,'added_identity_evidence':[{'proposal_id':'op-l-asn-hydrate-alias','json_pointer':'/ontology_mapping/evidence/2','category':'CAS_RN_CROSS_REFERENCE','reason':'New explicit unique CAS-to-NCIT lookup; previous two database assertions remain as superseded historical provenance.'}]})
dump('correction-ledger.json',{'at':NOW,'author':'worker08:/root/organics','scope':'All31 full payloads; isolated author corrections, no self approval','entries':list(changes.values()),'new_referral_execution':[{'finding_id':k,'route_before_fix':'successors/issue-1227-v1/COORDINATOR-NEW-FINDINGS-v1.json','status':'implemented; independent review pending'}for k in ['OP1227-REF-001','OP1227-REF-002','OP1227-REF-003']]})

new_e=[]
def evidence(eid,path,kind,locator,claim,url=None,accessed=None):
    z={'evidence_id':eid,'capture':{'root':'artifact','path':str(path.relative_to(B)),'sha256':sha(path)},'kind':kind,'locator':locator,'supports_or_contradicts':claim,'url':url}
    if url:z['accessed_at']=accessed
    new_e.append(z)
evidence('op1227-categories',O/'category-correction-ledger.json','local_validation','entries by proposal_id and exact json_pointer','Per-assertion provenance correction; preserves inherited human evidence and separate component evidence categories.')
evidence('op1227-corrections',O/'correction-ledger.json','local_validation','entries by proposal_id','Bounded correction actions and input/final hashes; author assessment only, not scientific approval.')
evidence('op1227-cas-lookup',O/'cas-lookup.json','local_validation','rows and unique_term','Explicit unique CAS5794-13-8 lookup supports CAS_RN_LOOKUP on exact NCIT:C87433, separate from lexical agreement.')
evidence('op1227-native-ncit',O/'ncit-native-resolution.json','local_validation','native_function and accepted_normalized_labels','Native canonical/exact-synonym resolver recognizes NCIT:C87433 Asparagine Monohydrate and the L-specific name.')
ncit=B/'successors/issue-1201-v1/shared-primary/ols-ncit-C87433.json'
ret=json.loads((B/'successors/issue-1201-v1/shared-primary/retrievals-v4.json').read_text());nr=next(x for x in ret if x['name']=='ols-ncit-C87433')
evidence('op1227-ncit-exact',ncit,'ontology','/_embedded/terms/0 annotation.CAS_Registry, Chemical_Formula, exact synonym L-Asparagine Monohydrate','Official exact L-monohydrate evidence: CAS5794-13-8 and C4H8N2O3.H2O. Excludes DL hydrate CAS69833-18-7.',nr['url'],nr['accessed_at'])
web=json.loads((O/'nalidixic-web-read.json').read_text())
evidence('op1227-nbrc1301',O/'nalidixic-web-read.json','primary_source','Successful NBRC1301 response, composition lines16 and22','NBRC1301 names a 30 mg/ml nalidixic-acid solution and separate filtration; does not validate NBRC1314.', 'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1301',web['retrieved_at'])
for suffix,url in [('nbrc1314','https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1314'),('togo2023','https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2023')]:
    evidence('op1227-failed-'+suffix,O/'nalidixic-web-read.json','unsuccessful_search','Exact URL response reports inaccessible through web tool','Actual unsuccessful read; no exact primary contents inspected and no chemical rejection inferred.',url,web['retrieved_at'])
evidence('op1227-referrals',O/'new-finding-referrals-v3.json','local_validation','referrals OP1227-REF-001 through003','Exact before/input/source evidence and native checks for the three findings routed to coordinator before correction.')

for p in P:
    if changes[p['proposal_id']]['actions']:
        p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['op1227-categories','op1227-corrections']))
    if p['proposal_id']=='op-l-asn-hydrate-alias':p['evidence_ids']+=['op1227-cas-lookup','op1227-native-ncit','op1227-ncit-exact']
    if p['proposal_id']=='op-nalidixic-new':p['evidence_ids']+=['op1227-nbrc1301','op1227-failed-nbrc1314','op1227-failed-togo2023']
    if p['proposal_id'] in ['op-soy-flour-alias','op1201-r2a-medium','op1201-plain-flour']:p['evidence_ids']+=['op1227-referrals']
    for cid in p['case_ids']:
        d=dm[cid];d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[e for e in p['evidence_ids'] if e.startswith('op1227-')]))
        for f in changes[p['proposal_id']]['findings']:
            issue=1226 if f=='W08-IR-001' else 1201 if f=='OP1227-REF-002' else 1227
            d['issue_refs']=list(dict.fromkeys(d['issue_refs']+[f'https://github.com/CultureBotAI/MediaIngredientMech/issues/{issue}']))
for d in D:
    d['independent_review']={'status':'pending','evidence_ids':[]}
    d['primary_reviewer']='worker08:/root/organics; issue1227 bounded successor author, not independent approval'
    i=d['index_for_human_navigation']
    if i==24:
        d['reasoning']='ChEBI:100147 establishes nalidixic acid as distinct from its sodium salt. Readable NBRC1301 confirms the named acid in a 30 mg/ml stock. The separate NBRC1314 occurrence retains its frozen label and 100 mg/ml transcription, but exact primary applicability is held after unsuccessful NBRC1314 and TOGO M2023 reads; the normalized note does not substitute for the unread source.'
        d['applicability']='CM_OCC:0c4b4cf6bb41a8f450de7de792fc7f12e5c998b15757a5cc8cbf8732c22a566a (NBRC1301) is supported by the readable primary table and separate-filtration instruction. CM_OCC:9b9a89f81c52463d464c370ab10bd2fe099e86ab4d2b17ceab5073aaf22c3cdd (NBRC1314 / TOGO M2023) is source-held and unverified. Both IDs and frozen doses remain; neither whole stock is equated to the acid molecule.'
        d['missing_requirement']='Readable exact NBRC1314 or TOGO M2023 primary composition is required to verify that occurrence and its 100 mg/ml stock claim. This does not block the independently supported NBRC1301 acid candidate.'
        d['occurrence_assessments']=[{'occurrence_id':'CM_OCC:0c4b4cf6bb41a8f450de7de792fc7f12e5c998b15757a5cc8cbf8732c22a566a','status':'primary_source_supported','evidence_ids':['op1227-nbrc1301']},{'occurrence_id':'CM_OCC:9b9a89f81c52463d464c370ab10bd2fe099e86ab4d2b17ceab5073aaf22c3cdd','status':'source_held_unverified','evidence_ids':['op1227-failed-nbrc1314','op1227-failed-togo2023'],'missing_fact':'Readable exact primary composition for NBRC1314 / TOGO M2023.'}]
    if i==136:
        d['reasoning']='L-Asparagine*H2O names the L monohydrate, CAS5794-13-8. Official NCIT:C87433 contains that CAS, monohydrate formula and exact L-specific synonym. Explicit unique local CAS lookup and native term resolution justify NCIT:C87433 as primary identity with CAS_RN_LOOKUP, superseding the inherited CAS-primary/parent treatment. The DL hydrate and anhydrous L amino acid remain distinct.'
        d['applicability']+=' The inherited non-isomeric SMILES is retained only as connectivity/hydration representation; it does not prove racemization. L identity rests on the supported exact form and stereo-specific InChI. No dependent active component uses the replaced CAS ID; generated references remain a later synchronized-integration obligation.'
    if i==71:d['applicability']+=' The six names in the liquid MICRO definition establish neither closure nor concrete omitted inputs, so completeness is UNKNOWN. Definition-level pyruvate is CHEBI:15361; no sodium counterion, quantitative salt recipe or agar-formula inference is added.'
    if i==121:d['reasoning']+=' The actual lookup grade is SYNONYM_MATCH: Trypticase soy broth is an exact synonym of canonical tryptic soy broth, preserving own-identifier exact identity.'
    if i in [13,157]:d['reasoning']+=' The inherited Soy flour name resolves through the ontology synonym of soybean flour, so the successor records SYNONYM_MATCH without changing the material identity.'
    if i==180:
        d['applicability']='The exact frozen MediaDive ingredient1465 source record contains amount 4 g and derived g_l 4. These fields are preserved as source transcription, not newly validated experimental concentration. The ingredient page identifies Plain flour but does not establish the previously claimed 2 g/L for this occurrence. FOODON:00001056 denotes a food product made from flour and is not the ingredient itself. Generic flour is retained under section3 step4; no grain species is inferred.'
        d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['op1227-referrals']));d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1227']))
    if i==183:d['applicability']=d['applicability'].replace('Partial composition is sufficient for the stock;', 'The named constituent is sufficient to represent the source-qualified stock with UNKNOWN composition closure;')

dump('decisions.json',{'schema_version':1,'worker_slot':8,'shard_sha256':sha(B/'provenance/shard-08.json'),'phase':'shard','decisions':D})
dump('proposals.json',{'schema_version':1,'proposals':P})
dump('evidence-additions.json',{'schema_version':1,'evidence':new_e})
dump('full-payload-assessment.json',{'at':NOW,'author':'worker08:/root/organics','independence':'Author reassessment only. Separate skeptical review required.','proposal_reviews':assessments})
dump('guard-validation.json',{'at':NOW,'status':'PASS','payloads':guards,'scope':'Native closed-schema guard only; no source, role, export or integration approval.'})
print(json.dumps({'decisions':len(D),'proposals':len(P),'changed_payloads':sum(bool(x['actions'])for x in changes.values()),'evidence_additions':len(new_e),'category_changes':sum(x['disposition']=='corrected' for x in ledger),'native_guard':'PASS'}))
