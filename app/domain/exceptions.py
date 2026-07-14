class DomainError(Exception):
    message = 'Error de dominio'

    def __init__(self):
        super().__init__(self.message)

class InsumoNotFound(DomainError):
    message = "Insumo no encontrado"

class StockInsumoInsuficiente(DomainError):
    message = "No hay suficiente stock del insumo"

class ProveedorNotFound(DomainError):
    message = 'Proveedor no encontrado'

class InsumoYaExiste(DomainError):
    message = 'El insumo ya se encuentra registrado'

class ProveedorYaExiste(DomainError):
    message = 'El proveedor ya se encuentra registrado'