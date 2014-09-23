import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(.5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        print str(e)
        return None


def checkVulns(banner):
    with open("vuln.txt", 'r') as f:
        for line in f.readlines():
            print line
            if line in banner:
                print "[+] Server is vulnerable" + banner.strip('\n')


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = "192.168.0." + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print "[+] " + ip + ": " + banner
                checkVulns(banner)


if __name__ == "__main__":
    main()
