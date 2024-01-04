#archivo = open("file.txt",'r')
#caracter= archivo.read(1)
#contador=1
#while caracter != "":
#    caracter =archivo.read(1)
#    contador=contador + 1

#print("contador: ",contador)
#archivo.close()
caracter= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def isLowerCase (charFile):
    contador=-1
    for char in caracter:
        contador += 1
        if char == charFile:
            if char == 'z':
                return 0
            else:
                return contador+1
    
    return -1

#ord, chr
archive = open("file",'r')

charFile = archive.read(1)
indice = isLowerCase(charFile)
while charFile != "":
    if indice != -1:
        print(caracter[indice],end="")
    else:
        print(charFile,end="")
        
    charFile = archive.read(1)
    indice = isLowerCase(charFile)

#print("contador: ",contador)
archive.close()

