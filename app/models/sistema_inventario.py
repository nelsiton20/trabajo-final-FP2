from app.models.ingreso import Ingreso
from app.models.salida import Salida
from app.models.proveedor import Proveedor
from app.models.insumo import Insumo
from app.domain.exceptions import InsumoNotFound, DomainError, ProveedorNotFound, InsumoYaExiste, ProveedorYaExiste

class SistemaInventario:
    def __init__(self, stock_minimo: int):
        self.__insumos: list[Insumo] = []
        self.__proveedores: list[Proveedor] = []
        self.__movimientos = []
        self.__stock_minimo = stock_minimo

    def agregar_insumo(self, insumo):
        self.__insumos.append(insumo)

    def agregar_proveedor(self, proveedor):
        self.__proveedores.append(proveedor)

    def producto_esta_registrado(self, codigo: str) -> bool:
        for insumo in self.__insumos:
            if insumo.get_codigo() == codigo:
                raise InsumoYaExiste()
    
    def proveedor_esta_registrado(self, codigo: str) -> bool:
        for proveedor in self.__proveedores:
            if proveedor.get_codigo() == codigo:
                raise ProveedorYaExiste()
    
    def buscar_insumo(self, codigo):
        for insumo in self.__insumos:
            if insumo.get_codigo() == codigo:
                return insumo
        
        raise InsumoNotFound()

    def buscar_proveedor(self, codigo):
        for proveedor in self.__proveedores:
            if proveedor.get_codigo() == codigo:
                return proveedor
        raise ProveedorNotFound()

    def registrar_ingreso(self, codigo_insumo, cantidad, codigo_proveedor):
        try:
            insumo = self.buscar_insumo(codigo_insumo)
            proveedor = self.buscar_proveedor(codigo_proveedor)

            ingreso = Ingreso(insumo, cantidad, proveedor)
            ingreso.realizar_movimiento()
            self.__movimientos.append(ingreso)
            print("Ingreso registrado correctamente.")
        except DomainError as e:
            print("--------------")
            print(e)
            print("--------------")

    def registrar_salida(self, codigo_insumo, cantidad, motivo):
        try:
            insumo = self.buscar_insumo(codigo_insumo)
            
            if insumo is None:
                raise InsumoNotFound()
            
            salida = Salida(insumo, cantidad, motivo)
            salida.realizar_movimiento()
            self.__movimientos.append(salida)
            print("Salida registrada correctamente.")
        except DomainError as e:
            print('----------------')
            print(e)
            print('----------------')

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

    def alerta_stock_minimo(self):
        if not self.__insumos:
            print('No hay insumos registrados en el kardex')
            return

        print('PRODUCTOS CON STOCK BAJO')
        for insumo in self.__insumos:
            if insumo.get_stock() <= self.__stock_minimo:
                print(insumo)