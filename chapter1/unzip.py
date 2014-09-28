import zipfile


def extractFile(zFile, password):
    try:
        zFile.extracall(pwd=password)
        return password
    except:
        return


def main():
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open("dictonary.txt")
    for line in passFile.readlines():
        password = line.strip("\n")
        guess = extractFile(zFile, password)
        if guess:
            print"[+] PassWord = " + password + "\n"
            exit(0)


if __name__ == "__main__":
    main()
