from pathlib import Path
s=Path('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/fetch.py').read_text();exec(s.split('urls={}')[0])
urls={
'chebi-ox-bile':'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:752954',
'micro-ox-bile':'https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000610',
'sigma-phc-uk':'https://www.sigmaaldrich.com/GB/en/product/aldrich/461164',
'sigma-phc-sds':'https://www.sigmaaldrich.com/US/en/sds/aldrich/461164',
'mesh-congocidine-term':'https://id.nlm.nih.gov/mesh/T028107.json'
}
exec('def f(kv):'+s.split('def f(kv):')[1].split("(C/'retrieval-log.json')")[0]);(C/'retrieval-tertiary-log.json').write_text(json.dumps(r,indent=2)+'\n');print([(x['key'],x.get('http_status'),x.get('error')) for x in r])
