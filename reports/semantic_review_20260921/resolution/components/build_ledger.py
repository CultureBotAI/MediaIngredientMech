"""Rebuild the bounded, source-context component adjudication ledger for #710."""
from pathlib import Path
import csv
import hashlib
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

REASONS = {
    'PYG': 'The 114 raw occurrences span multiple species and Bergey chapters. Generic PYG recipes corroborate a family but do not independently verify every source preparation; original chapter/recipe comparison remains open.',
    'PYGS': 'Raw source is Clostridium frigidicarnis. Adam et al. 2011 (doi:10.1111/j.1472-765X.2011.03071.x) corroborates starch-containing PYGS for this species, but the originating Bergey/1999 recipe chain was not inspected; no automatic promotion from a later same-species recipe.',
    'PYEG': 'Raw source is Clostridium scindens. The prior literature report centers on Caulobacter and unrelated PYEG uses. Current culture-collection growth recipes cannot establish the original substrate preparation.',
    'Fastidious_Anaerobe_Broth_With_Meat_Granules': 'Raw source is Fastidiosipila sanguinis; the Bergey abstract confirms this medium label but does not specify manufacturer or ingredients. The ignored Edison report contains no answer. The four inferred components remain unverified against original source/product methods.',
    'Modified_Cooked_Meat_Medium': 'Raw source is Caproiciproducens galactitolivorans. The prior generic handbook interpretation does not identify its source-specific modified recipe or establish the exact meat preparation; source recipe remains required.',
    'PY-cellobiose': 'Raw contexts are Clostridium polysaccharolyticum and Eubacterium siraeum. Named carbohydrate plausibility and generic PY expansion do not independently compare both original source preparations.',
    'PY-fructose': 'Raw source is Clostridium formicaceticum. The prior report primarily relied on Pectinatus portalensis PYF; this different-organism recipe does not establish the original PY-fructose preparation.',
    'PY-maltose': 'Raw source is Clostridium leptum. The prior report explicitly required upstream context before accepting an example formulation; original source recipe remains uninspected.',
    'PY-pectin': 'Raw source is Treponema pectinovorum. ATCC1223 supports a pectin-containing recipe for that species but does not demonstrate that its branded polypeptone formula equals the original PY-pectin source; keep original-source review open.',
    'PYG-002_Tween_80': 'Raw source is Holdemanella biformis. Source label supplies Tween concentration but does not independently identify the PY base formulation or prove all inferred component identities.',
    'PY-glucose-rumen_Fluid': 'Raw source is Treponema socranskii. The retained clarified-rumen-fluid identifier is more specific than the source label; the original preparation/clarification method and PY base still require verification.',
    'PYG_Rumen_Fluid': 'Raw source is Eubacterium ruminantium. An unrelated 1993 experimental paper supports rumen-fluid-supplemented PYG for this species, but neither clarification nor the original source-specific recipe has been verified.',
}

