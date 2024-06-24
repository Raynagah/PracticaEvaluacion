#Importamos las funciones que utilizaremos a lo largo del código.
import json, time;
#Creamos la función para listar a los trabajadores
def listar_trabajadores():
    print("Ha elegido listar trabajadores.");
    try:
        #Abrimos el archivo que contiene a los trabajadores en modo lectura.
        with open('trabajadores.json', 'r', encoding='utf-8') as archivo:
            trabajadores=json.load(archivo);
    except:
        print("No hay trabajadores para listar, intente agregando trabajadores para comenzar.");
    else:
        #Incorporamos un ciclo For que utilice el archivo de trabajadores como base para el recorrido que debe hacerse.
        for i in range(len(trabajadores)):
            print(f"Trabajador {i+1}");
            trabajador=(trabajadores[i]);
            print(f"Nombre: {trabajadores['nombre']}\nApellido: {trabajadores['apellido']}\nCargo: {trabajadores['cargo']}\n");