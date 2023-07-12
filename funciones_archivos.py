import os

def menu():
    os.system("cls")
    try:
        print("════════════════════════════════════════   MENU   ════════════════════════════════════════")
        print("")
        print("1-  Cargar datos del archivo (obligatorio)")
        print("2-  Imprimir lista de peliculas")
        print("3-  Asignar tiempo de duracion (entre 100 y 240min)")
        print("4-  Filtrar por tipo")
        print("5-  Mostrar duraciones ordenadas por genero y duracion de forma descendente")
        print("6-  Guardar peliculas (PUNTO 5)")
        print("7-  Salir")
 
        
        opcion=int(input("Ingrese una opcion:"))
        
        return opcion

    except ValueError:
        print("----------------OPCION INVALIDA--------------------")
        os.system("pause")
        os.system("cls")

def cargar_archivo(nombre_archivo)->list:
    """
    Function: 
        Ingresa direccion del archivo a cargar, por ejemplo: 'carpeta//ejemplo.csv'.

    Args:
        nombre_archivo (str): Archivo a cargar

    Returns:
        Se carga el archivo en formato de lista de diccionarios y los muestra.
    """
    os.system("cls")
    separador = ","


    with open(nombre_archivo, encoding="utf-8") as archivo:
        lista_diccionario = []
        for linea in archivo:
            linea = linea.strip("\n")                                                   # Saco el salto de linea y elimino $
            columnas = linea.split(separador)                                           # Separo con , los datos

            id, titulo, genero, duracion = columnas                                     # Asigno las columnas

            diccionarios = {
                "id_peli": id,
                "titulo": titulo,
                "genero": genero,                                                         # Creo los diccionarios
                "duracion": duracion,
            }                                           

            lista_diccionario.append(diccionarios)                                        # Los agrego a la lista_diccionario


        return lista_diccionario
    
def guardar_csv(lista_tipo,direccion_archivo_nuevo):
    with open(direccion_archivo_nuevo,"w",encoding="utf-8") as file:
        renglon = 0
        for i in lista_tipo:
            linea= f'{i["id_peli"]},{i["titulo"]},{i["genero"]},{i["duracion"]}'
            file.writelines("\n")
            file.writelines(linea)
            renglon+=1
        print("Datos guardados en el archivo CSV correctamente.")

def seguir_salir():
    """
    Function: 
        Nos pregunta si deseamos continuar o finalizar un programa
    Returns:
        Nos retorna una respuesta, si es "S" continua, si no, finaliza el programa
    """
    continuar_salir=input("Desea continuar? s/n: ")
    while continuar_salir != "s" and continuar_salir != "n":
        continuar_salir=input("ERROR, desea continuar? s/n: ")
    if continuar_salir =="n":
        quit("----------------------------FIN DEL PROGRAMA-------------------------------")
