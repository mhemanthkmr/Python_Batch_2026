import mysql.connector

HOST = "localhost"
USER = "test"
PASSWORD = "test"
PORT = "3306"
DATABASE = "finance"

conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    port=PORT,
    database=DATABASE
)
conn.autocommit=True
print(conn)

# Creating a new cursor to execute the Query
cursor = conn.cursor()

name = input("Enter a name:")

query = f"""insert into user (
    name
) VALUES ('{name}');"""

cursor.execute(query)
# data = cursor.fetchall()
# print(data)
conn.close()