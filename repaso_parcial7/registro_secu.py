


class Secundario:
    def __init__(self, leg, nom, anio, dep):
        self.legajo = leg
        self.nombre = nom
        self.anio = anio
        self.deporte = dep


def to_string(secundario):
    r = " "
    r += "Legajo: " + str(secundario.legajo)
    r += " - Nombre:  " + secundario.nombre
    r += " - Año: " + str(secundario.anio)
    r += " - Deporte: " + str(secundario.deporte)
    return r