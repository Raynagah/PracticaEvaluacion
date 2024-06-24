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

    #Agregar trabajador a un diccionario
    trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargo, "sueldoBruto": sueldo_bruto}

    #Agregar el trabajador antes ingresado a una lista de trabajadores
    lista_Trabajadores.append(trabajador)
    print(lista_Trabajadores)

