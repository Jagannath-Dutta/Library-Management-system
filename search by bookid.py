 # -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:16:16 2020

@author: Sumedha Roy
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
bookid=input("enter book_id you want to search:")
cursor.execute("select * from book where Book_id='{}'".format(bookid))
data=cursor.fetchall()
for row in data:
    print(row)
mycon.close()
              