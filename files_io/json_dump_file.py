#Dumping data


import json

data={
    'name':'Gebb Ebero',
    'age':23,
    'country':'Philippines',
    'is_retired':True
}

with open('json_data.json','w') as fobj:
    json.dump(data,fobj)