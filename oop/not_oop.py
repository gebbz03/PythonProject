#Global Variable

restaurant_name='7 Eleven'
restaurant_owner='Gebb Ebero'


def restaurant_details():
    print(restaurant_name,restaurant_owner)

def another_restaurant():
    #Local Variable
    restaurant_address='Badas'
    print(restaurant_name,restaurant_owner)
    print(restaurant_address)

restaurant_details()
another_restaurant()
print("---------------------------OOP---------------------------")
