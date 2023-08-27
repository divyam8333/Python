#Importing Libraries
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@",
    database="db1"
)

cursor=mydb.cursor()
s="Insert into Students(SName,Rollno,branch,age) Values(%s,%s,%s,%s)"
val=("Aman Chaturvedi","1009","CSE-DS","20") #Creating Single Tuple
cursor.execute(s,val)
mydb.commit()      #Commit() saves all the Changes

mydb.close()