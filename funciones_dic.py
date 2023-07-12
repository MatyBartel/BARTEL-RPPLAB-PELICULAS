import random
import os
def mostrar_diccionarios(lista):
    for diccionario in lista:
        print (diccionario)
        print()

def duracion_random(diccionario):
    duracion_aleatoria = random.randint(100, 240)
    diccionario["duracion"] = duracion_aleatoria
    return diccionario

def aplicar_duracion_random(lista_diccionarios):
    return list(map(lambda diccionario: duracion_random(diccionario), lista_diccionarios))

def filtrar_por_tipo(lista_diccionarios,tipo_ingresado)->list:
    """
    Function: Busca por tipo de pelicula ingresada y muestra los diccionarios que coincidan

    Args:
        lista_diccionarios (list): Lista que recibe
        tipo_ingresado (str): Tipo de pelicula que buscara coincidencias
    
    Returns:
        lista_diccionarios (dict): Lista que tiene los diccionarios que coinciden con el tipo de pelicula

    """

    lista_tipo = []
    for diccionario in lista_diccionarios:
        if 'genero' in diccionario and str(tipo_ingresado).lower() == diccionario['genero'].lower():
            lista_tipo.append(diccionario)

    if lista_tipo == []:
        print("-NO EXISTEN PELIS CON ESE GENERO-")

    return lista_tipo

def mostrar_tres_claves(lista_dic:list,key:str,key_2:str,key_3:str)->list:
    """
    Function: Recibe una lista de diccionarios y tres claves,termina reduciendo la lista original agregando las claves con diccionarios a una nueva lista.

    Args:
        lista_dic (list): Lista de diccionarios que recibe
        key (_type_): Clave nro 1
        key_2 (_type_): Clave nro 2

    Returns:
        lista_reducida (list): Lista de diccionarios reducida a tres diccionarios
    """
    generos = {}

    for clave in lista_dic:
        genero = clave[key]
        titulo = clave[key_2]
        duracion = clave[key_3]

        if genero in generos:
            generos[genero].append({"titulo": titulo, "duracion": duracion})
        else:
            generos[genero] = [{"titulo": titulo, "duracion": duracion}]

    print("══════════════════════════════════════ PELICULAS ORDENADAS POR GENERO Y DURACION ══════════════════════════════════════  ")
    
    for genero, productos in generos.items():
        print(f"genero: {genero}")
        for producto in productos:
            print(f"titulo: {producto['titulo']}, duracion: {producto['duracion']}")
        print()

    os.system("pause")
    os.system("cls")
    return lista_dic

def ordenar_lista_duracion(lista_diccionarios: list, clave_principal: str, clave_auxiliar: str) -> list:
    """
    Function: Ordena la lista según el abecedario de forma ascendente según la clave especificada.

    Args:
        lista_diccionarios (list): Lista a ordenar.
        clave_principal (str): Clave principal para el ordenamiento.
        clave_auxiliar (str): Clave auxiliar para el ordenamiento secundario.

    Returns:
        list: Lista ordenada de forma descendente.
    """
    tam = len(lista_diccionarios)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista_diccionarios[i][clave_principal] > lista_diccionarios[j][clave_principal] or (lista_diccionarios[i][clave_principal] == lista_diccionarios[j][clave_principal] and float(lista_diccionarios[i][clave_auxiliar]) < float(lista_diccionarios[j][clave_auxiliar])):
                lista_diccionarios[i], lista_diccionarios[j] = lista_diccionarios[j], lista_diccionarios[i]

    return lista_diccionarios

def ordenar_lista_generos(lista_diccionarios: list, clave_principal: str) -> list:
    """
    Function: Ordena la lista según el orden alfabético ascendente de la clave especificada.

    Args:
        lista_diccionarios (list): Lista a ordenar.
        clave_principal (str): Clave por la cual se ordenará la lista.

    Returns:
        list: Lista ordenada de forma ascendente.
    """

    tam = len(lista_diccionarios)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista_diccionarios[i][clave_principal] > lista_diccionarios[j][clave_principal]:
                aux = lista_diccionarios[i]
                lista_diccionarios[i] = lista_diccionarios[j]
                lista_diccionarios[j] = aux

    return lista_diccionarios