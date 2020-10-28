import socket
import select


def server():
    s = socket.socket()

    s.setblocking(0)

    s.bind(('', 1235))
    s.listen(5)
    print('Server starting...')

    inputs = [s]
    outputs = []
    while True:
        readable, writable, erros = select.select(inputs, outputs, inputs)
        for i in readable:
            if i is s:
                conn1, addr1 = i.accept()
                inputs.append(conn1)
            else:
                data1 = i.recv(1024)
                if data1:
                    msg = "server: " + data1.decode()
                    i.sendall(msg.encode())

                    with open('chats.txt', 'w') as r:
                        r.write(data1.decode())

                    print(">", data1.decode())
                    # conn1.send(data1)
                else:
                    inputs.remove(i)
                    i.close()


if __name__ == '__main__':
    server()
