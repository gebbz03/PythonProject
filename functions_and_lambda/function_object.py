#Function are first-class object


def str_upper(str):
    return str.upper()

print(str_upper("hello"))
stup=str_upper
print(stup("hello"))
print("------------------------")

#Function can be passed as argument

def greetings(func):
    greet=func("Welcome, nice to meet you")
    print(greet)

greetings(str_upper)
print("------------------------")


#Functional Programming

up_list=list(map(str_upper,["Life","is","cool"]))
print(up_list)
print("------------------------")


#Nested function

def hello(str):
    def print_upper(s):
        return s.upper()

    print(print_upper(str))

hello("mango")
