def ins_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j + 1] = v[j]
            j -= 1
        v[j+1] = x

def shell_sort_hibbard(v):
    increments = hibbard_increments(len(v))
    return shell_sort_aux(v,increments)

def shell_sort_aux(v,increments):
    """ Escribe el resto del codigo de Shell aqui, sabiendo que increments es un vector de incrementos.
    Para usar el algoritmo de ordenación se llamará a la función shell_sort_hibbard. """
    for increment in increments:
        for i in range(increment,len(v)):
            tmp = v[i]
            j = i
            seguir = True
            while j - increment >= 0 and seguir:
                if tmp < v[j - increment]:
                    v[j] = v[j - increment]
                    j -= increment
                else:
                    seguir = False
            v[j] = tmp

def hibbard_increments(array_length):
    increments = []
    k = 1
    gap = 2**k - 1
    while gap < array_length:
        increments.insert(0, gap)
        k += 1
        gap = 2**k - 1
    return increments
