'''
part 2 of ultimately building a p2p chat program. see part1.py for all details.
    Also next, will start working in a more object-oriented way.

'''

import socket, threading,sys
import argparse
import time
import numpy as np

if(sys.version_info[0]!=3):
    raise Exception('Please use python3. exiting.')

p=argparse.ArgumentParser()
p.add_argument('--server',default=False,action='store_true',help='run as server')
p.add_argument('--ip',type=str,help='server ip address (as client)')
p.add_argument('--matrix_demo',default=False,action='store_true',help='transmit & receive matrix data')

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
                connection.send(bytes(data,'utf-8')) # can only send bytes
            if not data:
                print(str(a[0])+':'+str(a[1]),'disconnected')
                self.connections.remove(c)
                c.close()
                break
    def h2(self,c,a):
        while True:
            data=bytes('here','utf-8')
            rand_arr=np.array(np.random.rand(3,3)*10,int)
            arr_bytes=rand_arr.tobytes()
            for connection in self.connections:
                connection.send(bytes(arr_bytes))
            if not data:
                print(str(a[0])+':'+str(a[1]),'disconnected')
                self.connections.remove(c)
                c.close()
                break
            time.sleep(1) # wait a second before sending next packet

    def run(self):
        while True:
            c,a = self.sock.accept()
            if(args.matrix_demo):
                # special case
                cThread = threading.Thread(target=self.h2,args=(c,a))
            else:
                # normal operation (per video)
                cThread = threading.Thread(target=self.handler,args=(c,a))
            # allows you to close program even if threads still running
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0])+':'+str(a[1]),'connected')

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
            if(args.matrix_demo):
                # special case
                print('new data:')
                arr=np.frombuffer(data,dtype=int).reshape((3,3))
                print(arr)
            else:
                # normal operation
                print(data)
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""),'utf-8'))

if(args.server):
    server = Server()
    server.run()
else:
    client = Client(args.ip)
