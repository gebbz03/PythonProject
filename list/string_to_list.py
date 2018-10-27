#Splitting string to list items

import re
cars="toyota,honda,bmw,audi"

car_list=re.split(',', cars)
print(car_list)