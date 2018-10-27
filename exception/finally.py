def div(x,y):
    try:
        result=x/y

    except ZeroDivisionError:
        print("Error divison by zero")

    else:
        print("Result is: ",result)

    finally:
        print("Execute finally clause")


div(100,10)
div(2,0)                    