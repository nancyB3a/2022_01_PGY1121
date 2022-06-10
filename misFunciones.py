def existeRut(rut, ruts):
    existe=False
    for pos in range(len(ruts)):
        if rut==ruts[pos]:
            existe=True
            break
    return existe

def returnPos(rut, ruts):
    for pos in range(len(ruts)):
        if rut==ruts[pos]:
            break
    return pos

def validaRut():
    #Rut debe ser un número entero que se encuentre dentro del rango de 5000000 y 99999999
    while True:
        try:
            rut=validaInt("Ingrese RUT del paciente => ")
            if(5000000<=rut<=99999999):
                break
            else:
                print("Rut Fuera de rango [5000000 - 99999999]!!")
        except:
            print("RUT es un número!!!")
    return rut

def validaInt(texto):
    while True:
        try:
            valorInt=int(input(texto))  
            break      
        except:
            print("El Valor Ingresado Debe ser un Número!!!")
    return valorInt
