import funciones_profesional






def principal():
    vec = []
    fd = "pro_tipo.dat"
    menu = "================= Menú de Opciones ==================\n"\
           "1 - Cargar el vector de profesionales\n"\
           "2 - Mostrar el vector de profesionales\n"\
           "3 - Archivo por tipo de trabajo\n"\
           "4 - Mostrar el archivo\n"\
           "5 - Búsqueda de un profesional por DNI\n"\
           "6 - Buscar un profesional por nombre\n"\
           "7 - Buscar un profesional por filiación\n"\
           "8 - Matriz de conteo por filiación y trabajo\n"\
           "9 - Salir\n"\
           "===========================================================\n"
    opcion = 0
    while opcion != 9:
        print(menu)
        opcion = int(input("Ingrese una opción: "))
        print()
        if opcion == 1:
            funciones_profesional.cargar_vector(vec)
        elif opcion == 2:
            funciones_profesional.display_vector(vec)
        elif opcion == 3:
            x_imp = int(input("Ingrese el importe que sea superado: "))
            funciones_profesional.cargar_archivo_trab_imp(vec, x_imp,fd)
        elif opcion == 4:
            funciones_profesional.mostrar_archivo(fd)
        elif opcion == 5:
            x_dni = int(input("Ingrese el DNI del profesional a buscar: "))
            funciones_profesional.buscar_profe_dni(vec, x_dni)
        elif opcion == 6:
            nom = input("Ingrese el nombre del profesional a buscar: ")
            funciones_profesional.buscar_profe_nom(vec, nom)
        elif opcion == 7:
            x_fili = int(input("Ingrese un número de filiación: "))
            funciones_profesional.buscar_pro_fili(vec, x_fili)
        elif opcion == 8:
            mat_conteo = funciones_profesional.matriz_conteo(vec)
            funciones_profesional.mostrar_matriz_conteo(mat_conteo)
        else:
            print("PROGRAMA FINALIZADO")







if __name__ == "__main__":
    principal()