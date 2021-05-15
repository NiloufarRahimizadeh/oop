import pymysql


connection = pymysql.Connect(host='localhost', user='poulstar', password='poulstar', database='gpn')
sql = "Delete from users where email='niloufar'"

with connection.cursor() as cursor:
    cursor.execute(sql)