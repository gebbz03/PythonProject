#CSV File Read

import csv

with open('sample.csv','r') as fobj:
    fcsv=csv.reader(fobj)

    sum=0
    for i, row in enumerate(fcsv):
        print(i,row[0],row[1])
        sum += int(row[1]) if  i > 0 else 0
    print("Total cost: ",sum)    