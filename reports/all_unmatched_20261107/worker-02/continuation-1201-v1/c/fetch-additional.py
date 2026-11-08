exec(open('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/fetch.py').read().split('urls={}')[0])
urls={
'bd-emjh-manual':'https://www.seco.us/ASSETS/DOCUMENTS/ITEMS/EN/279410.pdf',
'mesh-netropsin-browser':'https://meshb.nlm.nih.gov/record/ui?ui=D009429',
'mesh-netropsin-concept':'https://id.nlm.nih.gov/mesh/M0014675.json',
'ols-ox-bile':'https://www.ebi.ac.uk/ols4/api/search?q=ox%20bile&ontology=micro,foodon,mesh,ncit,chebi&rows=100',
'ols-cherry-pulp':'https://www.ebi.ac.uk/ols4/api/search?q=cherry%20pulp&ontology=foodon,mesh,ncit,chebi&rows=100',
'chebi-polycarbonate-term':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:61433',
'sigma-phc':'https://www.sigmaaldrich.com/US/en/product/aldrich/461164',
'dsmz-498':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium498.pdf',
'dsmz-399':'https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf',
'mesh-sodium-silicate':'https://id.nlm.nih.gov/mesh/C005691.json',
'mesh-sodium-silicate-preferred':'https://id.nlm.nih.gov/mesh/M0047391.json',
'ols-netropsin':'https://www.ebi.ac.uk/ols4/api/search?q=Netropsin&ontology=chebi,ncit,mesh&rows=50',
'ols-mucin':'https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT:C16883'
}
exec(open('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/fetch.py').read().split('def f(kv):')[1].split("(C/'retrieval-log.json')")[0].join(['def f(kv):','']))
(C/'retrieval-additional-log.json').write_text(json.dumps(r,indent=2)+'\n');print([(x['key'],x.get('http_status'),x.get('error')) for x in r])
