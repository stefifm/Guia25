import registro_audiovisual
from registro_audiovisual import Licenciantes
import random
import pickle
import os.path

#------------------------------------------------------------------------------
# Validaciones

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

def add_in_order(vec, licenciantes):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == licenciantes.codigo:
            pos = c
            break
        if licenciantes.codigo < vec[c].codigo: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [licenciantes]


def cargar_vector(vec):
    nom = ("Kimi Raikkonen", "Charles Leclerc", "Sebastian Vettel",
               "Lewis Hamilton", "Valtteri Bottas", "Max Verstappen",
               "Alex Albon", "Lance Stroll", "Nico Hulkenberg",
               "Sergio Pérez","Esteban Ocon", "Daniel Ricciardo")
    n = validar(0, "Ingrese la cantidad de licenciantes: ")
    for i in range(n):
        codigo = random.randint(1000, 10000)
        nombre = random.choice(nom)
        total = round(random.random() * 10000, 2)
        idioma = random.randint(0, 6)
        pais = random.randint(0, 34)
        licenciante = Licenciantes(codigo, nombre, total, idioma, pais)
        add_in_order(vec, licenciante)
    print("Ya se cargó el vector\n")

# Opcion 2
def display_vector(vec):
    for i in range(len(vec)):
        print(registro_audiovisual.to_string(vec[i]),"\n")

# Opcion 3
def buscar_binaria(vec, x_cod):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x_cod == vec[c].codigo:
            return c
        if x_cod < vec[c].codigo: #Cuando es para menor a mayor
            der = c - 1
        else:
            izq = c + 1
    return -1

def buscar_codigo(vec, x_cod):
    pos = buscar_binaria(vec, x_cod)
    if pos != -1:
        print("Se encontró los datos del licenciante")
        x_val = int(input("Ingrese el valor para incrementar el total a "
                          "pagarle: "))
        vec[pos].total += x_val
        print("Los datos del licenciante con el total incrementado")
        print(registro_audiovisual.to_string(vec[pos]))
    else:
        print("No se encontró al licenciante")

# Opcion 4
def matriz_acumulador(vec):
    mat_acu = [[0] * 7 for i in range(35)]
    for i in range(len(vec)):
        filas = vec[i].pais
        columnas = vec[i].idioma
        mat_acu[filas][columnas] += vec[i].total
    return mat_acu

def mostrar_matriz(mat_acu):
    for j in range(len(mat_acu[0])):
        print("\nIdioma:",j)
        print()
        for i in range(len(mat_acu)):
            if mat_acu[i][j] > 0:
                print("País:",i," =====> Total a pagar: $",
                      round(mat_acu[i][j],2))

# Opcion 5
def generar_archivo_idioma(vec, x_idio, fd):
    m = open(fd, "wb")
    c = 0
    for i in range(len(vec)):
        if vec[i].idioma == x_idio:
            pickle.dump(vec[i], m)
            c += 1
    print("El archivo",fd,"está cargado y tiene",c,"registros\n")
    m.close()

# Opcion 6
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No se encontró el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        licenciante = pickle.load(m)
        print(registro_audiovisual.to_string(licenciante))
    m.close()