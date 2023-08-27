import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@",
    database="db1"
)
cursor=mydb.cursor()
query="Select * from Students"
cursor.execute(query)

result=cursor.fetchall()
for i in result:
    print(i)

mydb.close()