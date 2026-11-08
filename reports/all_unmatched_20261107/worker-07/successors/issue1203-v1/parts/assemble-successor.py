"""2026-11-08 append-only worker07 issue1203 ledger assembly.

Preserves all published inputs; carries 186 unchanged decisions and explicitly
reassesses the17-occurrence CM case plus the shared C-P08 KG linkage.
"""
import copy, datetime, hashlib, json
from pathlib import Path
import yaml
R=Path('reports/all_unmatched_20261107/worker-07')
S=R/'successors/issue1203-v1'
CM='CM_NAME:9dd78dd62f6762ad602b4126b067042b0cc68ba65bd212f9a10b07ec20b33e8e'
KG='KG_CASE:ac6686c0d61be7f652dcf0c2a495b463e1adf24fee613329fd02707bd19d759d'
P75='C-P08-ISSUE1203-V1'; P350='W07-MG350-ISSUE1203-V1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def capture(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}
def write(name,obj):
    p=S/name
    if p.exists():raise RuntimeError(f'Refusing overwrite {p}')
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def evidence(eid,path,kind,locator,support,cases):
    return dict(evidence_id=eid,capture=capture(path),kind=kind,url=None,
                locator=locator,supports_or_contradicts=support,case_ids=cases)

d=json.loads((R/'decisions.json').read_text()); e=json.loads((R/'evidence.json').read_text()); p=json.loads((R/'proposals.json').read_text())
a=json.loads((S/'research/occurrence-assessment.json').read_text())
extra=json.loads((S/'research/occurrence-evidence.json').read_text())['evidence']
# These shared captures are explicitly assessed for the frozen KG source_record,
# and the350 contrasts do not imply7.5g/L ingredient-wide applicability.
for item in extra:
    if item['evidence_id'] in ['MG1203-DSMZ-1592','MG1203-DSMZ-1593','MG1203-DSMZ-1593A','MG1203-DSMZ-1673','MG1203-DSMZ-1677','MG1203-DSMZ-1678','MG1203-CHEBI-31795']:
        item['case_ids'].append(KG)
e['evidence'] += extra
e['evidence'] += [
    evidence('MG1203-OCCURRENCE-AUTHOR',S/'research/occurrence-assessment.json','source_snapshot','occurrences[0:17], each exact occurrence/source/path/raw component and primary locator','Per-occurrence authored scientific assessment; independent approval is separate.',[CM]),
    evidence('MG1203-DEDUP',S/'research/dedup-review.json','local_validation','catalogue_owner_candidates, proposed_stocks, search_scope and exact captured candidates','Ignored-inclusive pre-mint search supports C-P08 reuse and distinct350g/L proposal; no other-shard case approval.',[CM,KG]),
    evidence('MG1203-COORDINATOR-FINDING',S/'captures/coordinator-finding.json','source_snapshot','CROSS-SHARD-G12-STOCK-SCOPE, original ledger and payload hashes','Supersedes the global pure-solute alias applicability claim while preserving correct CHEBI31795.',[CM]),
]
rows=copy.deepcopy(a['occurrences'])
for row in rows:
    strength=(row['stock_concentration'] or {}).get('value')
    row['proposal_ids']=[P75 if strength=='7.5' else P350] if strength else []
    row['resolved_material_identifier']=(
        'kgmicrobe.ingredient:mediadive_2154_magnesium_sulfate_heptahydrate_stock' if strength=='7.5'
        else 'kgmicrobe.ingredient:dsmz_1673_1677_1678_magnesium_sulfate_heptahydrate_stock_350g_l' if strength=='350'
        else 'CHEBI:31795')
    row['alias_policy']='Exact occurrence-qualified relation only; no new globally resolving unqualified raw-label synonym.'
