import pymysql


class Connect_database():
    def do_connect():
        try:
            con = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='my_db_n')
            cur = con.cursor()
            print("Connected")
        except:
            print("Access denied!")
        return con, cur

