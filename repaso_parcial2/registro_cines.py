


class Pelicula:
    def __init__(self, num, titulo, imp, tipo, pais):
        self.numero = num
        self.titulo = titulo
        self.importe = imp
        self.tipo = tipo
        self.pais = pais

def cadena_tipo(cod_tip):
    if cod_tip < 0 and cod_tip > 9:
        return "Valor no válido"
    tipos = ("Acción", "Comedia", "Drama", "Suspenso", "Terror", "Musical",
             "Documental", "Animado", "Fantasía", "Época")
    return tipos[cod_tip]

def cadena_pais(cod_pais):
    if cod_pais < 0 and cod_pais > 19:
        return "Valor no válido"
    paises = ("Argentina", "España", "EEUU", "Italia", "Francia",
              "Gran Bretaña", "México", "Portugal", "Corea", "Brasil",
              "Noruega", "India", "China", "Japón", "Hungría", "Rusia",
              "Polonia", "Alemania", "Uruguay", "Chile")
    return paises[cod_pais]


def to_string(pelicula):
    r = " "
    r += "Número: " + str(pelicula.numero)
    r += " - Título: " + pelicula.titulo
    r += " - Importe: " + str(pelicula.importe)
    r += " - Tipo: " + str(pelicula.tipo) + "." + cadena_tipo(pelicula.tipo)
    r += " - País de Origen: " + str(pelicula.pais) + "." +  cadena_pais(
        pelicula.pais)
    return r