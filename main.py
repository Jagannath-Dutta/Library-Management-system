# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:18:35 2020

@author: jagan
"""

import mysql.connector as sqltor

mycon=sqltor.connect(host="localhost", 
                     user="root", 
                     password="root", 
                     database="sample", 
                     auth_plugin='mysql_native_password')
if mycon.is_connected:
    print ('Database connection successful')

cursor=mycon.cursor()

print("****WELCOME TO MY LIBRARY MANAGEMENT SYSTEM****")
print("-------------------")

userid=input("enter userid:")
password=input("enter password:")

sql="select * from login where userid='{}' and password='{}'".format(userid,password)

cursor.execute(sql)

result=cursor.fetchall()

if (result):
	print("login success")
    
else:
	print("login unsuccess")

if (result):
    print("1.insert\n2.display\n3.search by bookid\n4.search by bookname\n5.search by category\n6.bookissue\n7.bookreturn\n8.update price\n9.update quantity\n10.delete a record")
    ch=int(input("enter your choice"))
    if ch==1:
        bookid=input('Enter A Book ID: ') 
        bookname=input('Enter Book name: ') 
        authorname=input('Enter name od the author: ') 
        publishername=input('Enter the name of Publisher: ') 
        category=input('Enter Book Catergory(Subject wise): ') 
        price=input('Enter Price of the book: ') 
        quantity=input('Enter Quantity of the book: ') 
        sql1="Insert into book(Book_id,Book_Name,Author_Name,Publisher_Name,Category,Price,Quantity) values('{}','{}','{}','{}','{}','{}','{}')".format(bookid,bookname,authorname,publishername,category,price,quantity) 
        cursor.execute(sql1)
        mycon.commit()
        print('successfully inserted')
        mycon.close()
    elif ch==2:
        mycursor=mycon.cursor() 
        mycursor.execute("SELECT * FROM book") 
        myresult = mycursor.fetchall() 
        if myresult==[]:
            print('No such record found')
        if myresult!=[]:
            for row in myresult:
                print(row)
        mycon.commit()
        mycon.close()
    elif ch==3:
        cursor=mycon.cursor() 
        bookid=input("enter book_id you want to search:") 
        cursor.execute("select * from book where Book_id='{}'".format(bookid)) 
        data=cursor.fetchall()
        if data==[]:
            print('No such record found')
        if data!=[]:
            for row in data:
                print(row)
        mycon.commit()
        mycon.close()
    elif ch==4:
        cursor=mycon.cursor() 
        bookname=input("enter book_name you want to search:") 
        cursor.execute("select * from book where Book_Name='{}'".format(bookname)) 
        data=cursor.fetchall() 
        if data==[]:
            print('No such record found')
        if data!=[]:
            for row in data:
                print(row)
        mycon.commit()
        mycon.close()
    elif ch==5:
        cursor=mycon.cursor() 
        category=input("enter category of book you want to search:") 
        cursor.execute("select * from book where Category='{}'".format(category))
        data=cursor.fetchall()
        if data==[]:
            print('No such record found')
        if data!=[]:
            for row in data:
                print(row)
        mycon.commit()
        mycon.close()
    elif ch==6:
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
    elif ch==7:
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
        
        sql1="update book set Quantity=Quantity+1 where Book_id='{}'".format(bookid) 
        cursor.execute(sql1) 
        mycon.commit() 
        print("updated succesfully")
        mycon.close()
    elif ch==8:
        cursor=mycon.cursor() 
        bookid=input("enter the book_id you want to update:") 
        newprice=input("enter the new price of the book:") 
        cursor.execute("update book set Price='{}' where Book_id='{}'".format(newprice,bookid)) 
        mycon.commit() 
        print("successfully updated")
        mycon.close()
    elif ch==9:
        cursor=mycon.cursor() 
        bookid=input("enter the book_id you want to update:") 
        quan=input("enter the new no of quantity of the book:") 
        cursor.execute("update book set Quantity='{}' where Book_id='{}'".format(quan,bookid)) 
        mycon.commit() 
        print("successfully updated")
        mycon.close()
    elif ch==10:
        cursor=mycon.cursor() 
        bookid=input("enter the book_id you want to delete:") 
        cursor.execute("delete from book where Book_id='{}'".format(bookid)) 
        mycon.commit() 
        print("successfully deleted")
        mycon.close()
    else:
        print("Wrong Choice")

print("------THANK  YOU------")
mycon.close()    
 

    
	



