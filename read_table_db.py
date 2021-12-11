import psycopg2

def read_tables():
    # query from DB
    query ="""SELECT * FROM table_name"""
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(user="postgres",
                                password="password",
                                host="localhost",
                                port="5432",
                                database="database_name")
        cur = conn.cursor()
        # command to query on DB
        cur.execute(query)
        # fetch all rows.
        query_results = cur.fetchall()
        # print the query results
        print(query_results)           
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
    read_tables()