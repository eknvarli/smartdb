# Test
from smartdb.modules import table_type_detector
from smartdb.modules import password_strength_check

import sqlite3


# Creating a test database.
conn = sqlite3.connect('my.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')


# Example table controller
if table_type_detector.detect(conn, 'users') == 'AUTH_TABLE':
    print('This is a auth table.')


# Example password checker
mypassword = 'Test123!'
try:
    password_strength_check(mypassword)
except Exception as e:
    print(e)