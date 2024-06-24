# Cuando el usuario seleccione mostrar planillas sueldo tendremos 2 tipos, uno con filtro y otro general
# Cada planilla debe mostrar TRABAJADOR, CARGO, SUELDO BRUTO, DESC. SALUD, DESC. AFP, LIQUIDO A PAGAR
# Se debe crear un archivo con las planillas


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


    


