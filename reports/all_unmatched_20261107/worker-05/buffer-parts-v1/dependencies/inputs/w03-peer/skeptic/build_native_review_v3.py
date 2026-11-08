"""Private read-only native review producer; never writes corpus or canonical reviews."""
from pathlib import Path
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import sys
import yaml

ROOT = Path.cwd()
BASE = ROOT / '.temp/peptone-consumer-independent-v1'
OUT = BASE / 'skeptic'
NATIVE = OUT / 'native'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_new(p, value, raw=False):
    assert not p.exists(), str(p)
    p.write_bytes(value if raw else (json.dumps(value, indent=2) + '\n').encode())

def relative(p):
    return str(p.relative_to(ROOT))

spec = importlib.util.spec_from_file_location('record_review_native', ROOT / 'scripts/record_review.py')
native = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = native
spec.loader.exec_module(native)

ledger = json.loads((OUT / 'final-perclaim-assessment-v1.json').read_text())
claims = ledger['claims']
assert len(claims) == len({c['target_id'] for c in claims}) == 20
targets = json.loads((NATIVE / 'targets-normalized.json').read_text())['targets']
original_inspect = json.loads((NATIVE / 'inspect-before-final-adjudication.json').read_text())
native.assert_current_source(ROOT, original_inspect)

# Bound all final peer evidence and review receipts. Captured failed requests remain
# preserved input evidence of access limits, never positive scientific evidence.
extra = set(i['path'] for i in original_inspect['source']['inputs'])
for subtree in ['other', 'ambiguous']:
    for p in sorted((BASE / subtree).rglob('*')):
        if p.is_file():
            extra.add(relative(p))
for name in ['context/ROUTES.md', 'context/claims-20.json', 'context/input-receipt.json',
             'context/owner-bindings-20.json', 'context/authentic-causal-case.json',
             'context/issue1176-comment-6719248666.json', 'context/native-dependency-probe.json',
             'route-and-composition-v2.json', 'validation/native-record-schema.json',
             'validation/native-probe-reuse.json']:
    extra.add(relative(BASE / name))
for p in sorted((BASE / 'context/target-owners').glob('*.yaml')):
    extra.add(relative(p))
for p in sorted(OUT.iterdir()):
    if p.is_file():
        extra.add(relative(p))
