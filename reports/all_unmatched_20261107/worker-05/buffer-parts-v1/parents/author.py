from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, shutil, subprocess
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient

W = Path.cwd()
C = W.parents[2]
B = W / 'reports/all_unmatched_20261107/worker-05'
S = W / '.temp/w05-buffer-parts-v1/parents'
CORE = B / 'tellurium-polypeptone-v1/core'
PUBLIC = 'buffer-parts-v1/parents/'
AUTHOR = '/root/buffer_hepes'
AT = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
objsha = lambda x: hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()

def write(path, obj):
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

def exact_copy(src, dest):
    assert not dest.exists(), dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    assert sha(src) == sha(dest)
    return dict(source_path=str(src), source_sha256=sha(src), copied_path=str(dest.relative_to(S)), copied_sha256=sha(dest))

pids = ['W05-FINAL-MAT-032', 'W05-FINAL-MAT-039']
allp = json.loads((CORE / 'proposals.json').read_text())['proposals']
ps = [copy.deepcopy(p) for p in allp if p['proposal_id'] in pids]
cids = [p['case_ids'][0] for p in ps]
alld = json.loads((CORE / 'decisions.json').read_text())
ds = [copy.deepcopy(d) for d in alld['decisions'] if d['case_id'] in cids]
olde = json.loads((CORE / 'evidence.json').read_text())['evidence']
ledger = []
for filename in ['proposals.json', 'decisions.json', 'evidence.json', 'proposal-lineage.json']:
    f = CORE / filename
    ledger.append(dict(path=str(f), sha256=sha(f), scope='Complete bytes parsed; only the two assigned parent proposal/source-case objects are changed.'))
write(S / 'input/selected-proposals.json', dict(schema_version=1, proposals=ps))
write(S / 'input/selected-decisions.json', dict(schema_version=1, decisions=ds))
source = B / 'contracts/shard-05.json'
frozen = [x for x in json.loads(source.read_text())['cases'] if x['case_id'] in cids]
write(S / 'input/frozen-cases.json', dict(source=dict(path=str(source), sha256=sha(source)), cases=frozen))
ledger.append(dict(path=str(source), sha256=sha(source), scope='Both complete frozen assigned source cases, including all inherited hold objects and raw occurrence provenance.'))
for p in ps:
    for which in ['before_capture', 'after_capture']:
        f = B / p[which]['path']; assert sha(f) == p[which]['sha256']
        ledger.append(exact_copy(f, S / ('input/original-before' if which == 'before_capture' else 'input/current-selected') / f.name))

mf = C / 'preflight/w05-consolidated-remaining-work-v1/MANIFEST.json'
ledger.append(exact_copy(mf, S / 'input/assignment/MANIFEST.json'))
for m in json.loads(mf.read_text())['files']:
    f = mf.parent / m['capture']; assert sha(f) == m['sha256']
    ledger.append(exact_copy(f, S / 'input/assignment' / f.name))
for n in ['comment6719578158.json', 'comment6719660443.json', 'remaining-capture-receipt.json']:
    ledger.append(exact_copy(S.parent / 'issues' / n, S / 'input/issues' / n))
for n in ['MAPPING_SEMANTICS.md', '.claude/skills/add-media/SKILL.md', '.claude/skills/curate-yaml-record/SKILL.md', '.claude/skills/curate-yaml-record/references/review-checklist.md', 'src/mediaingredientmech/schema/mediaingredientmech.yaml']:
    f = W / n
    if f.is_file(): ledger.append(dict(path=str(f), sha256=sha(f), scope='Current identity/partonomy, guarded curation and schema contract.'))

old_thermo = W / '.temp/w05-tellurium-polypeptone-v1/polypeptone'
for n in ['thermo.pdf', 'thermo.pdf.receipt.json']:
    ledger.append(exact_copy(old_thermo / 'captures' / n, S / 'captures' / n))
ledger.append(exact_copy(old_thermo / 'read/thermo.txt', S / 'read/thermo.txt'))
# Keep the original capture's actual acquisition time and retriever; this is a new applicability assessment, not a new download.
thermo_receipt = json.loads((S / 'captures/thermo.pdf.receipt.json').read_text())
assert thermo_receipt['sha256'] == sha(S / 'captures/thermo.pdf')
for n in ['Soya_Pepton.yaml', 'Soya_Peptone.yaml', 'Phytone.yaml', 'Bacto_Soytone.yaml', 'Polypeptone.yaml']:
    f = W / 'data/ingredients/mapped' / n
    if f.exists(): ledger.append(exact_copy(f, S / 'input/adjacent-owners' / n))

