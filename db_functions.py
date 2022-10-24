        
def create_connection(db_name):
    """ 
    create a database connection to the SQLite database
        specified by db_name
    return: Connection object or None
    """
    conn = None
    try:
        conn = db.connect(db_name)
        return conn
    except Error as e:
        print(e)

    return conn

def conn_execute(sql_code):
    """
    excute sql code on the connection to the sqlite database
    """
    try:
        c.execute(sql_code)
    except Error as e:
        print(e)
    conn.close()