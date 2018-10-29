
#Decorator discussion

def decor(decoratedFunc):
    def inner():
        print("Inner function")

    return inner

def testFunc():
    print("Test Func")


decorated_func=decor(testFunc)
decorated_func()    