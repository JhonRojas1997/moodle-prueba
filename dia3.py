idd = 000
biblioteca = {
}
while True:
    print("Menu biblioteca")
    print("[1] Para ingresar libro")
    print("[2] Para ver libros")
    print("[3] Para buscar libro")
    print("[4] Modificar libro")
    print("[5] Eliminar libro")
    menu = int(input("Digite una opcion: "))
    if menu == 1:
        nombre = str(input("Digite el nombre del libro: "))
        autor = str(input("Digite el autor del libro: "))
        fecha = int(input("Digite el año del libro: "))
        idd = idd + 1
        biblioteca[idd] = {"Nombre": nombre, "Autor": autor, "Fecha": fecha }
    elif menu == 2:
        for clave, valor in biblioteca.items():
         print(f"{clave}: {valor}")
        
    elif menu == 3:
        buscar = str(input("Digite id de librio a buscar"))
        if buscar in biblioteca:
            libro = biblioteca[buscar]
            print(libro)    
    elif menu == 4:
        id2 = int(input("Digite id de libro a modificar"))
        if id2 in biblioteca:
            nombre = str(input("Digite el nombre del libro: "))
            autor = str(input("Digite el autor del libro: "))
            fecha = int(input("Digite el año del libro: "))
            biblioteca[id2]["Nombre"] = nombre
            biblioteca[id2]["Autor"] = autor
            biblioteca[id2]["Fecha"] = fecha
        else:
            print("No se encuntra este id")

    elif menu == 5:
        print("eliminar libr0")
        numero = int(input("digita la key del libro a eliminar"))
        biblioteca.pop(numero)
    salir = str(input("Desea volver al menu? "))
    if salir == "no":
        break

