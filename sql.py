import mysql.connector

mdb=mysql.connector.connect(host='localhost',user='root',passwd='Anvijain@2305',auth_plugin='mysql_native_password',database='Demodata')

print(mdb)

cur=mdb.cursor()
#Fetching data
#cur.execute(" Select Course,Marks from Students where Marks>90 ")

#for i in cur:
    #print(i)

#Inserting Data
#cur.execute("Insert into Students (Name,Course,Marks) values ('Amjam1','SQL','75')")
cur.execute(" Select Name, Course, Marks from Students")

for i in cur:
    print(i)

#Commit all DML commands.
mdb.commit()

cur.execute('')