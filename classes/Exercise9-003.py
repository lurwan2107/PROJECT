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

    def describe_user(self):
        print('\nPlease tell me about yourself\n')
        print(f"My name is {self.user_fst_nm} {self.user_lst_nm}")
        print(f"I was born in {self.state} state of {self.country}, and i'm a {self.occption}\n")


    def greet_user(self):
        print(f"That's great, nice to meet you {self.user_fst_nm} {self.user_lst_nm}!\n")

user_info1 = User('Lurwan', 'Abdullahi', 'Nigeria', 'Katsina', 'Student')
user_info1.describe_user()
user_info1.greet_user() 