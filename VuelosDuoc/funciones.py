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
        print("| ", end="")
        for c in range(6): 
            if c==3:#imprimir pasillo del avión
                print("     ", end="")           
            if len(asientos[f,c])==0: #asiento vacío
                #necesito imprimir SIN SALTAR línea
                print(f"{str(asiento).ljust(2)}  ", end="")
            else: #asiento ocupado
                print(" X ", end="")
            asiento+=1
        print("|")
        if asiento==31:#separar los asientos VIP
            print("|____________      ____________|")
            print("|____________      ____________|")

def comprarPasaje(asientos, pasajeros):
    asiento=validaInt("Ingrese N° de Asiento: ")
    pasajero=[]
    if 1<=asiento<=42:
        f,c= validaVacio(asiento,asientos) 
        print(f"{f,c}")  
        if f==-1 and c==-1:#asiento ocupado
            print("Asiento Ocupado!!")
        else: #asiento disponible
            if asiento>30:
                print("Valor Pasaje: $240.000")
            else:
                print("Valor Pasaje: $78.900")
            compra=validaInt("Desea Continuar con la Compra? [1: Sí / 2:No]: ")
            if compra==1:
                pasajero.append(input("Ingrese Nombre: "))
                pasajero.append(input("Ingrese Rut: "))
                pasajero.append(input("Ingrese Fono: "))
                
                while True:
                    banco=validaInt("Banco [1: Banco Duoc / 0: Otro]")
                    if 0<=banco<=1:
                        break
                    else:
                        print("Banco No Válido!!")
                pasajero.append(banco)
                pasajeros[f,c]=pasajero
                asientos[f,c]=" X "
                print("Pasajero agregado con Exito!!")  
            else:
                print("Siga Cotizando!!")                             
    else:
        print("Asiento fuera de Rango")    

def validaVacio(asiento,asientos):
    contador=1
    disponible=False
    for f in range(7):
        for c in range(6):
            if asiento==contador:
                if len(asientos[f,c])==0:
                    disponible=True
                    break    
                else:
                    break
            contador+=1
        if disponible:
            break                    
    if disponible:
        return(f,c)
    else:
        return(-1,-1)    
    