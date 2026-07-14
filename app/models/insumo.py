from app.domain.exceptions import StockInsumoInsuficiente

class Insumo:
    def __init__(self, codigo: str, nombre: str, unidad: str, stock: int, precio: float):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__unidad = unidad
        self.__stock = stock
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_stock(self):
        return self.__stock
    
    def get_precio(self):
        return self.__precio

    def ingresar_stock(self, cantidad):
        self.__stock = self.__stock + cantidad

    def retirar_stock(self, cantidad):
        if cantidad > self.__stock:
            raise StockInsumoInsuficiente()
        self.__stock = self.__stock - cantidad

    def __str__(self):
        return f"Codigo: {self.__codigo} | Insumo: {self.__nombre} | Unidad: {self.__unidad} | Stock: {self.__stock} | Precio: {self.__precio}"