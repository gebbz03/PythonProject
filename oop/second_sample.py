
class Person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age

    def details(self):
        #self is optional, you can set any variable
        print(self.name,self.age,sep='|')


bill1=Person()
bill1.details()  

bill2=Person("Gebb Ebero",23)
bill2.details()  