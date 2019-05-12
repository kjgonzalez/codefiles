'''
part 2 of ultimately building a p2p chat program. see part1.py for all details.
'''

import socket, threading, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp

sock.bind(('0.0.0.0',10000))

sock.listen(1)
connections = []

def handler(c,a):
    global connections # want global access
    while True:
        data = c.recv(1024) # 1024 bytes max
        for connection in connections:
            connection.send(bytes(data)) # can only send bytes
        if not data:
            connections.remove(c)
            c.close()
            break
while True:
    c,a = sock.accept()
    cThread = threading.Thread(target=handler,args=(c,a))
    cThread.daemon = True # allows you to close program even if threads still running
    cThread.start()
    connections.append(c)
    print(connections)
