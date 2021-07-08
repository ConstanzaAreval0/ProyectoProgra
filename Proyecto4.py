#Proyecto Programación 4.


#Abrir el Archivo.
archivo = open("CasosGeneroEtarioEtapaClinica_std.csv", "r")

#Leer el archivo
def Leer(archivo):
    leer = archivo.readlines()
    for i in leer:
        print(i)

print(Leer(archivo))
    
#Cerrar el Archivo
archivo.close()