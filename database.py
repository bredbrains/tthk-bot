import pymysql
import os

class Database:
    def __init__(self):
        self.mysql_connection = {
            "host": os.environ["mysql_host"],
            "login": os.environ["mysql_login"],
            "password": os.environ["mysql_password"],
            "database": os.environ["mysql_db"]
        }