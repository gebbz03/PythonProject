

class Alien:
    legs=5

    def __init__(self,name):
        self.name=name


alien1=Alien("Alien 1") 
alien2=Alien("Alien 2")
alien1.legs=40
print(alien1.legs,alien2.legs)

alien1.__class__.legs=99
print(alien1.name,alien2.name)
print(alien1.legs,alien2.legs)


Alien.legs=10
print(alien1.legs,alien2.legs)