import numpy as np
import funciones as fn

afiliados=np.empty([7,100], object)
certificados=fn.llenaValores()
opcion=0
while opcion!=4:
    opcion=fn.menu()
    if opcion==1:
        afiliados=fn.afiliacion(afiliados)        
    elif opcion==2:
        columna=fn.buscar(afiliados)
        fn.imprimeAfiliado(afiliados,columna)
    elif opcion==3:
        fn.imprimeCertificado(afiliados, certificados)
    elif opcion==4:
        print("bye")