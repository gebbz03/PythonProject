#Method Overriding
class Math:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        return self.x + self.y


class MathExtended1(Math): #Child class
    def __init__(self,x,y):
        super().__init__(x,y)

    def subtract(self):
        return self.x - self.y

    def sum(self): #Override
        return self.x + self.y + 100

    def show_all(self):
        print("Sum: "+str(self.sum()))
        print("Subtract: "+str(self.subtract()))


math_ext_obj=MathExtended1(10,2)
math_ext_obj.show_all()