soy_text = (
    'Replace the provisional local self-mapping with the supported generic MICRO:0000181 soy peptone identity under MAPPING_SEMANTICS section 3. '
    'The complete active term and its BD definition-source discussion describe generic enzymatic soy-flour digest; MediaDive ingredient 75 names Soy peptone with soybean/soymeal synonyms, '
    'and the Thermo Fisher guide independently defines generic soy peptones as enzymatic digests of soy flour. '
    'This is not an identity assertion for Phytone, Difco/Bacto Soytone or any supplier, enzyme or lot. '
    'Do not import the erroneous Hordeum vulgare parenthesis, branded/papaic synonyms, or annotated ash/NaCl numbers. '
    'Preserve all prior aliases and five branded/alternative withdrawals, complete original histories, occurrence totals, Bacto Soytone tombstone, source quarantines, sibling/incoming-reference obligations, and physical-form/role/export holds. '
    'The inherited Peptic digest of soybean meal alias is not newly supported or approved by this generic term assessment.'
)
pep_text = (
    'Complete the previously missing nonidentity family grounding: generic Peptone remains kgmicrobe.ingredient:peptone and maps NARROW_MATCH to FOODON:03315306 protein hydrolyzates, yielding native broadMatch plus the local B1 identity row. '
    'The manufacturer guide defines peptones as water-soluble products of partial protein hydrolysis from plant, yeast or animal material; the protein-hydrolyzate family is broader than this unspecified peptone material. '
    'The complete FoodOn record is an active SIREN-derived material class with a flavoring annotation and a pending-classification food-material parent; neither annotation establishes an assay role, supplier, feedstock, enzyme, processing specification or exact peptone identity. '
    'MICRO:0000178 adds unsupported mammalian origin; MICRO:0000174 adds an unestablished enzymatic process; MICRO:0000172 explicitly discusses plant/animal protein and does not establish coverage of the source-unspecified yeast possibility. '
    'No exact applicable generic Peptone identity was established in the bounded official searches. '
    'Preserve both MicrobeDecoder observations, plural/raw provenance, truncated-token rejection, all histories/statistics, provisional roles and all source/owner/export holds. '
    'Incoming MICRO:0000178 references require separately authored source-specific reconciliation, not a blanket retarget.'
)
notes_by_pid = dict(zip(pids, [soy_text, pep_text]))
newps, deltas = [], []
for p in ps:
    current = yaml.safe_load((B / p['after_capture']['path']).read_text())
    r = copy.deepcopy(current)
    if p['proposal_id'] == pids[0]:
        r['identifier'] = 'MICRO:0000181'
        r['ontology_mapping'].update(ontology_id='MICRO:0000181', ontology_label='soy peptone', ontology_source='MICRO', mapping_quality='EXACT_MATCH')
        newev = [
            dict(evidence_type='LLM_SUGGESTION', source='https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000181', notes='Full active term and BD definition-source annotation support the generic enzymatic soybean-flour digest identity. This interpretation excludes the erroneous Hordeum vulgare parenthesis, branded Bacto/Soytone and papaic synonyms, and product-specific numeric composition; it does not approve inherited peptic-process aliases or branded-product equivalence.'),
            dict(evidence_type='LLM_SUGGESTION', source='https://mediadive.dsmz.de/rest/ingredient/75', notes='Source ingredient 75 names generic Soy peptone and soybean/soymeal aliases with no branded product identity. Read together with the manufacturer generic soy-peptone definition, this supports the generic MICRO:0000181 scope; supplier, specific enzyme, lot, physical form and source admission remain unresolved.'),
            dict(evidence_type='LLM_SUGGESTION', source=thermo_receipt['url'], notes='Printed page 26 defines generic soy peptones as enzymatic digests of soy flour; page 33 distinguishes named products and processing. This supports the generic material identity only and supplies no whole-stock composition, specific enzyme, branded equivalence or role approval.')
        ]
        identity = 'Existing generic Soy Peptone owner receives the supported MICRO:0000181 primary identity; no owner merge or sibling/product identity decision. The provisional local identity remains in immutable predecessor history.'
        predicate = 'Native exactMatch to MICRO:0000181 replaces the provisional local self row; no parent identity or arbitrary winning owner. Source, role, alias and export holds remain.'
    else:
        r['ontology_mapping'].update(ontology_id='FOODON:03315306', ontology_label='protein hydrolyzates', ontology_source='FOODON', mapping_quality='NARROW_MATCH')
        newev = [
            dict(evidence_type='LLM_SUGGESTION', source=thermo_receipt['url'], notes='Printed page 7 defines peptones as water-soluble products of partial hydrolysis of proteins from plant, yeast or animal sources. This supports nonidentity membership in the broader protein-hydrolyzate material family without supplying the source observations\' feedstock, enzyme, manufacturer, lot or role.'),
            dict(evidence_type='LLM_SUGGESTION', source='https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315306', notes='The complete active term protein hydrolyzates, including SIREN annotation and pending-classification parent, was compared with the manufacturer material definition. Use only the broader protein-hydrolyzate material relation, NARROW_MATCH / native broadMatch, retaining local Peptone identity. The flavoring annotation is not evidence of an assay or nutritional role. No exact identity or animal/plant substrate is inferred from the label.'),
            dict(evidence_type='LLM_SUGGESTION', source='https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000178', notes='The complete MICRO peptone definition restricts its material to enzymatic mammalian protein digest. The two frozen unqualified MicrobeDecoder peptones observations do not supply that origin or process, so this term is excluded as their exact generic owner identity.')
        ]
        identity = 'Preserve kgmicrobe.ingredient:peptone as the existing generic material identity. The two source observations remain unresolved as to actual supplier, feedstock, process and assay identity.'
        predicate = 'Native broadMatch to FOODON:03315306 plus exactMatch kgmicrobe.ingredient:peptone B1 registry row; no broad/parent identity substitution.'
    r['ontology_mapping']['evidence'].extend(newev)
    text = notes_by_pid[p['proposal_id']]
    r['curation_history'].append(dict(timestamp=AT, curator='Codex /root/buffer_hepes; W05 consolidated report-only parent correction', action='CORRECTED', changes=text + ' Isolated guarded successor proposal only; no maintained write or source admission.', previous_status=r['mapping_status'], new_status=r['mapping_status'], llm_assisted=True, llm_model='gpt-6'))
    r['notes'] += '\n\nConsolidated parent-grounding successor (prior scope text retained as historical provenance): ' + text + ' Independent exact-byte review and root integration remain pending.'
    dest = S / 'proposed' / Path(p['owner_path']).name
    assert not dest.exists()
    write_validated_ingredient(r, dest)
    assert yaml.safe_load(dest.read_text()) == r
    # Material changes are exactly bounded. Every previous history/evidence object stays intact.
    changed = [k for k in set(current) | set(r) if current.get(k) != r.get(k)]
    assert set(changed) <= {'identifier', 'ontology_mapping', 'curation_history', 'notes'}
    assert r['curation_history'][:-1] == current['curation_history']
    assert r['ontology_mapping']['evidence'][:-len(newev)] == current['ontology_mapping']['evidence']
    np = copy.deepcopy(p)
    np['description'] += ' Consolidated parent-grounding successor: ' + text
    np['parent_predecessor_capture'] = copy.deepcopy(p['after_capture'])
    np['after_capture'] = dict(root='artifact', path=PUBLIC + 'proposed/' + dest.name, sha256=sha(dest))
    np['identity_consequence'] = identity
    np['predicate_consequence'] = predicate
    np['parent_successor_author'] = AUTHOR
    np['parent_successor_at'] = AT
    np['independent_review'] = dict(status='pending exact successor bytes; historical reviews retained separately', evidence_ids=[])
    newps.append(np)
    deltas.append(dict(proposal_id=p['proposal_id'], case_ids=p['case_ids'], before_capture=p['before_capture'], predecessor_capture=p['after_capture'], after_capture=np['after_capture'], changed_top_level_fields=sorted(changed), prior_history_events_preserved=len(current['curation_history']), appended_history_events=1, prior_mapping_evidence_objects_preserved=len(current['ontology_mapping']['evidence']), appended_mapping_evidence_objects=len(newev), other_fields_parsed_identical=True))

