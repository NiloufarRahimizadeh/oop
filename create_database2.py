import pymysql

connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar')


with connection.cursor() as cr:
    cr.execute("CREATE DATABASE data_base")

    
