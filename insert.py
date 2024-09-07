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
bookname=input('Enter Book name: ') 
authorname=input('Enter name od the author: ') 
publishername=input('Enter the name of Publisher: ') 
category=input('Enter Book Catergory(Subject wise): ')
price=input('Enter Price of the book: ')
quantity=input('Enter Quantity of the book: ')



sql="Insert into book(Book_id,Book_Name,Author_Name,Publisher_Name,Category,Price,Quantity) values('{}','{}','{}','{}','{}','{}','{}')".format(bookid,bookname,authorname,publishername,category,price,quantity)

cursor.execute(sql)
mycon.commit()
mycon.close()

 
