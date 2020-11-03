


class Compras:
    def __init__(self, num_cupon, num_cli, nom_cli, monto, pais, rub):
        self.nro_cupon = num_cupon
        self.nro_cliente = num_cli
        self.nom_cliente = nom_cli
        self.monto = monto
        self.pais = pais
        self.rubro = rub


def to_string(compras):
    r = " "
    r += "Número de cupón: " + str(compras.nro_cupon)
    r += " - Número de cliente: " + str(compras.nro_cliente)
    r += " - Nombre del cliente: " + str(compras.nom_cliente)
    r += " - Monto: $" + str(compras.monto)
    r += " - País: " + str(compras.pais)
    r += " - Rubro: " + str(compras.rubro)
    return r
