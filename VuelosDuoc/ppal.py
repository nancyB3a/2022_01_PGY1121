import numpy as np
import funciones as fn
#creo matriz de 7 filas y 6 columnas, la lleno de 'vacios'
asientos=np.empty([7,6], str)
pasajeros=np.empty([7,6], object)
opcion=0
while opcion!=5:
    opcion=fn.menu()
    if opcion==1:
        fn.imprimeAsientos(asientos)
    elif opcion==2:
        asientos, pasajeros= fn.comprarPasaje(asientos,pasajeros)
    elif opcion==3:
        asientos, pasajeros=fn.anularPasaje(asientos,pasajeros)
    elif opcion==4:
        asientos, pasajeros=fn.modificaPasajero(asientos,pasajeros)
