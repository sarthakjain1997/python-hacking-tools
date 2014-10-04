import argparse

parser = argparse.ArgumentParser(u"port scan")

parser.add_argument('-H', "--host", type=str, help=u"target host")
parser.add_argument('-p', "--port", type=int, help=u"target port")

args = parser.parse_args()
host = args.host
port = args.port

if host is None or port is None:
    pass
    exit(0)
