import zipfile
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extracall(pwd=password)
        print"[+] PassWord = " + password + "\n"
    except:
        pass


def main():
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open("dictonary.txt")
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == "__main__":
    main()
