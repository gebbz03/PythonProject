
import hello
import Calculator


#hello.printHello("Gebb Ebero")


var1 = "n"

while(var1 == "n"):

    print("1.   Addition")
    print("2.   Subtraction")
    print("3.   Division")
    print("4.   Multiplication")


    userSelected = input("Input: ")

    num1=input("Please enter first number:  ")
    num2=input("Please enter second number:  ")

    math=Calculator.Math(float(num1),float(num2))



    if(userSelected == "1"):
        print("---------------ADDITION---------------")
    
        res = math.addition()
        print("---------------------------------------")
        print("RESULT:  "+str(res))
        print("---------------------------------------")

    elif(userSelected == "2"):
        print("---------------SUBTRACTION---------------")
        
        res = math.subtraction()
        print("---------------------------------------")
        print("RESULT:  "+str(res))
        print("---------------------------------------")

    elif(userSelected == "3"):
        print("---------------DIVISION---------------")
        
        res = math.division()
        print("---------------------------------------")
        print("RESULT:  "+str(res))
        print("---------------------------------------")
        
    elif(userSelected == "4"):
        print("---------------MULTIPLICATION---------------")
        
        res = math.multiplication()
        print("---------------------------------------")
        print("RESULT:  "+str(res))
        print("---------------------------------------")

    else:
        print("---------------------------------------")
        print("Invalid selection")    
        print("---------------------------------------")


    var1=input("Do you want to exit? (y/n)  ")    



