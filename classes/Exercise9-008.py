"""Writing a seperate class, the instance of the class
   will be used as an attribute of another class."""


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

"""Writing a seperate class, the instance of the class
   will be used as an attribute of another class."""

class Privilages:
    def __init__(self):
        self.privilege_s = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        k = 1
        print('\nAdmin have the privilege to do the following:')
        for i in self.privilege_s:
            print(f'{k}. {i}')
            k += 1

class Admin(User):
    def __init__(self, first_name, last_name, nationality, state_of_origin, occupation):
        super().__init__(first_name, last_name, nationality, state_of_origin, occupation)
        self.privileges = Privilages() # changes to attribute
    

user_info1 = User('Lurwan', 'Abdullahi', 'Nigeria', 'Katsina', 'Student')
user_info1.describe_user()
user_info1.greet_user() 
top_admin = Admin('Lurwan', 'Abdullahi', 'Nigeria', 'Katsina', 'Student')
top_admin.privileges.show_privileges() # Calling the class