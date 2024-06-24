#4 funciones, login; agregar trabajador; listar trabajadores; imprimir planilla sueldos.

"""
Login
"""
#Funcion de incio de sesion
def funcion_login():

    flag = True

    #Crear usuarios y contraseñas
    usuarios_login = [{"user": "carlos", "password": "123"},{"user": "rodri", "password": "321"}];

    #Guardar informacion de los diccionarios que estan dentro de la lista
    uss = usuarios_login[0];
    uss1 = usuarios_login[1];

    print("\n~Inicio de~ \n ~Sesion~");

    #Ciclo de repeticion para inciar sesion e ingresar al sistema
    while flag == True:

        #Pedir datos al usuario
        user = input("\nIngrese su usuario --> ");
        contra = input("Ingrese su contraseña --> ");

        #Validar datos ingresados del usuario
        if user == uss["user"] and contra == uss["password"]:
            print("\nInicio de sesion exitoso\n");
            flag = False

        elif user == uss1["user"] and contra == uss1 ["password"]:
            print("\nInicio de sesion exitoso\n");
            flag = False

        else:
            print("\nAcceso incorrecto. Intentelo nuevamente...");

"""
Agregar Trabajadores
"""

#Funcion para agregar trabajadores
def funcion_agregar(lista_Trabajadores):

    #Pedirle ingreso de datos al usuario
    nombre = input("\nIngresar nombre: ")
    apellido = input("Ingresar apellido: ")

    #Validar cargos
    print("Cargos: CEO - Desarrollador - Analista de Datos")
    cargos = ["CEO", "Desarrollador", "Analista de Datos"]
    flag1 = True
    while flag1 == True:
        cargo = input("Ingresar cargo: ")
        if cargo in cargos:
            flag1 = False
        else:
            print("Vuelva a intentarlo")

    flag = True
    #Validar sueldo
    while flag == True:
        try:
            sueldo_bruto = int(input("Ingresar sueldo bruto: "))
        except:
            print("El sueldo ingresado debe ser en numeros...")
        else:
            flag = False

    print()

    descuentoSalud = sueldo_bruto * 0.07
    descuentoAFP = sueldo_bruto * 0.12
    sueldoLiquido = sueldo_bruto - descuentoSalud - descuentoAFP

    #Agregar trabajador a un diccionario
    trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargo, "sueldoBruto": sueldo_bruto, "descuentoSalud": descuentoSalud, "descuentoAFP": descuentoAFP, "sueldoLiquido": sueldoLiquido}

    #Agregar el trabajador antes ingresado a una lista de trabajadores
    lista_Trabajadores.append(trabajador)
    print(lista_Trabajadores)

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

#                   Planilla General    
def planillaGeneral(listaTrabajadores):
    import json

    datos=listaTrabajadores

    archivo = "planillaSueldos.json"
    #Creacion de archivo json con la planilla
    with open(archivo, "w", encoding='utf-8') as archivo:
        json.dump(datos, archivo)
    print("La planilla se ha creado correctamente.")

def planillaFiltrada(listaTrabajadores, cargo):
    import json
    listaFiltro=[]
    #Filtrando en la lista de trabajadores
    for i in range(len(listaTrabajadores)):
        trabajador = listaTrabajadores[i]
        if trabajador["cargo"] == cargo:
            listaFiltro.append(trabajador)
    if cargo=="CEO":
        archivo = (f"planilla{cargo}.json")
    elif cargo=="Desarrollador":
        archivo = (f"planilla{cargo.upper()}.json")
    elif cargo=="Analista de datos":
        archivo = ("planillaANALISTA.json")
    else:
        print("Error.")

    with open(archivo, "w", encoding='utf-8') as archivo:
        json.dump(listaFiltro,archivo)
    print(f"La planilla {cargo} ha sido creada correctamente.")