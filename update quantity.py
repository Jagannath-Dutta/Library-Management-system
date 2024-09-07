# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:27:46 2021

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
bookid=input("enter the book_id you want to update:")
quan=input("enter the new no of quantity of the book:")
cursor.execute("update book set Quantity='{}' where Book_id='{}'".format(quan,bookid))
mycon.commit()
print("successfully updated")
mycon.close()