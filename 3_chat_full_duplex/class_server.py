import socket
import select


class Server:
    def __init__(self):
        self.sock = socket.socket()

    def start_server(self):
        self.sock.setblocking(0)
        self.sock.bind(('', 12347))
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


if __name__ == '__main__':
    server = Server()
    server.start_server()
