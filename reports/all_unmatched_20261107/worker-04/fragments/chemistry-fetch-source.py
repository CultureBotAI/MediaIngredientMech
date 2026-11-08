"""Second primary capture pass, 2026-11-08: source endpoints and case recipes."""
import importlib.util,json,pathlib,concurrent.futures,re
spec=importlib.util.spec_from_file_location('capture','reports/all_unmatched_20261107/worker-04/fragments/chemistry-fetch.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
jobs=[(f'mediadive-ingredient-{i}.html',f'https://mediadive.dsmz.de/ingredients/{i}') for i in m.IDS]
jobs += [(f'dsmz-{i}.pdf',f'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{i}.pdf') for i in [1047,906,661,863,1344,1005]]
jobs += [(f'nbrc-{i}.html',f'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO={i}') for i in [989,943,1632,1625,392,931,809,1378]]
jobs += [(f'togo-{i}.json',f'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M{i}') for i in [1146,1147,2692,2809,2978,3061,3058,3037,2240,2262,194,945,946,2248]]
jobs += [('pubmed-grisamine.xml','https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=13242476&retmode=xml')]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p: receipts=list(p.map(m.capture,jobs))
(m.ROOT/'source-retrieval-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
print(json.dumps(receipts,indent=2))
