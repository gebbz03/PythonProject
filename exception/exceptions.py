
#try and catch block
def div(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except Exception as e:
        print("Error occured",e)
        return None    

    return result    

print(div(4,2))
print(div(4,0))
print(div('1','2'))    
