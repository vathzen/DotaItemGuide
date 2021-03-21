import json,requests,os

r = requests.get('https://api.opendota.com/api/constants/items')
serialized = []
for s in r.json().values():
    serialized.append({"model":"Home.Item","pk":s['id'],"fields":s})
with open(os.path.join('./DotaItemGuide/Home/fixtures/','items.json'),'w') as out:
    json.dump(serialized,out)