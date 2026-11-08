from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import yaml

P = Path(__file__).resolve().parent
W = P.parents[2]
C = W.parents[2]
R = C / 'workers/w09/worktree/.temp/tenvit-mc-continuity-decision-v1'
assert W.name == 'worktree' and C.name == 'all-unmatched-20261107'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def dump(name, obj):
    with (P / name).open('x') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')

now = datetime.now(timezone.utc).isoformat()
owner_path = W / 'data/ingredients/mapped/Mc_vitamins.yaml'
owner = yaml.safe_load(owner_path.read_text())
mix_path = R / 'mc-primary/captures/Mixes.csv'
mix = list(csv.reader(mix_path.open()))
assert mix[1111] == ['Media', 'Mc_vitamins', '']
literal = mix[1115:1125]
assert len(literal) == len(owner['components']) == 10
for i, (name, amount, unit) in enumerate(literal):
    comp = owner['components'][i]
    assert (name, amount, unit) == (comp['component_name'], comp['concentration_value'], 'g/L')
    assert comp['concentration_unit'] == 'G_PER_L'
assert mix[1113] == ['X', '100', '']
assert sha(owner_path) == '59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'

cross = list(csv.reader((R / 'mc-primary/captures/compounds_to_cas.csv').open()))
cross_numbers = [81, 191, 349, 441, 354, 299, 92, 131, 28, 271]
comments = [
    'Biotin name and CAS 58-85-5 are compatible with retained CHEBI:15956; no child-wide role or literature approval.',
    'Folic acid name and CAS 59-30-3 are compatible with retained CHEBI:27470; no folate salt substituted.',
    'The literal hydrochloride and CAS 58-56-0 agree with CHEBI:30961. The free base is not substituted.',
    'The literal HCl form and CAS 67-03-8 agree with CHEBI:49105; its chloride/hydrochloride constitution is retained.',
    'Riboflavin name and CAS 83-88-5 agree with CHEBI:17015; no phosphate derivative is inferred.',
    'Nicotinic acid and CAS 59-67-6 agree with CHEBI:15940; no nicotinate salt is inferred.',
    'SCI-TENVIT-003 confirmed: literal calcium D,L-pantothenate cannot be identified with D-specific CHEBI:31345. The crosswalk combines D and D,L synonyms under CAS 137-08-6/C8731; it does not resolve this contradiction. Withdrawing component_id and using UNMAPPED preserves the known literal recipe and quantity without guessing the actual purchase.',
    'The literal vitamin B12 is compatible with the generic vitamin class CHEBI:176843. Crosswalk row 131 names cyanocobalamin, but that does not justify changing this existing generic component or identifying JCM/NBRC vitamers. The child owner CAS assertion is not independently approved here.',
    'p-Aminobenzoic acid and CAS 150-13-0 agree with CHEBI:30753; position-specific identity is preserved.',
    'Literal lipoic acid is retained at generic CHEBI:16494. The crosswalk DL synonym/CAS 1077-28-7 and the existing child preferred name do not establish that a stereounspecified ontology structure is a racemate. No new stereochemical assertion or whole-child approval is made.',
]
child_index = {}
for f in (W / 'data/ingredients').rglob('*.yaml'):
    o = yaml.safe_load(f.read_text())
    if o.get('identifier') in {c['component_id'] for c in owner['components']}:
        child_index.setdefault(o['identifier'], []).append({
            'path': str(f.relative_to(W)), 'sha256': sha(f),
            'mapping_status': o.get('mapping_status'), 'preferred_term': o.get('preferred_term'),
            'read_scope': 'Identifier, preferred term, status, full ontology_mapping and chemical_properties; not whole-child scientific approval.'})

component_rows = []
for i, c in enumerate(owner['components']):
    component_rows.append({'index': i, 'literal_Mixes_row': 1116+i, 'original_component': c,
                           'crosswalk_row': cross_numbers[i], 'crosswalk_fields': dict(zip(cross[0], cross[cross_numbers[i]-1])),
                           'catalog_candidates': child_index[c['component_id']], 'appraisal': comments[i]})

