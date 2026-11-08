from pathlib import Path
s=Path('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/fetch.py').read_text();exec(s.split('urls={}')[0])
urls={'mg6-epa':'https://www.govinfo.gov/content/pkg/FR-2020-07-20/pdf/2020-14401.pdf','mg6-icsc':'https://inchem.org/documents/icsc/icsc/eics1197.htm','mn7-inconsistent-sds':'https://alphachem.com.au/wp-content/uploads/2024/11/SDS-Manganese-Sulphate-Tetrahydrate.pdf'}
exec('def f(kv):'+s.split('def f(kv):')[1].split("(C/'retrieval-log.json')")[0]);(C/'retrieval-review2-log.json').write_text(json.dumps(r,indent=2)+'\n');print([(x['key'],x.get('http_status'),x.get('error')) for x in r])