write('occurrence-dispositions.json',dict(schema_version=1,case_id=CM,case_input_sha256=a['case_input_sha256'],author_agents=['/root/mg_occurrence_author','/root'],occurrences=rows))
e['evidence'].append(evidence('MG1203-OCCURRENCE-DISPOSITIONS',S/'occurrence-dispositions.json','source_snapshot','all17 occurrence rows including proposal routing and precise independent holds','Root-integrated exact source outcomes; no synonym-based stock-to-solute closure.',[CM]))
changed={x['case_id']:x for x in d['decisions'] if x['case_id'] in [CM,KG]}
cm=changed[CM]; kg=changed[KG]
cm['disposition']='stock_product_mixture_context'
cm['reasoning']='All17 frozen occurrences were reassessed individually. Six are nominal7.5g/L stock inputs and reuse the C-P08 registry identity; six are nominal350g/L stock inputs with a distinct source-qualified stock proposal. Five denote CHEBI:31795 solute components, including two components of a mixed20x basal stock, not that stock as a whole. Withdraw the proposed global RAW_TEXT alias: it cannot encode these source distinctions. Correct heptahydrate chemistry is preserved.'
cm['applicability']='Only the17 exact occurrence IDs and unchanged source-case digest are covered. occurrence_dispositions is the authoritative disjoint partition: 6stock7.5,6stock350,5solute. Nominal stock identity is settled despite unreported solvent/preparation;1677/1678 conflicting dose units and1845 missing mixed-stock denominator remain genuine holds.1818 batch-normalization and1845 nesting corrections are explicit settled integration requirements, not deferred evidence searches.'
cm['proposal_ids']=[P75,P350]
cm['missing_requirement']='Complete stock composition/preparation requires source-specific solvent and preparation evidence;1677/1678 dose conflicts require authoritative clarification;1845 basal-stock final volume is unreported. None blocks the isolated nominal stock proposals. See exact per-occurrence holds; no percent-volume conversion, global alias or export approval.'
cm['occurrence_dispositions']=rows
cm['issue_refs']=['https://github.com/CultureBotAI/MediaIngredientMech/issues/1203']
cm['evidence_ids']=[x for x in cm['evidence_ids'] if not x.startswith('W07-')]+[x['evidence_id'] for x in extra]+['MG1203-OCCURRENCE-AUTHOR','MG1203-OCCURRENCE-DISPOSITIONS','MG1203-DEDUP','MG1203-COORDINATOR-FINDING']
cm['supersedes']={'commit':'be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','ledger_capture':capture(R/'decisions.json'),'reason':'Prior all17 existing_identity_or_alias closure and unqualified pure-owner RAW_TEXT proposal failed supplied-stock applicability.'}
kg['proposal_ids']=[P75]
kg['evidence_ids']=[x for x in kg['evidence_ids'] if x not in ['c-e-dsmz-mg-1673','c-e-dsmz-mg-1677','c-e-dsmz-mg-1678'] and not x.startswith('W07-')]+[x['evidence_id'] for x in extra if KG in x['case_ids']]+['MG1203-DEDUP']
kg['applicability']+=' Successor reuses the same proposed registry identity for six verified CM occurrences. Ingredient2154 endpoint alone supplies no stock strength. Other350g/L recipes remain excluded; their predecessor evidence descriptions were inaccurate and are replaced by exact350g/L evidence IDs. Existing native WITHHOLD row1888 and helper-constant occurrence count remain unchanged.'
kg['issue_refs']=list(dict.fromkeys(kg['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1203']))
kg['supersedes']={'commit':'be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','ledger_capture':capture(R/'decisions.json'),'reason':'Shared C-P08 payload/source attribution and duplicate avoidance reassessed; original7.5g/L stock-versus-solute conclusion and all native holds retained.'}
for dec in changed.values():
    dec['independent_review']={'status':'pending','evidence_ids':[]}
    dec['native_review_scope']='Exact current Mgso4_X_7_H2o owner identity and proposed source relation only; new stock owners remain isolated proposals. New bounded native observation will link preserved prior reviews without superseding their other76 targets or five findings.'
