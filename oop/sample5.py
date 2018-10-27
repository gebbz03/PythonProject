
class Person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age

    def change_name(self,name):
        self.name=name    

    def details(self):
        #self is optional, you can set any variable
        print(self.name,self.age,sep='|')

#Directly change
person_x=Person(name='Stone Cold',age=49)
person_x.details()

person_x.name="Rock"
person_x.details()
print("-------------------------------")


#Indirectly change
person_x.change_name('Triple X')
person_x.details()


