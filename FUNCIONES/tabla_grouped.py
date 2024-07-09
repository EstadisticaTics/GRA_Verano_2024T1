def tabla_grouped(clases, lim_inf, lim_sup, mrks, fa, fr, facum):
    """
    Función para imprimir una tabla con la información de las clases y sus frecuencias.
    
    Parámetros:
    - clases (list): lista de números que representan las clases
    - lim_inf (list): lista de números que representan los límites inferiores de cada clase
    - lim_sup (list): lista de números que representan los límites superiores de cada clase
    - mrks (list): lista de números que representan las marcas de clase
    - fa (list): lista de números que representan las frecuencias absolutas
    - fr (list): lista de números que representan las frecuencias relativas
    - facum (list): lista de números que representan las frecuencias acumuladas
    
    Lo que hace:
    - Imprime una tabla con encabezados para cada columna
    - Itera sobre la lista de clases y sus correspondientes límites inferiores, superiores, marcas de clase, frecuencias absolutas, relativas y acumuladas
    - Imprime cada fila de la tabla con la información correspondiente a cada clase
    
    Uso:
    - Se utiliza para visualizar la información de las clases y sus frecuencias de manera organizada
    - Se aplica a las listas de clases, límites inferiores, superiores, marcas de clase, frecuencias absolutas, relativas y acumuladas para imprimir la tabla
    """
    
    # Imprime la cabecera de la tabla
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("{:^10}".format("Clase"), "{:^25}".format("Limite Inferior"), "{:^25}".format("Limite Superior"), "{:^20}".format("Marca de clase"), "{:^20}".format("Frecuencia Absoluta"), "{:^25}".format("Frecuencia Relativa"), "{:^25}".format("Frecuencia Acumulada"))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    
    # Itera sobre la lista de clases y sus correspondientes información
    for i in range(len(clases)):
        # Imprime cada fila de la tabla con la información correspondiente a cada clase
        print("{:^10}".format(f"Clase {clases[i]}"), "{:^25.3f}".format(lim_inf[i]), "{:^25.3f}".format(lim_sup[i]), "{:^20.3f}".format(mrks[i]), "{:^20}".format(fa[i]), "{:^25.3f}".format(fr[i]), "{:^25.3f}".format(facum[i]))
        