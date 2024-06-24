import json, time;

def listar_trabajadores():
    print("Ha elegido listar trabajadores.");
    try:
        with open('trabajadores.json', 'r', encoding='utf-8') as archivo:
            trabajadores=json.load(archivo);
    except:
        print("No hay trabajadores para listar, intente agregando trabajadores para comenzar.");
    else:
        for i in range(len(trabajadores)):
            print(f"Trabajador {i+1}");
            trabajador=(trabajadores[i]);
            print(f"Nombre: {trabajadores['nombre']}\nApellido: {trabajadores['apellido']}\nCargo: {trabajadores['cargo']}\n");
