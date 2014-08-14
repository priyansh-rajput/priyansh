import MySQLdb
try:
    db=MySQLdb.connect("localhost","root","Promact2013","pythondb")
    cus=db.cursor()
    query="""create table student
            (
            id int primary key auto_increment,
            fname varchar(50),
            lname varchar(50),
            age int,
            rollno int,
            couse varchar(50))"""
    cus.execute("drop table student")
    cus.execute(query)
    print "Successfully student Table Created..!"
except Exception as e1:
    print e1.message
finally:
    db.close()
    
