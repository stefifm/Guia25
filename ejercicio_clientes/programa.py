

import os

def procesar_archivo(vec_clientes):
    if not os.path.exists("Enunciado2020.csv"):
        print("Error. No existe el archivo")
        return

    arch = open("Enunciado2020.csv")
    for linea in arch:
        if linea[0] != "#":
            linea = linea.replace("\n", "")

            tokens = linea.split(",")