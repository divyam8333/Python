#Importing Libraries
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@",
    database="db1"
)

cursor=mydb.cursor()
query="Delete from Students where Rollno=1000"
cursor.execute(query)

#All changes will be permanently Saved
mydb.commit()

#Disconnecting from the server
mydb.close()