import funciones_compra





def principal():
    menu = "======== Menú de Opciones ==========\n"\
            "1 - Carga y muestra del archivo\n"\
            "2 - Generación del vector\n"\
            "3 - Matriz de conteo\n"\
            "4 - Segundo archivo con transacciones fuera de Argentina\n"\
            "5 - Archivo de reclamos\n"\
            "6 - Salir"
    fd = "transacciones.dat"
    newd = "transacciones_exterior.dat"
    recd = "reclamos.dat"
    vec = []
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            funciones_compra.generar_archivo(fd)
            funciones_compra.mostrar_archivo(fd)
        elif opcion == 2:
            funciones_compra.armar_vector(fd, vec)
            funciones_compra.display(vec)
        elif opcion == 3:
            mat = funciones_compra.matriz_conteo(vec)
            funciones_compra.mostrar_matriz_conteo(mat)
        elif opcion == 4:
            funciones_compra.carga_archivo_exterior(newd, vec)
            funciones_compra.mostrar_archivo(newd)
        elif opcion == 5:
            nro_reclamo = int(input("Ingrese un cupón a reclamar: "))
            funciones_compra.busqueda_archivo_reclamos(recd, nro_reclamo, vec)
            funciones_compra.mostrar_archivo(recd)
        else:
            print("Programa finalizado")






if __name__ == "__main__":
    principal()