# connector | SmartDB

import sqlite3


def connector(db):
    try:
        conn = sqlite3.connect(str(db))
        if conn:
            return conn
    except Exception as e:
        print('Error: {}'.format(e))