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

connection = create_connection("school.db")

student_courses_query = """
SELECT Students.name, Enrollments.course_id
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
WHERE Enrollments.student_id = 73518;
"""


i = execute_read_query(connection, student_courses_query)

print(i)


course_students_query = """
SELECT Courses.course_name, Students.name
FROM Enrollments
JOIN Courses ON Enrollments.course_id = Courses.course_id
JOIN Students ON Enrollments.student_id = Students.student_id
WHERE Enrollments.course_id = 113
"""

i = execute_read_query(connection, course_students_query)

print(i)


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
execute_query(connection, create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
execute_query(connection, create_posts_table)

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

execute_query(connection, create_comments_table)  
execute_query(connection, create_likes_table)

# inserts users in database
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

# execute_query(connection, create_users)

# Insert posts in database
create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

# execute_query(connection, create_posts)

# Insert comments and likes in database
create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

# execute_query(connection, create_comments)
# execute_query(connection, create_likes)  



#Creating the requested tables
create_students_table = """
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  student_id INTEGER NOT NULL, 
  name TEXT, 
  major TEXT,
  FOREIGN KEY (student_id) REFERENCES users (id)
);
"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  course_id INTEGER NOT NULL, 
  course_name TEXT, 
  instructor TEXT,
  FOREIGN KEY (course_id) REFERENCES users (id)
);
"""


execute_query(connection, create_students_table)
execute_query(connection, create_courses_table)  



#Filling requested tables with requested data

create_students = """
INSERT INTO
  students (student_id, name, major)
VALUES
  (73518, 'James', 'Rizzology'),
  (72874, 'Leila', 'Quantum Field Theory'),
  (36284, 'Brigitte', 'Finance'),
  (27492, 'Mike', 'History'),
  (33791, 'Elizabeth', 'Spookiness');
"""



create_courses = """
INSERT INTO
  courses (course_id, course_name, instructor)
VALUES
  (113, 'Rizz', 'Livvy Dunne'),
  (101, 'Math', 'Jack Black'),
  (311, 'Gooning', 'Jacob Sartorius'),
  (752, 'Looksmaxxing', 'John Mew'),
  (324, 'Economics', 'John Johnson');
"""


execute_query(connection, create_students)  
# execute_query(connection, create_courses)


create_enrollmens_table = """
CREATE TABLE IF NOT EXISTS Enrollments (
  enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Students(student_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
"""


create_enrollments = """
INSERT INTO
  Enrollments (student_id, course_id)
VALUES
  (73518, 113),
  (72874, 101),
  (36284, 311),
  (27492, 752),
  (33791, 324);
"""
execute_query(connection, create_enrollmens_table)  
# execute_query(connection, create_enrollments)
