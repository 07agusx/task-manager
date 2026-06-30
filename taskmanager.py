tareas = []

def add_task(tareas, task):
    if len(task.strip("")) <= 0 or task.isdigit():
        print("Por favor ingrese una tarea valida.")
    else:
        tareas.append({"nombre": task, "completada": False})
        print(f"Nueva tarea agregada: {tareas}")

def validation_task(tareas, indice):
    if indice >= len(tareas) or indice < 0:
        return False
    else:
        return True

def complete_task(tareas, indice):
    if validation_task(tareas, indice):
        tareas[indice]["completada"] = True
        print(f"El estado de la siguiente tarea fue actualizada: {tareas[indice]}")
    else:
        print("Por favor ingrese una posición de la lista de tareas válida.")

def delete_task(tareas, delete):
    if validation_task(tareas, delete):
         print(f"La siguiente tarea fue eliminada: {tareas.pop(delete)}")
    else:
        print("Por favor ingrese una posición de la lista de tareas válida.")

while True:
    print("")
    print("¡Bienvenido al --Gestor de tareas-- !")
    print("""
            - - - Opciones - - -
          
1 = Añadir una tarea
2 = Completar una tarea
3 = Eliminar una tarea
4 = Mostrar la lista de tareas
5 = Salir del programa
          """)
    
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            añadir = input("Ingrese el nombre de la tarea que desea añadir: ")
            add_task(tareas, añadir)
        case "2":
            try:
                actualizar = int(input("Ingrese la posición de la tarea que desea actualizar: "))
            except ValueError:
                print("Ingrese una posición númerica válida.")
            else:
                complete_task(tareas, actualizar)
        case "3":
            try:
                eliminar = int(input("Ingrese la posición de la tarea que desea eliminar: "))
            except ValueError:
                print("Ingrese una posición númerica válida.")
            else:
                delete_task(tareas, eliminar)
        case "4":
            if len(tareas) > 0:
                print("--Lista de tareas--")
                print(tareas)
            else:
                print("La lista se encuentra vacia, agrega tareas para visualizarla.")
        case "5":
            print("Saliendo del gestor de tareas...")
            break
        case _:
            print("ERROR: Por favor ingrese una opción valida.")

 