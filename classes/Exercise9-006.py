"""Adding a new class in another class Exercise"""

class Restaurant:
    
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.name}")
        print(f"The type of cousine they sell is {self.type}\n")


    def open_restaurant(self):
        print(f"\nThe {self.name} restaurant was opened since in the morning\n")
    
    # INHERITANCE
"""The new added subclass that will inherit the superclass
   'Restaurant' together with it's attribute and methods"""

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = ['banana flavor', 'orange flavor', 'apple flavor']

    def display_flavor(self):
        print(f"The list of flavor we have availbale are:")
        for z in self.flavors:
            print(f'- {z}')


restaurant = Restaurant('GUSTO', 'Chiken Wing')
restaurant.describe_restaurant()
restaurant.open_restaurant()
ice_item = IceCreamStand('BILNAF KITCHEN', 'KIBAB') # Instance for IceCreamClass
ice_item.display_flavor() # Calling the display method
        