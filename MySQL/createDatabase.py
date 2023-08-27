import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aman123@"
)
cursor=mydb.cursor()

cursor.execute("Create database db1")
