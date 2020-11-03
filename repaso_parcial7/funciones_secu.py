import registro_secu
from registro_secu import Secundario
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
        print(registro_secu.to_string(vec[i]))

# Opcion 2
def buscar_directa(vec, x_legajo, x_deporte):
    for secundario in vec:
        if secundario.legajo == x_legajo and secundario.deporte == x_deporte:
            return secundario
    return None

def buscar_leg_dep(vec, x_legajo, x_deporte):
    sec = buscar_directa(vec, x_legajo, x_deporte)
    if sec != None:
        print("Se encontraron los datos")
        print(registro_secu.to_string(sec))
    else:
        print("No se encontró, pero vamos a agregarlo")
        print("Ingrese el nombre y el año para completar")
        x_nom = input("Ingrese el nombre del alumno: ")
        x_anio = validar_rango(1, 7, "Ingrese un año (1 a 7): ")
        new_reg = Secundario(x_legajo, x_nom, x_anio, x_deporte)
        vec.append(new_reg)
        display(vec)


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
        print("Deporte:", i)
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Año:",j+1," -----> Cantidad de inscritos:",mat[i][j])

# Opcion 4
def grabar_archivo(vec, fd):
    if not os.path.exists(fd):
        print("No está el arachivo. Vamos crearlo...")
        m = open(fd, "wb")
        for i in range(len(vec)):
            pickle.dump(vec[i], m)
        print("El archivo",fd,"ya se ha creado")
        m.close()
    else:
        print("El archivo existe")

def mostrar_archivo(file):
    band = False
    if not os.path.exists(file):
        print("No está el archivo.")
        return None
    m = open(file, "rb")
    t = os.path.getsize(file)
    while m.tell() < t:
        secundario = pickle.load(m)
        if secundario.anio == 7:
            print(registro_secu.to_string(secundario))
            band = True
    if band == False:
        print("No hay registros con alumnos del 7mo. año")
    m.close()