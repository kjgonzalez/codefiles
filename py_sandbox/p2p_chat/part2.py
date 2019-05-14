'''
part 2 of ultimately building a p2p chat program. see part1.py for all details.
    Also next, will start working in a more object-oriented way.

'''

import socket, threading,sys
import argparse

if(sys.version_info[0]!=3):
    raise Exception('Please use python3. exiting.')

p=argparse.ArgumentParser()
p.add_argument('--server',default=False,action='store_true',help='run as server')
p.add_argument('--ip',type=str,help='server ip address (as client)')

args=p.parse_args()

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
            cThread = threading.Thread(target=self.handler,args=(c,a))
            # allows you to close program even if threads still running
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp
    def __init__(self,address):
        self.sock.connect((address,10000))

        # want input and output threads
        iThread = threading.Thread(target = self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data=self.sock.recv(1024)
            if not data:
                break
            print(data)
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""),'utf-8'))

if(args.server):
    server = Server()
    server.run()
else:
    client = Client(args.ip)
