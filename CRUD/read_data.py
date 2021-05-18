import pymysql


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='data_base')


sql = "SELECT * from `users` "

with connection.cursor() as cr:
    cr.execute(sql)
    result = cr.fetchall()
    print(result)