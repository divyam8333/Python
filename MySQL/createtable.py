import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@",
    database="db1"
)

cursor=mydb.cursor()
studentRecord="Create Table Students(SName varchar(30) not null,Rollno int not null,branch varchar(15),age int)"

cursor.execute(studentRecord)