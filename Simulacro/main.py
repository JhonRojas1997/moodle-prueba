from funciones import *
print("Bienvenido")
while True:
    print("[1] Para ingresar estudiante")
    print("[2] Para buscar estudiante")
    print("[3] Para actualizar informacion estudiante")
    print("[4] Para eliminar estudiante")
    print("[5] Para calcular promedio estudiantes")
    print("[6] Para listar estudiantes nota menor a 3")
    print("[7] Salir")
    menu = int(input("Digite una opcion"))
    if menu == 1:
        add()
    elif menu == 2:
        search()
    elif menu == 3:
        update()
    elif menu == 4:
        delete()
    elif menu == 5:
        calculate()
    elif menu == 6:
        thelist()
    elif menu == 7:
        break



