# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:55:18 2020

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


 
bookid=input('Enter the Book ID: ') 
roll=input('Enter Roll: ') 
Class=input('Enter Class: ') 
studentname=input('Enter Student name: ') 
returndate=input('Enter Return date: ')



sql="Insert into return1(Book_id,Roll,Class,Name,Return_date) values('{}','{}','{}','{}','{}')".format(bookid,roll,Class,studentname,returndate)

cursor.execute(sql)
mycon.commit()
print("inserted succesfully")
sql1="update book set Quantity=Quantity-1 where Book_id='{}'".format(bookid)
cursor.execute(sql1)
mycon.commit()
print("updated succesfully")
mycon.close()
