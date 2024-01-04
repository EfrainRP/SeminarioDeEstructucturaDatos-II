
class Alumno:
    def __init__ (self,cod,nom,c):
        self.codigo = cod
        self.nombre = nom
        self.carrera = c

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getCarrera(self):
        return self.carrera

    def setCodigo(self,cod):
         self.codigo = cod

    def setNombre(self,nom):
        self.nombre=nom

    def setCarrera(self,c_):
        self.carrera = c_
    
    def getString(self):
        return str("Codigo: " + str(self.codigo) +"  Nombre: " + self.nombre + "  Carrera: " + self.carrera + '\n')

    def getWrite(self):
        return str(self.codigo) + "/" + str(self.nombre) + "/" + str(self.carrera) + "/" + "\n" 

listAlum = []#Inicializacion de la lista de alumnos
listIndix = []#Inicializacion de la lista de sus indices

def ReadArchive():#Lectura del Archivo
    archive=open("AgendaV2",'r')
    for mystr in archive:
        list = mystr.split("/") #Uso de delimitadores, separando en una lista por cada '/'
        a = Alumno(int(list[0]),list[1],list[2])#iniciara con esos valores
        listIndix.append(a.getCodigo())
        listAlum.append(a)#Se agrega a la lista de alumnos
    archive.close()

def WriteArchive(): #Escritura en el Archivo
    archive=open("AgendaV2",'w')
    for mystr in listAlum: #.values, regresara una tupla a la lista de alumnos 
        archive.write(mystr.getWrite())
    archive.close()

def showList(): #Mostrara los datos existentes
    for mystr in listAlum:#.values, regresara la tupla de mis valores dentro a la lista de alumnos
        print(mystr.getString())
    
menu=1
ReadArchive()#Leera el archivo para meterlo a la lista de alumnos
while(menu!=3):
    opc=0 
    print("\t\tAGENDA V2")

    showList()#Mostrara todo el contenido a la lista de alumnos

    menu=int(input("(1)Agregar Alumno\n(2)Buscar Alumno\n(3)Salir\n\tSeleccione opcion: "))

    if menu==1:#Se agrega un registro al final del archivo y de la lista
        while(opc!=2):
            a = Alumno(int(input("\nAgregue el codigo: ")),str(input("Agregue el nombre: ")),str(input("Agregue su carrera: ")))
            
            archive=open("AgendaV2",'a')#Escribira hasta la ultima posicion del archivo
            archive.write(a.getWrite())#Escribira el dato al archivo

            listIndix.append(a.getCodigo())#Agregara el dato introducido al final a la lista de codigos
            listAlum.append(a) #Agregara el dato introducido al final a la lista de alumnos

            archive.close()

            opc=int(input("\n\tDesea agregar otro estudiante: [1]Si / [2]No: "))
        print("")

    elif menu == 2:#Buscar un alumno 
        opc=int(input("\n[1]Editar alumno / [2]Eliminar alumno / [3]Salir: "))

        while(opc!=3):
            x = int(input("\tIngrese el codigo del alumno a buscar: "))
            if x in listIndix:#Verificacion de que se encuentre en la lista de indice
                x = listIndix.index(x) #obtencion de la posicion en la lista

                if opc == 1:#Editara el dato en la posicion de la lista de alumnos
                    a = Alumno(int(input("\nIngrese el codigo del alumno: ")),str(input("Agregue el nombre: ")),str(input("Agregue su carrera: ")))
                    del listIndix[x]#Eliminando el dato viejo
                    del listAlum[x]
                    listIndix.insert(x,a.getCodigo())
                    listAlum.insert(x,a)
                    print("\n\tAlumno editado")

                elif opc == 2:#Eliminara el dato en la posicion de la listas
                    del listIndix[x]
                    del listAlum[x]
                    print("\n\tAlumno eliminado")
                
                opc=int(input("\nRealizar siguiente accion:\n[1]Editar alumno / [2]Eliminar alumno / [3]Salir: "))
            else:
                print("\nValor no encontrado")
            print(" ")
WriteArchive()#Escribira en el archivo cuando termine el programa
        

                