# Complete maintained-owner and selected-proposal identity collision scan. Path.rglob does not respect gitignore.
targets = {'MICRO:0000181', 'kgmicrobe.ingredient:peptone', 'kgmicrobe.ingredient:soy_peptone', 'FOODON:03315306', 'MICRO:0000178'}
scan = []
for f in sorted((W / 'data/ingredients').rglob('*.yaml')):
    r = yaml.safe_load(f.read_text()) or {}
    if r.get('identifier') in targets:
        scan.append(dict(path=str(f.relative_to(W)), sha256=sha(f), identifier=r.get('identifier'), mapping_status=r.get('mapping_status')))
overlay_hits = []
for p in allp:
    f = B / p['after_capture']['path']; assert sha(f) == p['after_capture']['sha256']
    r = yaml.safe_load(f.read_text())
    if r.get('identifier') in targets:
        overlay_hits.append(dict(proposal_id=p['proposal_id'], owner_path=p['owner_path'], after_capture=p['after_capture'], identifier=r['identifier']))
assert not [x for x in scan if x['identifier'] == 'MICRO:0000181']
assert not [x for x in overlay_hits if x['identifier'] == 'MICRO:0000181']
write(S / 'owner-identity-search.json', dict(author=AUTHOR, at=AT, ignored_files_included=True, method='Path.rglob over every maintained ingredient YAML, plus all current canonical selected full proposal payloads; no gitignore exclusions.', bounded_scope='Current W05 checkout and selected W05 proposals, not every other worker live head. Root must reconcile frozen/advancing cross-worker siblings separately.', maintained_records_scanned=len(list((W / 'data/ingredients').rglob('*.yaml'))), selected_proposals_scanned=len(allp), primary_identifier_targets=sorted(targets), maintained_hits=scan, selected_hits=overlay_hits, no_existing_MICRO_0000181_primary_identity_in_this_scan=True))

