"""
Registro del colegio de profesionales
"""

class Profesional:
    def __init__(self, dni, nom, imp, afil, trab):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.afiliacion = afil
        self.trabajo = trab

def cadena_afiliacion(cod_afil):
    if cod_afil < 0 and cod_afil > 4:
        return "Valor inválido"
    afiliacion = ("Vitalicio", "Transitorio", "Indirecto", "Directo",
                  "Completo")
    return afiliacion[cod_afil]

def cadena_trabajo(cod_tra):
    if cod_tra < 0 and cod_tra > 14:
        return "Valor inválido"
    trabajos = ("Empleado", "Jefe o Director", "Administrativo", "Gerencia",
                "Técnico", "Limpieza", "Recursos Humanos", "Mecánico",
                "Vendedor", "Mantenimiento", "Contador", "Cajero",
                "Banquero", "Programador", "Tester")
    return trabajos[cod_tra]


def to_string(profesional):
    r = " "
    r += "DNI: " + str(profesional.dni)
    r += " - Nombre: " + profesional.nombre
    r += " - Importe: " + str(profesional.importe)
    r += " - Afiliación: " + str(profesional.afiliacion) + "." + \
         cadena_afiliacion(profesional.afiliacion)
    r += " - Trabajo: " + str(profesional.trabajo) + "." + cadena_trabajo(
        profesional.trabajo)
    return r

