def car_infor(manufacturer, model, **kwargs):
    kwargs['Car manufacturer'] = manufacturer
    kwargs['Car model'] = model
    return kwargs

car = car_infor('German', 'Toyota 94', Color = 'Silver', Driving = 'Automatic')
print(f'\n{car}\n')