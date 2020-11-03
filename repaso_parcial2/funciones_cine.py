import registro_cines
from registro_cines import Pelicula
import pickle
import os.path
import random


def add_in_order(vec, peli):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].titulo == peli.titulo:
            pos = c
            break
        if peli.titulo < vec[c].titulo: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [peli]

def vector_peliculas(vec):
    nom = ("Esperando la Carrroza", "The Avengers", "Mujer Bonita", "Doom",
           "Contra lo Imposible", "Quien quiere ser Millonario",
           "Una Aventura Extraordinaria", "Mujer Bonita",
           "Belleza Americana", "Relatos Salvaje", "Roma", "Intensamente",
           "La Era del Hielo", "Red de Mentiras", "Red Social",
           "Africa", "F1 Drive To Survive")
    n = int(input("Cargue la cantidad de películas: "))
    for i in range(n):
        numero = random.randint(1, 300)
        titulo = random.choice(nom)
        importe = round(random.random() * 100000, 2)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)
        peli = Pelicula(numero, titulo, importe, tipo, pais)
        add_in_order(vec, peli)


def display(vec):
    for i in range(len(vec)):
        print(registro_cines.to_string(vec[i]))

# Opcion 3
def cargar_archivo(fd, vec, x):
    m = open(fd, "wb")
    for i in range(len(vec)):
        if vec[i].pais != 10 and vec[i].importe < x:
            pickle.dump(vec[i], m)
    m.close()

# Opcion 4
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No se ha cargado el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        peli = pickle.load(m)
        print(registro_cines.to_string(peli))
    m.close()

# Opcion 5
def busqueda_directa(vec, num):
    for pelicula in vec:
        if pelicula.numero == num:
            return pelicula
    return None


def buscar_numero(vec, num):
    pos = busqueda_directa(vec, num)
    if pos == None:
        print("No se encontraron los datos del registro")
    else:
        print("Se encontraron los datos buscados")
        print(registro_cines.to_string(pos))

# Opcion 6
def matriz_conteo(vec):
    mat = [[0] * 20 for i in range(10)]
    for i in range(len(vec)):
        filas = vec[i].tipo
        columnas = vec[i].pais
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Tipo de película:",registro_cines.cadena_tipo(i),
                      "======> País:", registro_cines.cadena_pais(j),
                      " - Cantidad de países:",mat[i][j])