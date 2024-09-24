

import sqlite3
sqlconn = sqlite3.connect("my_db.db")
print("Database connected")

cursor =sqlconn.cursor()
print("Database initialized")

sql_creat_table="""
 CREATE TABLE IF NOT EXIST User(
  id INTRGER PRIMARY KEY,
  name varchar (100),
  gender char(1)
  )
  """

sqlconn.execute(sql_creat_table)
print ("Table Created")

# Insert data into the table
sql_insert_data = """
INSERT INTO User (id, name, gender)
VALUES (?, ?, ?)
"""

# Example data
data = [
    (1, 'Alice', 'F'),
    (2, 'Bob', 'M'),
    (3, 'Charlie', 'M')
]
# Insert multiple rows
cursor.executemany(sql_insert_data, data)
print("Data Inserted")

# Commit the transaction to the database
sqlconnconn.commit()


