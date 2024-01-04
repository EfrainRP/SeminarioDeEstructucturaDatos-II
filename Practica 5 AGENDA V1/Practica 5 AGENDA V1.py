
archivoO=open("Agenda",'r')
archivoR=open("AgendaR",'w')

for linea in archivoO:
    archivoR.write(linea)

archivoO.close()
archivoR.close()

archivoR=open("AgendaR",'r')
archivoO=open("Agenda",'w')

for linea in archivoR:
    archivoO.write(linea)

archivoR.close()

print("\n\tAgenda de Estudiantes V1")

opc=1

while(opc==1):
    cod=int(input("\nAgregue el codigo: "))
    nom=str(input("Agregue el nombre: "))
    carrera=str(input("Agregue la carrera: "))
    opc=int(input("Desea agregar otro estudiante: [1]Si / [2]No "))
    info = str(cod) +" | "+ nom +" | "+ carrera + "\n"

    archivoO.write(info)

archivoO.close()