ev = []
def evidence(eid, file, kind, locator, support, case_ids=None, url=None, accessed_at=None, origin=None):
    row = dict(evidence_id=eid, capture=dict(root='artifact', path=PUBLIC + str(file.relative_to(S)), sha256=sha(file)), kind=kind, locator=locator, supports_or_contradicts=support, case_ids=case_ids or cids, url=url)
    if accessed_at: row['accessed_at'] = accessed_at
    if origin: row['original_capture_attribution'] = origin
    ev.append(row)
for f in sorted((S / 'captures').glob('*.json')):
    if '.receipt.' in f.name: continue
    receipt_path = f.with_name(f.stem + '.receipt.json')
    if not receipt_path.exists(): continue
    rec = json.loads(receipt_path.read_text()); assert rec['sha256'] == sha(f)
    eid = 'W05-PARENTS-' + f.stem.upper()
    evidence(eid, f, 'primary_source' if f.stem == 'mediadive75' else 'ontology', 'Full captured response, including all returned term annotations, status and hierarchy/search metadata.', 'Claim-specific applicability and excluded alternatives are assessed in primary-assessment.json; raw label/search presence alone is not identity approval.', url=rec['url'], accessed_at=rec['accessed_at'], origin=dict(retriever=rec.get('author', AUTHOR), receipt_path=PUBLIC + str(receipt_path.relative_to(S)), receipt_sha256=sha(receipt_path)))
evidence('W05-PARENTS-THERMO', S / 'captures/thermo.pdf', 'primary_source', 'Complete manufacturer guide; printed pp.7,26,33 read for generic peptone/soy-peptone material definitions and named-product distinctions.', 'Generic partial protein hydrolysates and generic enzymatic soy-flour digests; no product, role, numerical composition or assay-origin substitution.', url=thermo_receipt['url'], accessed_at=thermo_receipt['accessed_at'], origin=dict(retriever='/root/polypeptone (earlier W05 primary capture)', receipt_path=PUBLIC + 'captures/thermo.pdf.receipt.json', receipt_sha256=sha(S / 'captures/thermo.pdf.receipt.json'), reused_exact_bytes=True, current_applicability_assessor=AUTHOR))
evidence('W05-PARENTS-FROZEN-CASES', S / 'input/frozen-cases.json', 'source_snapshot', 'Both complete frozen source cases, raw identities, all occurrences and original held source/owner dispositions.', 'Unchanged source scope; only the local parent proposals are reassessed.')
evidence('W05-PARENTS-OWNER-SEARCH', S / 'owner-identity-search.json', 'source_snapshot', 'Every maintained individual YAML plus every selected W05 proposal, ignored files included.', 'No duplicate primary MICRO:0000181 owner is introduced in this bounded W05 overlay; sibling and cross-worker reconciliation remain root-owned.')
for n in ['comment6719578158', 'comment6719660443']:
    f = S / 'input/issues' / (n + '.json'); j = json.loads(f.read_text())
    evidence('W05-PARENTS-' + n.upper(), f, 'source_snapshot', 'Complete filed comment; creation and update times retained.', 'Filed bounded parent/direct-term scopes precede this successor proposal event. The filing itself is not scientific approval.', url=j['html_url'], accessed_at=next(x['accessed_at'] for x in json.loads((S / 'input/issues/remaining-capture-receipt.json').read_text()) if x['path'] == n + '.json'), origin=dict(retriever='/root', created_at=j['created_at'], updated_at=j['updated_at']))

