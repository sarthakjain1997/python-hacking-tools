import socket

socket.setdefaulttimeout(2)

s = socket.socket()
s.connect(('127.0.0.1', 3001))
banner = s.recv(1024)

if "FreeFloat Ftp Server (Version 1.00)" in banner:
    print "[+] FreeFloat FTP Server is vulnerable"
elif "3Com 3CDeamon FTP Server Version 2.0" in banner:
    print "[+] 3Com 3CDeamon FTP Server Version 2.0 is vulnerable"
else:
    print "[-] FTP Server is not vulnerable"
