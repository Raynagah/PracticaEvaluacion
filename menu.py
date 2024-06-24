#Importamos las funciones necesarias para la realización del programa.
import time
import funciones as funcion

#Declaramos variables para ejecutar el menú de opciones.
bandera_menu=True;
lista = []

print("¡Bienvenido a MenúDuoc!");
#Solicitamos al usuario que ingrese la opción que estime conveniente.
while bandera_menu:
    print("Escoja una de las siguientes opciones:\n");
    print("1.Agregar trabajador");
    print("2.Listar trabajadores");
    print("3.Mostrar planillas de sueldos");
    print("4.Salir");
    #Validamos que la opción ingresada por el usuario esté dentro de los parámetros entregados. 
    try:
        opcion=int(input("Ingrese la opción deseada: "));
    except:
        print("La opción ingresada no es válida, intentelo nuevamente");
    else:
        #De acuerdo con la opción ingresada, llamamos a la función correspondiente.
        if opcion==1:
            funcion.funcion_agregar(lista)
            print("");
        elif opcion==2:
            funcion.listar_trabajadores()
            print("");
        elif opcion==3:
            print("");
        elif opcion==4:
            #Cuando el usuario lo desee, saldrá del programa utilizando la opción número 4.
            bandera_menu=False;
            print("Saliendo del programa...");
            time.sleep(1);
        else:
            print("La opción ingresada no es válida, intentelo nuevamente");  
