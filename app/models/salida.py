from app.models.movimiento import Movimiento

class Salida(Movimiento):
    def __init__(self, insumo, cantidad, motivo):
        super().__init__(insumo, cantidad)
        self.__motivo = motivo

    def realizar_movimiento(self):
        return self.get_insumo().retirar_stock(self.get_cantidad())

    def __str__(self):
        return f"SALIDA -> Insumo: {self.get_insumo().get_nombre()}, Cantidad: {self.get_cantidad()}, Motivo: {self.__motivo}"