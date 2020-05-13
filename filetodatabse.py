import mysql.connector

mdb=mysql.connector.connect(host='localhost',user='root',passwd='Anvijain@2305',auth_plugin='mysql_native_password',database='Demodata')

cur=mdb.cursor()
#cur.execute('Delete from Students')
#mdb.commit()

#cur.execute('ALTER TABLE Students ADD Gender varchar(10)')

with open('File5.csv','r') as fp:
    for line in fp:
        data=line.strip().split(',')
        cur.execute(f"INSERT INTO Students (Name,Course,Marks,Gender) VALUES ('{data[0]}','{data[2]}','{data[3]}','{data[1]}');")
     
        mdb.commit()    
          
cur.execute('Select * from Students')
for i in cur:
    print(i)
