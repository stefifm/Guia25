"""
Funciones para el programa principal de ventas
"""
import registro_ventas
from registro_ventas import Venta
import random
import pickle
import os.path


def add_in_order(vec, venta):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].numero == venta.numero:
            pos = c
            break
        if venta.numero < vec[c].numero: #menor a mayor
            der = c - 1
        else:
            izq = c + 1
    if izq > der:  # esto valida la posición del puntero izq
        pos = izq
    vec[pos:pos] = [venta]

def vector_ventas(vec):
    desc = ("Vaso", "Software", "Películas", "Platos", "Herramientas",
            "Limpieza", "Muebles", "Juguetes", "Papel", "Escolares",
            "Colchones", "Libros", "Funda para Celulares", "PC",
            "Celulares", "Pilas", "Jabón líquido para Ropa", "Perfumería")
    n = int(input("Ingrese la cantidad de ventas a registrar: "))
    for i in range(n):
        numero = random.randint(100, 3000)
        descripcion = random.choice(desc)
        monto = round(random.random() * 1000, 2)
        articulo = random.randint(0, 9)
        vendedor = random.randint(0, 4)
        venta = Venta(numero, descripcion, monto, articulo, vendedor)
        add_in_order(vec, venta)

def display(vec):
    for i in range(len(vec)):
        print(registro_ventas.to_string(vec[i]))

# Opcion 2

def matriz_conteo(vec):
    mat = [[0] * 5 for i in range(10)]
    for i in range(len(vec)):
        filas = vec[i].articulo
        columnas = vec[i].vendedor
        mat[filas][columnas] += 1
    return mat

def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Vendedor:",j,"Artículo",i,"Cantidad de ventas:",
                      mat[i][j])

# Opcion 3
def matriz_acumulacion(vec):
    mat = [[0] * 5 for i in range(10)]
    for i in range(len(vec)):
        filas = vec[i].articulo
        columnas = vec[i].vendedor
        mat[filas][columnas] += vec[i].monto
    return mat


def mostrar_matriz_acu(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Vendedor:",j,"Artículo",i,"Monto Recaudado: $",
                      round(mat[i][j], 2))

# Opcion 4
def mayor(vec):
    mayor = vec[0]
    for i in range(len(vec)):
        if vec[i].monto > mayor.monto:
            mayor = vec[i]
    return mayor

#Opcion 5
def busqueda_directa_num(vec, x):
    for venta in vec:
        if venta.numero == x:
            return venta
    return None

def buscar_venta_num(vec, x):
    ven = busqueda_directa_num(vec, x)
    if ven != None:
        print("Se encontró la venta. Estos son sus datos")
        print(registro_ventas.to_string(ven))
    else:
        print("No se encontró la venta")

# Opcion 6
def busqueda_directa_desc(vec, d):
    for venta in vec:
        if venta.descripcion == d:
            return venta
    return None

def buscar_venta_desc(vec, d):
    des = busqueda_directa_desc(vec, d)
    if des != None:
        print("Se encontró la venta. Estos son sus datos")
        print(registro_ventas.to_string(des))
    else:
        print("No se encontró la venta")

# Opcion 7
def monto_art_3(vec):
    acu = 0
    for i in range(len(vec)):
        if vec[i].articulo == 3:
            acu += vec[i].monto
    return acu

# Opcion 8
def generar_archivo(vec, fd):
    m = open(fd, "wb")
    for i in range(len(vec)):
        pickle.dump(vec[i], m)
    m.close()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No se cargó el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        venta = pickle.load(m)
        print(registro_ventas.to_string(venta))
    m.close()

# Opcion 9
def grabar_archivo_mont_sup(vec, mont, md):
    m = open(md, "wb")
    for i in range(len(vec)):
        if vec[i].monto > mont:
            pickle.dump(vec[i], m)
    m.close()

# Opcion 10
def grabar_archivo_art_a(vec, art, ad):
    m = open(ad, "wb")
    for i in range(len(vec)):
        if vec[i].articulo == art:
            pickle.dump(vec[i], m)
    m.close()

# Opcion 11
def vec_archivo_v(fd, ven):
    vec_ven = []
    if not os.path.exists(fd):
        print("El archivo no se ha generado")
        return vec_ven
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        venta = pickle.load(m)
        if venta.vendedor == ven:
            vec_ven.append(venta)
    m.close()
    return vec_ven

# Opcion 12
def promedio(fd):
    if not os.path.exists(fd):
        print("El archivo no se ha generado")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    c = 0
    acu = 0
    while m.tell() < t:
        venta = pickle.load(m)
        c += 1
        acu += venta.monto
    p = round(acu / c, 2)
    m.close()
    return p

# Opcion 13
def mostrar_archivo_vendedor_v(fd, ve):
    if not os.path.exists(fd):
        print("No se cargó el archivo")
        return None
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        venta = pickle.load(m)
        if venta.vendedor == ve:
            print(registro_ventas.to_string(venta))
    m.close()