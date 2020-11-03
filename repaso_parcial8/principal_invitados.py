import funciones_invitados
import registro_invitados



def principal():
    vec = funciones_invitados.generar_vector()
    menu = "============ Menú de Opciones ==============\n"\
           "1 - Mostrar la lista completa de invitados\n"\
           "2 - Matriz de Conteo\n"\
           "3 - Invitado de mayor donación para cierta ONG\n"\
           "4 - Archivo de cierta ONG\n"\
           "5 - Total recaudado de una ONG\n"\
           "6 - Salir\n"\
           "==============================================\n"
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            funciones_invitados.display(vec)
        elif opcion == 2:
            mat = funciones_invitados.matriz_conteo(vec)
            funciones_invitados.mostrar_matriz(mat)
        elif opcion == 3:
            x_ong = int(input("Ingrese el número de ONG: "))
            mayor = funciones_invitados.mayor(vec, x_ong)
            if mayor is None:
                print("Esa ONG no recibió donaciones")
            else:
                print("La mayor donación fue:",registro_invitados.to_string(
                    mayor))
        elif opcion == 4:
            ong = int(input("Ingrese el número de ONG: "))
            funciones_invitados.generar_archivo(vec, ong)
            # funciones_invitados.mostrar_archivo(fd)
        elif opcion == 5:
            cod_ong = int(input("Ingrese el número de ONG: "))
            rd = "donaciones" + str(cod_ong) + ".dat"
            funciones_invitados.total_recaudado(rd,cod_ong)
        else:
            print("Programa finalizado")






if __name__ == "__main__":
    principal()