#CHECK ITEM OR EXIST

set_country={'bangladesh','malaysia','singapore','usa'}
country='bangladesh'

if country in set_country:
    print(country.title(),'exists')
else:
    print("Not exists")    