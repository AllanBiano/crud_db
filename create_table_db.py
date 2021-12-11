import psycopg2

def create_table():
    create_table =  """CREATE TABLE table_name (
                        col1 SERIAL PRIMARY KEY,
                        col2 VARCHAR(255) NOT NULL
                    )"""
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(user="postgres",
                                password="password",
                                host="localhost",
                                port="5432",
                                database="database_name")
        cur = conn.cursor()
        # command to create a table on DB
        cur.execute(create_table)     
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    create_table()