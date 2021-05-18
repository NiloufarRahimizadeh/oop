import pymysql
from create_connector import Connect_database




sql = """CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) COLLATE utf8_bin NOT NULL,
    `family` varchar(255) COLLATE utf8_bin NOT NULL,
    `age` varchar(255) COLLATE utf8_bin NOT NULL,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) """

con, cur = Connect_database.do_connect()
cur.execute(sql)

