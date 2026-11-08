"""2026-11-08: author issue1203 isolated successor stock payloads; no maintained writes.

Input: immutable C-P08 and exact DSMZ recipe evidence reviewed in this successor.
Output: two guarded, closed-schema payloads in this successor's proposed_owners.
Run once; published predecessors and successor payloads are never overwritten.
"""
import copy
from pathlib import Path
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient

ROOT = Path('reports/all_unmatched_20261107/worker-07')
OUT = ROOT / 'successors/issue1203-v1'

def sources(media, notes):
    return [{'evidence_type': 'RECIPE_SOURCE',
             'source': f'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{m}.pdf',
             'source_record': f'DSMZ {m}: magnesium sulfate heptahydrate stock row',
             'notes': notes} for m in media]

def mapping_sources(media, notes):
    items=sources(media,notes)
    for item in items:
        item['evidence_type']='MANUAL_CURATION'
        item.pop('source_record')
    return items

scope75 = (
    'Nominal source-qualified stock: DSMZ1592,1593 and1593a each explicitly list '
    '10 mL of magnesium sulfate heptahydrate stock at7.5 g/L for1000 mL medium. '
    'MediaDive solutions5518,5736,6270 corroborate the scoped recipe rows. '
    'This extends the already proposed C-P08 identity to six exact CultureMech '
    'occurrences, in addition to the frozen KG source_record for ingredient2154. '
    'The ingredient2154 endpoint identifies the solute and supplies medium links; '
    'it does not define a universal stock concentration. Solvent, complete '
    'composition and stock preparation/final-volume convention are unreported. '
    'Medium make-up water is not evidence for the separately prepared stock solvent. '
    'Component-list completeness remains UNKNOWN. No stock-to-solute equivalence, '
    'conversion of frozen percent-volume fields, or global raw-label alias is asserted. '
    'The six occurrence IDs and frozen raw quantities are retained in the paired '
    'source ledger; occurrence statistics count these six distinct frozen recipe '
    'records only, not all uses of ingredient2154 or unique biological media.'
)
old = yaml.safe_load((ROOT/'proposed_owners/c-C-P08.yaml').read_text())
stock75 = copy.deepcopy(old)
stock75['occurrence_statistics'] = {'total_occurrences': 6, 'media_count': 6}
stock75['ontology_mapping']['evidence'] = mapping_sources(['1592','1593','1593a'], scope75)
stock75['components'][0]['source'] = (
    'Stock concentration explicitly7.5 g/L in DSMZ1592/1593/1593a recipe rows '
    'and the frozen KG source_record; not a concentration declared by the '
    'ingredient2154 identity endpoint and not final-medium concentration.'
)
stock75['component_assertion']['evidence'] = sources(['1592','1593','1593a'], scope75)
stock75['notes'] = scope75
record_curation_event(stock75, curator='codex_worker07_root_issue1203',
    action='SOURCE_SCOPE_REFINED', previous_status='MAPPED', new_status='MAPPED',
    llm_assisted=True, changes='Append-only successor to unpublished-in-catalogue C-P08: '
    'reuse its existing registry identity for six exact CultureMech stock occurrences; '
    'correct concentration attribution to recipe rows, retain unknown solvent and '
    'preparation, and preserve the original creation event. Proposal only.')

scope350 = (
    'Nominal source-qualified350 g/L magnesium sulfate heptahydrate stock, explicitly '
    'identified in DSMZ1673/1677/1678. Six exact CultureMech occurrences refer to '
    'this strength, distinct from C-P08 at7.5 g/L and from pure CHEBI:31795. '
    'DSMZ1673 specifies10 mL/L stock. DSMZ1677 prints3.30 g beside the350 g/L '
    'stock qualifier while MediaDive5781 gives3.3 mL and an inconsistent g_l field; '
    'DSMZ1678 specifies3.3 mL/L while MediaDive5782 usesg/L. The1677/1678 dose '
    'conflicts remain held pending authoritative clarification; no corrected dose '
    'or final-medium concentration is inferred. All three sources explicitly '
    'support the nominal stock strength, regardless of unresolved dispensing units. '
    'Solvent, complete composition and stock preparation/final-volume convention '
    'are unreported. Instructions to make the whole medium up with water do not '
    'establish the stock solvent. Component-list completeness remains UNKNOWN. '
    'This records the common stated nominal source formulation, not proven equality '
    'of unreported preparation details or every ingredient2154 occurrence. '
    'The raw source label is retained in evidence, not added as a global resolving '
    'stock or solute synonym. Occurrence statistics count six distinct frozen '
    'recipe records in this reviewed scope, not unique biological media.'
)
stem = 'Dsmz_1673_1677_1678_Magnesium_Sulfate_Heptahydrate_Stock_350g_L'
identity = 'kgmicrobe.ingredient:' + stem.lower()
label = 'Magnesium sulfate heptahydrate stock 350 g/L (DSMZ 1673/1677/1678)'
stock350 = {
    'identifier': identity, 'preferred_term': label, 'mapping_status': 'MAPPED',
    'ingredient_type': 'STOCK_SOLUTION', 'solution_type': 'MINERAL_STOCK',
    'ontology_mapping': {'ontology_id': identity, 'ontology_label': label,
        'ontology_source': 'kgmicrobe.ingredient', 'mapping_quality': 'FALLBACK_REGISTRY',
        'evidence': mapping_sources(['1673','1677','1678'], scope350)},
    'synonyms': [{'synonym_text': 'Mg(SO4) x 7 H2O (350 g/L stock; DSMZ 1673/1677/1678)',
        'synonym_type': 'CATALOG_VARIANT',
        'source': 'Curator-qualified source formulation name; unqualified raw label preserved in occurrence evidence.'}],
    'components': [{'component_name': 'MgSO4 x 7 H2O', 'component_id': 'CHEBI:31795',
        'reference_scope': 'MIM_CATALOG', 'concentration_value': '350',
        'concentration_unit': 'G_PER_L',
        'source': 'Explicit stock strength in DSMZ1673/1677/1678; not final-medium concentration or dispensing dose.'}],
    'component_assertion': {'method': 'RECIPE_TRANSCRIPTION', 'completeness': 'UNKNOWN',
        'evidence': sources(['1673','1677','1678'], scope350)},
    'occurrence_statistics': {'total_occurrences': 6, 'media_count': 6},
    'notes': scope350, 'curation_history': [],
}
record_curation_event(stock350, curator='codex_worker07_root_issue1203',
    action='CREATED', new_status='MAPPED', llm_assisted=True,
    changes='Propose a source-qualified350 g/L magnesium sulfate heptahydrate stock '
    'after maintained-owner and campaign-proposal deduplication; retain unknown '
    'solvent/preparation and explicit1677/1678 dose conflicts. Isolated proposal only.')
for name, record in [('stock-7p5g-L.yaml',stock75), ('stock-350g-L.yaml',stock350)]:
    path=OUT/'proposed_owners'/name
    if path.exists(): raise SystemExit(f'Refusing overwrite: {path}')
    write_validated_ingredient(record,path)
    print(path)
