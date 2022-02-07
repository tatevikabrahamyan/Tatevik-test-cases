import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

#Create cursor
c = conn.cursor()

#Create a Table
c.execute("""CREATE TABLE customers (

    First_name text,
    Last_name text,
    email text
)""")

#Datatypes:
# NULL
# Integer
# Real
# Text
# BLOB

# Commit our command
conn.commit()

#Close our connection
conn.close()
