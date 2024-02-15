# Table Type Detector
import sqlite3

def detect(conn, table):
    cur = conn.cursor()
    
    # run command
    cur.execute(f'PRAGMA table_info({table})')
    columns = cur.fetchall()
    column_names = [column[1] for column in columns]

    # get column data
    for x in column_names:
        # basic algorithm
        column_lower = str(x).lower()

        # AUTH_TABLE
        if column_lower == 'username':
            return 'AUTH_TABLE'
        if column_lower == 'password':
            return 'AUTH_TABLE'
        
        # REFERENCE_TABLE
        if column_lower == 'customer_id':
            return 'REFERENCE'
        if column_lower == 'order_id':
            return 'REFERENCE'
        #TODO: Add new options.
        
        # ...
        else:
            print(f'Table "{table}" type is not recognized.')
            return False