import sqlite3

## Connect to sqlite
connection = sqlite3.connect('chat.db')

## Create a cursor
cursor = connection.cursor()

## Create a table
table_info = """
create table if not exists chat (
    NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT
);"""

cursor.execute(table_info)

## Insert data
cursor.execute("insert into chat values ('John', 'A', '1', 90)")
cursor.execute("insert into chat values ('Doe', 'B', '2', 80)")
cursor.execute("insert into chat values ('Jane', 'C', '3', 70)")

## Commit the changes
connection.commit()

## Fetch data
cursor.execute("select * from chat")
data = cursor.fetchall()

## Print the data
for row in data:
    print(row)

## Close the connection
connection.close()
