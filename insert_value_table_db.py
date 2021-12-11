import psycopg2

def insert_values():
    query ="""INSERT INTO table_name (col1, col2) VALUES (value1, value2) RETURNING col1;"""
    conn = None
    vendor_id = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(user="postgres",
                                password="password",
                                host="localhost",
                                port="5432",
                                database="database_name")
        cur = conn.cursor()
        # query from DB        
        cur.execute(query)
        vendor_id = cur.fetchone()[0]        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("PostgreSQL connection is closed")
    return vendor_id


if __name__ == '__main__':
    insert_values()