import mysql.connector
from rich import print

# Key Important things to connect with database
"""
1. Username 
2. Password
3. Host
4. Database
5. Port
"""
def create_connection(database="finance"):
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        database=database,
        user="test",
        password="test"
    )
    conn.autocommit = True
    return conn


def execute_query(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

def fetch_data_from_cursor(cursor):
    data = cursor.fecth_all()
    return data

conn = create_connection()
query = "SELECT * FROM user;"
insert_query = "INSERT INTO user (name) values ('Yashwanth');"
cursor = execute_query(conn, query)
data = fetch_data_from_cursor(cursor)
conn.close()