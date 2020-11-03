import registro_compras
from registro_compras import Compras
import random
import pickle
import os.path


def generar_archivo(fd):
    m = open(fd, "wb")
    nom = ("nom1", "nom2", "nom3", "nom4", "nom5", "nom6", "nom7", "nom8",
           "nom9", "nom10", "nom11", "nom12", "nom13", "nom14", "nom15",
           "nom16", "nom17")
    n = int(input("Ingrese la cantidad de compras: "))
    for i in range(n):
        nro_cupon = random.randint(1, 523)
        nro_cliente = random.randint(1, 1000)
        nom_cliente = random.choice(nom)
        monto = round(random.random() * 1000, 2)
        pais = random.randint(0, 193)
        rubro = random.randint(0, 5)
        compras = Compras(nro_cupon, nro_cliente, nom_cliente, monto, pais, rubro)
        pickle.dump(compras, m)

    m.close()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No se encuentra el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        compras = pickle.load(m)
        print(registro_compras.to_string(compras))
    m.close()


# Opcion 2
def add_in_order(vec, compras):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].nro_cupon == compras.nro_cupon:
            pos = c
            break
        if compras.nro_cupon < vec[c].nro_cupon: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [compras]



def armar_vector(fd, vec):
    if not os.path.exists(fd):
        print("No se encuentra el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        compras = pickle.load(m)
        add_in_order(vec, compras)
    m.close()

def display(vec):
    for i in range(len(vec)):
        print(registro_compras.to_string(vec[i]))

# Opcion 3
def matriz_conteo(vec):
    mat = [[0] * 6  for i in range(194)]
    for i in range(len(vec)):
        filas = vec[i].pais
        columnas = vec[i].rubro
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz_conteo(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Rubro:",j," =====> País:",i,"Cantidad de "
                                                   "transacciones:",mat[i][j])


# Opcion 4
def carga_archivo_exterior(newd, vec):
    m = open(newd, "wb")
    for i in range(len(vec)):
        if vec[i].pais != 32:
            pickle.dump(vec[i], m)
    m.close()

# Opcion 5
def buscar_binaria(vec, nro_reclamo):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if nro_reclamo == vec[c].nro_cupon:
            return c
        if nro_reclamo < vec[c].nro_cupon: #Cuando es para menor a mayor
            der = c - 1
        else:
            izq = c + 1
    return -1

def busqueda_archivo_reclamos(recd, nro_reclamo, vec):
    pos = buscar_binaria(vec, nro_reclamo)
    if pos != -1:
        reclamo = vec[pos]
        m = open(recd, "ab")
        pickle.dump(reclamo, m)
        m.close()
    else:
        print("No existe el cupón")