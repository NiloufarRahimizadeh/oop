import pymysql


connection = pymysql.connect(host='localhost', user = 'poulstar', password='poulstar', database='data_base')
sql = "INSERT INTO `users` (`name`, `email`) VALUE (%s, %s)"

data = ("nilo", "nilourz1993@gmail.com")

with connection.cursor() as cr:
    cr.execute(sql, data)
    connection.commit()