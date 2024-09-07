# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:52:25 2020

@author: jagannnnnnnnnnnnnnn
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
newprice=input("enter the new price of the book:")
cursor.execute("update book set Price='{}' where Book_id='{}'".format(newprice,bookid))
mycon.commit()
print("successfully updated")
mycon.close()
              