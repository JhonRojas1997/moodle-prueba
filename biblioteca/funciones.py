inventario = {}
nombre = ""
precio = ""
stock = ""
cantidad = ""
total = 0
total2 = 0
def agregar(nombre, precio, stock):
    while True:
        nombre = input("Digite el nombre: ")
        if nombre in inventario:
            print("Este producto ya se encuentra en inventario")
        else:
            precio = input("Digite el precio por unidad: ")
            stock = input("Digite la cantidad actual de stock en el inventario ")
            if precio.isdigit() and stock.isdigit() and float(precio) > 0 and int(stock) > 0:
                inventario[nombre] = {"Precio": precio, "Cantidad": stock}
                print(inventario)
                break
            else:
                print("Precio y stock deben ser valores numericos y mayores a 0")
def consultar(nombre, precio, cantidad):
    while True:
        nombre = input("Digite el nombre del producto a buscar: ")
        if nombre in inventario:              
            cantidad = inventario[nombre]["Cantidad"]
            precio = inventario[nombre]["Precio"]
            print(f"Nombre: {nombre}")
            print(f"Precio: {precio}")
            print(f"Cantidad: {cantidad}")
            break       
        else:
            print("Este producto no se encuentra en inventario")
            break
def actualizar(nombre, precio, stock):
    while True:
        nombre = input("Digite el nombre del producto a modificar: ")
        if nombre in inventario:
            precio = input("Digite el precio por unidad: ")
            stock = input("Digite la cantidad a sumar en el stock del producto: ")
            if precio.isdigit() and stock.isdigit() and float(precio) > 0 and int(stock) > 0:
                inventario[nombre]["Precio"] = precio
                inventario[nombre]["Cantidad"] = int(inventario[nombre]["Cantidad"]) + int(stock)
                break
            else:
                print("Precio y stock deben ser valores numericos y mayores a 0")
        else:
            print("Este producto no se encuentra en inventario")
            break
def eliminar(nombre):
    while True:
        nombre = input("Digite el nombre del producto a eliminar: ")
        if nombre in inventario:
            inventario.pop(nombre)
            break
def total(total2, total):
    while True:
        total = lambda productos: sum(float(p["Precio"]) * int(p["Cantidad"]) for p in inventario.values())
        total2 = total(inventario)
        print(f"El total de todos los productos en inventario es: {total2}")
        break