def main():
    baseline = ROOT / 'reports/semantic_review_20260921'
    all_findings = list(csv.DictReader((baseline / 'findings.tsv').open(), delimiter='\t'))
    selected = [r for r in all_findings if r['kind'] in {'component_source_scope', 'ambiguous_abbreviation', 'recipe_identity'}]
    assertions = {r['edge_id']: r for r in csv.DictReader((baseline / 'kgx_assertions.tsv').open(), delimiter='\t')}
    plans = {r['source_record']: r for r in json.loads((OUT / 'applied-changes.json').read_text())}
    contexts = json.loads((OUT / 'source-contexts.json').read_text())['records']
    rows = []
    for f in selected:
        path = f['source_record']
        stem = Path(path).stem
        a = assertions.get(f['affected_unit'], {})
        disposition = 'OPEN_SOURCE_VERIFICATION'
        reason = REASONS.get(stem, '')
        if stem == 'GYPS':
            disposition = 'CORRECTED' if a.get('object') == 'CHEBI:28017' or f['kind'] == 'ambiguous_abbreviation' else 'SOURCE_VERIFIED'
            reason = 'Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.'
        elif stem == 'TYGVS_Glucose':
            reason = 'Raw source is Treponema medium. Later primary oral TYGVS protocols disagree in named peptone (Trypticase versus Tryptone); neither a different-species recipe nor a shared acronym establishes the original preparation. Adversarial review rejected a tentative promotion; all four original claims remain provisional pending the actual citation chain.'
        elif stem == 'CMC_PY_Horse_Serum':
            disposition = 'WITHDRAWN_FALSE_MIXTURE'
            reason = 'Love et al. 1979 (doi:10.1099/00207713-29-3-241) describes separate cooked meat-carbohydrate and peptone-yeast cultures with horse serum. The source expression was incorrectly flattened into one mixture, and CMC wrongly expanded as carboxymethylcellulose. All four edges withdrawn; raw expression retained as AMBIGUOUS.'
        elif stem == 'BHI':
            disposition = 'WITHDRAWN_EXACT_FORMULATION'
            reason = 'Raw BHI belongs to Hespellia porcina; no formulation/quantity comparison with CultureBotHT/FEBA CultureMech:015492 is established. Link downgraded to CANDIDATE_UNVERIFIED; it is explicitly not a verified recipe relationship.'
        current = plans.get(path, {}).get('after_path', path)
        rows.append({
            'finding_id': f['finding_id'], 'kind': f['kind'], 'source_record': path,
            'current_record': current, 'current_record_sha256': digest(ROOT / current),
            'original_assertion': f['affected_unit'], 'original_object': a.get('object',''),
            'disposition': disposition, 'reason': reason,
            'source_context_rows': '|'.join(str(c['csv_row']) for c in contexts.get(path, [])),
            'source_dois': '|'.join(sorted({c['Bergey_Article_link'] for c in contexts.get(path, [])})),
            'change_plan': 'applied-changes.json' if path in plans else '',
        })
    assert len(rows) == 54 and len({r['finding_id'] for r in rows}) == 54
    with (OUT / 'dispositions.tsv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    related = [r for r in all_findings if r['kind'] == 'existing_record_review' and any(s in r['reason'].lower() for s in ('component', 'partonomy', 'constituent'))]
    with (OUT / 'related-record-findings.tsv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(related[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(related)
    research = {}
    for path in contexts:
        report = ROOT / 'research/ingredients' / (Path(path).stem + '-edison-literature.md')
        if report.exists():
            research[str(report.relative_to(ROOT))] = {'sha256': digest(report), 'status': 'NO_ANSWER' if report.read_text().startswith('(no answer') else 'REVIEWED_AS_LEAD_NOT_PRIMARY_EVIDENCE'}
    manifest = {
        'scope': 'All 51 original interpreted/abbreviation component assertions, both ambiguity findings and the BHI exact-formulation finding. Other record findings remain in the full baseline; this is not full-graph semantic approval.',
        'finding_count': len(rows), 'component_count': sum(r['kind']=='component_source_scope' for r in rows),
        'dispositions': dict(Counter(r['disposition'] for r in rows)),
        'remaining_component_findings': sum(r['kind']=='component_source_scope' and r['disposition']=='OPEN_SOURCE_VERIFICATION' for r in rows),
        'related_record_findings_preserved_without_adjudication': len(related),
        'ignored_research_reports_examined': research,
        'gyps_primary_pdf': {'url':'https://archimer.ifremer.fr/doc/2002/publication-528.pdf','sha256':'a89cbee98ab86fc02044b4344e617dcf705907820e0acc83cdd8948d9bcaf661','locator':'page 1622, Culture medium and conditions','retention':'Full publisher PDF retained only in local /private/tmp/mim-gyps.pdf; report uses a paraphrase and source hash.'},
        'files': {n:digest(OUT/n) for n in ['before-records.json','applied-changes.json','source-contexts.json','dispositions.tsv','related-record-findings.tsv','build_ledger.py','README.md','validate_components.py','validation.json','review-issue-tygvs.md']},
        'release_verdict': 'FAIL',
    }
    (OUT / 'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:manifest[k] for k in ['finding_count','component_count','dispositions','remaining_component_findings','release_verdict']},indent=2))

if __name__ == '__main__':
    main()
