import os
from urllib.parse import urlparse
import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_uri = os.getenv("DATABASE_URL", None)
print(database_uri)


def get_conn():
    if database_uri:
        result = urlparse(database_uri)
        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        conn = psycopg2.connect(database=database,
                                user=username,
                                password=password,
                                host=hostname
                                )
    else:
        conn = psycopg2.connect(host="localhost",
                                database="realestate1",
                                user="postgres",
                                password="root")
    return conn


conn = get_conn()


def execute_query(query, conn=conn):
    with conn:
        try:
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            # print(result)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
            raise error
        return result


def create_tables():
    with conn:
        cur = conn.cursor()
        with open("Airline_schema.sql", "rt") as f:
            cur.execute(f.read())
        with open("Airline_data.sql", "rt") as f:
            cur.execute(f.read())
        cur.close()
        return True


if __name__ == "__main__":
    print(execute_query("SELECT version()", conn))
    print(execute_query("SELECT * from admin", conn))
