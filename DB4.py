import pymysql

def connect():
    return pymysql.connect(host="localhost", user="root", password="123", database="mytest")

def welcomeInterface():
    print("What do you want to do? 1.Add 2.Delete 3.Update 4.Select 5.Quit.",end=' ')

def handleCommand(command):
    if("1" == command):
        add()
        return
    if("2" == command):
        delete()
        return
    if("3" == command):
        update()
        return
    if("4" == command):
        select()
        return
    print("err: Comand error.")

def add():
    try:
        db = connect()
        cursor = db.cursor()
    except:
        print("err: Connect error")
        return
    
    TID = input("Please input TID:") or ""
    TNAME = input("Please input TNAME:") or ""
    TDEPT = input("Please input TDEPT:") or ""
    TAGE = input("Please input TAGE(0<TAGE<=200):") or ""
    TGENDER = input("Please input TGENDER(M or F):") or ""
    sql = "INSERT INTO teacher(TID,TNAME,TDEPT,TAGE,TGENDER) VALUES(%s,%s,%s,%s,%s);"
    try:
        cursor.execute(sql, [TID,TNAME,TDEPT,TAGE,TGENDER])
        db.commit()
        print("Insert done.")
    except pymysql.Error as e:
        print("err: Run error")
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()


def delete():
    try:
        db = connect()
        cursor = db.cursor()
    except:
        print("err: Connect error")
        return
    
    deleteStandard = input("Delete according to? 1.TID 2.TNAME 3.TDEPT 4.TAGE 5.TGENDER 6.All data:")
    if("1" == deleteStandard):
        TID = input("Please input TID:")
        sql = "DELETE FROM teacher where TID='" + TID + "';"
    if("2" == deleteStandard):
        TNAME = input("Please input TNAME:")
        sql = "DELETE FROM teacher where TNAME='" + TNAME + "';"
    if("3" == deleteStandard):
        TDEPT = input("Please input TDEPT:")
        sql = "DELETE FROM teacher where TDEPT='" + TDEPT + "';"
    if("4" == deleteStandard):
        TAGE = input("Please input TAGE:")
        sql = "DELETE FROM teacher where TAGE='" + TAGE + "';"
    if("5" == deleteStandard):
        TGENDER = input("Please input TGENDER:")
        sql = "DELETE FROM teacher where TGENDER='" + TGENDER + "';"
    if("6" == deleteStandard):
        sql = "DELETE FROM teacher;"
    
    try:
        cursor.execute(sql)
        db.commit()
        print("Delete done.")
    except pymysql.Error as e:
        print("err: Run error")
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()


def update():
    try:
        db = connect()
        cursor = db.cursor()
    except:
        print("err: Connect error")
        return
    
    originDataField = input("What data you want to change? 1.TID 2.TNAME 3.TDEPT 4.TAGE 5.TGENDER:")
    if("1" == originDataField):
        originDataField = "TID"
    if("2" == originDataField):
        originDataField = "TNAME"
    if("3" == originDataField):
        originDataField = "TDEPT"
    if("4" == originDataField):
        originDataField = "TAGE(0<AGE<=200)"
    if("5" == originDataField):
        originDataField = "TGENDER(F or M)"

    newData = input("Set " + originDataField + " to?")

    updateStandard = input("Set " + originDataField + " to " + newData + " according to?1.TID 2.TNAME 3.TDEPT 4.TAGE 5.TGENDER 6.All data.")
    if("1" == updateStandard):
        TID = input("Please input TID:")
        sql = "UPDATE teacher set " + originDataField + "='" + newData + "' WHERE TID='" + TID + "';"
    if("2" == updateStandard):
        TNAME = input("Please input TNAME:")
        sql = "UPDATE teacher set " + originDataField + "='" + newData + "' WHERE TNAME='" + TNAME + "';"
    if("3" == updateStandard):
        TDEPT = input("Please input TDEPT:")
        sql = "UPDATE teacher set " + originDataField + "='" + newData + "' WHERE TDEPT='" + TDEPT + "';"
    if("4" == updateStandard):
        TAGE = input("Please input TAGE(0<AGE<=200):")
        sql = "UPDATE teacher set " + originDataField + "='" + newData + "' WHERE TAGE='" + TAGE + "';"
    if("5" == updateStandard):
        TGENDER = input("Please input TGENDER(F or M):")
        sql = "UPDATE teacher set " + originDataField + "='" + newData + "' WHERE TGENDER='" + TGENDER + "';"
    if("6" == updateStandard):
        sql = sql = "UPDATE teacher set " + originDataField + "='" + newData + "';"
    
    try:
        cursor.execute(sql)
        db.commit()
        print("Update done.")
    except pymysql.Error as e:
        print("err: Run error")
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()

def select():
    try:
        db = connect()
        cursor = db.cursor()
    except:
        print("err: Connect error")
        return
    
    selectDataField = input("Which data you want to select? 1.TID 2.TNAME 3.TDEPT 4.TAGE 5.TGENDER 6.All data:")
    if("1" == selectDataField):
        selectDataField = "TID"
    if("2" == selectDataField):
        selectDataField = "TNAME"
    if("3" == selectDataField):
        selectDataField = "TDEPT"
    if("4" == selectDataField):
        selectDataField = "TAGE"
    if("5" == selectDataField):
        selectDataField = "TGENDER"
    if("6" == selectDataField):
        selectDataField = "*"

    selectStandard = input("Select " + selectDataField + " according to?1.TID 2.TNAME 3.TDEPT 4.TAGE 5.TGENDER 6.All data.")
    if("1" == selectStandard):
        TID = input("Please input TID:")
        sql = "SELECT " + selectDataField + " FROM teacher WHERE TID='" + TID + "';"
    if("2" == selectStandard):
        TNAME = input("Please input TNAME:")
        sql = "SELECT " + selectDataField + " FROM teacher WHERE TNAME='" + TNAME + "';"
    if("3" == selectStandard):
        TDEPT = input("Please input TDEPT:")
        sql = "SELECT " + selectDataField + " FROM teacher WHERE TDEPT='" + TDEPT + "';"
    if("4" == selectStandard):
        TAGE = input("Please input TAGE(0<AGE<=200):")
        sql = "SELECT " + selectDataField + " FROM teacher WHERE TAGE='" + TAGE + "';"
    if("5" == selectStandard):
        TGENDER = input("Please input TGENDER(F or M):")
        sql = "SELECT " + selectDataField + " FROM teacher WHERE TGENDER='" + TGENDER + "';"
    if("6" == selectStandard):
        sql = "SELECT " + selectDataField + " FROM teacher;"
    
    try:
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except pymysql.Error as e:
        print("err: Run error")
        print(e.args[0], e.args[1])
    cursor.close()
    db.close()

if __name__ == "__main__":
    while(True):
        welcomeInterface()
        
        command = input()
        if("5" == command):
            print("Thanks for using, bye!")
            break
        else:
            handleCommand(command)