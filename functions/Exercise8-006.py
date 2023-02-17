def city_country(city, country):
    complete_name = f'\n{city}, {country}\n'
    return complete_name.title()
calling_function1 = city_country('katsina', 'nigeria')
calling_function2 = city_country('porto', 'portugal')
calling_function3 = city_country('chicago', 'america')
print(calling_function1)
print(calling_function2)
print(calling_function3)
