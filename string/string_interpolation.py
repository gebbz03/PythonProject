#String Interpolation
#Old Style

person='%s\'s age is %d'
print(person%('Bill',55))

#New Style

person='{name}\'s age is {age}'
print(person.format(name="Bill",age=55))
print(person.format(name="Gebb",age=23))
print("------------------------------------")

#Formatted String literal python 3.6+

name="Gebb Ebero"
age=23
person=f'{name}\'s age is {age}'
print(person)
