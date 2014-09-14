#
# TCP socket client
#

import socket


socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(('127.0.0.1', 3001))
print "connection socket ip: localhost port:3001"
banner = s.recv(1024)
print banner
