# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:24:43 2020

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
category=input("enter category of book you want to search:")
cursor.execute("select * from book where Category='{}'".format(category))
data=cursor.fetchall()
for row in data:
    print(row)
mycon.close()
              