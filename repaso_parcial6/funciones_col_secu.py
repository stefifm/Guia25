import registro_col_secu
from registro_col_secu import Secundario
import random
import pickle
import os.path
#------------------------------------------------------------------------------
def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. El valor debe ser mayor a cero")
    return n

def validar_rango(inf, sup, mensaje):
    """
    Valida si un número está en cierto rango
    :param inf: Un número que marca el inicio del rangp
    :param sup: Otro número que indica el final del rango
    :param mensaje: Un mensaje cualquiera
    :return: El número que puede estar dentro del rango y si no, marca error
    """
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup))
    return n



#------------------------------------------------------------------------------
# Opcion 1


def add_in_order(vec, secundario):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].nombre == secundario.nombre:
            pos = c
            break
        if secundario.nombre < vec[c].nombre: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [secundario]


def carga_vector(vec):
    nom = ("alu1", "nom2", "cal3", "bru4", "mon5", "car6", "feli7", "halo8",
           "sato9", "kim10", "nor11", "xavi12", "lun13", "fer14", "bar15",
           "veg16", "tod17")
    n = validar(0, "Ingrese la cantidad de registros de alumnos: ")
    for i in range(n):
        legajo = random.randint(1000, 7000)
        nombre = random.choice(nom)
        anio = random.randint(1, 7)
        deporte = random.randint(0, 9)
        secundario = Secundario(legajo, nombre, anio, deporte)
        add_in_order(vec, secundario)

def display(vec):
    for i in range(len(vec)):
        print(registro_col_secu.to_string(vec[i]))

# Opcion 2

def buscar_binaria(vec, x_nom):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x_nom == vec[c].nombre:
            return c
        if x_nom < vec[c].nombre: #Cuando es para menor a mayor
            der = c - 1
        else:
            izq = c + 1
    return -1

def buscar_alumno(vec, x_nom):
    pos = buscar_binaria(vec, x_nom)
    if pos != -1:
        print("Se contró al alumno. Estos son sus datos")
        print(registro_col_secu.to_string(vec[pos]))
    else:
        print("No se encontraron los datos del alumno")

# Opcion 3
def matriz_conteo_dep_anio(vec):
    mat = [[0] * 7 for i in range(10)]
    for i in range(len(vec)):
        filas = vec[i].deporte
        columnas = vec[i].anio - 1
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("Deporte:",i," ======> Año:",j+1," -----> Cantidad de "
                                                   "inscritos:",
                  mat[i][j])

# Opcion 4

def cargar_archivo_anio(vec, x_anio, fd):
    m = open(fd, "wb")
    for i in range(len(vec)):
        if vec[i].anio == x_anio:
            pickle.dump(vec[i], m)
    print("El archivo",fd,"ya está cargado")
    m.close()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No se encuentra cargado el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        sec_anio = pickle.load(m)
        print(registro_col_secu.to_string(sec_anio))
    m.close()