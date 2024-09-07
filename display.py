# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:41:50 2020

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

mycursor=mycon.cursor()

mycursor.execute("SELECT * FROM book")

myresult = mycursor.fetchall()

for row in myresult:
  print(row)

mycon.close()
