

class Invitado:
    def __init__(self, nom, mesa, ong, don):
        self.nombre = nom
        self.mesa = mesa
        self.ong = ong
        self.donacion = don


def cadena_ong(cod_ong):
    if cod_ong < 0 and cod_ong > 9:
        return "Valor no válido"
    ongs = ("Missing Children", "Caritas", "PUPI", "Medicos Sin Fronteras",
            "Vida Silvestre", "Aldeas", "Fundaleu", "Cimientos",
            "Uniendo Caminos", "Adoptarse")
    return ongs[cod_ong]

def to_string(invitado):
    r = " "
    r += "Nombre del invitado: " + invitado.nombre
    r += " - Mesa: " + str(invitado.mesa)
    r += " - ONG: " + str(invitado.ong) + "." + cadena_ong(invitado.ong)
    r += " - Donación: " + str(invitado.donacion)
    return r

