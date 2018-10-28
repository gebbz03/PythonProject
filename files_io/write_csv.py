#CSV File Write

import csv

list_item=[["name","age","country"],
           ["Bill Gates",55,"US"],
           ["Steve Jobs",57,"US"],
           ["Swift",35,"Canada"]]

with open('people.csv','w') as fobj:
    fcsv=csv.writer(fobj)
    fcsv.writerows(list_item)           

