import socket
import threading


class Client:

    def __init__(self):
        self.sock = socket.socket()
        self.CACHE = ''

    def recive_message(self):
        while True:
            with open('chats.txt', 'r') as data:
                data = data.read().splitlines()[-1]
                if data != self.CACHE:
                    print('~', data)
                    self.CACHE = data

    def user_message(self):
        message = input("> ")
        self.CACHE = message
        self.send_message(message.encode())

    def send_message(self, message):
        self.sock.connect(('127.0.0.1', 12347))
        self.sock.send(message.encode())
        self.close_socket()

    def close_socket(self):
        self.sock.close()


if __name__ == '__main__':
    client = Client()
    while True:
        threading.Thread(target=client.recive_message(),
                         args=()).start()
        client.recive_message()
