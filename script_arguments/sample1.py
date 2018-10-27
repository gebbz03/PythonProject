import sys
from mspack import msmath

def process_command(*args):
    command=args[0]
    x=int(args[1])
    y=int(args[2])

    if command == 'sum':
        print('Sum is: ',msmath.sum(x,y))

    if command == 'sub':
        print('Subtract is: ',msmath.subtract(x,y))

    if command == 'mul':
        print('Multiplication is: ',msmath.multiplication(x,y))

    if command == 'div':
        print('Division is: ',msmath.division(x,y))          

if len(sys.argv) >= 4:

    command = sys.argv[1].lower()
    x       = sys.argv[2]
    y       = sys.argv[3]


    try:
        process_command(command,x,y)

    except Exception as e:
        print("Error in process command:",e)

else:

    print("Command and Parameters are not sufficient")



#sample command in cmd
# python sample1.py sum 2 4                