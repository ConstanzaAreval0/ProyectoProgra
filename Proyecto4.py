#Programación Proyecto 4.


#Importar librerias a utilizar.
import pandas as pd
import matplotlib.pyplot as plt

#Leer Dataframe.
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto16/CasosGeneroEtarioEtapaClinica.csv") 

#Menu. 
#Filtrado entre Grupo de edad o Sexo.
print("Bienvenido/a!\nA continuación se desplegará un gráfico sobre casos de contagios de CoVid-19 durante los últimos días")
print("Seleccione entre las siguientes opciones en que parametros desea visualizar los datos:")
print("1) Grupo de edad\n2) Sexo")
Opcion = input()
def FiltradoEdadSexo(Opcion):
    while True:
        if Opcion == "1":
            return "Grupo de edad"
        elif Opcion == "2":
            Eleccion = "Sexo"
            return "Sexo"
        else:
            print("Error!\nHa ingresado un carácter inválido.") 
            print("Seleccione una opción valida!")
            Opcion = input()    
def FiltradoGrupo(Opcion):
    print("\nHa seleccionado:", FiltradoEdadSexo(Opcion))
    print("A continuación, seleccione una de las siguientes opciones.")
    if FiltradoEdadSexo(Opcion) == "Grupo de edad":
        print("1) 00 - 04 años")
        print("2) 05 - 09 años")
        print("3) 10 - 14 años")
        print("4) 15 - 29 años")
        print("5) 20 - 24 años")
        print("6) 25 - 29 años")
        print("7) 30 - 34 años")
        print("8) 35 - 39 años")
        print("9) 40 - 44 años")
        print("10) 45 - 49 años")
        print("11) 50 - 54 años")
        print("12) 55 - 59 años")
        print("13) 60 - 64 años")
        print("14) 65 - 69 años")
        print("15) 70 - 74 años")
        print("16) 75 - 79 años")
        print("17) 80 y más años")
        Grupo = input()
        while True:
            if Grupo == "1":
                return "00 - 04 años"
            elif Grupo == "2":
                return "05 - 09 años"
            elif Grupo == "3":
                return "10 - 14 años"
            elif Grupo == "4":
                return "15 - 29 años"
            elif Grupo == "5":
                return "20 - 24 años"
            elif Grupo == "6":
                return "25 - 29 años"
            elif Grupo == "7":
                return "30 - 34 años"
            elif Grupo == "8":
                return "35 - 39 años"
            elif Grupo == "9":
                return "40 - 44 años"
            elif Grupo == "10":
                return "45 - 49 años"
            elif Grupo == "11":
                return "50 - 54 años"
            elif Grupo == "12":
                return "55 - 59 años"
            elif Grupo == "13":
                return "60 - 64 años"
            elif Grupo == "14":
                return "65 - 69 años"
            elif Grupo == "15":
                return "70 - 74 años"
            elif Grupo == "16":
                return "75 - 79 años"
            elif Grupo == "17":
                return "80 y más años"
            else:
                print("Error!\nHa ingresado un carácter inválido.") 
                print("Seleccione una opción valida!")
                Grupo = input()
    elif FiltradoEdadSexo(Opcion) == "Sexo":
        print("1) Masculino")
        print("2) Femenino")
        Grupo = input()
        while True:
            if Grupo == "1":
                return "M"
            elif Grupo == "2":
                return "F"
            else:
                print("Error!\nHa ingresado un carácter inválido.") 
                print("Seleccione una opción valida!")
                Grupo = input()

#Tomar filas segun filtrado.
Filter = df.loc[df[FiltradoEdadSexo(Opcion)] == FiltradoGrupo(Opcion)]
#Crear Dataframe filtrado.
Data = pd.DataFrame(Filter)

#Obtener ultimas 7 fechas. Eje x.
Ejex = list(Data.columns.values)
Ejex = Ejex[-7:]

#Obtener valores de las ultimas 7 fechas. Eje y.
#Por ahora solo toma datos de fila 1.
Contagios = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto16/CasosGeneroEtarioEtapaClinica.csv", ",")
Contagios = Contagios.iloc[1,[-7, -6, -5, -4, -3, -2, -1]] 
Contagios = list(Contagios)

#Graficar información.
plt.bar(Ejex, Contagios)
plt.show()
