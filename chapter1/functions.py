import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        print str(e)
        return None


def checkVulns(banner):
    if "FreeFloat Ftp Server (Version 1.00)" in banner:
        print "[+] FreeFloat FTP Server is vulnerable"
    elif "3Com 3CDeamon FTP Server Version 2.0" in banner:
        print "[+] 3Com 3CDeamon FTP Server Version 2.0 is vulnerable"
    else:
        print "[-] FTP Server is not vulnerable"


def main():
    ip1 = "127.0.0.1"
    ip2 = "127.0.0.2"
    ip3 = "127.0.0.3"
    ip4 = "127.0.0.4"
    port = 21
    banner1 = retBanner(ip1, port)
    banner2 = retBanner(ip2, port)
    banner3 = retBanner(ip3, port)
    banner4 = retBanner(ip4, port)
    if banner1:
        print "[+] " + ip1 + ": " + banner1.strip("\n")
        checkVulns(banner1)
    if banner2:
        print "[+] " + ip2 + ": " + banner2.strip("\n")
        checkVulns(banner2)


if __name__ == "__main__":
    main()
