def frec_abs(datos_entrada):
    '''
    clases, fa_absoluta = frec_abs(datos_entrada)
    Regresa las clases y frecuencias absolutas 
    de cada clase dada una lista de datos
    
    Ejemplo:
    datos_entrada = [0, 1, 2, 0, 1, 3, 1, 3]
    clases, fa_absoluta = frec_abs(datos_entrada)
    >>> clases = [0, 1, 2, 3]
    >>> fa_absoluta = [2, 3, 1, 2]
    '''
    clases, fa_absoluta = [], []
    for elemento in datos_entrada:
        if elemento not in clases:
            clases.append(elemento)
            fa_absoluta.append(1)
        else:        
            idx = clases.index(elemento)        
            fa_absoluta[idx] += 1

    return clases, fa_absoluta 
 