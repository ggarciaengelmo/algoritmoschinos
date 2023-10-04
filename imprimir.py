'''
Hecho por:
Antonio Serrano Rodríguez  a.serrano1@udc.es 
Marcos Güeto Sandá m.gueto@udc.es
Guillermo García Engelmo g.garcia2@udc.es
'''
def tabular(fila: list):
    '''muestra por pantalla una fila de 5 columnas con separaciones fijas para poder hacer tablas'''
    print("{:<2} {:<8} {:<12} {:<20} {:<20} {:<18}".format(*fila)) #selecciona todos los elementos de la lista 'fila' para mostrarlos por pantalla 


def imprimir_tabla(l: list, f: callable, g: callable, h: callable, filas = 5):
    '''muestra por pantalla una tabla en la que se muestran
    los tiempos de ejecucion de un algoritmo y la convergencia respecto a tres funciones a medida que crece la longitud de la entrada'''
    if g(2) == 4: # averiguar que funcion estamos usando como cota ajustada para imprimir la cabecera de la tabla correctamente
        tabular(['','n','t(n)', 't(n)/n**1.8','t(n)/n**2', 't(n)/n**2.2'])
    else:
        tabular(['','n','t(n)', 't(n)/n**0.8','t(n)/n', 't(n)/n**1.2'])

    n = 500 # tamaño inicial del vector de numeros  
    for i in range(filas): # imprimir cada fila de la tabla con la longitud del vector creciendo en una progresion geometrica de razon = 2
        tabular([l[i][1],n, l[i][0], l[i][0]/f(n), l[i][0]/g(n),l[i][0]/h(n)])
        n *= 2
