archive = open("file.txt",'r')
archive2 = open("code.txt",'w')
charFile = archive.read(1)

while charFile != "":
    if charFile.islower():
        code = ord(charFile)
        if code > 123: #si llega a la z cambiara a la a, que es 97 en ascii
            code-=26
        else:
            code+=1

        archive2.write(chr(code))
        
    else:
        archive2.write(charFile)
    charFile = archive.read(1)

archive.close()
archive2.close()

archive = open("code.txt",'r')
archive2 = open("decode.txt",'w')

charFile = archive.read(1)
while charFile != "":
    if charFile.islower():
        code = ord(charFile)
        if code < 96: #si llega a la a cambiara a la z, que es 97 en ascii
            code-=26
        else:
            code-=1

        archive2.write(chr(code))
    else:
        archive2.write(charFile)
    charFile = archive.read(1)

archive.close()
archive2.close()