media_path = R / 'mc-primary/captures/Medias.csv'
media = list(csv.reader(media_path.open()))
starts = [i for i,r in enumerate(media) if r and r[0] == 'Media'] + [len(media)]
occurrences = []
for a,b in zip(starts,starts[1:]):
    for i,r in enumerate(media[a:b], a):
        if r and r[0] == 'Mc_vitamins':
            occurrences.append({'media_name': media[a][1], 'block_rows': [a+1,b], 'component_row': i+1, 'literal': r})
assert len(occurrences) == 22
cons = json.loads((R / 'mc-primary/captures/consolidated_media.json').read_text())
cons_matches = [{'name': k, 'matches': [r for r in v.get('ingredients', []) if r.get('name') == 'Mc_vitamins']}
                for k,v in cons.items() if isinstance(v,dict) and any(r.get('name') == 'Mc_vitamins' for r in v.get('ingredients', []))]
assert len(cons_matches) == 22

source_specs = [
    ('mc-primary/captures/Mixes.csv', 'CSV rows 1112–1125, all ten inputs and X=100', 'Owning recipe: literal names, order, g/L quantities and stock multiplier metadata; no solvent or preparation statement in this block.'),
    ('mc-primary/captures/Mixes.csv.20260611', 'Same complete Mc block', 'Earlier local archived block has the same ten input values; no asserted date of original web retrieval.'),
    ('mc-primary/captures/compounds_to_cas.csv', 'All ten exact rows 28,81,92,131,191,271,299,349,354,441', 'Raw dictionary examined independently. Row 92 is internally D/DL-conflicting; row 131 is cyanocobalamin-specific, not a universal vitamin B12 assertion.'),
    ('mc-primary/captures/Medias.csv', 'All 22 Mc-containing block boundaries and Mc rows', 'Owning-source continuity/count check. No scientific reapproval of other receiving-medium ingredients.'),
    ('mc-primary/captures/consolidated_media.json', 'All 22 Mc-containing entries and complete Mc ingredient objects', 'Imported 22-media occurrence provenance; null parsed units are not silently corrected.'),
    ('mc-primary/captures/mc-thesis2014.pdf', 'Printed pages 28–29, inspected through captured pdftotext derivative', 'McCas example: 100X vitamin solution, same nominal ten masses added to 1 L autoclaved distilled water. Not proven CultureBot import genealogy.'),
    ('mc-primary/captures/mc-thesis2014.txt', 'Lines 1067–1076 and 1109–1126', 'Actual rendered recipe text read; only bounded recipe passage inspected, not an unread-paper claim.'),
    ('primary/captures/ols31345-retry.capture', 'Whole term JSON; label, active state, synonyms, CAS and stereochemical structure', 'CHEBI:31345 is D-specific despite a generic-looking label; not an exact DL identity.'),
    ('primary/captures/sigma-c8731-web-response.json', 'Captured official page response, C8731 identifiers/synonyms/structure', 'Manufacturer D form/CAS137-08-6 contrast; this is a saved web-tool response, not raw HTTP or proof of a purchase.'),
    ('primary/captures/C-E-jcm-197.capture', 'Entire recipe and all nested stock/preparation text', 'Ten vitamin masses plus 1 L distilled-water input; stock filter sterilization while gassing N2. No final-volume or calcium stereo/B12-vitamer inference.'),
    ('primary/captures/C-E-nbrc-837.capture', 'Entire recipe and all nested stock/preparation text', 'Matching nominal ten masses plus 1 L distilled-water input. Filter-sterile stock added anaerobically; no explicit stock gassing statement.'),
    ('primary/captures/vm-fetch-2630e40c26a0b155.capture', 'Entire NBRC903 recipe and all nested stock/preparation text', 'Matching nominal ten masses plus 1 L distilled-water input. Filter sterilization and anaerobic addition; no explicit stock gas inferred.'),
    ('primary/captures/atcc2672-retry.txt', 'Complete rendered ATCC2672 recipe and both nested stocks', 'Named vitamin stock explicitly uses D-(+)-calcium pantothenate. This comparator does not override Mc DL text or establish current MD-VS product equality.'),
    ('primary/captures/atcc-mdvs-retry.txt', 'Full captured page text; formulation and handling sections', 'Current MD-VS table adds monopotassium phosphate 900 mg/L and uses its own thiamine wording; product boundary preserved.'),
    ('primary/ontology-query.json', 'All ten term label/definition/CAS/structure rows', 'Read-only local ChEBI255 query receipt reviewed; no fresh query or universal ontology absence asserted.'),
]
original_receipts = [
    'mc-primary/capture-register.json', 'mc-primary/probes/mc-thesis2014.pdf.retry.json',
    'primary/probes/ols31345-retry.json', 'primary/captures/w04-source-capture-receipt-excerpts.json']
