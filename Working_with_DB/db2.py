from os import curdir
from sqlite3 import Cursor
import mysql.connector

con = mysql.connector.connect(host = "qwallitydb.cywlir8bfmdo.eu-central-1.rds.amazonaws.com",
password = "mysqlpass",
username = "qwallity",
database = "qwallity_db")

coursor = con.cursor()
coursor.execute('select * from courses where author = "Team2_2" order by date_created desc')

for raw in coursor:
    print(raw)

con.close()
