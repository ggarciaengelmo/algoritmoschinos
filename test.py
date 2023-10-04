from algoritmos import *
import random
import numpy as np

def aleatorio(n: int) -> list:
    ''' Devuelve un vector con n numeros pseudoaleatorios en el rango [−n,...,+n]'''
    v = list(range(n))
    for i in v:
        v[i] = random.randint(-n, n)
    return v

def ordenado(v) -> bool:
    '''comprueba que un vector está ordenado'''
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return False
    return True

def test_aleatorio(f: callable, nombre_funcion = 'Ordenación'): 
    '''Muestra por pantalla la ordenacion de un vector desordenado aleatoriamente hecha por una funcion'''
    v1 = aleatorio(10)
    print('Inicialización aleatoria')
    print(v1)
    if ordenado(v1):
        print('ordenado? 1')
    else:
        print('ordenado? 0')
        print(nombre_funcion)
        f(v1)
        print(v1)
        if ordenado(v1):
            print('ordenado? 1')
        else:
            print('ordenado? 0')

def test_descendente(f: callable, nombre_funcion = 'Ordenación'):
    '''Muestra por pantalla la ordenacion de un vector ordenado de mayor a menor hecha por una funcion'''
    v1 = list(np.arange(10,1,-1))
    print('Inicialización descendente')
    print(v1)
    if ordenado(v1):
        print('ordenado? 1')
    else:
        print('ordenado? 0')
        print(nombre_funcion)
        f(v1)
        print(v1)
        if ordenado(v1):
            print('ordenado? 1')
        else:
            print('ordenado? 0')
    




'''
def ordenado(v, i = 0) -> bool:
    comprueba que un vector está ordenado
    if i >= len(v)-1:
        return True
    if v[i] > v[i+1]:
        return False
    else:
        return ordenado(v, i+1)
       
'''
if __name__ == "__main__":
    test_descendente(ins_sort, 'Ordenación por inserción')
    print()
    test_descendente(shell_sort_hibbard, 'Ordenación shell')
