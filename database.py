import pymysql
import os

from models.user import User


class Database:
    def __init__(self):
        self.mysql_connection = {
            "host": os.environ["mysql_host"],
            "user": os.environ["mysql_user"],
            "password": os.environ["mysql_password"],
            "database": os.environ["mysql_db"]
        }
        self.connection = pymysql.connect(
            host=self.mysql_connection["host"],
            user=self.mysql_connection["user"],
            password=self.mysql_connection["password"],

        )

    def call_cursor(self):
        return self.connection.cursor()


class UserRequest(User):
    def __init__(self):
        self.database = Database()
        self.cursor = self.database.call_cursor()

    def get_user(self, id) -> User:
        self.cursor.execute(f"""SELECT vkid, thkruhm, sendStatus FROM users WHERE vkid={id};""")
        response = self.cursor.fetchone()
        user = User(response["vkid"], response["thkruhm"], response["sendStatus"])
        return user

    def get_all_users(self) -> list:
        users = list()
        self.cursor.execute("""SELECT vkid, thkruhm, sendStatus FROM users;""")
        response = self.cursor.fetchall()
        for user in response:
            users.append(User(user["vkid"], user["thkruhm"], user["sendStatus"]))
        return users
