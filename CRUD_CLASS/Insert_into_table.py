import pymysql
from create_connector import Connect_database

class Create():
    def __init__(self, name=None, family=None, age=None, email=None):
        self.name = name
        self.family = family
        self.age = age
        self.email = email
    def do_create(self):
        try:
            con, cur = Connect_database.do_connect()
            query = "INSERT INTO users (name, family, age, email) VALUES (%s, %s, %s, %s)"
            data = (self.name, self.family, self.age, self.email)
            cur.execute(query, data)
            con.commit()
            print("Created")
        except:
            print("Not Created!")



