import json, hashlib, pathlib, copy, datetime

S = pathlib.Path('.temp/w05-buffer-parts-v1')
R = S / 'review'
B = pathlib.Path('reports/all_unmatched_20261107/worker-05')
C = S / 'control/composed-final-v5'
ME = '/root/final_skeptical'
CHILD = ME + '/preservation_audit'
def read(p): return json.loads(pathlib.Path(p).read_text())
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def obj(o): return hashlib.sha256(json.dumps(o,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def bind(p): return {'path':str(p),'sha256':sha(p)}
def save(n,o):
    p=R/n
    if p.exists():
        assert n=='polypeptone-metadata-v3-rereview.json',p
        return bind(p)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
    return bind(p)
def resolve(c):
    assert c['root']=='artifact'
    p=c['path']
    q=S/p.removeprefix('buffer-parts-v1/') if p.startswith('buffer-parts-v1/') else B/p
    assert q.is_file(),q
    assert sha(q)==c['sha256'],q
    return q
def changed(a,b): return sorted(k for k in set(a)|set(b) if a.get(k)!=b.get(k))

# Exact metadata-only rereview. Earlier scientific review remains immutable.
poly=S/'polypeptone-final'
p2=read(poly/'proposals-v2.json')['proposals'][0]
p3=read(poly/'proposals-v3.json')['proposals'][0]
assert changed(p2,p3)==sorted(['evidence_ids','predicate_consequence','final_grounding_status','previous_final_grounding_status','metadata_correction'])
assert p3['evidence_ids']==p2['evidence_ids']+['W05-REMAINING-POLYPEPTONE-STATUS-CONSISTENCY']
assert p3['previous_final_grounding_status']==p2['final_grounding_status']
assert p2['after_capture']==p3['after_capture']
assert sha(resolve(p3['after_capture']))=='1eff09e546e9dcf0c0ae6c10e7da74488301f1f50d4270b2310c48b5122ea89d'
dv2=read(poly/'decisions-v2.json')['decisions']; dv3=read(poly/'decisions-v3.json')['decisions']
md=[]
for a,b in zip(dv2,dv3):
    assert a['case_id']==b['case_id']
    assert changed(a,b)==['evidence_ids','polypeptone_final_reassessment']
    x=copy.deepcopy(b);x['evidence_ids']=a['evidence_ids'];x['polypeptone_final_reassessment'].pop('active_grounding_status')
    assert x==a
    assert b['polypeptone_final_reassessment']['active_grounding_status']==p3['final_grounding_status']
    md.append({'case_id':b['case_id'],'selected_decision_object_sha256':obj(b)})
e2=read(poly/'evidence-v2.json')['evidence']; e3=read(poly/'evidence-v3.json')['evidence']
assert e3[:len(e2)]==e2 and len(e3)==len(e2)+1
for e in e3: resolve(e['capture'])
metadata_review=save('polypeptone-metadata-v3-rereview.json',{
 'reviewer':ME,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'finding_id':'W05-CONSOLIDATED-POLYPEPTONE-METADATA-001','disposition':'RESOLVED_EXACT_V3_METADATA_ONLY',
 'finding':bind(poly/'status-finding-before-fix.json'),
 'inputs':[bind(poly/f'{x}-v{v}.json') for x in ['proposals','decisions','evidence'] for v in [2,3]],
 'changed_proposal_fields':changed(p2,p3),'selected_proposal_object_sha256':obj(p3),'after_capture':p3['after_capture'],
 'case_reviews':md,
 'assessment':'The stale self-only/open status is preserved as previous_final_grounding_status. Current status and native predicate consequence now describe the already independently reviewed local named Polypeptone identity with NARROW_MATCH mesh:D010461. Both complete source decisions only add this status and its exact evidence link. Old evidence entries and full YAML are identical. Source associations, quantities, coupled-owner continuity, role and export holds remain; no other worker review is closed. The new consistency entry is a report assertion supported by the retained before-fix finding, not a fresh primary acquisition.',
 'limitations':['No new payload change or extension of the previously reviewed scientific scope.','No whole-owner application or coordinator acceptance.']})

D=read(C/'decisions.json')['decisions'];P=read(C/'proposals.json')['proposals'];E=read(C/'evidence.json')['evidence']
di={x['case_id']:x for x in D};pi={x['proposal_id']:x for x in P};ei={x['evidence_id']:x for x in E}
assert len(di)==len(D)==188 and len(pi)==len(P)==155 and len(ei)==len(E)==1766
oldE=read(B/'tellurium-polypeptone-v1/core/evidence.json')['evidence'];oldEI={x['evidence_id']:x for x in oldE}
assert len(oldE)==1627 and all(ei[k]==v for k,v in oldEI.items())
newE=[x for x in E if x['evidence_id'] not in oldEI]
assert len(newE)==139
ev=[]
for e in newE:
    q=resolve(e['capture'])
    assert all(c in di for c in e.get('case_ids',[]))
    assert e.get('supports_or_contradicts')
    ev.append({'evidence_id':e['evidence_id'],'object_sha256':obj(e),'kind':e['kind'],'capture':e['capture'],'actual_path':str(q),'accessed_at':e.get('accessed_at'),'assessed_at':e.get('assessed_at'),'original_capture_attribution':e.get('original_capture_attribution'),'case_ids':e.get('case_ids',[])})
for x in D+P:
    assert all(i in ei for i in x.get('evidence_ids',[]))
evidence_binding=save('final-new-evidence-bindings-v1.json',{'reviewer':ME,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'old_entries_unchanged':len(oldE),'new_entries':len(newE),'entries':ev,'scope':'Exact capture/reference/chronology-field binding; scientific applicability is in the actual separate lane reviews, not inferred from hashes. Historical initial assessments remain dated and are qualified by their explicit successors.'})

names=['buffer-review-v1.json','chemical-report-scientific-review-v1.json','media-scientific-review-v1.json','parents-scientific-review-v1.json','polypeptone-scientific-review-v1.json','dependencies/main-review.json']
lane={n:read(R/n) for n in names}
payloads={}; cases={}
for n,d in lane.items():
    for v in d.get('payload_reviews',[]):
        w=copy.deepcopy(v);w['assessment_origin']=bind(R/n);w['actual_scientific_reviewer']=CHILD if n.startswith('dependencies/') else ME
        payloads[w['proposal_id']]=w
    for v in d.get('case_reviews',[]):
        cases.setdefault(v['case_id'],[]).append({'assessment':v['assessment'],'origin':bind(R/n),'reviewer':ME})

# Final generic term supersedes the earlier broader candidate and its assay-gate reasoning.
direct=read(R/'direct-parent-independent-review-v1.json')
generic='W05-FINAL-MAT-039';generic_case='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151'
payloads[generic]={'proposal_id':generic,'after_capture':pi[generic]['after_capture'],'assessment':direct['assessment'],'assessment_origin':bind(R/'direct-parent-independent-review-v1.json'),'actual_scientific_reviewer':ME,'interpretation_reassessment':bind(R/'ontology-interpretation-reassessment-v1.json')}
cases[generic_case]=[{'assessment':'The complete frozen two-observation peptones case has the ordinary generic Peptone material sense. NLM D010461 explicitly names Peptone and defines conventional partial protein hydrolysates, consistent with the manufacturer definition. The merely possible base-hydrolysis route or absent precipitation assay does not establish a different actual preparation and must not block exact-term priority. The selected generic owner is mesh:D010461; the older local/D011492 proposal and its stronger food-use/assay reasoning remain preserved as history and are explicitly qualified. Neither source process nor measured lot behavior is invented. Twelve authentic child origins are dependency corrections attached to this existing case, not new W05 source ownership; their literal/raw scopes remain intact. Five genuine named generic parts now reference this exact parent; the other unsupported parts remain UNMAPPED.','origin':bind(R/'direct-parent-independent-review-v1.json'),'reviewer':ME}]
rcm=read(R/'rcm-direct-reference-review-v1.json')
for v in rcm['payload_reviews']:
    w=copy.deepcopy(v);w.update(assessment_origin=bind(R/'rcm-direct-reference-review-v1.json'),actual_scientific_reviewer=ME);payloads[v['proposal_id']]=w
for v in rcm['case_reviews']:cases[v['case_id']].append({'assessment':v['assessment'],'origin':bind(R/'rcm-direct-reference-review-v1.json'),'reviewer':ME})
deps=read(R/'dependency-direct-reference-review-v1.json')
for v in deps['payload_reviews']:
    w=copy.deepcopy(v);w.update(assessment_origin=bind(R/'dependency-direct-reference-review-v1.json'),actual_scientific_reviewer=ME);payloads[v['proposal_id']]=w
for v in lane['dependencies/main-review.json']['case_delta_reviews']:
    cases.setdefault(v['case_id'],[]).append({'assessment':v['assessment'],'origin':bind(R/'dependencies/main-review.json'),'reviewer':CHILD,'scope':'Actual independent source/payload dependency assessment; final composed complete decision independently bound by parent reviewer.'})

# Unchanged earlier chemical review wording is made unambiguous here without rewriting it.
tris='CHEM-C1193-Tris-HCl-salt'
payloads[tris]['assessment']='The complete weighed Tris hydrochloride salt payload retains CAS1185-53-1, form-specific registry identity and NARROW_MATCH to CHEBI9754. Native output correctly contains the broader parent row plus the CAS and local compound identity rows. The weighed salt contexts remain distinct from the nominal buffer-stock contexts reviewed separately; no salt substitution, acid/base partonomy or pH-derived stoichiometry is inferred. Full unchanged source-supported payload, historical evidence and holds were reread.'
payloads[tris]['wording_clarification']='This avoids reading the prior lane receipt phrase about seven weighed contexts as a count of seven salt-only occurrences. No payload, source or decision count changes.'

composition=read(R/'composition-independent-final-v5.json');cr=read(C/'composition-receipt.json')
assert composition['full_decision_composition_exact'] and not composition['errors']
expectedP={x['proposal_id'] for x in cr['payload_reviews']};expectedD={x['case_id'] for x in cr['case_reviews']}
assert set(payloads)==expectedP and len(payloads)==35,(set(payloads)^expectedP)
assert set(cases)==expectedD and len(cases)==21,(set(cases)^expectedD)
finalP=[]
for k,w in sorted(payloads.items()):
    v=pi[k];assert w['after_capture']==v['after_capture'],k
    resolve(w['after_capture'])
    # Previous object hashes remain in the original attributed receipts; bind the actual final selected object here.
    for f in ['proposal_object_sha256','selected_proposal_object_sha256']:w.pop(f,None)
    w['selected_proposal_object_sha256']=obj(v)
    w['case_ids']=v['case_ids'];w['conclusion']='PASS_BOUNDED_SOURCE_PROPOSAL_WITH_LIMITATIONS'
    w['source_owner_export_approval']=False
    if k=='W05-FINAL-MAT-030':w['metadata_rereview']=metadata_review
    if k=='W05-FINAL-MAT-032':w['unchanged_final_direct_lane_binding']=bind(S/'parents-direct-v1/proposals.json')
    finalP.append(w)
finalD=[]
for k,parts in sorted(cases.items()):
    d=di[k];summary=' '.join(x['assessment'] for x in parts)
    if k=='CM_NAME:c98f85469e959e1e268c0a4c07a445d17a3e19ba15f579493d946f9cac1c92c8':
        summary='The authentic clarified-rumen JCM1423/1424 reference266 facts and distinct held companion remain unchanged. The current dependency additions concern two PYG/PY-glucose composites whose rumen component stays literal and UNMAPPED; they do not reinterpret the clarified source case or establish untreated fluid. Their unsupported peptone references are independently withdrawn, preserving the exact earlier processing and recipe holds. '+summary
    if k=='KG_CASE:d987d7fef6b2a7e4162cfe6eefc6ca350a825368479583e9234adfd79185142a':
        summary='The complete existing cooked-meat source decision remains intact. Only the FAB dependency report/evidence is added: actual methods associate FAB with Oxoid, while the separate PYG assay and LabM/Neogen comparator cannot supply its historical formula. The unsupported peptone resolving reference is withdrawn without asserting peptone absent. '+summary
    if k=='KG_CASE:c32b77bb4cf6ac08f95e5ee9c40834693b98899db178b6451c581aabf6cccb25':
        summary+=' The authentic rejected Bacto Soytone tombstone now has an explicitly empty representative, preventing native shared-FOODON fallback while retaining its own rejected continuity. This is neither branded/generic synonym equality nor a reassignment of the shared source associations. Exact original owner binding is deduplicated; current shared-owner/source, role and export holds remain.'
    if k in {x['case_id'] for x in dv3}:summary+=' The exact v3 report-only status correction has been independently rereviewed: current supported source-proposal grounding replaces stale self-only wording, while historical status and all source/owner/role/export limitations remain.'
    finalD.append({'case_id':k,'selected_decision_object_sha256':obj(d),'case_input_sha256':d['case_input_sha256'],'source':d['source'],'occurrence_ids':d['occurrence_ids'],'selected_disposition':d['disposition'],'assessment':summary,'assessment_origins':parts,'final_composition_reviewer':ME,'composition_check':bind(R/'composition-independent-final-v5.json'),'conclusion':'PASS_BOUNDED_COMPOSED_DECISION_WITH_SOURCE_HOLDS','source_owner_export_approval':False})

# Root native checks are read and bound as separate validation evidence, never as science.
V=B/'buffer-parts-v1/validation'
nativefiles=['consolidated-validation.receipt.json','full-overlay/native-validation.json','full-strict.receipt.json','full-strict.stdout.log','native-row-projections.json']
validation=[bind(V/n) for n in nativefiles]
assert read(V/'consolidated-validation.receipt.json')['exit_code']==0
assert read(V/'full-strict.receipt.json')['exit_code']==0
nv=read(V/'full-overlay/native-validation.json');nr=read(V/'native-row-projections.json')
assert nv['candidate_payloads']==155 and nv['overlay_records']==3029 and nr['status']=='PASS'
assert nv['inputs']['proposals']['sha256']==sha(C/'proposals.json')
reviewedids=set(payloads)
selected_native=[x for x in nr['reviewed_projections'] if x['proposal_id'] in reviewedids]
assert len(selected_native)==35
for x in selected_native: assert x['after_capture']==pi[x['proposal_id']]['after_capture']
nativebinding=save('selected-native-review-binding-v1.json',{'reviewer':ME,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':bind(V/'native-row-projections.json'),'validation_receipts':validation,'selected_complete_rows':selected_native,'scope':'Thirty-five scoped complete projection results are bound to the exact reviewed payloads. Author full155 isolated guard/schema/overlay checks are retained independently from the scientific assessments. No final saved native review bundle or maintained/export application is claimed.'})

findings=[]
for n in ['buffer-review-v1.json','chemical-report-scientific-review-v1.json','media-scientific-review-v1.json','polypeptone-scientific-review-v1.json']:
    for x in lane[n].get('finding_dispositions',[]):findings.append({'origin':bind(R/n),**x})
findings.extend([
 {'finding_id':'W05-PARENTS-NEW01','disposition':'MISSING_FORMAL_AXIOM_CONFIRMED; STRONGER_FOOD_USE_GATE_QUALIFIED; CLOSER_MESH_TERMS_SELECTED','assessment':'The complete FoodOn member_of existential was omitted from the earlier candidate assessment. Its existence is confirmed, but external classification membership does not entail a source food-use, has-role, assay or certification gate. The actual definition-level rereview supports generic Peptone exact D010461 and named Polypeptone broader D010461; earlier stronger inference is preserved and expressly qualified.','review':bind(R/'ontology-interpretation-reassessment-v1.json')},
 {'finding_id':'W05-CONSOLIDATED-PARENTS-REVIEW-001','disposition':'RESOLVED_EXACT_TOMBSTONE_V2','assessment':'Only the newly authored unsupported human-attribution phrase was removed. All inherited evidence enums and original objects remain unchanged.','review':bind(R/'tombstone-independent-review-v1.json'),'finding':bind(R/'parents-new-finding-v1.json')},
 {'finding_id':'W05-CONSOLIDATED-POLYPEPTONE-METADATA-001','disposition':'RESOLVED_EXACT_V3_METADATA_ONLY','review':metadata_review},
 {'finding_id':'W07-W05-MAT-PARENT-001','disposition':'BOUNDED_SOURCE_PARENT_PROPOSALS_SUPPORTED; CONTINUITY_AND_SOURCE_HOLDS_REMAIN','assessment':'Soy generic exact MICRO181 and Peptone generic exact MeSH D010461 are supported by full material definitions and actual source observations. The tombstone and child reference continuity is separately reviewed; no arbitrary shared-owner winner or release of source unions follows.'},
 {'finding_id':'W05-FINAL-SKEPTIC-CHEM-006','disposition':'CONTEXT_RETAINED; NO_NEW_ENUM_CORRECTION','assessment':'Earlier native disposition correction remains unchanged; this successor does not restore the invalid custom curation_proposal value.'},
 {'finding_id':'PEPTONE-SOURCE-001','disposition':'SOURCE_SPECIFIC_HOLDS_PRESERVED','assessment':'Bare PY/PYG abbreviations and source-specific FAB product formula gaps do not establish literal generic peptone constituents. Ten unsupported resolving references remain withdrawn; the five actual named generic constituents are supported separately.','review':bind(R/'dependencies/main-review.json')}
])
# Dedup repeated finding IDs by retaining every actual receipt, while selecting explicit latest interpretation.
fg={}
for f in findings:
    fid=f.get('finding_id') or f.get('id')
    if not fid:continue
    fg.setdefault(fid,[]).append(f)

ledger_names=['independent-primary-assessment-v1.json','independent-html-read-v1.json','buffer-frozen-context-read-addendum-v1.json','parents-media-source-read-ledger-v1.json','chemical-report-scientific-review-v1.json','dependencies/source-read-ledger.json','dependency-direct-reference-review-v1.json','polypeptone-scientific-review-v1.json','ontology-interpretation-reassessment-v1.json']
ledgers=[bind(R/n) for n in ledger_names if (R/n).is_file()]
completed=datetime.datetime.now(datetime.timezone.utc).isoformat()
main={
 'schema_version':1,'review_id':'W05-CONSOLIDATED-INDEPENDENT-SCIENCE-V1','reviewer':ME,'completed_at':completed,
 'base_head':'0bac12cabfd1f67f212631d8eef9aa46379f6b41','verdict':'PASS_BOUNDED_REPORT_AND_SOURCE_PROPOSALS_WITH_EXPLICIT_LIMITATIONS',
 'source_owner_export_approval':False,
 'independence':'No primary/source/payload authorship by this reviewer. Main reviewer independently assesses twenty-five complete final payloads and all final composition. Ten exact unchanged dependency payloads reuse the actual separate child scientific judgments verbatim, with child attribution and immutable byte binding; the other five dependency payloads received fresh final full-payload review by the main reviewer after direct-parent changes.',
 'actual_scientists':[{'identity':'/root/buffer_hepes','scope':'HEPES; generic Soy/Peptone parent alternatives and final direct Peptone; authentic Bacto Soytone tombstone'},{'identity':'/root/buffer_tris','scope':'Tris; fifteen source-specific dependency payloads, including five final direct-parent successors'},{'identity':'/root','scope':'Media components and captions; chemical report verification; named Polypeptone final grounding/alias/status successors'}],
 'actual_reviewers':[{'identity':ME,'scope':'Twenty-five final complete payloads, twenty-one final complete decisions and exact composition; own actual source read ledgers below'},{'identity':CHILD,'scope':'Fifteen complete dependency payloads, twenty prior outcomes, all130 raw source observations and source-specific primary passages in the earlier sealed lane. Ten exact unchanged payload judgments reused; five later changed direct references independently rereviewed by main reviewer.','receipt':bind(R/'dependencies/main-review.json'),'manifest':bind(R/'dependencies/MANIFEST.json')}],
 'scope':{'cases':21,'complete_payloads':35,'new_authentic_origins':13,'changed_prior_payloads':8,'retained_current_case_universe':188,'retained_final_proposal_universe':155,'evidence_universe':1766,'old_evidence_unchanged':1627,'new_evidence_entries':139,'new_assigned_cases':0,'maintained_changes':0},
 'selected_inputs':[bind(C/f'{n}.json')for n in ['decisions','proposals','evidence','proposal-lineage','composition-receipt']]+[bind(S/'control/selection-final-v5.json')],
 'case_reviews':finalD,'payload_reviews':finalP,
 'scientific_interpretation_reassessment':bind(R/'ontology-interpretation-reassessment-v1.json'),
 'finding_dispositions':[{'finding_id':k,'attributed_dispositions':v,'latest_selected_interpretation':v[-1]}for k,v in sorted(fg.items())],
 'no_unreported_new_scientific_finding':True,
 'actual_read_ledger_bindings':ledgers,
 'lane_review_bindings':[bind(R/n)for n in names]+[bind(R/n)for n in ['direct-parent-independent-review-v1.json','rcm-direct-reference-review-v1.json','dependency-direct-reference-review-v1.json','tombstone-independent-review-v1.json','parents-final-integrity-v1.json']],
 'exact_final_evidence_bindings':evidence_binding,'polypeptone_status_rereview':metadata_review,
 'exact_composition_check':bind(R/'composition-independent-final-v5.json'),'native_validation_binding':nativebinding,
 'chronology':'Buffer correction private history07:40:53 precedes formal finding filing07:43:24, and its first publication at5156 was08:25:04. This supplement verifies already-correct buffers without inventing a new payload event or backdating formal filing. Parent NEW01 worker report precedes its private candidate selection while formal GitHub filing follows; exact actual times and later interpretation changes are retained in receipts. Historical primary capture times and authors are not reauthored.',
 'current_scientific_conclusions':['Whole nominal HEPES/Tris stocks have no unsupported speciation/moiety parts or paired assertion; stockstrength/sourcepH/quantities remain distinct from dry salt and receiving-medium pH.','Marine seven and RCM three source-supported references are justified individually; fifteen other nominal inputs retain explicit form/process/identity limits. COMPLETE concerns each printed approximate named formula, not lot composition.','Generic Peptone exact MeSH D010461 and generic Soy Peptone exact MICRO181 are supported; named Polypeptone retains its local identity with broader D010461, and specific BD labels remain nonresolving provenance.','An explicit empty rejected Bacto Soytone representative prevents unsafe shared-identifier fallback; it does not choose a new live owner or assert branded/generic equivalence.','Twelve authentic child origins and three existing composites preserve original source-label and preparation scope; five explicit generic inputs now reference direct MeSH Peptones, ten unsupported references remain withdrawn.','All source-specific occurrence, quantity, processing, association, source-admission, role and export holds remain. No guessed chemical identity, owner union, assay requirement or arbitrary winning identifier is introduced.'],
 'limitations':['This is a report-only scientific proposal review. Root still owns final wrapper/native review persistence and publication; final integration and export acceptance remain separate.','Hash preservation and native validation are mechanical evidence and are not presented as fresh chemistry approval of every155 payload or every188 case.','Historical exact unchanged reviews/captures are reused only with actual attribution. Raw recipe/source rows do not constitute full-text review of every cited publication.','Large quarantined Soy association sets are preserved, not newly adjudicated row by row; explicit shared-owner and source-association holds remain.','Full prior private candidates and initial reviewer judgments, including the stronger assay/use-gate interpretation, remain immutable with this explicit successor qualification.','No new scientific approval of another worker combined owner, no merging and no automatic retirement of their whole-owner review.']
}
mainbinding=save('main-review.json',main)
handoff=save('HANDOFF.json',{'reviewer':ME,'completed_at':completed,'main_review':mainbinding,'scope':main['scope'],'verdict':main['verdict'],'actual_child_review':bind(R/'dependencies/main-review.json'),'final_selector':bind(S/'control/selection-final-v5.json'),'source_owner_export_approval':False,'next':'Root may prepare the final canonical/native report assembly from these exact reviewed bytes; a separate final assembly review must bind its actual final output. This review tree is sealed and must remain immutable.'})
files=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size}for p in sorted(R.rglob('*'))if p.is_file() and p.name!='FINAL-MANIFEST-v1.json']
manifest=save('FINAL-MANIFEST-v1.json',{'reviewer':ME,'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'main_review':mainbinding,'handoff':handoff,'members':files,'member_count':len(files),'scope':'All original independent review files, failed local diagnostics, earlier judgments, child review and final successors are retained; manifest excludes only itself.'})
print(json.dumps({'main_review':mainbinding,'manifest':manifest,'handoff':handoff,'completed_at':completed,'case_reviews':len(finalD),'payload_reviews':len(finalP)},indent=2))
