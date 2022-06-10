from datetime import datetime
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
        try:
            opcion=int(input("Opción=> "))
            if opcion<1 or opcion>4:
                print("Opción NO Válida!!")
        except:
            print("Opción es numérica!!!")
    if opcion==1: #Registrar Paciente
        #Rut debe ser un número entero que se encuentre dentro del rango de 5000000 y 99999999
        while True:
            try:
                rut=int(input("Ingrese RUT del paciente => "))
                if(5000000<=rut<=99999999):
                    ruts.append(rut)
                    break
                else:
                    print("Rut Fuera de rango [5000000 - 99999999]!!")
            except:
                print("RUT es un número!!!")
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
            try:
                edad=int(input("Ingrese edad del paciente => "))
                if(0<=edad<=110):
                    edades.append(edad)
                    break
                else:
                    print("Edad Fuera de rango [0 - 110]!!")
            except:
                print("Edad es un número!!!")
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
        while True:
            try:
                rut=int(input("Ingrese RUT del paciente => "))
                if(5000000<=rut<=99999999):                    
                    break
                else:
                    print("Rut Fuera de rango [5000000 - 99999999]!!")
            except:
                print("RUT es un número!!!")
        #verifico que rut Exista
        existe=False
        for pos in range(len(ruts)):
            if rut==ruts[pos]:
                existe=True
                break
        #pregunto si lo encontró
        registro=""
        if existe:
            registro=listRegistros[pos]
            fecha=str(datetime.now())
            observaciones=input("Ingrese observaciones => ")
            registro+="\nAtención fecha: "+fecha+" - Obs: " + observaciones
            listRegistros.insert(pos, registro)
            print("Atención Registrada con EXITO!!!")
        else:
            print("Paciente NO Registrado!!")
    elif opcion==3:
        while True:
            try:
                rut=int(input("Ingrese RUT del paciente => "))
                if(5000000<=rut<=99999999):                    
                    break
                else:
                    print("Rut Fuera de rango [5000000 - 99999999]!!")
            except:
                print("RUT es un número!!!")
        #verifico que rut Exista
        existe=False
        for pos in range(len(ruts)):
            if rut==ruts[pos]:
                existe=True
                break
        #pregunto si lo encontró
        if existe:
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