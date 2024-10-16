import random
import os
from pynput import keyboard as kb

def crea_tablero(dif=3):
    '''
    Recibe un int(dif) de dificultad y devuelve una lista
    de listas de dimensión dif * dif.
    '''
    nros = list(range(dif * dif))
    random.shuffle(nros)
    lista = []
    for f in range(dif):
        fila = []
        for c in range(dif):
            fila.append(nros.pop())
        lista.append(fila)
    return lista


'''
Necesitamos crear estas variables de manera global para poner manipularlas y utilizarlas
dentro del la función que "atrapa" las teclas presionadas
'''
dif = int(input("Seleccione la dificultad (2, 3, 4, etc): "))
tablero = crea_tablero(dif)

def es_correcto():
    '''
    Verifica si el tabler contiene, en orden, los números
    desde el 1 hasta dif*dif-1 (es decir, el mayor posible del tablero -1)
    '''
    numero = 1
    while numero < dif**2:
        for f, filas in enumerate(tablero):
            for c, columnas in enumerate(filas):
                if tablero[f][c] != numero and (tablero[f][c] != 0):
                    return False
                numero +=1
    return True
        
def imprime():
    '''
    Limpia la consola e imprime el tablero junto a las instrucciones
    '''
    os.system("cls")
    for f in tablero:
        for c in f:
            print(F'{c if c != 0 else " ":^3}' , " ",end="")
        print("",end="\n")
    print("**** Presione W, A, S o D para mover ****")
    print("**** Presione ESCAPE para terminar ****")

def on_release(key):
    '''
    Función que atrapa la tecla presionada.
    Si es ESC, cancela, si está dentro del 'wasd', realiza el movimiento deseado
    y termina por imprimir nuevamente el tablero
    '''
    mueve = str(key)
    if mueve in "'w'a's'd'":
        if es_correcto():
            print("Ganaste!")
            return False
        else:
            for f, filas in enumerate(tablero):
                if 0 in filas:
                    indice = f, filas.index(0)
            nuevo_indice = list(indice)
            if mueve == "'w'" and indice[0] != dif-1:
                nuevo_indice[0] += 1
            if mueve == "'s'" and indice[0] != 0:
                nuevo_indice[0] -= 1
            if mueve == "'a'" and indice[1] != dif-1:
                nuevo_indice[1] += 1
            if mueve == "'d'" and indice[1] != 0:
                nuevo_indice[1] -= 1
            numero_cambia = tablero[nuevo_indice[0]][nuevo_indice[1]]
            tablero[indice[0]][indice[1]] = numero_cambia
            tablero[nuevo_indice[0]][nuevo_indice[1]] = 0
            imprime()
    if key == kb.Key.esc:
        return False

def run():
    '''
    Función principal que imprime el tablero y comienza a "escuchar" las teclas presionadas
    '''
    imprime()
    with kb.Listener(on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    run()