# Se crea una variable llamada total y se da u valor inicial de cero
total = 0
print("Bienvenid@")
# Se crea bucle while  para que la secuencia se repita hasta que le de un break
while True: 
    # Se registra el nombre del producto en una variable 
    nombre = str(input("Digite el nombre del producto: "))
    while True:
            #Se le da a la variable el tipo entero y le decimos que en caso de que la variable valor sea mayor a 0 rompa el ciclo para que continue al siguiente paso de lo contrario de un error que diga que el valor debe ser mayor a 0
            valor = input("Digite el valor: ")
            try:
                valor = int(valor)
                if valor > 0:               
                    break
                else:
                    print("El precio debe ser un valor positivo. Intente nuevamente.")
                    #Se le dice que haga una excepcion y que en el caso de que el valor que se ingresa no sea del tipo que debe ser de un mensaje de valor invalido
            except ValueError:
             print("Valor invalido.")
    while True:
            desc = input("Digite el descuento: ")
            try:
                desc = int(desc)
                if 0 <= desc <= 100:             
                    break
                else:
                    print("El descuento debe estar entre 0 - 100")
            except ValueError:
             print("Valor invalido.")
    while True:
        cantidad = input("Ingrese la cantidad de: ")
        try:
            cantidad = int(cantidad)
            #se hace la operacion adecuada para calcular el total a pagar del producto y se guarda en la variable valor
            if cantidad > 0:
                total = valor * cantidad *(1 - desc / 100) 
                
                #se imprime en pantalla el valor total a pagar del producto
                print(f"El total es de: {total}")
                break
            else:
                print("La cantidad debe ser un valor positivo. Intente nuevamente.")
        except ValueError:
            print("Valor invalido.")
            #Se da una opcion de si desea agregar otro producto en el caso de dar n Se da un break y se sale del ciclo principal y en el caso de dar s se repite el ciclo desde el nombre del producto
    continuar = input("¿Desea agregar otro producto? (s/n): ")
    if continuar == "n":
        break            
    
    
        

        
    