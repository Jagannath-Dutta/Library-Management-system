# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:11:07 2020

@author: jagan
"""

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", 
                     user="root", 
                     password="root", 
                     database="sample", 
                     auth_plugin='mysql_native_password')
if mycon.is_connected:
    print ('Successfully connected')

cursor=mycon.cursor()



bookid=input('Enter A Book ID: ') 
roll=input('Enter Roll: ') 
Class=input('Enter Class: ') 
studentname=input('Enter Student name: ') 
issuedate=input('Enter Issue date: ')



sql="Insert into issue1(Book_id,Roll,Class,Name,Issue_Date) values('{}','{}','{}','{}','{}')".format(bookid,roll,Class,studentname,issuedate)

cursor.execute(sql)
mycon.commit()
print("inserted succesfully")
sql1="update book set Quantity=Quantity-1 where Book_id='{}'".format(bookid)
cursor.execute(sql1)
mycon.commit()
print("updated succesfully")
mycon.close()

 
