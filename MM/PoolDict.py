import pymysql as mysql
def ConnectionPool():
    db=mysql.Connect(host='localhost',port=3306,user="root",password="DEVIL143@beer", db="mm")
    cmd=db.cursor(mysql.cursors.DictCursor)
    return (db,cmd)