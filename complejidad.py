import time
import numpy as np
from test import *

def crear_lista_vectores(x = 0):
    lista_vectores = []
    lon = 128
    if x == 1: #ascendente
        for i in range(7):
            lista_vectores.append(list(np.arange(1,lon)))
            lon *= 2
    elif x == 2: #descendente
        for i in range(7):
            lista_vectores.append(list(np.arange(lon,1, -1)))
            lon *= 2
    else: #desordeado
        for i in range(7):
            lista_vectores.append(aleatorio(lon))
            lon *= 2
    return lista_vectores

def medirTiempos(f1: callable, f2: callable, lista_vectores) -> tuple: 
    '''mide el tiempo de ejecucion de dos funciones, el primero en 5 vectores de longitud creciente, el segundo, en 10.'''

    lista_de_tiempos1 = [] #listas en donde se almacenaran los tiempos de ejecucion de las funciones
    lista_de_tiempos2 = []
    for i in range(7):
        lista_de_tiempos1.append(medirTiempo(f1, lista_vectores[i]))
        lista_de_tiempos2.append(medirTiempo(f2, lista_vectores[i]))
    return lista_de_tiempos1, lista_de_tiempos2


def medirTiempo(f: callable, v: list) -> float:
    '''mide el tiempo de ejecucion de una funcion a la que se le pasa una lista que no modifica'''
    tinicio = time.perf_counter_ns()
    f(v)
    tfinal = time.perf_counter_ns()
    t = (tfinal - tinicio, '')
    if t[0] < 10**6: #si el tiempo de ejecucion no llega a los 1000 microsegundos, se repite 1000 veces la ejecucion para que la medicion sea mas precisa
        tinicio = time.perf_counter_ns()
        for i in range(1000):
            f(v)
        tfinal = time.perf_counter_ns()
        t = ((tfinal - tinicio)/1000, '*') #se realiza la media de las 1000 ejecuciones y se muestra, mediante un asterisco en el segundo elemento de la tupla, que se empleo un bucle para medir el tiempo
    return t 

if __name__ == "__main__":
    from algoritmos import *
    l = crear_lista_vectores(0)
    t = medirTiempos(ins_sort, shell_sort_hibbard, l)
    from imprimir import *
    imprimir_tabla(t,)