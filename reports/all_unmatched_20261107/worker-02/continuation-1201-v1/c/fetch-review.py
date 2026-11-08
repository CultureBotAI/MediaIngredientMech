from pathlib import Path
s=Path('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/fetch.py').read_text();exec(s.split('urls={}')[0])
urls={
'phc-commonchem-api':'https://commonchemistry.cas.org/api/detail?cas_rn=61630-98-6',
'phc-commonchem-html':'https://commonchemistry.cas.org/detail?cas_rn=61630-98-6',
'phc-tss':'https://www.techservesolutions.in/en/products/poly-hexamethylene-carbonate-diol-61630-98-6',
'phc-original-paper':'https://academic.oup.com/femsle/article-pdf/161/2/255/19099706/161-2-255.pdf',
'phc-government-inventory':'https://sthjj.beijing.gov.cn/bjhrb/index/xxgk69/sthjlyzwg/wrygl/10944115/2021022509423935075.pdf',
'mg6-americanelements':'https://www.americanelements.com/print/view/pdf/product_datasheet/block_1?view_args%5B%5D=48037',
'phc-sigma-materials-pdf':'https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/marketing/global/documents/161/628/al_ms_ad3_bio_polymers.pdf',
'mg-cas-lead-not-mn':'https://www.shenghechemical.com/product/magnesium-sulphate-anhydrous/'
}
exec('def f(kv):'+s.split('def f(kv):')[1].split("(C/'retrieval-log.json')")[0]);(C/'retrieval-review-log.json').write_text(json.dumps(r,indent=2)+'\n');print([(x['key'],x.get('http_status'),x.get('error')) for x in r])
