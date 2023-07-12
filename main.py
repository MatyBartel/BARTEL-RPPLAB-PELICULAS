from funciones_archivos import *
from funciones_dic import *
import os

while True:
    os.system("cls")
    match(menu()):
        case 1:
            try:
                lista_diccionario =  cargar_archivo(nombre_archivo=input("-Ingrese direccion del archivo a usar 'carpeta//ejemplo.csv' :"))      # Bartel Matias RPP 1A LABO\movies.csv
                print("-ARCHVIO CARGADO CON EXITO-")
            except FileNotFoundError:
                print("ERROR: El archivo que ingreso no existe, ingrese la direccion correctamente.")
            os.system("pause")
            os.system("cls")
        case 2:
            try:
                print("-LISTA PELICULAS-")
                mostrar_diccionarios(lista_diccionario)
            except NameError:
                print("ERROR: El archivo no esta cargado, PUNTO 1.")
            os.system("pause")
            os.system("cls")
        case 3:
            try:
                lista_dic_tiempos = aplicar_duracion_random(lista_diccionario) 
                mostrar_diccionarios(lista_dic_tiempos) 
            except NameError:
                print("ERROR: El archivo no esta cargado, PUNTO 1.")
            os.system("pause")
            os.system("cls")
        case 4:
            try:
                lista_filtrada = filtrar_por_tipo(lista_diccionario,tipo_ingresado=input("Ingrese tipo de pelicula:"))
                if lista_filtrada == []:
                    print("NO SE PUDO GENERAR EL ARCHIVO CSV")
                else:
                    guardar_csv(lista_filtrada,".//filtrado_por_tipo.csv") 
            except NameError:
                print("ERROR: El archivo no esta cargado, PUNTO 1.")
            os.system("pause")
            os.system("cls")
        case 5:
            try:
                lista_ordenada_por_genero_duracion = ordenar_lista_duracion(lista_dic_tiempos,"genero","duracion")
                mostrar_tres_claves(lista_ordenada_por_genero_duracion,"genero","titulo","duracion")
            except NameError:
                print("ERROR: El archivo no tiene generados duracion,PUNTO 3.")
            os.system("pause")
            os.system("cls")
        case 6:
            try:
                guardar_csv(lista_ordenada_por_genero_duracion,direccion_archivo_nuevo=input("Ingrese donde y el nombre para guardar EJ: ./nuevo.csv:")) 
            except NameError:
                    print("ERROR: No se utilizo la opcion 5 de ordenar")
            os.system("pause")
            os.system("cls")
        case 7:
            seguir_salir()