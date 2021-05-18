import pymysql


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar')

try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE gpn')
finally:
    connection.close()