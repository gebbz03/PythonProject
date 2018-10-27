#Global Variable

class Restaurant:
    def details(self):
        print(self.name,self.owner)

    def details_with_address(self,address):
        self.details()
        print(address)


#Instantiation    
restaurant1=Restaurant()

#creating variable
restaurant1.name='7 Eleven'
restaurant1.owner='Gebb Ebero'

restaurant1.details()
restaurant1.details_with_address('Badas')

print(type(restaurant1))
