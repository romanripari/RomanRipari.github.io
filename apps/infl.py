
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