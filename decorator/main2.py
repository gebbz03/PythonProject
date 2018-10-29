
#Decorator discussion

def decor(decoratedFunc):
    def inner():
        print("Inner function")

    return inner

def testFunc():
    print("Test Func")


#syntactic sugar

@decor
def testFunc1():
    print("Test Func1")


testFunc1()    