import os

from bot import Bot

token = os.environ["tokens"]

if __name__ == '__main__':
    bot = Bot(token)
