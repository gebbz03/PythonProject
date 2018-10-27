#List Modification

mix_list=['honda',29,4.4,False]
print(mix_list)
mix_list[0]='toyota'
print(mix_list)

#Adding item in list

mix_list.append('audi')
print(mix_list)

#Shortcut version for adding list

mix_list += ['mercedez']
print(mix_list)

mix_list.insert(2,'proton')
print(mix_list)


#Deleting item in list

cars2=['honda','toyota','audi']
print(cars2)
del cars2[0]
print(cars2)