from asyncio import StreamReader
from asyncore import write
from codecs import StreamWriter
import mysql.connector

con = mysql.connector.connect(user = 'qwallity',
                              password = 'mysqlpass',
                              host = 'qwallitydb.cywlir8bfmdo.eu-central-1.rds.amazonaws.com',
                              database = 'qwallity_db')   

cursor = con.cursor()   

cursor.execute("Select * from qwallity_db.courses")

f = open("Working_with_DB\log.txt", 'w')

# Write into file
for raw in cursor:
     #print(str(raw))
     f.write(str(raw))
     f.write("\n")

f.close()   
    
# print(cursor.rowcount)
con.close()

# read from file 
# data = open("Working_with_DB\log.txt","r");


# for d in data:
#     print(d)
 
# data.close()

            

    
 