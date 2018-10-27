
class Person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age

    def details(self):
        #self is optional, you can set any variable
        print(self.name,self.age,sep='|')

people_list=[]
for x in range(0,3):
    person=Person("Person "+str(x),30+x)
    people_list += [person]

for x in people_list:
    x.details()    
