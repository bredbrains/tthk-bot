from bot import Bot
import os

token = os.environ["token"]

if __name__ == '__main__':
    bot = Bot(token)
