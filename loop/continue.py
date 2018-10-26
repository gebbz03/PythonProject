#Continue Statement

#Omit even number 1 to 20

x=0
while x < 20:
    x +=1
    if x % 2 == 0:
        continue
    print(x)