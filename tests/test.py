# Test
from smartdb.algorithms import table_type_detector
from smartdb.algorithms import password_strength_check

from smartdb import prompts

import sqlite3


# Creating a test database.
conn = sqlite3.connect('my.db')
prompts.create_table(conn, 'users', {
    'username':'TEXT',
    'role':'TEXT',
    'password':'TEXT'
})


# Example table controller
if table_type_detector.detect(conn, 'users') == 'AUTH_TABLE':
    print('This is a auth table.')


# Example password checker
mypassword = 'Test123!'
try:
    password_strength_check(mypassword)
except Exception as e:
    print(e)