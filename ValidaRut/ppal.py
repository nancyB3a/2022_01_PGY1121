import funciones as fn 
rut=input("Ingrese RUT (sin guión ni dígito): ")
if 7<=len(rut)<=8:
    dv=fn.validaRut(rut)
    print(f"El DV del rut ingresado es: {dv}")
    print(f"{rut}-{dv}")
else:
    print("Rut debe estar entre 1000000 y 99999999")