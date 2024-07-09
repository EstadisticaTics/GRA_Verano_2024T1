def fa_grouped(lim_inf, lim_sup, datos):
    """
    Función para calcular la frecuencia absoluta de cada clase.
    
    Parámetros:
    - lim_inf (list): lista de números que representan los límites inferiores de cada clase
    - lim_sup (list): lista de números que representan los límites superiores de cada clase
    - datos (list): lista de números que representan los datos de entrada
    
    Lo que hace:
    - Inicializa una lista de frecuencias con ceros, con la misma longitud que la lista de límites inferiores
    - Itera sobre cada dato en la lista de datos
    - Para cada dato, itera sobre la lista de límites inferiores y superiores
    - Si el dato cae dentro del rango de una clase (límite inferior <= dato <= límite superior), incrementa la frecuencia correspondiente
    - Rompe el ciclo para evitar contar el mismo dato en múltiples clases
    - Devuelve la lista de frecuencias absolutas
    
    Uso:
    - Se utiliza para calcular la frecuencia absoluta de cada clase en un conjunto de datos
    - Se aplica a las listas de límites inferiores, superiores y datos de entrada para obtener la frecuencia absoluta de cada clase
    """
    
    # Inicializa una lista de frecuencias con ceros
    frecuencias = [0] * len(lim_inf)
    
    # Itera sobre cada dato en la lista de datos
    for dato in datos:
        # Itera sobre la lista de límites inferiores y superiores
        for i in range(len(lim_inf)):
            # Si el dato cae dentro del rango de una clase, incrementa la frecuencia correspondiente
            if lim_inf[i] <= dato <= lim_sup[i]:
                frecuencias[i] += 1
                # Rompe el ciclo para evitar contar el mismo dato en múltiples clases
                break
    
    # Devuelve la lista de frecuencias absolutas
    return frecuencias
  