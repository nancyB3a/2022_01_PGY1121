def validaRut(rut):
    multiplicador=2
    acumulador=0
    i=len(rut)-1
    while i>=0:
        if multiplicador==8:
            multiplicador=2
        acumulador+=multiplicador*int(rut[i])
        multiplicador+=1
        i-=1
    digito=11-(acumulador%11)
    if digito==11:
        return 0
    elif digito==10:
        return 'K'
    else:
        return digito