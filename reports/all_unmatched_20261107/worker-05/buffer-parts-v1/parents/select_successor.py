from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, shutil
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

S = Path(__file__).resolve().parent; W = Path.cwd(); B = W / 'reports/all_unmatched_20261107/worker-05'
PUBLIC = 'buffer-parts-v1/parents/'; AT = datetime.now(timezone.utc).isoformat(); AUTHOR = '/root/buffer_hepes'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
objsha = lambda x: hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',', ':'),ensure_ascii=False).encode()).hexdigest()
def write(name, x):
    p=S/name; assert not p.exists(),p; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
ps = json.loads((S/'proposals.json').read_text())['proposals']
ds = json.loads((S/'decisions.json').read_text())['decisions']
baseps = {p['proposal_id']:p for p in json.loads((S/'input/selected-proposals.json').read_text())['proposals']}
baseds = {d['case_id']:d for d in json.loads((S/'input/selected-decisions.json').read_text())['decisions']}
pep = next(p for p in ps if p['proposal_id']=='W05-FINAL-MAT-039')
basep = baseps[pep['proposal_id']]
r = yaml.safe_load((B/basep['after_capture']['path']).read_text()); base = copy.deepcopy(r)
text = (
    'Complete the supported nonidentity family grounding: retain kgmicrobe.ingredient:peptone and use NARROW_MATCH to mesh:D011492 Protein Hydrolysates, with native broadMatch plus the local B1 identity row. '
    'The active primary NLM concept M0017860 defines a complex mixture produced by partial or extensive hydrolysis; the manufacturer guide defines generic peptones as water-soluble partial protein hydrolysates and includes plant, yeast or animal material and acid, base or enzyme processing. '
    'Assess the direct MeSH Peptones term D010461 before this broader route: its acid-or-enzyme and precipitation criteria are not established for the complete source-unspecified generic scope. '
    'MICRO:0000178 adds unsupported mammalian origin, MICRO:0000174 an unverified enzymatic process, and MICRO:0000172 does not establish yeast coverage. '
    'Do not select FOODON:03315306 after full OWL inspection reveals an actual member-of food-additive restriction in addition to its SIREN comment; preserve the initial private candidate and NEW01 report as unselected evidence. '
    'CHEBI:749541 is a sparse imported molecular-entity class without established whole-mixture scope. MICRO:0000167 is a supported but less specific undefined-mixture option. '
    'The MeSH descriptor indexing annotation about therapeutic/nutrient use is not imported as a clinical or assay role. '
    'Preserve the two MicrobeDecoder observations, raw plural, rejected truncated token, all previous history/evidence/statistics, provisional roles, source holds and source-specific incoming-reference reconciliation; no owner, source-case or export admission.'
)
r['ontology_mapping'].update(ontology_id='mesh:D011492',ontology_label='Protein Hydrolysates',ontology_source='MESH',mapping_quality='NARROW_MATCH')
new_evidence = [
    dict(evidence_type='LLM_SUGGESTION',source='https://id.nlm.nih.gov/mesh/M0017860',notes='Primary NLM concept for active descriptor D011492 defines a complex mixture produced by partial or extensive hydrolysis. Compared with the manufacturer generic partial-protein-hydrolysate definition, this supports a broader material relation only: NARROW_MATCH / native broadMatch, preserving kgmicrobe.ingredient:peptone. The descriptor indexing annotation does not establish clinical use or approve an organism/assay role.'),
    dict(evidence_type='LLM_SUGGESTION',source='https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf',notes='Printed page7 defines generic peptones as water-soluble partial protein hydrolysates from plant, yeast or animal sources and includes acid, base or enzyme processing. This supports broader Protein Hydrolysates membership without selecting feedstock, enzyme, supplier, lot, numerical composition or organism role.'),
    dict(evidence_type='LLM_SUGGESTION',source='https://id.nlm.nih.gov/mesh/M0016245',notes='The direct Peptones descriptor D010461 was assessed under native section3 exact-term precedence. Its primary concept specifies acid-or-enzyme partial hydrolysis and solubility/nonprecipitation criteria. The source-unspecified owner and two observations do not establish that complete narrower specification; manufacturer generic scope also includes base hydrolysis. No exact D010461 identity is asserted merely from its matching name.'),
    dict(evidence_type='LLM_SUGGESTION',source='https://raw.githubusercontent.com/FoodOntology/foodon/master/foodon.owl',notes='Full FOODON:03315306 class has an actual subclass restriction member_of some FOODON:03400181 food additive (us cfr), in addition to its SIREN flavoring rdfs:comment. The initial private FoodOn candidate is unselected because these source peptones do not establish that membership. This statement is a negative applicability finding; it does not edit or disapprove other owners automatically.')
]
r['ontology_mapping']['evidence'].extend(new_evidence)
r['curation_history'].append(dict(timestamp=AT,curator='Codex /root/buffer_hepes; W05 consolidated report-only parent correction',action='CORRECTED',changes=text+' This event describes the selected successor relative to the published source payload; the earlier unselected private FoodOn candidate remains separately preserved and was never applied.',previous_status='MAPPED',new_status='MAPPED',llm_assisted=True,llm_model='gpt-6'))
r['notes'] += '\n\nConsolidated parent-grounding successor (prior scope text preserved as history): '+text+' Independent exact-byte review and root integration remain pending.'
out=S/'proposed-v2/Peptone.yaml';assert not out.exists();write_validated_ingredient(r,out)
assert r['curation_history'][:-1]==base['curation_history'] and r['ontology_mapping']['evidence'][:-len(new_evidence)]==base['ontology_mapping']['evidence']
assert all(r.get(k)==base.get(k) for k in base if k not in ['ontology_mapping','curation_history','notes'])
failed=copy.deepcopy(pep['after_capture'])
newp=copy.deepcopy(basep)
newp.update(description=basep['description']+' Consolidated parent-grounding successor: '+text,after_capture=dict(root='artifact',path=PUBLIC+'proposed-v2/Peptone.yaml',sha256=sha(out)),parent_predecessor_capture=basep['after_capture'],unselected_private_candidate_capture=failed,parent_successor_author=AUTHOR,parent_successor_at=AT,identity_consequence='Preserve kgmicrobe.ingredient:peptone; do not assign mammalian, food-additive, supplier, enzyme, physical test or exact MeSH Peptones scope to the unqualified owner/observations.',predicate_consequence='Native broadMatch mesh:D011492 plus exactMatch kgmicrobe.ingredient:peptone B1 registry row; no exact family identity or role inference.',independent_review=dict(status='pending exact final successor bytes; historical reviews retained separately',evidence_ids=[]))
ps=[newp if p['proposal_id']==newp['proposal_id'] else p for p in ps]

