#String


title="Python Course"
title1='Java Course'

print(title)
print(title1)

print(title[0],title[1],title[-1],title[-2])
print("--------------------------------------")

#String operation
name="Jonathan Swift"

print(name.title())
print(name.upper())
print(name.lower())
print("--------------------------------------")

#String concatenation

first_name="Steve"
last_name="Jobs"
name=first_name+' '+last_name
print(name)
print(first_name+' '+last_name)
print("--------------------------------------")

#String Newline

print(first_name+"\n"+last_name)
print("--------------------------------------")

#Whitespace
namex="Steve Jobs"
namex="     Mr. X       "
print('_'+namex+'_')
print('_'+namex.lstrip()+'_')
print('_'+namex.rstrip()+'_')
print('_'+namex.strip()+'_')
print('_'+namex.lstrip().rstrip()+'_')
print("--------------------------------------")

#Printing Single and Double Quote

shop_name="Gebb'z Shop"
print(shop_name)

shop_name='Gebb"z Shop'
print(shop_name)

shop_name='Gebb\'z Shop'
print(shop_name)
