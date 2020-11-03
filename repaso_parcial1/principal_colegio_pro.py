"""
Un colegio o asociación de profesionales mantiene información sobre sus
distintos miembros. Por cada miembro se
registran los campos siguientes: número de dni del profesional (un número
entero), nombre del profesional (una
cadena), importe que paga al colegio por mes, tipo de afiliación (un valor
entre 0 y 4 incluidos, por ejemplo de la forma
0: vitalicio, 1: transitorio, 2: indirecto, etc.) y un número que identifica el tipo de trabajo que desempeña (un número
entero entre 0 y 14 incluidos, para indicar (por ejemplo): 0: empleado, 1: jefe o director, 2: administrativo, etc.) Se pide
definir un tipo registro Profesional con los campos que se indicaron, y un programa completo con menú de opciones
para hacer lo siguiente:
1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado). Puede cargar
los datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede
ordenado de menor a mayor, según el dni de los profesionales. Se considerará incorrecta la solución basada en
cargar el arreglo completo y ordenarlo al final.
2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
3- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo tipo
de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.
4- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
5- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar
nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un
mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
6- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación por
cada posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados
que sean diferentes de 0.
"""
import funciones_colegio_pro




def principal():
    vec = []
    fd = "tipo_trabajo.dat"
    opcion = 0
    while opcion != 7:
        print("Menú de opciones")
        print("1) Carga del arreglo de registros")
        print("2) Mostrar el arreglo ya cargado")
        print("3) Crear archivo por tipo de trabajo")
        print("4) Mostrar el archivo")
        print("5) Búsqueda de un profesional")
        print("6) Matriz de conteo")
        print("7) Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            funciones_colegio_pro.cargar_vector(vec)
        elif opcion == 2:
            funciones_colegio_pro.display(vec)
        elif opcion == 3:
            funciones_colegio_pro.grabar_archivo_tipo_trabajo(fd, vec)
        elif opcion == 4:
            funciones_colegio_pro.mostrar_archivo(fd)
        elif opcion == 5:
            nom = input("Ingrese el nombre del profesional a buscar: ")
            funciones_colegio_pro.busqueda_profesional(vec, nom)
        elif opcion == 6:
            mat = funciones_colegio_pro.matriz_conteo(vec)
            funciones_colegio_pro.mostrar_matriz(mat)
        else:
            print("PROGRAMA FINALIZADO")









if __name__ == "__main__":
    principal()