
def grabar(archivo,contenido):
    m = open(archivo, "wt")
    m.write(contenido)
    m.close()
    print("Archivo grabado")

def leer(archivo):
    m = open(archivo, "rt")
    contenido = m.read()
    m.close()
    return contenido

def principal():
    archivo = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido que desee: ")
    grabar(archivo,contenido)
    read = leer(archivo)
    print("Contenido del archivo es:",read)

principal()
