from app.models.movimiento import Movimiento

class Ingreso(Movimiento):
    def __init__(self, insumo, cantidad, proveedor):
        super().__init__(insumo, cantidad)
        self.__proveedor = proveedor

    def realizar_movimiento(self):
        self.get_insumo().ingresar_stock(self.get_cantidad())

    def __str__(self):
        return f"INGRESO -> Insumo: {self.get_insumo().get_nombre()}, Cantidad: {self.get_cantidad()}, Proveedor: {self.__proveedor.get_nombre()}"