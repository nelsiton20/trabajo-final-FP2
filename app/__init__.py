from app.models.sistema_inventario import SistemaInventario
from app.models.proveedor import Proveedor
from app.models.insumo import Insumo

def app():
    sistema = SistemaInventario(11)

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

    while opcion != 9:
        print("\n------ SISTEMA DE INVENTARIO ------")
        print("1. Listar insumos")
        print("2. Listar proveedores")
        print("3. Registrar ingreso")
        print("4. Registrar salida")
        print("5. Listar movimientos")
        print('6. Registrar nuevo insumo a inventario')
        print('7. Registrar nuevo proveedor')
        print('8. Mostrar insumos en alerta')
        print("9. Salir")

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
            codigo_insumo = input('Ingrese código del insumo: ')
            
            if sistema.producto_esta_registrado(codigo_insumo):
                print('El insumo ya está registrado')
                continue

            nombre_insumo = input('Ingresa nombre del insumo: ')
            unidad_insumo = input('Ingrese unidad del insumo: ')
            stock_insumo = input('Ingrese el stock del insumo: ')

            sistema.agregar_insumo(Insumo(codigo_insumo, nombre_insumo, unidad_insumo, stock_insumo))
            print('Producto creado y agregado al inventario')

        elif opcion == 7:
            codigo_proveedor = input('Ingrese el código del proveedor: ')

            if sistema.proveedor_esta_registrado(codigo_proveedor):
                print('El proveedor ya se encuentra registrado')    
                continue

            nombre_proveedor = input('Ingresa el nombre del proveedor: ')
            ruc_proveedor = input('Ingresa el ruc del proveedor: ')

            sistema.agregar_proveedor(Proveedor(codigo_proveedor, nombre_proveedor, ruc_proveedor))
            print('Proveedor agregado al sistema correctamente')

        elif opcion == 8:
            sistema.alerta_stock_minimo()

        elif opcion == 9:
            print("Gracias por usar el sistema.")

        else:
            print("Opcion no valida.")