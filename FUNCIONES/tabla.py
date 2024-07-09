def tabla(clase, fa_sorted, frecuencia_rel, frecuencia_rel_acum):
    """
    Función para imprimir una tabla con las clases, frecuencias absolutas, frecuencias relativas y frecuencias relativas acumuladas.
    
    Parámetros:
    - clase (list): lista de strings que representan las clases o categorías
    - fa_sorted (list): lista de números que representan las frecuencias absolutas ordenadas
    - frecuencia_rel (list): lista de números que representan las frecuencias relativas
    - frecuencia_rel_acum (list): lista de números que representan las frecuencias relativas acumuladas
    
    Lo que hace:
    - Imprime una tabla con encabezados para las clases, frecuencias absolutas, frecuencias relativas y frecuencias relativas acumuladas
    - Itera sobre las listas de entrada y imprime cada fila de la tabla con los valores correspondientes
    - Formatea los valores para que se muestren de manera clara y organizada
    
    Uso:
    - Se utiliza para mostrar los resultados del análisis de frecuencias en una tabla fácil de leer
    - Se aplica a las listas de clases, frecuencias absolutas, frecuencias relativas y frecuencias relativas acumuladas para imprimir la tabla
    """
    
    # Imprimir encabezados de la tabla
    print("-----------------------------------------------------------------------------------")
    print("{:^10}".format("Clases"), "{:^15}".format("Fa"), "{:^20}".format("Fr"), "{:^20}".format("F acumulada"))
    print("-----------------------------------------------------------------------------------")
    
    # Iterar sobre las listas de entrada y imprimir cada fila de la tabla
    for i in range(len(clase)):
        print("{:^10}".format(f"Clase {clase[i]}"), "{:^15}".format(fa_sorted[i]), "{:^20.3f}".format(frecuencia_rel[i]), "{:^20.3f}".format(frecuencia_rel_acum[i])) 
        