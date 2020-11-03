import funciones_cine






def principal():
    vec = []
    flag = False
    fd = "pelisin10.dat"
    opcion = 0
    while opcion != 7:
        print("Menú de opciones")
        print("1) Carga del arreglo de registros")
        print("2) Mostrar el arreglo ya cargado")
        print("3) Crear archivo por país e importe")
        print("4) Mostrar el archivo")
        print("5) Búsqueda de una película")
        print("6) Matriz de conteo")
        print("7) Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            funciones_cine.vector_peliculas(vec)
            flag = True
        elif opcion == 2 and flag == True:
            funciones_cine.display(vec)
        elif opcion == 3 and flag == True:
            val_imp = int(input("Ingrese un importe para ser comparado: "))
            funciones_cine.cargar_archivo(fd, vec, val_imp)
        elif opcion == 4 and flag == True:
            funciones_cine.mostrar_archivo(fd)
        elif opcion == 5 and flag == True:
            num = int(input("Ingrese un número de identificación de "
                            "película: "))
            funciones_cine.buscar_numero(vec, num)
        elif opcion == 6 and flag == True:
            mat = funciones_cine.matriz_conteo(vec)
            funciones_cine.mostrar_matriz(mat)
        elif flag == False:
            print("El vector no se ha cargado")
        else:
            print("Programa finalizado")







if __name__ == "__main__":
    principal()