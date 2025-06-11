'''
Python MySQL Connector
It is a python driver that helps to integrate Python and MySQL.
'''

# Connecting to MySQL Server
#importing required libraries
import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='College'
)

#preparing a cursor object
cursorobj=dataBase.cursor()

#creatting a database
'''cursor.execute("CREATE DATABASE College")'''

#creating a table
'''StudentRec="""CREATE TABLE STUDENT(NAME VARCHAR(20) NOT NULL, SECTION VARCHAR(10), ID INT NOT NULL)"""
cursorobj.execute(StudentRec)'''

#inserting single row into table
'''sql = "INSERT INTO STUDENT (NAME, SECTION, ID) VALUES (%s, %s, %s)" # In  mysql.connector %s is the placeholder used for all data types including strings, integers, floats, etc.
val = ("Ngima", "CG10", 10)
cursorobj.execute(sql, val)
dataBase.commit()
dataBase.close()'''

#inserting multiple rows into table
'''sql="INSERT INTO STUDENT( NAME,SECTION,ID) VALUES (%s,%s,%s)"
val=[("Rabi","CG10",20),("Rosi","CG11",30),("Numa","CG12",40)]
cursorobj.executemany(sql,val)
dataBase.commit() '''

#Select data from MySQL table using Python
'''query="SELECT * FROM STUDENT"
cursorobj.execute(query)
result=cursorobj.fetchall()
for x in result:
    print(x)'''

#Select all data from MySQL table using Python
'''query="SELECT * FROM STUDENT where ID >=20"
cursorobj.execute(query)
result=cursorobj.fetchall()
print(result)'''

#updating the data from table
'''query="UPDATE STUDENT SET ID= 35 WHERE NAME='Numa'"
cursorobj.execute(query)
dataBase.commit() #to save changes
result=cursorobj.fetchall()
print(result)'''

#deleting the data from table
'''query="DELETE FROM STUDENT WHERE NAME='Numa'"
cursorobj.execute(query)
dataBase.commit() #to save changes
print(cursorobj.fetchall())'''

#drop table
'''query="DROP TABLE STUDENT"
cursorobj.execute(query)
dataBase.commit()'''

#check
query="SHOW TABLES"
cursorobj.execute(query)
print(cursorobj.fetchall())
dataBase.close()