read_rows = [{'path': str(R/rel), 'sha256': sha(R/rel), 'locator': loc, 'appraisal': appraisal,
              'inspected_at': now, 'retrieval_time_policy': 'Original acquisition remains in named source receipts; this is a local inspection, not a new retrieval.'}
             for rel,loc,appraisal in source_specs]
dump('source-read-ledger-v1.json', {
    'reviewer': 'worker08:/root/organics', 'inspection_at': now, 'network_requests_by_this_reviewer': 0,
    'sources': read_rows, 'original_retrieval_receipts': [{'path':str(R/r),'sha256':sha(R/r)} for r in original_receipts],
    'local_lookup_corrections': 'Initial guessed inputs/primary and primary/*.txt paths did not exist. An ignored-inclusive file search located primary/captures; those actual bytes were then read. This is a local path correction, not unavailable scientific evidence.',
    'source_limit': 'No new network failure, denial or unread paper is claimed. Prior recorded failures remain in original packets. All sources remain outside this writable review directory and were not modified.'})

dump('source-assessment-v1.json', {
    'reviewer':'worker08:/root/organics', 'author':'worker08:/root',
    'status':'PRIMARY_ASSESSMENT_COMPLETE_FINAL_CANDIDATE_PENDING', 'at':now,
    'independence':'I did not author Mc_vitamins or this proposed correction. Earlier W08 vitamin/comparator review involvement is disclosed and is not reused as authority for this fresh Mc assessment.',
    'before':{'path':str(owner_path),'sha256':sha(owner_path),'full_owner_read':True,'top_field_count':len(owner),
              'original_history_count':len(owner['curation_history'])},
    'component_appraisals':component_rows,
    'owning_source_occurrences':occurrences,
    'consolidated_occurrence_provenance':cons_matches,
    'source_assertion_scope':'COMPLETE is defensible for the explicitly transcribed ten-input Mc Mixes list. It does not assert all physical constituents of a finished solution, carrier, final volume, stock gas or universal JCM/NBRC DL composition.',
    'nominal_comparison':'Mc, JCM197, NBRC837 and NBRC903 support a common nominal ten-vitamin recipe. Generic CB/Wolfe also overlaps nominally. No exclusive winning owner, merge, global alias or final cross-owner route follows from this bounded review.',
    'known_finding':{'id':'SCI-TENVIT-003','field':'components[6]','status':'CONFIRMED_IN_BEFOREIMAGE; await candidate withdrawal of D-specific ID','source_paths':[str(mix_path),str(R/'mc-primary/captures/compounds_to_cas.csv'),str(R/'primary/captures/ols31345-retry.capture')]},
    'remaining_holds':['Actual supplied D versus DL material is unresolved; do not guess a registry identifier from the conflicting crosswalk.',
                       'All other existing identities, raw aliases, source statistics, quantities, role assertions and original history must stay unchanged.',
                       'Generic B12 and generic lipoic reference preservation does not approve inherited child CAS, stereochemical, role or literature assertions.',
                       'No transfer of external McCas solvent protocol to the CultureBot Mc list or transfer of Mc DL/g-per-L semantics to JCM/NBRC batch tables.',
                       'W04 and coordinator cross-owner continuity/routing disposition remains pending; 65 nominal source contexts are an upper bound, not accepted route claims.',
                       'No downstream export, maintained installation or general release approval.'],
    'new_findings':[], 'final_payload_review_complete':False,
    'source_packet':{'path':str(R/'HANDOFF.json'),'sha256':sha(R/'HANDOFF.json')},
    'supporting_read_index':{'path':'source-read-ledger-v1.json','sha256':sha(P/'source-read-ledger-v1.json')}})
print(json.dumps({n:sha(P/n) for n in ['source-read-ledger-v1.json','source-assessment-v1.json']},indent=2))
