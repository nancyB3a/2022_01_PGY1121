def menu():
    while True:
        print("1.- N° Primo")
        print("2.- Factorial")
        print("3.- Palíndrome")
        print("4.- Salir")
        op=validaInt("Opción => ")
        if 1<=op<=4:
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


def primo():
    while True:        
        nro=validaInt("Ingrese un N°: ")
        break        
    esPrimo=True
    for n in range(2, nro):
        if nro%n==0:
            esPrimo=False
            break
    return esPrimo

def factorial():
    while True:
        num=validaInt("Ingrese N°: ")
        break
    fac=0
    for i in range(1, num):
        fac+=num*i
        print(fac)
    print(f"El factorial de {num} es {fac}")