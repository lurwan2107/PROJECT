"""Creating a restaurant class with 2 methods
    and call all the methods once"""

class Restaurant:
    
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type
        self.number_served = 0               # Added attribute

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.name}")
        print(f"The type of cousine they sell is {self.type}\n")


    def open_restaurant(self):
        print(f"\nThe {self.name} restaurant was opened since in the morning")
        print(f"The number of people served is {self.number_served}\n")  #printing the number of people served

    """Adding new method and use it to print
       the number of people served"""
    def set_number_served(self, num_served):
        self.number_served = num_served
        print(f"Number of people served are {self.number_served}\n")

    """Adding new method that will increment 
       the number of people served"""
    def increment_number_served(self, num):
        self.number_served += num
        print(f"Number of people served today {self.number_served}\n")


restaurant = Restaurant('GUSTO', 'Chiken Wing')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(150)       #Calling the new method
restaurant.increment_number_served(250) #Calling new additional method 
        