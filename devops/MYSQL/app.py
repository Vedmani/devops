import mysql.connector

mydb = mysql.connector.connect(host = "mysqldb",
			       user = "root",
			       passwd = "password",
			       auth_plugin = "mysql_native_password")
cur = mydb.cursor()
cur.execute("CREATE DATABASE test1")
cur.execute("SHOW DATABASES")
for i in cur:
    print(i)
