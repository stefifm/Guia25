import registro_invitados
from registro_invitados import Invitado
import random
import pickle
import os.path

def add_in_order(vec, invitado):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].nombre == invitado.nombre:
            pos = c
            break
        if invitado.nombre < vec[c].nombre: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [invitado]



def generar_vector():
    vec = []
    nom = ("Kimi Raikkonen", "Charles Leclerc", "Sebastian Vettel",
               "Lewis Hamilton", "Valtteri Bottas", "Max Verstappen",
               "Alex Albon", "Lance Stroll", "Nico Hulkenberg",
               "Sergio Pérez","Esteban Ocon", "Daniel Ricciardo")
    n = int(input("Ingrese la cantidad de registros: "))
    for i in range(n):
        nombre = random.choice(nom)
        mesa = random.randint(0, 12)
        ong = random.randint(0, 9)
        donacion = round(random.random() * 2000, 2)
        invitado = Invitado(nombre, mesa, ong, donacion)
        add_in_order(vec, invitado)
    return vec

# Opcion 1

def display(vec):
    for i in range(len(vec)):
        print(registro_invitados.to_string(vec[i]))

# Opcion 2
def matriz_conteo(vec):
    mat = [[0] * 10 for i in range(13)]
    for i in range(len(vec)):
        filas = vec[i].mesa
        columnas = vec[i].ong
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz(mat):
    for j in range(len(mat[0])):
        print("ONG:",registro_invitados.cadena_ong(j))
        for i in range(len(mat)):
            if mat[i][j] > 0:
                print("Mesa:",i," ======> Cantidad de invitados:",mat[i][j])

# Opcion 3:
def mayor(vec, x_ong):
    mayor = None
    for i in range(len(vec)):
        if vec[i].ong == x_ong:
            if mayor is None:
                mayor = vec[i]
            elif vec[i].donacion > mayor.donacion:
                mayor = vec[i]
    return mayor

# Opcion 4
def generar_archivo(vec, ong):
    m = open("donaciones" + str(ong) + ".dat", "wb")
    for i in range(len(vec)):
        if vec[i].ong == ong:
            pickle.dump(vec[i], m)
    print("El archivo", "donaciones" + str(ong) + ".dat", "fue generado")
    m.close()

# def mostrar_archivo(fd):
#     if not os.path.exists(fd):
#         print("No existe el archivo")
#         return None
#     m = open(fd, "rb")
#     t = os.path.getsize(fd)
#     while m.tell() < t:
#         invitado = pickle.load(m)
#         print(registro_invitados.to_string(invitado))
#     m.close()

# Opcion 5
def total_recaudado(fd, cod_ong):
    acu = [0] * 13
    if not os.path.exists(fd):
        print("No existe el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        invitado = pickle.load(m)
        a = int(invitado.mesa)
        if invitado.ong == cod_ong:
            acu[a] += invitado.donacion
    m.close()
    for i in range(13):
        print("Mesa:",i," ====> Total Recaudado:", acu[i])