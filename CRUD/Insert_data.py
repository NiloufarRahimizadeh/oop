import pymysql 


connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='data_base')



with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('niloufarrahimizade@yahoo.com', 'very-secret'))

# connection is not autocommit by default. So you must commit to save
# your changes.
connection.commit()


