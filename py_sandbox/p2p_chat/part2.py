'''
part 2 of ultimately building a p2p chat program. see part1.py for all details.
    Also next, will start working in a more object-oriented way.

'''

import socket, threading, sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0',10000))
        self.sock.listen(1)
    def handler(self,c,a):
        while True:
            data = c.recv(1024) # 1024 bytes max
            for connection in self.connections:
                connection.send(bytes(data)) # can only send bytes
            if not data:
                self.connections.remove(c)
                c.close()
                break
    def run(self):
        while True:
            c,a = self.sock.accept()
            cThread = threading.Thread(target=handler,args=(c,a))
            # allows you to close program even if threads still running
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

server = Server()
server.run()
