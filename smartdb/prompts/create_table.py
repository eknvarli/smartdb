# create_table | SmartDB
import sqlite3


def create_table(conn, table, columns):
    column_list = ','.join(str(column) + ' ' + str(type) for column,type in columns.items())
    cur = conn.cursor()
    
    # prompt
    prompt = f'CREATE TABLE IF NOT EXISTS {table}({column_list})'
    cur.execute(prompt)
    if conn:
        print('Table was successfully created')
        return True