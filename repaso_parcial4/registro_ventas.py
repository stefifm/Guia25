"""
Registro del tipo Ventas
"""


class Venta:
    def __init__(self, num, desc, mont, art, ven):
        self.numero = num
        self.descripcion = desc
        self.monto = mont
        self.articulo = art
        self.vendedor = ven


def to_string(venta):
    r = " "
    r += "Número de venta: " + str(venta.numero)
    r += " - Descripción: " + venta.descripcion
    r += " - Monto: $" + str(venta.monto)
    r += " - Artículo: " + str(venta.articulo)
    r += " - Vendedor: " + str(venta.vendedor)
    return r
