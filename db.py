import psycopg2
from db_con import config
 
def create_table():
    command = """CREATE TABLE IF NOT EXISTS subdata (
                   id VARCHAR(10) PRIMARY KEY,
                   is_self BOOL,
                   url TEXT,
                   permalink TEXT,
                   processed BOOL
               )"""                  
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_sub(id, is_self, url, permalink, processed=False):
    command = """INSERT INTO subdata VALUES (%s, %s, %s, %s, %s)
                   ON CONFLICT 
                   DO NOTHING"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command, [id, is_self, url, permalink, processed])
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def upd_proc(id):
    command = """UPDATE subdata
                   SET processed = TRUE
                   WHERE id = %s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command, [id,])
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
                   
