#Iteration
tp=1,2,'Bill',4.4,False
for t in tp:
    print(t)

print("-----------------------------------")

#Comparing

t1=1,2,3
t2=1,2,3

if t1 == t2:
    print("Both are equal")
else:
    print("Not equal") 

print("-----------------------------------")


#Unpacking or multiple assignment

t3=5,7,11
x,y,z=t3
print(x,y,z,sep='|')

print("-----------------------------------")

t4=5,7,11
xx,yy,_=t4
print(xx,yy,sep='|')
