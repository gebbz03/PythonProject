#sum of list numbers

list_of_number=[1,2,3,4,5]
sum=0

for num in list_of_number:
    sum +=num
print("Sum is: {sum}".format(sum=sum))
print("-----------------------------------")


list_of_number2=[1,2,'Math',4,5.5,5]
sum2=0

for num2 in list_of_number2:
    if type(num2) == int:
        sum2 += num2
print("Sum2 is: {sum2}".format(sum2=sum2))