issue_src=S.parent/'issues/issue1193-comments-followup-v2.json';issue_dest=S/'input/issues/issue1193-comments-followup-v2.json';assert not issue_dest.exists();shutil.copyfile(issue_src,issue_dest)
pages=json.loads(issue_dest.read_text()); comments=[x for page in pages for x in page] if pages and isinstance(pages[0],list) else pages
comment=next(x for x in comments if x['id']==6719869465)
assert comment['created_at']=='2026-11-08T09:34:21Z'

ev=json.loads((S/'evidence.json').read_text())['evidence']; seen={x['capture']['sha256'] for x in ev}
for receipt in sorted((S/'captures').glob('*.receipt.json')):
    rec=json.loads(receipt.read_text());f=S/'captures'/rec['path'];assert sha(f)==rec['sha256']
    if sha(f) in seen:continue
    ev.append(dict(evidence_id='W05-PARENTS-'+f.stem.upper(),capture=dict(root='artifact',path=PUBLIC+'captures/'+f.name,sha256=sha(f)),kind='ontology',locator='Complete captured ontology/descriptor/concept/graph response or full official OWL; precise read scope and comparison in primary-assessment.json.',supports_or_contradicts='Claim-specific positive/negative applicability assessment only. Direct ontology scope was read, not selected by label alone; source preparation and roles remain held.',case_ids=[d['case_id'] for d in ds],url=rec['url'],accessed_at=rec['accessed_at'],original_capture_attribution=dict(retriever=rec.get('author',AUTHOR),receipt_path=PUBLIC+'captures/'+receipt.name,receipt_sha256=sha(receipt))))
    seen.add(sha(f))
for eid,f,locator,support,url in [
    ('W05-PARENTS-PRIMARY-ASSESSMENT',S/'primary-assessment.json','Ten candidate term scopes, full source comparisons, explicit missing facts and selected/unselected options.','New agent interpretation, not historical author approval.',None),
    ('W05-PARENTS-NEW01',S/'new-finding-before-fix.json','Immutable report before the selected MeSH successor; initial unselected FoodOn candidate retained.','Formal FoodOn membership restriction is a newly reported applicability finding; coordinator owns shared-union triage.',None),
    ('W05-PARENTS-COMMENT6719869465',issue_dest,'Complete current issue comment collection; comment6719869465 created09:34:21Z.','Coordinator audit reports no demonstrated additional incoming Soy components, while shared-ID occurrence membership and tombstone representative remain separate pre-integration obligations. This author does not claim to have reaudited its entire59-member packet.','https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719869465'),
    ('W05-PARENTS-SOY-NATIVE',S/'validation-soy/receipt.json','Exact Soy payload guarded/strict and native row projection.','Technical one-row exact MICRO identity and rejected-alias exclusion; no scientific or release approval.',None)
]:
    ev.append(dict(evidence_id=eid,capture=dict(root='artifact',path=PUBLIC+str(f.relative_to(S)),sha256=sha(f)),kind='source_snapshot',locator=locator,supports_or_contradicts=support,case_ids=[d['case_id'] for d in ds],url=url))