oldp={x['proposal_id']:x for x in p['proposals']}
p['proposals']=[x for x in p['proposals'] if x['proposal_id'] not in ['C-P08','B-PROPOSAL-Mgso4_X_7_H2o']]
for pid,strength,name,owner,cases in [
    (P75,'7.5','stock-7p5g-L-v2.yaml',oldp['C-P08']['owner_path'],[CM,KG]),
    (P350,'350','stock-350g-L.yaml','data/ingredients/mapped/Dsmz_1673_1677_1678_Magnesium_Sulfate_Heptahydrate_Stock_350g_L.yaml',[CM])]:
    relevant=[o for o in rows if (o['stock_concentration'] or {}).get('value')==strength]
    ids=list(dict.fromkeys([eid for o in relevant for eid in o['evidence_ids']]+['MG1203-OCCURRENCE-DISPOSITIONS','MG1203-DEDUP']))
    proposal={'proposal_id':pid,'case_ids':cases,'description':f'Isolated source-qualified nominal{strength}g/L magnesium sulfate heptahydrate stock; six exact CM occurrences. '+('Reuse C-P08 registry identity and retain its frozen KG source context.' if strength=='7.5' else 'Distinct strength established after ignored-inclusive owner/proposal deduplication.'),'evidence_ids':ids,'owner_path':owner,'kind':'new_owner','before_sha256':None,'after_capture':capture(S/'proposed_owners'/name),'occurrence_ids':[o['occurrence_id'] for o in relevant],'identity_predicate_consequences':'Whole stock uses its own registry identity/FALLBACK_REGISTRY. CHEBI:31795 is the component only; no whole-to-component SKOS mapping or copied CAS. Qualified stock name only; no globally resolving bare raw alias.','publication_review_obligation':'Not applied or export-approved. Coordinator reconciles exact source bindings, applies through guarded writer, reviews complete published payload and retains existing content-bound WITHHOLD/REJECTED obligations.','limitations':'Stock solvent/preparation unreported; UNKNOWN component-list completeness. '+('Both1677/1678 source dose conflicts remain held, independent of settled stock strength.' if strength=='350' else 'No extension to350g/L, pure solute or every ingredient2154 use.'),'cross_shard_conflict':'w05 touches same pure CHEBI31795 owner; this successor withdraws its own raw alias. Other w01/w02 nominal stocks have distinct strengths/forms; no identity merge authorized.'}
    if strength=='7.5':proposal['supersedes']={'proposal_id':'C-P08','ledger_capture':capture(R/'proposals.json'),'after_capture':oldp['C-P08']['after_capture'],'relationship':'Same proposed identity; revised exact payload and expanded source-qualified applicability.'}
    p['proposals'].append(proposal)
write('decisions.json',d);write('evidence.json',e);write('proposals.json',p)
write('supersession.json',{'predecessor_commit':'be2f4c36d3d4ed79aabe29401c555ae3fd65d7b0','predecessor_ledgers':{n:capture(R/n) for n in ['decisions.json','evidence.json','proposals.json','MANIFEST.json']},'changed_case_ids':[CM,KG],'unchanged_case_count':186,'withdrawn_proposal':oldp['B-PROPOSAL-Mgso4_X_7_H2o'],'replacement_proposals':[P75,P350],'replaced_proposal':oldp['C-P08'],'superseded_evidence_descriptions':{'c-e-dsmz-mg-'+m:'MG1203-DSMZ-'+m for m in ['1673','1677','1678']},'scope':'Published predecessors immutable. Current successor ledgers supersede only declared source outcomes/payloads; all other source outcomes inherited without new scientific approval. Native prior five findings and remaining owners unchanged.'})
print(json.dumps({'cases':len(d['decisions']),'proposals':len(p['proposals']),'evidence':len(e['evidence']),'occurrences':len(rows)}))
