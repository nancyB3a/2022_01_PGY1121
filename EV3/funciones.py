import numpy as np
import random as rd

def menu():
    while True:
        print("")
        print("***** Isapre VIDA y SALUD ******")
        print("1. Grabar.")
        print("2. Buscar.")
        print("3. Imprimir.")
        print("4. Salir.")
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

def afiliacion(afiliados):
    for c in range(100):
        if afiliados[0,c] == None:  
            while True:                      
                rut=input("Ingrese Rut: ")
                if validaRut(rut):
                    break
                else:
                    print("El rut ingresado NO es Válido!!")            
            afiliados[0,c]=rut
            afiliados[1,c]= input("Ingrese Nombre: ")
            afiliados[2,c]= input("Ingrese Apellido: ")
            edad=0
            while True:
                edad=validaInt("Ingrese Edad: ")
                if edad>=18:                    
                    break
                else:
                    print("Edad fuera de rango!!")
            afiliados[3,c]=edad
            while True:
                #(C = Casado,S = Soltero, V = Viudo).
                estadoCivil=input("Ingrese estado civil (C = Casado,S = Soltero, V = Viudo): ")
                if estadoCivil.upper()=='C' or estadoCivil.upper()=='S' or estadoCivil.upper()=='V':
                    break;
                else:
                    print("Estado civil NO Válido!!")
            afiliados[4,c]=estadoCivil
            afiliados[5,c]=input("Ingrese género: ")
            afiliados[6,c]=input("Ingrese fecha de afiliación: ")
            break;                 
    return afiliados

def buscar(afiliados):
    existe=False
    rut=input("Ingrese RUT: ")
    for c in range(100):
        print(afiliados[0,c])
        if afiliados[0,c]==rut:
            existe=True
            break
    if not existe:
        print("Afiliado NO Existe")
        c=-1
    return c

def imprimeAfiliado(afiliados,columna):
    for f in range(1,7):
        print(f"{afiliados[f,columna]}")    
        
def llenaValores():
    certificados=np.empty([2,3],object)
    certificados[0,0]="Certificado de Afiliación"
    certificados[0,1]="Certificado de Datos Personales"
    certificados[0,2]="Certificado de Estado Civil"
    for c in range(3):
        azar=rd.randint(1000,1500)
        print(f"azar: {azar}")
        certificados[1,c]=azar
    return certificados

def imprimeCertificado(afiliados,certificados):
    columna=buscar(afiliados)
    print("¿Qué certificado desea imprimir?: ")
    while True:
        opcion=validaInt("0: Afiliación - 1: Datos Personales - 2: Estado Civil = ")
        if 0<=opcion<=2:
            break
        else:
            print("Opción NO Válida!!")
    print(50*"=")
    print(f"{certificados[0,opcion]} - Valor: ${certificados[1,opcion]}")
    print(50*"=")
    imprimeAfiliado(afiliados,columna)       

def validaRut(rut):
    rutSinDigito=rut[:-1]
    dv=rut[-1]
    multiplicador=2
    acumulador=0
    i=len(rutSinDigito)-1
    while i>=0:
        if multiplicador==8:
            multiplicador=2
        acumulador+=multiplicador*int(rutSinDigito[i])
        multiplicador+=1
        i-=1
    digito=11-(acumulador%11)
    if digito==11:
        digito=0
    elif digito==10:
        digito='K'
    return str(dv)==str(digito)
        