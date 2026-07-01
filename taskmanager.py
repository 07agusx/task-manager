tareas = []
cont_ids = 0 # Contador que se utilizara para darle valor a las IDs de las tareas


def add_task(tareas, task):
    global cont_ids
    if len(task.strip("")) <= 0 or task.isdigit(): # Verificar si la tarea cumple con los requisitos para añadirla
        print("Por favor ingrese una tarea valida.")
    else:
        tareas.append({"id": cont_ids, "nombre": task, "completada": False}) # Añadir la tarea
        cont_ids +=1 # Sumarle un 1 al contador para que la proxima tarea tenga un ID diferente
        print(f"Nueva tarea agregada: ID = {tareas[-1]['id']} | Nombre = {tareas[-1]['nombre']} | Completada = {tareas[-1]['completada']}")

def complete_task(tareas, ids):
    for tarea in tareas: #Buscar dentro del diccionario el ID que el usuario ingreso y verificar si se encuentra dentro de este
        if ids == tarea["id"]: 
            tarea["completada"] = True
            print(f"La siguiente tarea fue completada: {tarea}")
            break
    else:
        print("Ingrese un ID válido. Si no sabe cuales son los ID, utilice la opción 4.")

def delete_task(tareas, ids):
    for tarea in tareas: #Buscar dentro del diccionario el ID que el usuario ingreso y verificar si se encuentra dentro de este
        if ids == tarea["id"]: 
                print(f"La siguiente tarea fue eliminada: {tarea}")
                tareas.remove(tarea)  # Eliminamos el elemento especifico que el usuario pidio ingresando su ID
                break
    else:
        print("Ingrese un ID válido. Si no sabe cuales son los ID, utilice la opción 4.")

def show_task(tareas):
    for tarea in tareas:
        print(f"ID = {tarea["id"]} | Nombre = {tarea["nombre"]} | Completada = {tarea["completada"]}")

while True:
    print("")
    print("¡Bienvenido al --Gestor de tareas-- !")
    print("""
            - - - Opciones - - -
          
1 = Añadir una tarea
2 = Completar una tarea
3 = Eliminar una tarea
4 = Mostrar la lista de tareas y IDs
5 = Salir del programa
          """)
    
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            añadir = input("Ingrese el nombre de la tarea que desea añadir: ")
            add_task(tareas, añadir)
        case "2":
            try:
                actualizar = int(input("Ingrese el ID de la tarea que desea actualizar: "))
            except ValueError:
                print("Ingrese un ID válido.")
            else:
                complete_task(tareas, actualizar)
        case "3":
            try:
                eliminar = int(input("Ingrese el ID de la tarea que desea eliminar: "))
            except ValueError:
                print("Ingrese un ID válido.")
            else:
                delete_task(tareas, eliminar)
        case "4":
            if len(tareas) > 0:
                print("--Lista de tareas--")
                task_deco(tareas)
            else:
                print("La lista se encuentra vacia, agrega tareas para visualizarla.")
        case "5":
            print("Saliendo del gestor de tareas...")
            break
        case _:
            print("ERROR: Por favor ingrese una opción valida.")

 