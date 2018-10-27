

x=[1,2,3]
xx=x

print(x == xx)
print(x is xx)

y=list(x)
print(x == y)
print(x is y) #False because y is another object


l=[1,2,3]
print(l)

class Person:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'{self.__class__.__name__}class,obj name: {self.name}'

p1=Person('Steve')
p2=Person('Bill')

print(p1)
print(p2)