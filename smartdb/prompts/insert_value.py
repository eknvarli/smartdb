# insert_value | SmartDB

def insert_value(conn, table, values=[]):
    value_list = ','.join('"' + str(value) + '"' for value in values)
    cur = conn.cursor()

    prompt = f'INSERT INTO {table} VALUES({value_list})'
    cur.execute(prompt)

    if conn:
        conn.commit()

        print('Data successfully added.')
        return True