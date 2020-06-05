import pymysql

def connect():
    con = pymysql.connect(host="localhost", user="root", password="123", database="mytest")
    return con

if __name__ == "__main__":
    db = connect()
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchall()
    db.close()