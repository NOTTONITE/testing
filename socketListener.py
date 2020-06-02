import socket
from threading import Thread

HEADER = 64
ADDR = ("127.0.0.1", 6620)
FORMAT = "utf-8"
DC_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handleClient(conn, addr):
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DC_MESSAGE:
                connected = False
            print(msg)
            if msg != "!DISCONNECT":
                pass
                # I want to do bot.get_guild(712425196241551360) but I have no way of getting bot
    conn.close()

def run():
    print("[STARTING] Socket Server is starting")
    server.listen()
    print(f"[SERVER] Server is listening")
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handleClient, args=(conn, addr))
        thread.start()

