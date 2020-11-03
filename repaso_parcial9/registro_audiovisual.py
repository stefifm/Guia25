


class Licenciantes:
    def __init__(self, cod, nom, total, idio, pais):
        self.codigo = cod
        self.nombre = nom
        self.total = total
        self.idioma = idio
        self.pais = pais


def to_string(licenciantes):
    r = " "
    r += "Código del licenciante: " + str(licenciantes.codigo)
    r += " - Nombre: " + licenciantes.nombre
    r += " - Total a pagarle: " + "$" + str(licenciantes.total)
    r += " - Idioma: " + str(licenciantes.idioma)
    r += " - País: " + str(licenciantes.pais)
    return r