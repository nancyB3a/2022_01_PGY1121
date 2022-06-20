import numpy as np

def menu():
    while True:
        print("")
        print("***** VUELOS DUOC ******")
        print("1. Ver asientos disponibles.")
        print("2. Comprar asiento.")
        print("3. Anular Vuelo.")
        print("4. Modificar datos de pasajero.")
        print("5. Salir.")
        op=validaInt("Opción => ")
        if 1<=op<=5:
            break
        else:
            print("Opción Fuera de Rango!!")
    return op

def validaInt(texto):
    while True:
        try:
            valorInt=int(input(texto))  
            break      
        except:
            print("El Valor Ingresado Debe ser un Número!!!")
    return valorInt
  
def imprimeAsientos(asientos):
    asiento=1
    for f in range(7):
        print("| ", end="")#línea de inicio de fila + impresión SIN salto de línea
        for c in range(6): 
            if c==3:#imprimir pasillo del avión
                print("     ", end="")           
            if len(asientos[f,c])==0: #asiento vacío
                #necesito imprimir SIN SALTAR línea
                print(f"{str(asiento).ljust(2)}  ", end="")#con esta función ajusto el numero para ocupar 2 espacios
            else: #asiento ocupado
                print(f"{str(asientos[f,c]).ljust(2)}  ", end="")
            asiento+=1
        print("|")#línea de fin de fila
        if asiento==31:#separar los asientos VIP
            print("|____________      ____________|")
            print("|____________      ____________|")

def comprarPasaje(asientos, pasajeros):
    verPasajero(asiento, pasajero)
    asiento=validaInt("Ingrese N° de Asiento: ")
    pasajero=[]
    if 1<=asiento<=42:
        f,c= validaVacio(asiento,asientos) 
        print(f"{f,c}")  
        if f==-1 and c==-1:#asiento ocupado
            print("Asiento Ocupado!!")
        else: #asiento disponible
            if asiento>30:
                valorPasaje = 240000
            else:
                valorPasaje = 78900
            print(f"Valor Pasaje: ${valorPasaje}")
            compra=validaInt("Desea Continuar con la Compra? [1: Sí / 2:No]: ")
            if compra==1:
                pasajero.append(input("Ingrese Nombre: "))
                pasajero.append(input("Ingrese Rut: "))
                pasajero.append(input("Ingrese Fono: "))                
                while True:
                    banco=validaInt("Banco [1: Banco Duoc / 0: Otro]: ")
                    if 0<=banco<=1:
                        break
                    else:
                        print("Banco No Válido!!")
                pasajero.append(banco)                
                pasajeros[f,c]=pasajero
                asientos[f,c]="X"
                if banco==1:
                    total= int(valorPasaje*0.85)
                    print("Por pertenecer a Banco Duoc tiene un 15% de descuento.")
                    print(f"Su pasaje queda en ${total}.")
                print("Pasajero agregado con Exito!!")  
            else:
                print("Siga Cotizando!!")                             
    else:
        print("Asiento fuera de Rango")    
    return asientos, pasajeros

def validaVacio(asiento,asientos):
    contador=1
    disponible=False
    for f in range(7):
        for c in range(6):
            if asiento==contador:
                if len(asientos[f,c])==0:
                    disponible=True
                    break #rompe el for de las columnas  
                else:
                    break #rompe el for de las columnas
            contador+=1
        if disponible:
            break #rompe el for de las filas cuando ha encontrado vacía la posición buscada                   
    if disponible: #si llega hasta esta línea es por que finalizaron ambos for, de todos modos verifico el flag
        return(f,c)
    else:#no encuentra el asiento vacío, entonces retorno valores inexistentes
        return(-1,-1)   


def validaOcupado(asiento,asientos):
    contador=1
    ocupado=False
    for f in range(7):
        for c in range(6):
            if asiento==contador:
                if len(asientos[f,c])!=0:
                    ocupado=True
                    break #rompe el for de las columnas  
                else:
                    break #rompe el for de las columnas
            contador+=1
        if ocupado:
            break #rompe el for de las filas cuando ha encontrado ocupada la posición buscada                   
    if ocupado: #si llega hasta esta línea es por que finalizaron ambos for, de todos modos verifico el flag
        return(f,c)
    else:#encuentra el asiento vacío, entonces retorno valores inexistentes
        return(-1,-1)   
    
def verPasajero(asiento, pasajero):
    print(50*"=")
    print(f"Datos pasajero RUT {pasajero[1]} en el asiento N° {asiento}")
    print(50*"=")
    print(f"Nombre Pasajero: {pasajero[0]}")
    print(f"Fono Pasajero: {pasajero[2]}")
    if int(pasajero[3])==1:
        print("Banco Pasajero: Banco DUOC")
    else:
        print("Banco Pasajero: Otro Banco")
    print(50*"=")
           
def anularPasaje(asientos, pasajeros):
    asiento=validaInt("Ingrese N° de Asiento: ")
    if 1<=asiento<=42:
        f,c= validaOcupado(asiento,asientos) 
        if f==-1 and c==-1:#asiento vacío
            print("Asiento Vacío!!")
        else:
            pasajeros[f,c]="" 
            asientos[f,c]=""
            print("Reserva Anulada con EXITO!!")
    else:
        print("Asiento fuera de Rango") 
    return asientos, pasajeros 

def modificaPasajero(asientos, pasajeros):
    rut=validaInt("Ingrese RUT del pasajero: ")
    asiento=validaInt("Ingrese N° de Asiento: ")
    if 1<=asiento<=42:
        f,c= validaOcupado(asiento,asientos) 
        if f==-1 and c==-1:#asiento vacío
            print("Asiento Vacío!!")
        else:
            pasajero=pasajeros[f,c]
            if str(pasajero[1])==str(rut):  
                verPasajero(asiento,pasajero)
                opcion=validaInt("Que desea modificar? [1:Nombre / 2: Fono]: ")
                if 1<=opcion<=2:
                    if opcion==1: #modifica nombre
                        pasajero[0]=input("Ingrese nuevo Nombre: ")
                    else:
                        pasajero[2]=input("Ingrese nuevo Fono: ")
                    pasajeros[f,c]=pasajero
                    print("Datos Pasajero actualizado con EXITO!!")
                    verPasajero(asiento,pasajero)
                else:
                    print("Opción Fuera de Rango!!")
            else:
                print("RUT No coincide con el pasajero!!")
    else:
        print("Asiento fuera de Rango") 
    return asientos, pasajeros