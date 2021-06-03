
"""
Create a database and store your data in it
We will use SQLite to create the database.
SQLite is a database engine. It is a software that allows users to interact with a relational database.
In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines.
This allows for greater accessibility: copying a database is no more complicated than copying the file
that stores the data, and sharing a database implies just sending an email attachment.

You can use the sqlite3 module to manage SQLite database from Python. You don't need to install this module.
It is included in the standard library.
"""

# To use the module, you must first create a Connection object that represents the database.
# Here the data will be stored in the example.s3db file:
import sqlite3
conn = sqlite3.connect('example.s3db')

# Once you have a Connection, you can create a Cursor object and call its execute() method
# to perform SQL queries:
cur = conn.cursor()

# Executes some SQL query
cur.execute('SOME SQL QUERY')

# After doing some changes in DB don't forget to commit them!
conn.commit()

# To get data returned by SELECT query you can use fetchone(), fetchall() methods:
cur.execute('SOME SELECT QUERY')

# Returns the first row from the response
cur.fetchone()

# Returns all rows from the response
cur.fetchall()


"""
Objectives
In this stage, create a database named card.s3db with a table titled card. 
It should have the following columns:
    - id INTEGER
    - number TEXT
    - pin TEXT
    - balance INTEGER DEFAULT 0

Do not forget to commit your DB changes right after executing a query!
"""

"""
Theory: Introduction to operating systems
An operating system (OS) is a set of software that manages communication between all other applications 
and hardware. It turns a computer into something more than just a bunch of metal parts, namely, 
a complex system that can effectively perform different tasks.
"""