inspect = native.inspect_source(ROOT, targets, sorted(extra))
inspect['inspection_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
write_new(NATIVE / 'inspect-final-inputs-v3.json', inspect)

now = dt.datetime.now(dt.timezone.utc)
finished = now.isoformat().replace('+00:00', 'Z')
review_id = now.strftime('%Y%m%dT%H%M%SZ') + '-peptone-consumer-independent-v1'
ids = [c['target_id'] for c in claims]
generic = [c['target_id'] for c in claims if c['cohort'] == 'conditional_generic']
holds = [c['target_id'] for c in claims if c['cohort'] == 'source_identity_hold']
assert len(generic) == 8 and len(holds) == 10

evidence = []
def ev(eid, path, kind, support, summary, locator=None):
    p = ROOT / path
    row = {'evidence_id': eid, 'kind': kind, 'reference': path,
           'accessed_at': finished, 'support': support, 'summary': summary,
           'snapshot_sha256': sha(p)}
    if kind == 'search':
        row['search_scope'] = 'Exact bound source-access attempts and publication/repository leads listed in the fourteen-source catalog; no exhaustive claim about all library, historical or private files. Unread methods and inaccessible sources are explicitly recorded, never treated as inspected.'
    if locator:
        row['locator'] = locator
    evidence.append(row)
    return eid

ev('rules', 'MAPPING_SEMANTICS.md', 'authority', 'supports',
   'Sections 3 and 6 require source-specific identity and distinguish named unresolved parts from resolving MIM references.', 'Sections 3 and 6')
ev('ledger', relative(OUT / 'final-perclaim-assessment-v1.json'), 'prior_review', 'supports',
   'Separate skeptical adjudication of every PC01-PC20 claim, with exact source scopes and limitations.')
ev('raw-check', relative(OUT / 'raw-archive-recheck.json'), 'validation', 'supports',
   'Independent exact archive/member hash check and 134 row/column/literal readbacks; abbreviation literals are not ingredient expansions.')
ev('owner-check', relative(OUT / 'final-owner-component-recheck.json'), 'validation', 'supports',
   'All 19 maintained beforeimages match the frozen bytes; MRSsi remains an authentic new-owner payload with null beforeimage.')
ev('composition', relative(OUT / 'combined-candidate-composition-readback.json'), 'record_content', 'supports',
   'Exact three combined proposal hashes checked: existing Marine withdrawal and two literal rumen withdrawals preserved; no final candidate approval.')
ev('routes', relative(BASE / 'route-and-composition-v2.json'), 'prior_review', 'supports',
   'Read-only authoring routes retain actual origins and distinguish causal W05 peptone case from observed child recipes.')
ev('issue1176', relative(BASE / 'context/issue1176-comment-6719248666.json'), 'prior_review', 'context_only',
   'Existing filed dependency finding and selected authoring route; no issue closure or mutation.')
ev('schema-check', relative(BASE / 'validation/native-record-schema.json'), 'validation', 'supports',
   'Root closed-schema validation on the exact 20 snapshot bytes; reused without claiming scientific support.')
ev('probe', relative(BASE / 'validation/native-probe-reuse.json'), 'validation', 'supports',
   'Frozen native probe remains structurally green when generic peptone moves but Bacto retains MICRO:0000178. This is an explicit limit, not identity proof.')
ev('fab-primary', relative(BASE / 'ambiguous/original-source-read-7.json'), 'primary_source', 'refutes',
   'Falsen 2005 primary-paper text mirror names Oxoid Fastidious Anaerobe Broth, not the inherited LabM/Neogen attribution. Its separate Anaerobe Systems PYG tests do not define FAB.', 'Printed p854; archived text extraction, not publisher PDF')
source_evidence = {}
for c in claims:
    sid = 'owner-' + c['target_id']
    target = next(t for t in targets if t['target_id'] == c['target_id'])
    ev(sid, target['path'], 'record_content', 'context_only',
       'Exact owner beforeimage or genuine new-owner proposal; complete bytes retained, review limited to specified component claim.', target['selector'])
    es = [sid, 'rules', 'ledger', 'raw-check']
    for n, s in enumerate(c['inspected_source_refs'], 1):
        eid = c['target_id'] + '-source-' + str(n)
        path = s['path']
        if not (ROOT / path).is_file():
            continue
        ev(eid, path, s.get('kind', 'primary_source'), s.get('support', 'partial'),
           s.get('scope', c['source_support']), s.get('locator'))
        es.append(eid)
    source_evidence[c['target_id']] = es

assessments = []
for c in claims:
    assessments.append({'assessment_id': 'assessment-' + c['target_id'], 'area': 'identity',
                        'topic': c['claim_key'],
                        'outcome': 'concern' if c['cohort'] == 'source_identity_hold' else 'supported',
                        'summary': c['source_support'] + ' ' + c['bounded_recommendation'],
                        'target_ids': [c['target_id']], 'evidence_ids': source_evidence[c['target_id']],
                        'details': c['quantity_limit'] + ' ' + c['remaining_requirement'] + ' ' + c['skeptical_conclusion']})

owners = lambda members: [copy.deepcopy(t['owner_paths'][0]) for t in targets if t['target_id'] in members]
known_targets = [x for x in ids if x != 'PC02']
findings = [
    {'finding_id': 'PEPTONE-1176-COUPLING',
     'issue_key': 'CultureBotAI.MediaIngredientMech.issue-1176.peptone-consumer-coupling',
     'category': 'identity', 'severity': 'major', 'status': 'open', 'certainty': 'confirmed',
     'title': 'Known generic-peptone retirement still requires source-specific consumer corrections',
     'description': 'Eight claims support generic peptone, ten require withdrawal of unsupported resolving identity, and the existing Marine product proposal already withdraws its link. None may silently inherit Bacto identity through MICRO:0000178. This is the existing #1176 dependency, not a new issue or an assertion that all current components denote Bacto.',
     'target_ids': known_targets, 'evidence_ids': ['ledger', 'issue1176', 'rules', 'probe', 'routes', 'composition'],
     'owner_paths': owners(known_targets), 'ownership_note': 'W05 authors authentic dependent proposals; compose existing worker origins and preserve W02 true new-owner MRSsi lineage. Root controls final integration.',
     'external_issues': ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1176#issuecomment-6719248666'],
     'rule_id': 'MAPPING_SEMANTICS sections 3 and 6'},
    {'finding_id': ledger['new_finding_id'],
     'issue_key': 'MediaIngredientMech.Fastidious_Anaerobe_Broth_With_Meat_Granules.FAB-source-applicability',
     'category': 'evidence', 'severity': 'major', 'status': 'open', 'certainty': 'confirmed',
     'title': 'Fastidious source context does not support inherited LabM/Neogen attribution',
     'description': 'The exact raw observation belongs to Fastidiosipila sanguinis. The inspected original Falsen 2005 article text identifies Oxoid Fastidious Anaerobe Broth; the active component evidence names LabM/Neogen. No inspected evidence equates these historical products. The Neogen 2019 formula and the paper\'s separate PYG assay are comparators, not applicable proof of the retained FAB peptone. Root was notified before any fix; root deduplicates and files the finding.',
     'target_ids': ['PC01'], 'field_paths': ['/component_assertion/evidence/0/notes', '/components/1'],
     'evidence_ids': ['fab-primary', 'owner-PC01', 'ledger', 'rules'], 'owner_paths': owners(['PC01']),
     'ownership_note': 'Bounded future source-attribution correction only; preserve inherited provenance and compose with existing meat-granule withdrawal. No recipe reconstruction or owner approval.',
     'rule_id': 'MAPPING_SEMANTICS sections 3 and 6; record review evidence applicability'}]

actions = [
    {'action_id': 'generic-coupling', 'description': 'Prepare the eight exact generic component corrections through the authentic existing/new child routes; apply only with separately accepted generic Peptone owner.',
     'finding_ids': ['PEPTONE-1176-COUPLING'], 'target_ids': generic, 'owner_paths': owners(generic),
     'acceptance_checks': ['Every claim remains bound to its exact source label, formula or primary abstract.', 'No supplier or catalogue is required merely to represent generic peptone.', 'Final exact child payloads receive independent review; preserve histories, quantities and holds.', 'MRSsi retains authentic new_owner/null-before; generic owner acceptance is an application prerequisite, not a reason for UNMAPPED fallback.']},
    {'action_id': 'minimal-withdrawals', 'description': 'For the ten unresolved whole-claim identities, propose minimal component_id withdrawal and UNMAPPED reference scope with honest provenance of the retained interpreted name.',
     'finding_ids': ['PEPTONE-1176-COUPLING'], 'target_ids': holds, 'owner_paths': owners(holds),
     'acceptance_checks': ['Retained peptone spelling is historical research interpretation where primary labels say only PY/PYG, not a new observed source constituent.', 'Preserve unknown quantities and component-assertion methods/completeness; append narrow evidence/history without erasing prior assertions.', 'Compose PC01 with meat-granule repair and PC08/PC15 with literal rumen-fluid UNMAPPED repair.', 'Do not transfer DSMZ/ATCC comparators or partial occurrence support to whole legacy owners.']},
    {'action_id': 'marine-withdrawal', 'description': 'Preserve W05/TARGET-012 existing product withdrawal while composing W03 alias lineage.',
     'finding_ids': ['PEPTONE-1176-COUPLING'], 'target_ids': ['PC04'], 'owner_paths': owners(['PC04']),
     'acceptance_checks': ['Keep literal Peptone UNMAPPED and nominal 5 g/L at standard reconstitution in the existing product correction.', 'Do not substitute the ATCC agar-minus-agar scratch formulation for commercial broth.', 'Separate final reviewer accepts the complete composed payload; this review does not approve parent-authored W03 alias proposal.']},
    {'action_id': 'fab-source-attribution', 'description': 'After root issue deduplication, supersede the active LabM/Neogen applicability assertion while retaining its exact historical provenance; document the original Oxoid wording and unresolved formulation.',
     'finding_ids': [ledger['new_finding_id']], 'target_ids': ['PC01'], 'owner_paths': owners(['PC01']),
     'acceptance_checks': ['Exact Falsen source and raw occurrence binding retained with mirror/read limitations.', 'No guessed Oxoid catalogue, historical formula, peptone identity or amount is introduced.', 'No FAB constituent is inferred from the paper\'s separate Anaerobe Systems PYG experiment.', 'Preserve cooked-meat withdrawal and all unrelated components/holds; independent exact successor review.']},
    {'action_id': 'gyps-retain', 'description': 'Retain the intended source-specific Bacto peptone reference for GYPS; do not include it in generic migration.',
     'finding_ids': [], 'target_ids': ['PC02'], 'owner_paths': owners(['PC02']),
     'acceptance_checks': ['Alain 2002 p1622 explicit Bacto-peptone (Difco) remains the narrow source proof.', 'No quantity expansion is made; final Bacto owner/alias/ontology/role/export approval remains separate.']}
]

review = {
 'schema_version': '1.0.0', 'review_id': review_id, 'kind': 'category',
 'repository': inspect['repository'], 'title': 'Independent source and skeptical review of twenty peptone component claims',
 'started_at': original_inspect['inspection_at'].replace('+00:00', 'Z'), 'finished_at': finished,
 'reviewer': {'identity': 'Codex /root/peptone_skeptic', 'kind': 'agent', 'independence': 'independent',
              'independence_basis': 'Separate in-process reviewer from both primary-source agents; independently read raw observations, current owners, archived primary evidence and actual composed proposals. Parent W03 authored Marine alias work and prior audit; PC04 is explicitly author-related and no final W03 payload is approved.'},
 'skill': 'review-yaml-category', 'completion': 'completed', 'verdict': 'needs_curation',
 'native_verdict': 'All twenty bounded component-source dispositions reviewed; conditional authoring recommendations and unresolved identity holds preserved.',
 'scientific_review': True,
 'summary': 'Eight generic recommendations, ten unresolved identity withdrawals, one source-specific Bacto retention, and one existing Marine product withdrawal. These are claim dispositions only, never whole-owner, role, form, supported-export or release approval. One new Fastidious source-applicability finding is reported to root before fixes.',
 'source': inspect['source'],
 'scope': {'description': 'Exact twenty incoming peptone component claims, including nineteen maintained beforeimages and one authentic MRSsi new-owner proposal.',
           'selection': 'Complete explicit PC01-PC20 targets frozen from minimal-couplings-28 and root claims-20.json; no sampling.',
           'coverage': 'full', 'population_size': 20, 'reviewed_target_ids': ids,
           'exclusions': [{'target': 'Whole owners, other components, ontology/role/form/export eligibility and final cross-shard merges', 'reason': 'Outside this bounded component-source review; preserved as holds.'}]},
 'targets': targets,
 'checks': [
    {'check_id': 'owner-bytes', 'name': 'Exact beforeimage and component accounting', 'status': 'passed', 'required': True, 'summary': 'Nineteen current owners equal frozen bytes; one genuine MRSsi new-owner payload; twenty unique claims checked.', 'target_ids': ids, 'evidence_ids': ['owner-check']},
    {'check_id': 'raw-binding', 'name': 'Original dataset readback', 'status': 'passed', 'required': True, 'summary': '134 exact source row/column/literal bindings verified independently; no abbreviation treated as ingredient proof.', 'target_ids': ids, 'evidence_ids': ['raw-check']},
    {'check_id': 'source-adjudication', 'name': 'Primary and independent skeptical adjudication', 'status': 'passed', 'required': True, 'summary': 'Every claim assessed against actual readable source context; unavailable exact sources yield explicit holds rather than forced identity.', 'target_ids': ids, 'evidence_ids': ['ledger', 'rules']},
    {'check_id': 'native-inspection', 'name': 'Native input capture before final adjudication', 'status': 'passed', 'required': True, 'summary': 'Native inspect_source and assert_current_source executed successfully; inspection itself supplies no scientific or schema verdict.', 'target_ids': ids},
    {'check_id': 'native-schema-reuse', 'name': 'Exact twenty-record closed-schema result reused', 'status': 'passed', 'required': True, 'summary': 'Read and bound root actual focused validation receipt on unchanged target bytes; not rerun by skeptic and not chemistry proof.', 'target_ids': ids, 'evidence_ids': ['schema-check']},
    {'check_id': 'native-probe-limit', 'name': 'Existing native partonomy counterfactual retained', 'status': 'passed', 'required': True, 'summary': 'Reused exact frozen counterfactual showing generic-owner-only migration can pass despite semantic narrowing to remaining Bacto owner.', 'target_ids': ids, 'evidence_ids': ['probe']},
    {'check_id': 'full-owner-gates', 'name': 'Full corpus, ontology, role and export approval', 'status': 'not_applicable', 'required': False, 'summary': 'Outside bounded read-only claim review; no extra full repository QC or export generation authorized.', 'target_ids': ids},
 ],
 'evidence': evidence, 'assessments': assessments, 'findings': findings, 'actions': actions,
 'boundary_decisions': [{'action': 'split', 'target_ids': ids,
    'rationale': 'Partition component-claim decisions by actual evidence strength and migration need. Consumer owners are not asserted synonymous or mergeable.',
    'evidence_ids': ['ledger', 'rules'], 'proposed_groups': [
      {'label': 'Eight conditional generic component migrations', 'target_ids': generic},
      {'label': 'Ten unresolved component identities with minimal withdrawals', 'target_ids': holds},
      {'label': 'One source-specific GYPS Bacto retention', 'target_ids': ['PC02']},
      {'label': 'One existing Marine product withdrawal', 'target_ids': ['PC04']}]}],
 'limitations': ledger['limitations'] + [
    'Native saver is intentionally not called: user restricts all outputs to the new private review subtree. Native YAML/Markdown validation, currentness and virtual canonical bundle parsing are performed without writing reviews/structured.',
    'Review source state is working_tree: private capture hashes are reviewer attestation, while exact source proposal Git-blob readbacks are separately recorded. No claim that private review files are committed.',
    'All scientific flags apply only to bounded claim dispositions; unresolved facts and unavailable sources remain explicit. No payload edits or proposal approval occurs.'],
 'notes': ['Primary scopes: /root/peptone_ambiguous_sources ten holds; /root/peptone_other_sources eight generic plus GYPS and Marine; /root/peptone_skeptic all twenty. Parent /root assembles final handoff and does not independently approve its own Marine proposal.',
           'PEPTONE-SOURCE-001 retains original issue key MediaIngredientMech:Fastidious_Anaerobe_Broth_With_Meat_Granules:FAB-source-applicability in ambiguous/finding-native-key-binding.json; the native Token-compatible dot spelling identifies the same finding, not a duplicate issue.',
           'Original captures retain original timestamps; independent read timestamps are not substituted as source retrieval times.',
           'No new provider calls by skeptical reviewer; primary agents used free read-only retrieval only.'],
 'links': ['https://github.com/CultureBotAI/MediaIngredientMech/issues/1176#issuecomment-6719248666'],
 'tags': ['read-only', 'component-source-review', 'peptone', 'no-owner-approval']
}

# Validate before immutable emission. Write no record, candidate or canonical review.
native.validate_review(review)
native.assert_current_source(ROOT, review)
raw = native._dump_document(review).encode()
markdown = native.render_markdown(review).encode()
native.parse_review_bundle(f'reviews/structured/{review_id}/review.yaml', raw, markdown)
write_new(NATIVE / 'review.yaml', raw, raw=True)
write_new(NATIVE / 'review.md', markdown, raw=True)
receipt = {'reviewer': '/root/peptone_skeptic', 'at': dt.datetime.now(dt.timezone.utc).isoformat(),
           'status': 'PASS', 'review_id': review_id, 'targets': 20,
           'source_inputs': len(review['source']['inputs']),
           'native_calls': ['inspect_source', 'assert_current_source', 'validate_review', 'render_markdown', 'parse_review_bundle'],
           'yaml_sha256': sha(NATIVE / 'review.yaml'), 'markdown_sha256': sha(NATIVE / 'review.md'),
           'canonical_persistence': False, 'private_persistence': True,
           'virtual_canonical_parse': True, 'scientific_scope': review['summary']}
write_new(NATIVE / 'validation.json', receipt)
print(json.dumps(receipt, indent=2))
