# get_all_datas | SmartDB

def get_all_datas(conn, table):
    cur = conn.cursor()

    prompt = f'SELECT * FROM {table}'
    cur.execute(prompt)   
    datas = cur.fetchall()

    return datas