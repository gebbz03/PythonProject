#Ignore Exception
def div(x,y):
    return x / y


try:
    div_result=div(2,0)
except:
    pass #do nothing
else:
    print("Div result is: " + str(div_result ))        