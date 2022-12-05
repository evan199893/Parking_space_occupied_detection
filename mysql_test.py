import pymysql

def writetoDB_korea(time_stamp, avalible, occupied):
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "ttv021015",
        "db": "parking_lot",
        "charset": "utf8"
    }
    
    db = pymysql.connect(**db_settings)
    cursor = db.cursor()
    #sql = "INSERT INTO information_table(name, time_stamp, avalible, occupied) VALUES ('Korea_1','2022-6-21_firt', 5, 7)"
    #sql = "INSERT INTO information_table(name, time_stamp, avalible, occupied) VALUES ('Japan_1','2022-6-21_firt', 7, 7)"
    command1 = "UPDATE information_table SET time_stamp = %s WHERE id = 2"
    command2 = "UPDATE information_table SET avalible = %s WHERE id = 2"
    command3 = "UPDATE information_table SET occupied = %s WHERE id = 2"
    command4 = "UPDATE information_table SET name = %s WHERE id = 2"
    command5 = "UPDATE information_table SET total = 18 WHERE id = 2"
    #command = "DELETE FROM information_table WHERE id = 1"
    
    try:
        cursor.execute(command1, time_stamp)
        db.commit()
        cursor.execute(command2, int(avalible))
        db.commit()
        cursor.execute(command3, int(occupied))
        db.commit()
        cursor.execute(command4, ('Korea, Gyeonggi-Do'))
        db.commit()
        cursor.execute(command5)
        db.commit()
        print('success')
    
    
    
    except Exception as ex:
        db.rollback()
        print(ex)
    
    db.close()

def writetoDB_japan(time_stamp, avalible, occupied):
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "ttv021015",
        "db": "parking_lot",
        "charset": "utf8"
    }
    
    db = pymysql.connect(**db_settings)
    cursor = db.cursor()
    #sql = "INSERT INTO information_table(name, time_stamp, avalible, occupied) VALUES ('Korea_1','2022-6-21_firt', 5, 7)"
    #sql = "INSERT INTO information_table(name, time_stamp, avalible, occupied) VALUES ('Japan_1','2022-6-21_firt', 7, 7)"
    command1 = "UPDATE information_table SET time_stamp = %s WHERE id = 3"
    command2 = "UPDATE information_table SET avalible = %s WHERE id = 3"
    command3 = "UPDATE information_table SET occupied = %s WHERE id = 3"
    command4 = "UPDATE information_table SET name = %s WHERE id = 3"
    command5 = "UPDATE information_table SET total = 7 WHERE id = 3"
    #command = "DELETE FROM information_table WHERE id = 1"
    
    try:
        cursor.execute(command1, time_stamp)
        db.commit()
        cursor.execute(command2, int(avalible))
        db.commit()
        cursor.execute(command3, int(occupied))
        db.commit()
        cursor.execute(command4, ('Japan, Osaka'))
        db.commit()
        cursor.execute(command5)
        db.commit()
        print('success')
    
    
    
    except Exception as ex:
        db.rollback()
        print(ex)
    
    db.close()