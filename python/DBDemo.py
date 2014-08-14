import MySQLdb
try:
    #connect with database
    db=MySQLdb.connect("localhost","root","Promact2013","pythondb")
    if not db:
        print "database does not connected..!"
    else:
        print "database successfully Connected...!"
        #create cursor object using cursor() method.
        cus=db.cursor()
        #execute sql Query usin execute()
        cus.execute("select version()")
        #fetch single row using fetchone()
        data=cus.fetchone()
        print "fetch Output::",data
        #close the Connection
        cus.close()
except Exception as e2:
    print e2.message 
