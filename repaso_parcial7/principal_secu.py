

import funciones_secu

__author__ = "Stefania Bruera"




def principal():
    menu = "======== Menú de Opciones ==========\n" \
           "1 - Carga y muestra del vector\n" \
           "2 - Buscar un alumno\n" \
           "3 - Matriz de conteo por deporte y año\n" \
           "4 - Generación del archivo\n" \
           "5 - Muestra del archivo\n" \
           "6 - Salir"
    vec = []
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            funciones_secu.carga_vector(vec)
            funciones_secu.display(vec)
        elif opcion == 2:
            x_legajo = int(input("Ingrese el legajo: "))
            x_deporte = funciones_secu.validar_rango(0, 9, "Ingrese el código de deporte: ")
            funciones_secu.buscar_leg_dep(vec, x_legajo, x_deporte)
        elif opcion == 3:
            mat = funciones_secu.matriz_conteo_dep_anio(vec)
            funciones_secu.mostrar_matriz(mat)
        elif opcion == 4:
            fd = input("Ingrese el nombre del archivo con extensión .dat: ")
            funciones_secu.grabar_archivo(vec, fd)
        elif opcion == 5:
            file = input("Ingrese el nombre del archivo con extensión .dat: ")
            funciones_secu.mostrar_archivo(file)
        else:
            print("Programa finalizado")



if __name__ == "__main__":
    principal()