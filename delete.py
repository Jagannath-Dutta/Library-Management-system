# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:27:06 2020

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
bookid=input("enter the book_id you want to delete:")
cursor.execute("delete from book where Book_id='{}'".format(bookid))
mycon.commit()
print("successfully deleted")
mycon.close()
              