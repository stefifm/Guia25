import funciones_col_secu


__author__ = "Stefania Bruera"




def principal():
    menu = "======== Menú de Opciones ==========\n" \
           "1 - Carga y muestra del vector\n" \
           "2 - Buscar un alumno\n" \
           "3 - Matriz de conteo por deporte y año\n" \
           "4 - Generación del archivo año\n" \
           "5 - Muestra del archivo\n" \
           "6 - Salir"
    vec = []
    fd = "anio.dat"
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion = funciones_col_secu.validar_rango(1, 6, "Ingrese una opción: ")
        if opcion == 1:
            funciones_col_secu.carga_vector(vec)
            funciones_col_secu.display(vec)
        elif opcion == 2:
            x_nom = input("Ingrese un nombre alumno: ")
            funciones_col_secu.buscar_alumno(vec, x_nom)
        elif opcion == 3:
            mat = funciones_col_secu.matriz_conteo_dep_anio(vec)
            funciones_col_secu.mostrar_matriz(mat)
        elif opcion == 4:
            x_anio = funciones_col_secu.validar_rango(1, 7, "Ingrese un año "
                                                            "(1 a 7): ")
            funciones_col_secu.cargar_archivo_anio(vec, x_anio, fd)
        elif opcion == 5:
            funciones_col_secu.mostrar_archivo(fd)
        else:
            print("Programa finalizado")



if __name__ == "__main__":
    principal()