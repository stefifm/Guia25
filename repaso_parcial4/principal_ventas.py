"""
Programa principal
"""

import funciones_ventas
import registro_ventas


def menu():
    print("\nMenú de Opciones")
    print("1) Carga del arreglo")
    print("2) Matriz de Conteo")
    print("3) Matriz de acumulación")
    print("4) Venta con mayor monto")
    print("5) Búsqueda de la venta X")
    print("6) Búsqueda con la descripción D")
    print("7) Monto recaudado del artículo 3")
    print("8) Archivo con todas las ventas del vector")
    print("9) Archivo cuyas ventas superen al monto M")
    print("10) Archivo cuyas ventas sean del artículo A")
    print("11) Vector del vendedor V a partir de la opcion 7")
    print("12) Recaudación promedio de la opcion 7")
    print("13) Archivo a partir de la opción 8 y vendedor V")
    print("14) Salir")






def principal():
    vec = []
    band = False
    fd = "ventas.dat"
    md = "sup_monto.dat"
    ad = "art.dat"
    opcion = 0
    while opcion != 14:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            funciones_ventas.vector_ventas(vec)
            funciones_ventas.display(vec)
            band = True
        elif opcion == 2 and band == True:
            mat_conteo = funciones_ventas.matriz_conteo(vec)
            funciones_ventas.mostrar_matriz(mat_conteo)
        elif opcion == 3 and band == True:
            mat_acu = funciones_ventas.matriz_acumulacion(vec)
            funciones_ventas.mostrar_matriz_acu(mat_acu)
        elif opcion == 4 and band == True:
            mayor = funciones_ventas.mayor(vec)
            print("La venta con mayor monto:",registro_ventas.to_string(mayor))
        elif opcion == 5 and band == True:
            x = int(input("Ingrese un número de venta: "))
            funciones_ventas.buscar_venta_num(vec, x)
        elif opcion == 6 and band == True:
            d = input("Ingrese una descripción: ")
            funciones_ventas.buscar_venta_desc(vec, d)
        elif opcion == 7 and band == True:
            monto_total = funciones_ventas.monto_art_3(vec)
            print("Monto total del artículo 3:",monto_total)
        elif opcion == 8 and band == True:
            funciones_ventas.generar_archivo(vec, fd)
            funciones_ventas.mostrar_archivo(fd)
        elif opcion == 9 and band == True:
            mont = int(input("Ingrese un monto para generar el archivo: $"))
            funciones_ventas.grabar_archivo_mont_sup(vec, mont, md)
            funciones_ventas.mostrar_archivo(md)
        elif opcion == 10 and band == True:
            art = int(input("Ingrese número de artículo (0 a 9): "))
            funciones_ventas.grabar_archivo_art_a(vec, art, ad)
            funciones_ventas.mostrar_archivo(ad)
        elif opcion == 11 and band == True:
            ven = int(input("Ingrese el número del vendedor (0 a 4): "))
            vec_ven = funciones_ventas.vec_archivo_v(fd, ven)
            funciones_ventas.display(vec_ven)
        elif opcion == 12 and band == True:
            prom = funciones_ventas.promedio(fd)
            print("Total recaudado:",prom)
        elif opcion == 13 and band == True:
            ve = int(input("Ingrese el número del vendedor (0 a 4): "))
            funciones_ventas.mostrar_archivo_vendedor_v(fd, ve)
        elif band == False:
            print("No se cargó el vector")
        else:
            print("=========== PROGRAMA FINALIZADO ===============")






if __name__ == "__main__":
    principal()