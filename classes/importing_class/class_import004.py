# this is where we called the Admin class.
# and it also worked properly
from class_import003 import Admin

top_admin = Admin('Lurwan', 'Abdullahi', 'Nigeria', 'Katsina', 'Student')
top_admin.privileges.show_privileges()