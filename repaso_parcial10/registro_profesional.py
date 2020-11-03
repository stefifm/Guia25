

class Profesional:
    def __init__(self, dni, nom, imp, fili, trab):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.filiacion = fili
        self.trabajo = trab


def to_string(profesional):
    r = " "
    r += "DNI: " + str(profesional.dni)
    r += " - Nombre: " + profesional.nombre
    r += " - Importe: " + "$" + str(profesional.importe)
    r += " - Filiación: " + str(profesional.filiacion)
    r += " - Trabajo: " + str(profesional.trabajo)
    return r