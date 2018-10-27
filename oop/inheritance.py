class Math:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        return self.x + self.y


class MathExtended1(Math):
    def __init__(self,x,y):
        super().__init__(x,y)

    def subtract(self):
        return self.x - self.y


math_obj=Math(2,4)
print(math_obj.sum())

math_ext_obj=MathExtended1(10,2)
print(math_ext_obj.subtract())
print(math_ext_obj.sum())


#Multiple Inheritance

class MathExtra:
    def division(self,x,y):
        return x/y

class MathExtended2(MathExtended1,MathExtra):
    def __init__(self,x,y):
        super().__init__(x,y)

    def multiplication(self):
        return self.x * self.y

math_ext2=MathExtended2(10,2)
print("Sum ",str(math_ext2.sum()))
print("Subtract",str(math_ext2.subtract()))
print("Multiplication ",str(math_ext2.multiplication()))
print("Division ",str(math_ext2.division(x=math_ext2.x,y=math_ext2.y)))                