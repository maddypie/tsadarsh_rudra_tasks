import socket
import time
import threading


prev = ''

def client():
    global prev

    s = socket.socket()
    s.connect(('127.0.0.1', 1235))

    def writer():
        global prev

        while True:
            with open('chats.txt', 'r') as r:
                data = r.read()
                if data != prev:
                    print(data)
                    prev = data
            time.sleep(1)

    threading.Thread(target=writer, args=()).start()
    while True:
        message = input("> ")
        prev = message
        s.send(message.encode())

    s.close()


if __name__ == '__main__':
    client()
