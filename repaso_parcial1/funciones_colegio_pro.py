"""
Funciones para el programa del colegio profesional
"""

import registro_colegio_pro
from registro_colegio_pro import Profesional
import random
import pickle
import os.path


def add_in_order(vec, profesional):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].dni == profesional.dni:
            pos = c
            break
        if profesional.dni < vec[c].dni: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [profesional]


def cargar_vector(vec):
    nom = ("nom1", "nom2", "nom3", "nom4", "nom5", "nom6", "nom7", "nom8",
           "nom9", "nom10", "nom11", "nom12", "nom13", "nom14", "nom15",
           "nom16", "nom17")
    n = int(input("Ingrese la cantidad de registros: "))
    for i in range(n):
        dni = random.randint(10000000, 40000000)
        nombre = random.choice(nom)
        importe = round(random.random() * 1000, 2)
        afiliacion = random.randint(0, 4)
        trabajo = random.randint(0, 14)
        profesional = Profesional(dni, nombre, importe, afiliacion, trabajo)
        add_in_order(vec, profesional)

def display(vec):
    for i in range(len(vec)):
        print(registro_colegio_pro.to_string(vec[i]))


#opcion 3

def grabar_archivo_tipo_trabajo(fd, vec):
    m = open(fd, "wb")
    for i in range(len(vec)):
        if vec[i].trabajo == 3 or vec[i].trabajo == 4 or vec[i].trabajo == 5:
            pickle.dump(vec[i], m)
            m.flush()
    print("El archivo está cargado")
    m.close()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no se ha cargado")
        return
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        pro = pickle.load(m)
        print(registro_colegio_pro.to_string(pro))
    m.close()

#opcion 5
def busqueda_directa(vec, nom):
    for profesional in vec:
        if profesional.nombre == nom:
            return profesional
    return None




def busqueda_profesional(vec, nom):
    pro = busqueda_directa(vec, nom)
    if pro == None:
        print("No se encuentra en el arreglo")
    else:
        print("El profesional se encuentra. Estos son sus datos")
        print(registro_colegio_pro.to_string(pro))

#opcion 6
def matriz_conteo(vec):
    mat = [[0] * 15  for i in range(5)]
    for i in range(len(vec)):
        filas = vec[i].afiliacion
        columnas = vec[i].trabajo
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Tipo de Trabajo:",j, "Tipo de afliación:",i,"- Cantidad "
                                                               "de "
                                                               "profesionales:", mat[i][j] )