"""To be called in file 2, 3, 4, 5, and 6
with different function import style"""

def make_pizza(size, *args):
    print(f'\nMaking a {size} - inch pizza')
    for n in args:
        print(f'- {n}')
