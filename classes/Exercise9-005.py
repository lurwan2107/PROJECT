""""Craeting a class that describe the different users
    imformation by craeting several instances"""


class User:
    
    
    def __init__(self, first_name, last_name,
                 nationality, state_of_origin,
                 occupation):
        
        self.user_fst_nm = first_name
        self.user_lst_nm = last_name
        self.country = nationality
        self.state = state_of_origin
        self.occption = occupation
        self.login_attempt = 0      # New attribute

    def describe_user(self):
        print('\nPlease tell me about yourself\n')
        print(f"My name is {self.user_fst_nm} {self.user_lst_nm}")
        print(f"I was born in {self.state} state of {self.country}, and i'm a {self.occption}\n")


    def greet_user(self):
        print(f"That's great, nice to meet you {self.user_fst_nm} {self.user_lst_nm}!\n")

    """New method to increment user login attempt"""
    def increment_login_attempt(self, num1):
        self.login_attempt += 1
        self.login_attempt += num1
        print(f"Your number of login is: {self.login_attempt}\n")

    """New method to reset user login attempt"""
    def rest_login_attempt(self, num2):
        self.login_attempt -= 1
        self.login_attempt -= num2
        print(f"You have {self.login_attempt} remaining login attempt\n")

user_info = User('Lurwan', 'Abdullahi', 'Nigeria', 'Katsina', 'Student')

user_info.describe_user()
user_info.greet_user()

user_info.increment_login_attempt(23) 
user_info.rest_login_attempt(23)