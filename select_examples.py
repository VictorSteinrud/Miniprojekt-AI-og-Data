import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("sm_app.sqlite")

# select and retrieve users
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

print()
# select and retrieve posts
select_posts = "SELECT * FROM posts WHERE user_id = 1"
posts = execute_read_query(connection, select_posts)

for post in posts:
    print(post)

print()
# select and retrieve comments
select_comments = "SELECT id, text FROM comments"
comments = execute_read_query(connection, select_comments)

for comment in comments:
    print(comment)

print()
# select and retrive comments with user
select_comm_user = "SELECT c.text, u.name FROM comments AS c, users AS u WHERE c.user_id = u.id" 
comm_users = execute_read_query(connection, select_comm_user)

for comm_user in comm_users:
    print(comm_user)
