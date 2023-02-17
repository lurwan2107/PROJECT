from class_import006 import User

"""Module that store Classes Privileges and Admin, seperate from user."""

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
    


