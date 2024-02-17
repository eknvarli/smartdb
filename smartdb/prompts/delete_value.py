# delete_value | SmartDB

def delete_value(conn, table, column, value):
    cur = conn.cursor()
    cur.execute(f'DELETE FROM {table} WHERE {column} = "{value}"')

    if conn:
        print('Delete operation was successful.')
        conn.commit()
        return True