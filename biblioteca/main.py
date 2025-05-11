from funciones import *
print("Bienvenido a Riwi inventario")
while True:
    print("[1] para ingresar productos")
    print("[2] para consultar productos")
    print("[3] para actualizar precios")
    print("[4] para eliminar producto")
    print("[5] Calcular valor total inventario")
    print("[6] Salir")
    menu = input("Digite una opcion: ")
    if menu == "1":
        agregar(nombre, precio, stock)
    elif menu == "2":
        consultar(nombre, precio, cantidad)
    elif menu == "3":
        actualizar(nombre, precio, stock)
    elif menu == "4":
        eliminar(nombre)
    elif menu == "5":
            total(total2, total)
    elif menu == "6":
            break
    else:
        print("El valor es invalido")
    continuar = input("Desea regresar al menu? (n/s)")
    if continuar == "n":
         break
