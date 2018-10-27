def div(x,y):
    return x/y

try:
    div_result=div(8,2)

except:
    print("Cannot divide by zero")

else:
    print("Div result is: "+str(div_result))