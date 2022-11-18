
def my_function(*args, **kwargs):
    text = 150
    mes1 =  1
    mes2 =  12
    dicInfl = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, ]
    try:
        dMes = float(text)
        for i in range(mes1-1, mes2-1):
            dMes = dMes * (1+ dicInfl[i])
        salida =  "$ {:.2f}".format(dMes)
    except:
        salida = "Escriba un valor numérico"
    return salida

print(my_function())

def SetMoneda(num, simbolo="US$", n_decimales=2):
    n_decimales = abs(n_decimales)
    num = round(num, n_decimales)
    num, dec = str(num).split(".")
    dec += "0" * (n_decimales - len(dec))
    num = num[::-1]
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    num = str.join(",", l)
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    
    if not n_decimales:
        return "%s %s" % (simbolo, num)
    return "%s %s.%s" % (simbolo, num, dec)




