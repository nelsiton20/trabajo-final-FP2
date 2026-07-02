class Insumo:
    def __init__(self, codigo, nombre, unidad, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__unidad = unidad
        self.__stock = stock

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_stock(self):
        return self.__stock

    def ingresar_stock(self, cantidad):
        self.__stock = self.__stock + cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock = self.__stock - cantidad
            return True
        else:
            return False

    def __str__(self):
        return f"Codigo: {self.__codigo} | Insumo: {self.__nombre} | Unidad: {self.__unidad} | Stock: {self.__stock}"


class Proveedor:
    def __init__(self, codigo, nombre, ruc):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__ruc = ruc

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"Codigo: {self.__codigo}, Proveedor: {self.__nombre}, RUC: {self.__ruc}"


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


class Ingreso(Movimiento):
    def __init__(self, insumo, cantidad, proveedor):
        super().__init__(insumo, cantidad)
        self.__proveedor = proveedor

    def realizar_movimiento(self):
        self.get_insumo().ingresar_stock(self.get_cantidad())

    def __str__(self):
        return f"INGRESO -> Insumo: {self.get_insumo().get_nombre()}, Cantidad: {self.get_cantidad()}, Proveedor: {self.__proveedor.get_nombre()}"


class Salida(Movimiento):
    def __init__(self, insumo, cantidad, motivo):
        super().__init__(insumo, cantidad)
        self.__motivo = motivo

    def realizar_movimiento(self):
        return self.get_insumo().retirar_stock(self.get_cantidad())

    def __str__(self):
        return f"SALIDA -> Insumo: {self.get_insumo().get_nombre()}, Cantidad: {self.get_cantidad()}, Motivo: {self.__motivo}"


class SistemaInventario:
    def __init__(self):
        self.__insumos = []
        self.__proveedores = []
        self.__movimientos = []

    def agregar_insumo(self, insumo):
        self.__insumos.append(insumo)

    def agregar_proveedor(self, proveedor):
        self.__proveedores.append(proveedor)

    def buscar_insumo(self, codigo):
        for insumo in self.__insumos:
            if insumo.get_codigo() == codigo:
                return insumo
        return None

    def buscar_proveedor(self, codigo):
        for proveedor in self.__proveedores:
            if proveedor.get_codigo() == codigo:
                return proveedor
        return None

    def registrar_ingreso(self, codigo_insumo, cantidad, codigo_proveedor):
        insumo = self.buscar_insumo(codigo_insumo)
        proveedor = self.buscar_proveedor(codigo_proveedor)

        if insumo != None and proveedor != None:
            ingreso = Ingreso(insumo, cantidad, proveedor)
            ingreso.realizar_movimiento()
            self.__movimientos.append(ingreso)
            print("Ingreso registrado correctamente.")
        else:
            print("No se encontro el insumo o proveedor.")

    def registrar_salida(self, codigo_insumo, cantidad, motivo):
        insumo = self.buscar_insumo(codigo_insumo)

        if insumo != None:
            salida = Salida(insumo, cantidad, motivo)
            resultado = salida.realizar_movimiento()

            if resultado == True:
                self.__movimientos.append(salida)
                print("Salida registrada correctamente.")
            else:
                print("No hay stock suficiente.")
        else:
            print("No se encontro el insumo.")

    def listar_insumos(self):
        print("\n--- LISTA DE INSUMOS ---")
        for insumo in self.__insumos:
            print(insumo)

    def listar_proveedores(self):
        print("\n--- LISTA DE PROVEEDORES ---")
        for proveedor in self.__proveedores:
            print(proveedor)

    def listar_movimientos(self):
        print("\n--- MOVIMIENTOS ---")
        for movimiento in self.__movimientos:
            print(movimiento)

def main():
    sistema = SistemaInventario()

    proveedor1 = Proveedor("P001", "Proveedor Mariscos EIRL", "20603822293")
    proveedor2 = Proveedor("P002", "Distribuidora Makis", "21648372934")

    sistema.agregar_proveedor(proveedor1)
    sistema.agregar_proveedor(proveedor2)

    insumo1 = Insumo("I001", "Pescado", "kg", 10)
    insumo2 = Insumo("I002", "Arroz", "kg", 20)
    insumo3 = Insumo("I003", "Nori", "caja", 5)

    sistema.agregar_insumo(insumo1)
    sistema.agregar_insumo(insumo2)
    sistema.agregar_insumo(insumo3)

    opcion = 0

    while opcion != 6:
        print("\n------ SISTEMA DE INVENTARIO ------")
        print("1. Listar insumos")
        print("2. Listar proveedores")
        print("3. Registrar ingreso")
        print("4. Registrar salida")
        print("5. Listar movimientos")
        print("6. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            sistema.listar_insumos()

        elif opcion == 2:
            sistema.listar_proveedores()

        elif opcion == 3:
            codigo_insumo = input("Ingrese codigo del insumo: ")
            cantidad = int(input("Ingrese cantidad a ingresar: "))
            codigo_proveedor = input("Ingrese codigo del proveedor: ")

            sistema.registrar_ingreso(codigo_insumo, cantidad, codigo_proveedor)

        elif opcion == 4:
            codigo_insumo = input("Ingrese codigo del insumo: ")
            cantidad = int(input("Ingrese cantidad a retirar: "))
            motivo = input("Ingrese motivo de salida: ")

            sistema.registrar_salida(codigo_insumo, cantidad, motivo)

        elif opcion == 5:
            sistema.listar_movimientos()

        elif opcion == 6:
            print("Gracias por usar el sistema.")

        else:
            print("Opcion no valida.")


main()
