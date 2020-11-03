import registro_profesional
from registro_profesional import Profesional
import random
import pickle
import os.path

#-----------------------------------------------------------------------------
#Validaciones









#-----------------------------------------------------------------------------



# Opcion 1
def add_in_order(vec, profesional):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].dni == profesional.dni:
            pos = c
            break
        if profesional.dni > vec[c].dni: #mayor a menor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [profesional]

def cargar_vector(vec):
    nom = ("Kimi Raikkonen", "Charles Leclerc", "Sebastian Vettel",
               "Lewis Hamilton", "Valtteri Bottas", "Max Verstappen",
               "Alex Albon", "Lance Stroll", "Nico Hulkenberg",
               "Sergio Pérez","Esteban Ocon", "Daniel Ricciardo")
    n = int(input("Ingrese la cantidad de profesionales: "))
    for i in range(n):
        dni = random.randint(10000000, 50000000)
        nombre = random.choice(nom)
        importe = round(random.random() * 1000, 2)
        filiacion = random.randint(0, 4)
        trabajo = random.randint(1, 15)
        profesional = Profesional(dni, nombre, importe, filiacion, trabajo)
        add_in_order(vec, profesional)


# Opcion 2
def display_vector(vec):
    for i in range(len(vec)):
        print(registro_profesional.to_string(vec[i]))

# Opcion 3
def cargar_archivo_trab_imp(vec, x_imp, fd):
    m = open(fd, "wb")
    for i in range(len(vec)):
        if vec[i].trabajo == 3 or vec[i].trabajo == 4 or vec[i].trabajo == 5\
                and vec[i].importe > x_imp:
            pickle.dump(vec[i], m)
    print("El archivo",fd,"está cargado")
    m.close()

# opcion 4
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        profesional = pickle.load(m)
        print(registro_profesional.to_string(profesional))
    m.close()

# Opcion 5
def buscar_binaria(vec, x_dni):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x_dni == vec[c].dni:
            return c
        if x_dni > vec[c].dni: #Cuando es para mayor a menor
            der = c - 1
        else:
            izq = c + 1
    return -1

def buscar_profe_dni(vec, x_dni):
    pos = buscar_binaria(vec, x_dni)
    if pos != -1:
        print("Se encontró los datos del profesional")
        print(registro_profesional.to_string(vec[pos]))
    else:
        print("No se encontraron los datos del profesional buscado")

# Opcion 6
def buscar_unica(vec, nom):
    for profesional in vec:
        if profesional.nombre == nom:
            return profesional
    return None

def buscar_profe_nom(vec, nom):
    pro = buscar_unica(vec, nom)
    if pro != None:
        print("Se encontró al profesional. Cambiar el importe")
        x_imp = int(input("Ingrese el nuevo importe: "))
        pro.importe = x_imp
        print("Registro con el nuevo importe")
        print(registro_profesional.to_string(pro))
    else:
        print("No se encontraron los datos del profesional buscado")

# Opcion 7
def buscar_variado(vec, x_fili):
    res = []
    for i in range(len(vec)):
        if vec[i].filiacion == x_fili:
            res.append(vec[i])
    return res

def buscar_pro_fili(vec, x_fili):
    res = buscar_variado(vec, x_fili)
    if res != []:
        print("Se encontraron todos los profesionales iguales a", x_fili)
        for i in range(len(res)):
            print(registro_profesional.to_string(res[i]))
    else:
        print("No se encontraron los datos de los profesionales buscados")

# Opcion 8
def matriz_conteo(vec):
    mat_conteo = [[0] * 5 for i in range(15)]
    for i in range(len(vec)):
        filas = vec[i].trabajo - 1
        columnas = vec[i].filiacion
        mat_conteo[filas][columnas] += 1
    return mat_conteo

def mostrar_matriz_conteo(mat_conteo):
    for j in range(len(mat_conteo[0])):
        print("\nFiliación:",j)
        print()
        for i in range(len(mat_conteo)):
            if mat_conteo[i][j] > 0:
                print("Tipo de trabajo:",i+1," =====> Cantidad de "
                                         "profesionales:",mat_conteo[i][j])