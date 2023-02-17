"""Creating a restaurant class with 2 methods
    and call all the methods once"""

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
restaurant.open_restaurant()

        