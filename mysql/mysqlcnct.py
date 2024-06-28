##creating database

# import mysql.connector
# mydb2=mysql.connector.connect(
# host="localhost",
# user='root',
# password='spectrum'
# )

# mycursor=mydb2.cursor()
# mycursor.execute("CREATE DATABASE mydb2")

#creating table

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="spectrum",
#   database="mydb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customerss (name VARCHAR(255), address VARCHAR(255))")




##delete

# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='spectrum',
#     database='mydb'
# )
# mycursor=mydb.cursor()

# sql='DELETE FROM customerss WHERE name="adhi"'
# mycursor.execute(sql)

# mydb.commit()


#insert

# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='spectrum',
#     database='mydb'
# )
# mycursor=mydb.cursor()

# sql='INSERT INTO customerss (name, address) VALUES(%s,%s)'
# val=('adhi','kzm12')
# mycursor.execute(sql,val)

# mydb.commit()


##select

# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='spectrum',
#     database='mydb'
# )
# mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM customerss")
# myrslt=mycursor.fetchall()
# for i in myrslt:
#     print(i)

##update

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='spectrum',
    database='mydb'
)
mycr=mydb.cursor()

sql="UPDATE  customerss SET name='adhithyan' WHERE name='adhi'"

mycr.execute(sql)
mydb.commit()

