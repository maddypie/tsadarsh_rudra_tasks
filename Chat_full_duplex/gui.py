import tkinter as tk
from tkinter import ttk
import threading
import time
import socket
import select

# from class_server import Server
# from class_client import Client


class Server:
    def __init__(self):
        self.sock = socket.socket()

    def start_server(self):
        self.sock.setblocking(0)
        self.sock.bind(('', 12346))
        self.sock.listen(5)
        inputs = [self.sock]

        while True:
            readable, writable, exceptions = select.select(inputs, [], inputs)
            for s in readable:
                if s is self.sock:
                    conn, addr = s.accept()
                    inputs.append(conn)
                else:
                    data = s.recv(1024)
                    if data:
                        self.write_to_file(data.decode())
                        print(data.decode())
                    else:
                        inputs.remove(s)
                        s.close()

    def write_to_file(self, data):
        with open('chats.txt', 'a') as content:
            content.write(data)
        return


class Client:

    def __init__(self):
        self.sock = socket.socket()

    def recive_message(self):
        message = input("> ")
        self.send_message(message)

    def send_message(self, message):
        self.sock.connect(('127.0.0.1', 12346))
        self.sock.send(message.encode())
        self.close_socket()

    def close_socket(self):
        self.sock.close()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.server = Server()
        self.client = Client()
        self.CHAT_HIS = tk.StringVar(value=[])
        self.MESSAGE = tk.StringVar(value='write here..')
        self.make_window()
        threading.Thread(target=self.start_server(),
                         args=()).start()
        print('hi')
        threading.Thread(target=self.update_chat_history(),
                         args=()).start()

    def start_server(self):
        self.server.start_server()

    def make_window(self):
        mainframe = ttk.Frame(self)
        self.make_chatspace(mainframe)
        self.make_message_box(mainframe)
        self.make_send_button(mainframe)
        mainframe.grid()

    def make_chatspace(self, root):
        chatspace = tk.Entry(root, textvariable=self.CHAT_HIS)
        chatspace.grid(row=0, rowspan=3, column=0, columnspan=2,
                       sticky='nsew')

    def make_message_box(self, root):
        message_box = ttk.Entry(root, textvariable=self.MESSAGE)
        message_box.grid(row=3, column=0, sticky='nsew')

    def make_send_button(self, root):
        message = self.MESSAGE.get()
        send_button = ttk.Button(root, text='Send',
                                 command=lambda: self.send_message(message))
        send_button.grid(row=3, column=1, sticky='nsew')

    def send_message(self, message):
        self.client.send_message(message)

    def update_chat_history(self):
        while True:
            with open('chat.txt', 'r') as content:
                data = content.read()
            self.CHAT_HIS.set(data)
            time.sleep(0.5)


if __name__ == '__main__':
    instance = App()
    instance.mainloop()
