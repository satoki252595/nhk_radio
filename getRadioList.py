import json
import requests
 
url = 'https://www.nhk.or.jp/radioondemand/json/index_v3/index.json'
 
resp = requests.get(url)
js = resp.json()
# print(type(js), js)
 
pg_list= js['data_list']
pg_names = []
result = []
for pg in pg_list:
    if pg['program_name'] not in pg_names:
        pg_names.append(pg['program_name'])
        result.append(pg)
 
result = sorted(result, key=lambda x: x['program_name'])
 
for d in result:
  title = d['program_name']
  file = d['detail_json']
  print(f'{title},{file}')
