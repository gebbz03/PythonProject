#Reference type

num_list=[1,2,3,4,5]
num_dict={'one':1,'two':2,'three':3}

def  change_num_list(list,dict):
    del list[0]
    list[-1]=50

    del dict['one']
    dict['three']=33
    print("Inner List: ",list)
    print("Inner Dict: ",dict)

print("Before")
print("Outer List: ",num_list)
print("Outer Dict: ",num_dict)
print("--------------------------------------------")
change_num_list(list=num_list, dict=num_dict)
print("After")
print("Outer List: ",num_list)
print("Outer Dict: ",num_dict)    