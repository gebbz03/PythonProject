


import json

data={
    'name':'Gebb Ebero',
    'age':23,
    'country':'Philippines',
    'is_retired':True
}

with open('json_data.json','r') as fobj:
    json_data=json.load(fobj)
    print(json_data)