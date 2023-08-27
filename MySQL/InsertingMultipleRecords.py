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
val=[("Rajesh Chaturvedi","1000","CSE-DS","48"),
      ("Astha Chaturvedi","1002","CSE","14"),
      ("Anita Chaturvedi","1001","AI-ML","45"),
      ("Itika Singh","1111","CS-BS","20")]
cursor.executemany(s,val)
mydb.commit()      #Commit() saves all the Changes

mydb.close()