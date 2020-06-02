import socketListener
import init
from threading import Thread

with open("token.txt") as f: token = f.readline()

Thread(target=socketListener.run).start()
init.bot.run(token)
