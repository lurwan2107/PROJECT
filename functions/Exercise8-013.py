def build_profile(first, last, **user_infor):
    user_infor['first name'] = first
    user_infor['last name'] = last
    return user_infor

user_profile = build_profile('Lurwan', 'Abdullahi', country = 'Nigeria', 
                              state = 'Katsina', LGEA = 'Jibia')
print(f'\n{user_profile}\n')

