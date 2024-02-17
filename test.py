# Test
from smartdb.algorithms import table_type_detector
from smartdb.algorithms import password_strength_check

from smartdb import prompts
from smartdb import tools


# Database connection
connection = tools.connector('my.db')
if connection:
    print('Database connection was successfully.')

# Creating a test database.
prompts.create_table(connection, 'users', {
    'username':'TEXT',
    'role':'TEXT',
    'password':'TEXT'
})


# Example table controller
if table_type_detector.detect(connection, 'users') == 'AUTH_TABLE':
    print('This is a auth table.')


# Generate strong password
mypassword = tools.generate_strong_password(20)
print('Generated Strong Password: {}'.format(mypassword))

# Example password checker
try:
    password_strength_check(mypassword)
except Exception as e:
    print(e)


# Insert value to database
prompts.insert_value(connection, 'users', [
    'Ekin',
    'Admin',
    mypassword
])


# Delete value from database
# prompts.delete_value(connection, 'users','username','Ekin')


# Update value from database
prompts.update_value(
    connection,
    table='users',
    column='username',
    new_value='Cenk',
    condition_column='username',
    condition_value='Ekin'
)


# Get all datas
datas = prompts.get_all_datas(connection, 'users')
print(datas)