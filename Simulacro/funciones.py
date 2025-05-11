students = {
    "1" : {"Name": "Jhon Rojas", "Age": 28, "Note": 4},
    "2" : {"Name": "Juan Ramirez", "Age": 20, "Note": 3},
    "3" : {"Name": "Steven Cardona", "Age": 18, "Note": 5},
    "4" : {"Name": "Andres Mercado", "Age": 45, "Note": 1},
    "5" : {"Name": "Antonio Gonzales", "Age": 65, "Note": 2}
}
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"
def add():
    # Se agrega la funcion para agregar lkos valores a al diccionario estudiantes
    id = input("Digite numero de documento")
    #Se verifica si el valor id es un numero sin signos ni caracteres especiales
    if id.isdigit():
        if id in students:
            print(DANGER + "Este documento ya se encuentra registrado." + RESET)
        else:
            name = input("Digite su nombre completo")
            age = input("Digite edad estudiante")
            note = input("Digite nota estudiante")
            if int(note) >=0 and int(note) <=5:
                if age.isdigit() and note.isdigit:
                    students[id] = {"Name": name, "Age": age, "Note": note}
                    print(SUCCESS + "Operación exitosa." + RESET)
            else:
                print(DANGER + "El valor de nota debe estar entre 0 -5" + RESET)
    else:
        print(DANGER + "Solo debes usar numeros, no signos ni letras" + RESET)
def search():
    # Se agrega la funcion para buscar los valores en el diccionario estudiantes con el id
    id = input("Digite numero de documento o nombre del estudiante")
    if id in students:
        name = students[id]["Name"]
        age = students[id]["Age"]
        note = students[id]["Note"]
        print(f"Documento: {id}")
        print(f"Nombre: {name}")
        print(f"Edad: {age}")
        print(f"Nota: {note}")
    else:
        for i, names in students.items():
            if names["Name"] == id:
                name = names["Name"]
                age = names["Age"]
                note = names["Note"]
                print(f"Nombre: {name}")
                print(f"Edad: {age}")
                print(f"Nota: {note}")
        else:
            print("Este usuario no existe")
            
def update():
    # Se agrega la funcion para actualizar los valores en el diccionario estudiantes con el id
    id = input("Digite numero de documento")
    if id.isdigit():
        if id in students:
            name = input("Digite su nombre completo")
            age = input("Digite edad estudiante")
            note = input("Digite nota estudiante")
            if note.isdigit() and age.isdigit():
                students[id]["Name"] = name  
                students[id]["Age"] = age
                students[id]["Note"] = note
                print(SUCCESS + "Operación exitosa." + RESET)
            else:
                print(DANGER + "Solo debes usar numeros, no signos ni letras" + RESET) 
        else:
            print(WARNING + "Este documento no existe." + RESET)
    else:
        print(DANGER + "Solo debes usar numeros, no signos ni letras" + RESET) 

    
def delete():
    # Se agrega la funcion para eliminar el calor especificado en el diccionario estudiantes con el id
    id = input("Digite numero de documento de estudiante a eliminar")
    if id.isdigit():
        if id in students:
            students.pop[id]
            print(SUCCESS + "Operación exitosa." + RESET)
        else:
            print(WARNING + "Este documento no existe." + RESET)
    else:
            print("Solo debes usar numeros, no signos ni letras")   
def calculate():
    #Se agrega la funcion para calcuñar en promedio de las notas de todos los estudiantes
    sum_stats = 0
    for i, notes in students.items():
        sum_stats = int(sum_stats)
        sum_stats += float(notes["Note"])
        can = len(students)
        stats = sum_stats / can
    print(SUCCESS + "Operación exitosa." + RESET)
    print(stats)
def thelist():
    #Se crea la funcion para imprimir los nobres y notas de todos los estudiantes por debajo de 3
    total_dates = 0
    total_notes = 0
    for i, dates in students.items():
        if float(dates["Note"]) <= 3:
            total_dates = dates["Name"]
            total_notes = dates["Note"]
        print(f" Nombre: {total_dates} Nota: {total_notes}")
    print(SUCCESS + "Operación exitosa." + RESET)
        