eids = [e['evidence_id'] for e in ev]
assert not set(eids) & {e['evidence_id'] for e in olde}
for p in newps: p['evidence_ids'] += [x for x in eids if x not in p['evidence_ids']]
updated_ds = []
case_deltas = []
for d in ds:
    old = copy.deepcopy(d)
    pid = d['proposal_ids'][0]
    reasoning = (
        'MediaDive ingredient 75 and independent manufacturer generic soy-flour digest definitions support generic MICRO:0000181 exact material identity. The complete term\'s erroneous taxonomy, branded/papaic aliases and numeric product annotations are excluded. Preserve the existing five branded/alternative withdrawals, all quarantines, sibling/incoming-reference, peptic-process alias, physical-form, role and export holds; no source occurrence or product equality is newly admitted.'
        if pid == pids[0] else
        'The two MicrobeDecoder peptones observations establish unspecified protein-digest material without mammalian origin, enzyme, supplier or lot. Retain local generic Peptone identity and complete the nonidentity FOODON:03315306 protein-hydrolyzate family grounding. Preserve plural/raw provenance, truncated-token rejection and assay/source/role holds. Historical and current dependent MICRO:0000178 references still require the separately authored source-level reconciliation, never automatic retargeting.'
    )
    d['reasoning'] = reasoning
    d['parents_reassessment'] = dict(author=AUTHOR, at=AT, status='primary complete; exact successor independent review pending', predecessor_decision_sha256=objsha(old), changed_proposal_ids=[pid], conclusion=reasoning, source_case_and_occurrence_membership_unchanged=True, inherited_hold_objects_unchanged=True, new_owner_or_release_approval=False, separate_dependency_reassessment_owner='/root/buffer_tris', primary_scope='Two existing parent owner proposals only; dependency case fields will be composed by root and independently rereviewed in full.')
    d['evidence_ids'] += [x for x in eids if x not in d['evidence_ids']]
    for u in ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719578158', 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719660443', 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226']:
        if u not in d['issue_refs']: d['issue_refs'].append(u)
    changes = {k: d[k] for k in d if d.get(k) != old.get(k)}
    assert set(changes) == {'reasoning', 'parents_reassessment', 'evidence_ids', 'issue_refs'}
    updated_ds.append(d)
    case_deltas.append(dict(case_id=d['case_id'], base_decision_sha256=objsha(old), changed_fields=changes, additive_arrays=['evidence_ids', 'issue_refs'], independent_full_final_composed_decision_review_required=True))
write(S / 'proposals.json', dict(schema_version=1, proposals=newps))
write(S / 'decisions.json', dict(schema_version=1, decisions=updated_ds))
write(S / 'case-deltas.json', dict(schema_version=1, author=AUTHOR, base_core=dict(path=str(CORE / 'decisions.json'), sha256=sha(CORE / 'decisions.json')), deltas=case_deltas))
write(S / 'evidence.json', dict(schema_version=1, evidence=ev))
write(S / 'authorship-and-delta.json', dict(author=AUTHOR, at=AT, base_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(), scope='Two parent owner payloads, two source-case parent deltas; complete inherited objects preserved; no dependency, Polypeptone or maintained writes.', proposals=deltas, changed_payload_count=2, changed_proposal_ids=pids, exact_review_pending=True))
write(S / 'read-ledger-initial.json', dict(author=AUTHOR, at=AT, inputs=ledger))
print(json.dumps(dict(proposals=[dict(proposal_id=p['proposal_id'], after_capture=p['after_capture']) for p in newps], evidence=len(ev), source_cases=len(updated_ds)),indent=2))
