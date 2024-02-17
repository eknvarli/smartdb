# update_value | SmartDB

def update_value(conn, table, column, new_value, condition_column, condition_value):
    cur = conn.cursor()

    # Update value in the table
    cur.execute(f"UPDATE {table} SET {column} = ? WHERE {condition_column} = ?", (new_value, condition_value))

    if conn:
        conn.commit()
        print('Data successfully updated.')
        return True
