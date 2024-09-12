import pymssql

conn = pymssql.connect(host = '127.0.0.1',user='sa',password='zfy@12345',database='Demo001')
cursor = conn.cursor()

cursor.execute('select * from MyTable')
mylist = cursor.fetchall()

print(mylist)