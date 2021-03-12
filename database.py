import pymysql
import os

from models.user import User


class Connection(pymysql.connections.Connection):
    def __init__(self):
        self.host = os.environ["mysql_host"]
        self.user = os.environ["mysql_user"]
        self.password = os.environ["mysql_password"]
        self.db = os.environ["mysql_db"]


class Database:
    def __init__(self):
        connection_data = Connection()
        self.connection = pymysql.connect(
            host=connection_data.host,
            user=connection_data.user,
            password=connection_data.password,
            db=connection_data.db
        )

    def call_cursor(self):
        return self.connection.cursor()


class UserRequest:
    def __init__(self):
        self.database = Database()
        self.cursor = self.database.call_cursor()

    def get_user(self, id: int) -> User:
        self.cursor.execute(f"""SELECT vkid, thkruhm, sendStatus FROM users WHERE vkid={id};""")
        response = self.cursor.fetchone()
        user = User(response[0], response[1], response[2])
        return user

    def get_all_users(self) -> list:
        users = list()
        self.cursor.execute("""SELECT vkid, thkruhm, sendStatus FROM users;""")
        response = self.cursor.fetchall()
        for user in response:
            users.append(User(user[0], user[1], user[2]))
        return users

    def add_user(self, user: User):
        self.cursor.execute(
            f"INSERT INTO users(vkid, thkruhm, sendStatus) VALUES ({user.vkid}, {user.group}, {user.sender_status})")
        self.database.connection.commit()

    def update_user(self, user: User):
        self.cursor.execute(
            f"UPDATE users SET thkruhm = {user.group}, sendStatus = {user.sender_status} WHERE vkid = {user.vkid}")
        self.database.connection.commit()