eids=[x['evidence_id'] for x in ev];assert len(eids)==len(set(eids))
for p in ps:p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+eids))
newds=[];deltas=[]
for d0 in ds:
    d=copy.deepcopy(d0);base_d=baseds[d['case_id']]
    if 'W05-FINAL-MAT-039' in d['proposal_ids']:
        reasoning='The two MicrobeDecoder peptones observations remain unspecified as to feedstock, supplier, processing and assay conditions. The generic owner retains kgmicrobe.ingredient:peptone with supported nonidentity mesh:D011492 Protein Hydrolysates grounding. Direct MeSH Peptones acid-or-enzyme/precipitation scope was assessed but is not fully established; the broader partial-or-extensive hydrolysis material definition is supported. The initial FoodOn candidate is unselected after formal food-additive membership restriction discovery. Preserve both raw observations, plural provenance, truncated-token rejection, histories/statistics and all role/source/export holds. Dependent references require separate source-level reconciliation.'
        d['reasoning']=reasoning
        d['parents_reassessment'].update(at=AT,conclusion=reasoning,selected_parent='mesh:D011492',selected_mapping_quality='NARROW_MATCH',primary_identifier='kgmicrobe.ingredient:peptone',direct_exact_term_assessed='mesh:D010461; acid-or-enzyme and precipitation scope not fully entailed',unselected_candidate_capture=failed,new_finding_id='W05-PARENTS-NEW01')
    else:
        d['parents_reassessment']['coordinator_dependency_followup']=dict(issue='https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719869465',attribution='Coordinator audit, not new component/source approval by this author',no_additional_incoming_component_assignment_demonstrated=True,explicit_continuity_obligations=['Four active shared FOODON owners plus Bacto_Soytone tombstone require final owner selection and explicit reviewed representative disposition.', '828 membership rows / 1079 occurrence associations are shared-ID associations, not a Soy-only partition; no global redirect.', 'Native source-label routing, source membership/count reconciliation and duplicate-baseline obligations remain root-owned.'])
    d['evidence_ids']=list(dict.fromkeys(base_d['evidence_ids']+eids))
    d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719869465']))
    changed={k:d[k] for k in d if d.get(k)!=base_d.get(k)}
    assert set(changed)=={'reasoning','parents_reassessment','evidence_ids','issue_refs'}
    newds.append(d);deltas.append(dict(case_id=d['case_id'],base_decision_sha256=objsha(base_d),changed_fields=changed,additive_arrays=['evidence_ids','issue_refs'],independent_full_final_composed_decision_review_required=True))
write('final/proposals.json',dict(schema_version=1,proposals=ps))
write('final/decisions.json',dict(schema_version=1,decisions=newds))
write('final/case-deltas.json',dict(schema_version=1,author=AUTHOR,base_core=json.loads((S/'case-deltas.json').read_text())['base_core'],deltas=deltas))
write('final/evidence.json',dict(schema_version=1,evidence=ev))
write('selection-receipt.json',dict(author=AUTHOR,at=AT,selected=[dict(proposal_id=p['proposal_id'],after_capture=p['after_capture']) for p in ps],unselected=dict(proposals='proposals.json',decisions='decisions.json',peptone_candidate=failed,reason='Superseded by final/ selection after NEW01, preserved unchanged.'),soy_payload_unchanged=True,peptone_delta_fields=['ontology_mapping','curation_history','notes'],peptone_prior_history_preserved=len(base['curation_history']),peptone_prior_mapping_evidence_preserved=len(base['ontology_mapping']['evidence']),peptone_new_history_events=1,peptone_new_MappingEvidence_types=[e['evidence_type'] for e in new_evidence],native_full_final_validation_pending=True,independent_exact_byte_review_pending=True))
print(json.dumps(dict(selected=[dict(proposal_id=p['proposal_id'],after_capture=p['after_capture']) for p in ps],evidence=len(ev)),indent=2))
