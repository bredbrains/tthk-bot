import os

import pymysql

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

    def cursor(self):
        return self.connection.cursor()


class UserRequest:
    def __init__(self):
        self.database = Database()
        self.cursor = self.database.call_cursor()

    def get_user(self, id: int) -> User:
        self.cursor.execute(f"""SELECT vkid, school_group, sender_status FROM users WHERE vkid={id};""")
        response = self.cursor.fetchone()
        user = User(response[0], response[1], response[2])
        return user

    def get_all_users(self) -> list:
        users = list()
        self.cursor.execute("""SELECT vkid, school_group, sender_status FROM users;""")
        response = self.cursor.fetchall()
        for user in response:
            users.append(User(user[0], user[1], user[2]))
        return users

    def add_user(self, user: User):
        self.cursor.execute(
            f"INSERT INTO users(vkid, school_group, sender_status) VALUES ({user.vkid}, {user.group}, {user.sender_status})")
        self.database.connection.commit()

    def update_user(self, user: User):
        try:
            self.cursor.execute(
                f"UPDATE users SET school_group = {user.group}, sender_status = {user.sender_status} WHERE vkid = {user.vkid}")
            self.database.connection.commit()
        except:
            self.add_user(user)

    def update_group(self, user: User):
        try:
            self.cursor.execute(
                f"UPDATE users SET school_group = {user.group} WHERE vkid = {user.vkid}")
            self.database.connection.commit()
        except:
            self.add_user(user)

    def update_sender_status(self, user: User):
        try:
            self.cursor.execute(
                f"UPDATE users SET sender_status = {user.sender_status} WHERE vkid = {user.vkid}")
            self.database.connection.commit()
        except:
            self.add_user(user)
