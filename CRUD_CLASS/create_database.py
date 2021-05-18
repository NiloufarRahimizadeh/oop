import pymysql


class Creat_Database:
    def do_create():
        con = pymysql.connect(host='localhost', user='poulstar', password='poulstar')

        try:
            with con.cursor() as cr:
                cr.execute("CREATE DATABASE my_db_n")
        except:
            print("Access denied!")
        finally:
            cr.close()

Creat_Database.do_create()