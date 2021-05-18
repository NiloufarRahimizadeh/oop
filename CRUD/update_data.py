import pymysql


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='data_base')


sql = "UPDATE users SET `password`='nil' WHERE  `email`='niloufarrahimizade@yahoo.com'"

with connection.cursor() as cr:
    cr.execute(sql)
    connection.commit()
    connection.close()