"""Creating a restaurant class with 2 methods
    and create 3 different 'instances' and call
    describe_restaurant method with each instances"""

class Restaurant:
    
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.name}")
        print(f"The type of cousine they sell is {self.type}\n")


    def open_restaurant(self):
        print(f"\nThe {self.name} restaurant was opened since in the morning\n")


restaurant = Restaurant('GUSTO', 'Chiken Wing')
restaurant.describe_restaurant()

restaurant1 = Restaurant('BILNAF KITCHEN', 'Fried Rice')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('CITY RESTAURANT', 'Chips')
restaurant2.describe_restaurant()

        