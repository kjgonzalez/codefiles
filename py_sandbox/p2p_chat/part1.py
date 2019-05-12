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

how to use:
on rpi:
    1. startup rpi
    2. ssh into rpi
    3. python3 part1.py
on local computer:
    1. use telnet to access rpi. recommended to use PuTTY

NOTE: if windows, you can use powershell command (must first be enabled) "telnet
    IPADDR PORT" ip address is same as used for ssh
NOTE: if dislike having immediate feedback, PuTTY can control this by going to
    "Terminal >> Local line editing" and selecting "Force on", which allows you
    to edit your text BEFORE hitting enter.
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
