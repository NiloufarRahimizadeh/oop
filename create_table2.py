import pymysql


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='data_base')

sql ='''CREATE TABLE `users`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255),
    `email` varchar(255),
    PRIMARY KEY(`id`)
    )'''

with connection.cursor() as cr:
    cr.execute(sql)