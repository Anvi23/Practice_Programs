#9-1. Restaurant: Make a class called Restaurant. 
#The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indicating 
# that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes
#individually, and then call both methods.

class Restaurant:
    def __init__(self,restaurant_name='',cuisine_type='',number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    
    def describe_restaurant(self):
        print(f'Restaurant {self.restaurant_name} has {self.cuisine_type} cuisine.')
        #return 'A' - to get the return statement, we need to call the method and print it. 
        #if we directly print anything in a method. We need not print(menthod())

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is Open.')
    
    def set_number_served(self,number_served):
        self.number_served=number_served
    
    def get_number_served(self):
        return number_served

    def increment_number_served(self,new_customers):
        self.number_served+=new_customers



indigo=Restaurant('Indigo Deli','Pizza')
print(indigo.restaurant_name)
print(indigo.cuisine_type)
indigo.describe_restaurant() #we can directly call a method without printing it. 
indigo.open_restaurant()

bistro=Restaurant('Bistro1','American/European')
yautcha=Restaurant('Yautcha','Asian')
sernya=Restaurant('New Sernya','Tibetan')

bistro.describe_restaurant()
yautcha.describe_restaurant()
sernya.describe_restaurant()

print(bistro.number_served)

bistro.set_number_served(10)
print(bistro.__dict__)


bistro.increment_number_served(16)
print(bistro.__dict__)

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class.
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 

class Icecreams_stand(Restaurant):
    def __init__(self,restaurant_name=''):
        super().__init__(self,restaurant_name)
        self.restaurant_name=restaurant_name
        

    def showflavors(self,*flavors):
        self.flavors=[flavors]
        return (self.restaurant_name, 'offers', self.flavors,'IceCream Flavors.')
    

havmor=Icecreams_stand()
print(havmor.showflavors('Chocolate','Roasted Almond'))