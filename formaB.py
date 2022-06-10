from datetime import datetime
import misFunciones as fn
#crear listas
ruts=[]
nombres=[]
direcciones=[]
correos=[]
edades=[]
sexos=[]
listRegistros=[]
previsiones=[]
opcion=0
while opcion!=4:
    opcion=0
    print("\t\tCentro Medico DUOC")
    print("="*60)
    print("1. Registrar Paciente")
    print("2. Atención Paciente")
    print("3. Consultar Datos Paciente")
    print("4. Salir")
    while opcion<1 or opcion>4: #Valido que las opciones estén entre 1 y 4
        opcion=fn.validaInt("Opción => ")
        if opcion<1 or opcion>4:
            print("Opción NO Válida!!")
    if opcion==1: #Registrar Paciente
        rut=fn.validaRut()     
        ruts.append(rut)
        nombres.append(input("Ingrese nombre del paciente => "))
        direcciones.append(input("Ingrese dirección del paciente => "))
        #Correo debe tener ‘@’
        contA=0
        while contA!=1:            
            correo=input("Ingrese su dirección de Correo => ")
            for x in correo:
                if(x=="@"):
                    contA+=1                   
            if(contA!=1):
                print("Correo Formato no válido")
                contA=0
        correos.append(correo)
        #Edad debe ser un número entero que se encuentre en el rango 0 y 110.
        while True:               
            edad=fn.validaInt("Ingrese edad del paciente => ")
            if(0<=edad<=110):
                edades.append(edad)
                break
            else:
                print("Edad Fuera de rango [0 - 110]!!")
        #Sexo debe ser un carácter que sólo acepta la letra f o m (mayúscula y minúscula).
        while True:
            sexo=(input("Ingrese sexo ['f'o 'm'] => ")).upper()
            if sexo=='F' or sexo=='M':
                sexos.append(sexo)
                break
            else:
                print("Sexo debe ser 'f'o 'm'")
        #PS debe ser una cadena de caracteres que sólo acepta los valores “ISAPRE” y “FONASA” 
        while True:     
            ps=input("Ingrese previsión ['ISAPRE'o 'FONASA'] => ")
            if ps=="ISAPRE" or ps=='FONASA':
                previsiones.append(ps)
                break
            else:
                print("Previsión debe ser 'ISAPRE'o 'FONASA'")
        #agrego un vacío a la lista de registro para reservar espacio en la lista
        listRegistros.append("")
        print("Paciente Registrado con EXITO!!!")
    elif opcion==2: #Registrar Atención del Paciente
        registro=""
        #valido rut
        rut=fn.validaRut()
        #verifico que rut Exista        
        if fn.existeRut(rut, ruts):
            pos=fn.returnPos(rut,ruts)
            registro=listRegistros[pos]
            fecha=str(datetime.now())
            observaciones=input("Ingrese observaciones => ")
            registro+="\nAtención fecha: "+fecha+" - Obs: " + observaciones
            listRegistros.insert(pos, registro)
            print("Atención Registrada con EXITO!!!")
        else:
            print("Paciente NO Registrado!!")
    elif opcion==3:
        #valido rut
        rut=fn.validaRut()
        #verifico que rut Exista
        if fn.existeRut(rut, ruts):
            pos=fn.returnPos(rut,ruts)
            if len(listRegistros[pos])>0:
                print("Atención(es) de Paciente")
                print(f"{ruts[pos]}  | {nombres[pos]} | {sexos[pos]} | {previsiones[pos]} | {listRegistros[pos]}")
            else:
                print("Paciente sin Atenciones")
                print(f"{ruts[pos]}  | {nombres[pos]} | {sexos[pos]} | {previsiones[pos]} | No registra Atenciones aún")
        else:
            print("Paciente NO Registrado!!")
    else:
        print("Salir del Sistema")                