"""
try:
    print "[+] 1337/0 = " + str(1337/0)
except Exception, e:
    print e
    print "[-] Error."
"""

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("127.0.0.1", 21))
except Exception, e:
    print "[-] Error = " + str(e)
