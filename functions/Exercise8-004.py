# Using default value
def make_shirt(size = 'Large', text = 'I Love Python'):
    print('\nThe shirt size is Medium and %s and it contains %s at the front' %(size.title(), text.title()))
    print('The remaining shirts are of different size\n')

make_shirt()
