import biblioteca as fn
opcion=0
while opcion!=4:
    opcion=fn.menu()
    if opcion==1:
        miFlag=fn.primo()
        if miFlag:
            print(f"Es PRIMO!!")
        else:
            print(f"No es PRIMO!!")
    elif opcion==2:
        fn.factorial()
    elif opcion==3:
        print("3")
print("bye")
    