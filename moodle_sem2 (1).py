calificaciones = []
print("======Bienvenido al sistema de notas Riwi======")
while True:
    print("[1] Ingresar sus notas\n[2] Buscar notas mayores\n[3] Buscar notas repetidas\n[4] Salir")
    try:
        menu = int(input("Elija una opcion: "))
        if menu == 1:
            while True:
                try:
                    notas = input("Digite sus notas separadas por comas (0 - 100): ")
                    calificaciones = [int(calificacion) for calificacion in notas.split(',')]
                    if all( 0 <= i <= 100 for i in calificaciones):
                        promedio = sum(calificaciones) / len(calificaciones)
                        if promedio >= 0 and promedio <= 70:
                            print(f"Su promedio es de: {promedio} usted ha reprobado")
                            break
                        elif promedio > 70 and promedio <= 100:
                            print(f"Su promedio es de: {promedio} usted ha aprobado" )
                            break
                    else:
                        print("Digite un valor entre 0 - 100")
                except (ValueError, KeyboardInterrupt):
                    print("Valor invalido")
        elif menu == 2:
            while True:
                try:
                    buscar = int(input("Digite la nota a buscar: "))
                    if buscar >= 0 and buscar <= 100:
                        mayores = [numero for numero in calificaciones if numero > buscar]
                        tam = len(mayores)
                        if tam == 0:
                            print("No hay notas mayores")
                            break
                        else:
                            print(f"Las siguientes notas son mayores: {mayores}")
                            print(f"La cantidad de numeros mayores son {tam}") 
                            break
                    else:
                        print("La nota debe estar entre 0 - 100")
                except (ValueError, KeyboardInterrupt):
                    print("Valor invalido")
        elif menu == 3:
            while True:        
                try:
                    buscar2 = int(input("Digite la nota a buscar: "))
                    cuenta = calificaciones.count(buscar2)
                    if buscar2 >= 0 and buscar2 <= 100:
                        if cuenta == 0:
                            print("Esta nota no existe")
                            break
                        elif cuenta == 1:
                            print(f"La nota {buscar2} no se encuentra repetida ")
                            break
                        elif cuenta >1:
                            print(f"La nota {buscar2} esta repetida en {cuenta} ocasion/es")
                            break
                    else:
                        print("La nota debe estar entre 0 - 100")
                except (ValueError, KeyboardInterrupt):
                        print("valor invalido")
        elif menu == 4:
            break
        else:
            print("numero invalido") 
    except (ValueError, KeyboardInterrupt):
        print("Valor invalido")      