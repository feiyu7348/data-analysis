#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymssql

conn=pymssql.connect(host='127.0.0.1',user='sa',password='Admin@123456',database='Temp202011170818identity')
cursor=conn.cursor()

cursor.execute('select * from ZzzScoreSet')
myList=cursor.fetchall()
print(myList)

for i in range(1,11):
    myTime=str(i)
    myScore=str(60+i)
    mySql="insert into ZzzScoreSet(Time,Score) Values (%s,%s)"
    myValues=(myTime,myScore)
    cursor.executemane(mySql,myValues)
    com.commit()


cursor.execute('select * from ZzzScoreSet')
myList=cursor.fetchall()
print(myList)