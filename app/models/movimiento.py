class Movimiento:
    def __init__(self, insumo, cantidad):
        self.__insumo = insumo
        self.__cantidad = cantidad

    def get_insumo(self):
        return self.__insumo

    def get_cantidad(self):
        return self.__cantidad

    def realizar_movimiento(self):
        pass