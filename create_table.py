import pymysql


sql = """CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) """


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='gpn')


with connection.cursor() as cur:
    cur.execute(sql)

