def sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    '''
    Regresa lista de frecuencias absolutas ordenadas
    
    Ejemplo:    
    clases_originales = [0, 5, 7, 6, 4, 2]
    clases_sorted = [0, 2, 4, 5, 6, 7]
    fa_absolutas = [2, 3, 2, 1, 1, 2]
    fa_sorted = sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    >>> [2, 2, 1, 3, 1, 2] 
    '''

    fa_sorted = []
    for elemento in clases_sorted:
        idx = clases_originales.index(elemento)
        fa = fa_absolutas[idx]
        fa_sorted.append(fa)

    return fa_sorted
