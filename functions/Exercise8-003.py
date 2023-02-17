
def make_shirt(size, text):
    print('The shirt size is %s and it contains %s at the front' %(shirt_size.title(), display_text.title()))
shirt_size = input('\nEnter the size of shirt: ')
display_text = input('\nEnter the shirt message: ')
# calling the function using positional argument
make_shirt(shirt_size, display_text)
# calling the function using keyword argument
make_shirt(size = shirt_size, text = display_text)