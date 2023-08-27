#Importing Libraries
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@",
    database="db1"
)

cursor=mydb.cursor()
query="Update Students SET branch='CSE-IT' where SName='Aman Chaturvedi'"
cursor.execute(query)

#For Changing Data permanently We use Commit()
mydb.commit()

#Disconnecting From Server
mydb.close()