#importamos las funciones necesarias para la realización del programa.
import time
import funciones;

#declaramos variables para ejecutar el menú de opciones.
bandera_menu=True;


print("¡Bienvenido a MenúDuoc!");
#solicitamos al usuario que ingrese la opción que estime conveniente.
while bandera_menu:
    print("Escoja una de las siguientes opciones:\n");
    print("1.Agregar trabajador");
    print("2.Listar trabajadores");
    print("3.Mostrar planillas de sueldos");
    print("4.Salir");
    try:
        opcion=int(input("Ingrese la opción deseada: "));
    except:
        print("La opción ingresada no es válida, intentelo nuevamente");
    else:
        if opcion==1:
            print("");
        elif opcion==2:
            print("");
        elif opcion==3:
            print("");
        elif opcion==4:
            #cuando el usuario lo desee, saldrá del programa utilizando la opción número 4.
            bandera_menu=False;
            print("Saliendo del programa...");
            time.sleep(1);
        else:
            print("La opción ingresada no es válida, intentelo nuevamente");  
