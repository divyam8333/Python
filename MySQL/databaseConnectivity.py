import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Aman123@')

print(mydb.connection_id)
