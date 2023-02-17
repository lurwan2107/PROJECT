def sandwich_item(*args):
    print(f'\nSandwich is made with the following items:')
    for s in args:
        print(f'- {s}')

sandwich_item('flour')
sandwich_item('sugar', 'oil', 'butter', 'water')