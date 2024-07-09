def ordenar_asc(arreglo):
    '''
    Regresa el arreglo ordenado de forma
    ascendente.
    
    Ejemplo:
    arreglo = [0, 5, 7, 6, 4, 2]
    arr_sorted = ordenar_asc(arreglo)
    >>> [0, 2, 4, 5, 6, 7]
    '''
    arr_len = len(arreglo)

    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]         

    return arreglo
