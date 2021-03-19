def CalculaDistancia(fecha1, fecha2):
    """
    Formato de fecha: DD, MM, AAAA.
    Entrada únicamente de tipo entero (1, 2, 3, 4, ...).
    El "mayor" va antes.
    """
    if isinstance(fecha1, list) and len(fecha1) == 3 and isinstance(fecha2, list) and len(fecha2) == 3:
        return Calculador(fecha1, fecha2)
    else:
        return Error("Los valores introducidos están mal ubicados. Utilice formato DD,MM,AAAA.")


def Calculador(fecha1, fecha2):
    difDias = DiferenciaDeDias(fecha1, fecha2)
    difMes = DiferenciaDeMeses(fecha1, fecha2)
    difAños = DiferenciaDeAños(fecha1, fecha2)
    dias = 0

    if difDias < 0:
        difMes -= 1
        mesACalcular = fecha2[1] - 1
        añoACalcular = fecha2[2]
        
        if mesACalcular == 0:
            mesACalcular = 12
            añoACalcular -= 1
            
        difDias += DiasPorMes(mesACalcular, añoACalcular)

    if difMes < 0:
        difAños -= 1
        difMes += 12
        
    if difAños < 0:
        return Error("Las fechas no pueden ir al revés.")

    # calcular distancia de años en días
    añoActual = fecha1[2]
    for i in range(1, difAños + 1):
        dias += DiasPorAño(añoActual)
        añoActual += i

    # calcular distancia de meses en días
    mesActual = fecha2[1]
    añoActual = fecha1[2]
    for i in range(1, difMes + 1):
        dias += DiasPorMes(mesActual, añoActual)
        mesActual += i
        if mesActual > 12:
            mesActual = 1
            añoActual += 1

    dias += difDias
    
    return "La diferencia entre " + str(fecha1) + " y " + str(fecha2) + " es de " + str(dias) + " días. Corresponde a: " + str(difAños) + " años, " + str(difMes) + " meses, " + str(difDias) + " días."
        
    
def DiasPorAño(año):
    if Bisiesto(año):
        return 366
    else:
        return 365

def DiasPorMes(mes, año):
    if mes == 2:
        if Bisiesto(año):
            return 29
        else:
            return 28
    elif (mes < 8 and mes % 2 == 1) or (mes > 7 and mes % 2 == 0):
        return 31
    else:
        return 30

def Bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            return año % 400 == 0
        return True
    else:
        return False

def DiferenciaDeDias(fecha1, fecha2):
    return fecha2[0] - fecha1[0]

def DiferenciaDeMeses(fecha1, fecha2):
    return fecha2[1] - fecha1[1]

def DiferenciaDeAños(fecha1, fecha2):
    return fecha2[2] - fecha1[2]

def Error(error = ""):
    print ("Error, inconsistencia en los datos: " , error)
    print("")
    print("Presione enter para salir o presione cualquier letra o número y enter para volver a intentarlo.")
    entrada = input()
    if entrada == "":
        exit()
    else:
        print("")
        print("")
        Inicio()
        
def RevisarDatos(entrada):

    lista = entrada.split(",")
    
    if len(lista) != 3:
        lista = entrada.split("/")
        if len(lista) != 3:
            Error("Los datos están introducidos en el formato incorrecto. Utilice DD,MM,AAAA o DD/MM/AAA y no use espacios. No puede prescindir de ningún valor.")

    if not (len(lista[0]) == 1 or len(lista[0]) == 2):
        Error("El día está expresado incorrectamente.")

    if not (len(lista[1]) == 1 or len(lista[1]) == 2):
        Error("El mes está expresado incorrectamente.")

    if not (0 < len(lista[1]) < 4):
        Error("El año está expresado incorrectamente.")
    

    lista2 = []
    
    try:
        lista2 = [int(lista[0]),int(lista[1]), int(lista[2])]
    except:
        Error("Los datos deben ser numéricos.")

    if not 0 < lista2[2]:
        Error("No exiten años negativos.")

    if not 0 < lista2[1] < 13:
        Error("No existe el mes " + str(lista2[1]))

    if not 0 < lista2[0] < DiasPorMes(lista2[1], lista2[2]) + 1:
        Error("El mes #" + str(lista2[1]) + " no tiene el día " + str(lista2[0]) + " para el año " + str(lista[2]) + ".")


    return lista2
        


def Inicio():
    print("Calcule la diferencia entre dos fechas.")
    print("")
    print("Introduzca la primera fecha en este formato: DD,MM,AAAA o DD/MM/AAA. No utilice espacios.")
    fecha = input()
    fecha1 = RevisarDatos(fecha)

    print("")
    print("Introduzca la segunda fecha en este formato: DD,MM,AAAA o DD/MM/AAA. No utilice espacios.")
    fecha = input()
    fecha2 = RevisarDatos(fecha)

    print(CalculaDistancia([int(fecha1[0]),int(fecha1[1]), int(fecha1[2])], [int(fecha2[0]),int(fecha2[1]), int(fecha2[2])]))

    print("")
    print("Presione enter para salir")
    input()
    exit()

Inicio()
