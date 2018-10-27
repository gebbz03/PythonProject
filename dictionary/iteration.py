#Iteration

asci_dict={'a':97,'b':98,'c':99,'d':100}

for key, value in asci_dict.items():
    print(key,value,sep='->')

print("-------------------------------------")    

asci_dict2={'a':97,'b':98,'c':99,'d':100}

for key in asci_dict2:
    print(key)


print("-------------------------------------")    

asci_dict3={'a':97,'b':98,'c':99,'d':100}

for value in asci_dict3.values():
    print(value)


print("-------------------------------------") 
#Sorted key while iterate

shop_items={
    'rice':44,
    'flour':33,
    'oil':32
}

print(shop_items)
print("-------------------------------------") 

for key in sorted(shop_items.keys()):
    print(key,shop_items[key])