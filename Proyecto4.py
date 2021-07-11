#Proyecto Programación 4.


#importar librerias a utilizar.
import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt

#leer archivo csv.
csv = pd.read_csv ("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto16/CasosGeneroEtarioEtapaClinica.csv")

#Crear Dataframe
Datos = pd.DataFrame (csv)

#Obtener columnas.
Edad = list(Datos.iloc[:,0])
Sexo = list(Datos.iloc[:,1])
Columnas =(Datos.iloc[:,2])

#Unir las columnas en Dataframe.
Columnas = np.colum_stack((
    Edad, Sexo, Etapa))
Columnas = pd.DataFrame(Columnas)
#-Edad = 0
#-Sexo = 1
#-Etapa = 2

#Menu
#print("Bienvenido/a!\nA continuación se desplegará un gráfico sobre casos de contagios de CoVid-19 durante los últimos días")
#print("Seleccione entre las siguientes opciones en que parametros desea visualizar los datos:")
#print("1) Grupo de edad\n2)Sexo")
#Opcion = input()
#def Filtrado(Opcion):

#Obtener ultimas 7 fechas. Eje x.
Fechas = list(Datos.columns.values
Fechas = Fechas[-7:]
              
#Obtener valores de las ultimas 7 fechas. Eje y.
#Por ahora solo toma datos de fila 1.
Contagios = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto16/CasosGeneroEtarioEtapaClinica.csv",",")
Contagios = Contagios.iloc[1,[-7, -6, -5, -4, -3, -2, -1]] 
Contagios = list(Contagios)

#Graficar información.
plt.bar(Fechas, Contagios)
plt.show()
