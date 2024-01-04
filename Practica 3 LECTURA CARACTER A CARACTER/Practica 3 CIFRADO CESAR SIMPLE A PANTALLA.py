archive = open("file",'r')

charFile = archive.read(1)

while charFile != "":
    if charFile.islower():
        code = ord(charFile)
        if code > 123: #si llega a la z cambiara a la a, que es 97 en ascii
            code-=26
        else:
            code+=1

        print(chr(code), end='')
    else:
        print(charFile, end='')
    charFile = archive.read(1)

archive.close()

