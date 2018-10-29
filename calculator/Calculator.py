
class Math:
    a = 0
    b = 0


    def __init__(self,firstNum,secondNum):
        self.a=firstNum
        self.b=secondNum

    def addition(self):
        result=self.a + self.b
        return result

    def subtraction(self):
        result=self.a - self.b
        return result

    def division(self):
        result=self.a / self.b
        return result

    def multiplication(self):
        result=self.a * self.b
        return result
