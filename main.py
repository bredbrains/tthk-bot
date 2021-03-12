import os

from bot import Bot

token = os.environ["token"]

if __name__ == '__main__':
    bot = Bot(token)
