import funciones_audiovisual



def principal():
    vec = []
    fd = "idioma.dat"
    menu = "================= Menú de Opciones ==================\n"\
           "1 - Cargar el vector de licenciantes\n"\
           "2 - Mostrar el vector de licenciantes\n"\
           "3 - Buscar y elevar el total a un licenciante\n"\
           "4 - Total a pagar por idioma y país\n"\
           "5 - Archivo de un idioma determinado\n"\
           "6 - Mostrar el archivo\n"\
           "7 - Salir\n"\
           "===========================================================\n"
    opcion = 0
    while opcion != 7:
        print(menu)
        opcion = funciones_audiovisual.validar_rango(1, 7,"Ingrese una "
                                                          "opción: ")
        print()
        if opcion == 1:
            funciones_audiovisual.cargar_vector(vec)
        elif opcion == 2:
            funciones_audiovisual.display_vector(vec)
        elif opcion == 3:
            x_cod = int(input("Ingrese el código de licenciante a buscar: "))
            funciones_audiovisual.buscar_codigo(vec, x_cod)
        elif opcion == 4:
            mat_acu = funciones_audiovisual.matriz_acumulador(vec)
            funciones_audiovisual.mostrar_matriz(mat_acu)
        elif opcion == 5:
            x_idio = funciones_audiovisual.validar_rango(0, 6, "Ingrese el Nº "
                                                               "de un idioma: ")
            funciones_audiovisual.generar_archivo_idioma(vec, x_idio, fd)
        elif opcion == 6:
            funciones_audiovisual.mostrar_archivo(fd)
        else:
            print("PROGRAMA FINALIZADO")







if __name__ == "__main__":
    principal()