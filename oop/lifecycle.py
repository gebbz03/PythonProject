

class X:
    def __init__(self,name):
        self.name=name
        print(self.name+" created")

    def __del__(self):
        print(self.name+" is destroyed")

x=X('X')
y=X('Y')
print("Hello World")
print('-------------------------------------')


def hello():
    x=X('hello_X')
    y=X('hello_Y')

hello()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
