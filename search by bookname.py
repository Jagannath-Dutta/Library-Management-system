# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:59:53 2020

@author: jagan
"""

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", 
                     user="root", 
                     password="root", 
                     database="sample", 
                     auth_plugin='mysql_native_password')
if mycon.is_connected:
    print("sucessfully connected")
cursor=mycon.cursor()
bookname=input("enter book_name you want to search:")
cursor.execute("select * from book where Book_Name='{}'".format(bookname))
data=cursor.fetchall()
for row in data:
    print(row)
mycon.close()