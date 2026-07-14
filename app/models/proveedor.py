class Proveedor:
    def __init__(self, codigo: str, nombre: str, ruc: str):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__ruc = ruc

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Codigo: {self.__codigo}, Proveedor: {self.__nombre}, RUC: {self.__ruc}"