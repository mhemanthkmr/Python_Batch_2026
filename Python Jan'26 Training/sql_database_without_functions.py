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

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="finance",
    user="test",
    password="test"
)

query = "SELECT * FROM user;"
insert_query = "INSERT INTO user (name) values ('Yashwanth');"
cursor = conn.cursor()
cursor.execute(insert_query)
conn.commit()