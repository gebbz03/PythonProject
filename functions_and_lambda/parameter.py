#Parameters

def welcome(name):
    print(f"Welcome {name}")

welcome('Bill')
welcome('Steve')
print("------------------------------------")



#Positional Argument

def person_details(name,age,country):
    print(name,age,country,sep='|')

person_details("Gebb",23,"Philippines")
person_details("Michael",25,"USA")   
print("------------------------------------")

#Keyword Argument

def pdetails(name,age,country):
    print(name,age,country,sep='|')

pdetails(name='Bil',age=55,country="USA")
pdetails(age=40,country='Canada',name='Swift')
print("------------------------------------")

#Default Value

def persona(name,age,country='Philippines'):
    print(name,age,country,sep='|')

persona(name="Bill",age=55,country="USA")
persona(name="Swift",age=40)
persona("Edelyn",age=23)
print("------------------------------------")


#non-default argument

def persona2(name='',age=0,country='Philippines'):
    print(name,age,country,sep='|')



