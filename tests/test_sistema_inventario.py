import pytest

from app.domain.exceptions import ProveedorYaExiste, InsumoYaExiste
from app.models.sistema_inventario import SistemaInventario
from app.models.insumo import Insumo
from app.models.proveedor import Proveedor

def test_crear_insumo_existente():
    with pytest.raises(InsumoYaExiste):
        sistema = SistemaInventario(5)

        sistema.agregar_insumo(Insumo('I001', 'Arroz', 'kg', 10, 5.50))
        sistema.agregar_insumo(Insumo('I001', 'Azúcar', 'kg', 20, 7))

def test_registrar_insumo_existente():
    with pytest.raises(ProveedorYaExiste):
        sistema = SistemaInventario(10)

        sistema.agregar_proveedor(Proveedor("P001", "Proveedor Mariscos EIRL", "20603822293"))
        sistema.agregar_proveedor(Proveedor("P001", "Distribuidora Makis", "21648372934"))