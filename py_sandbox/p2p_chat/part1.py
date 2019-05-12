'''
want to build a simple p2p program that can allow two computers to "chat". can
    perhaps build upon in the future. will start with part one of a two part
    series, given by "howCode"

sources:
    part1: https://www.youtube.com/watch?v=DIPZoZheMTo
    part2: https://www.youtube.com/watch?v=D0SLpD7JvZI
    part3: https://www.youtube.com/watch?v=Rvfs6Xx3Kww

"threads" necessary to handle multiple connections at once
* want to create multiple threads to handle multiple clients at once.


KJGNOTE: this should be run on the "server"
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
