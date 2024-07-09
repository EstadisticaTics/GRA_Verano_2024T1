import matplotlib.pyplot as plt

def plot_grafPie(datos, marcas_texto):
    """
    Función para dibujar un gráfico de pastel que muestra la distribución de datos.
    
    Parámetros:
    - datos (list): lista de números que representan los datos a mostrar en el gráfico
    - marcas_texto (list): lista de strings que representan las etiquetas para cada porción del gráfico
    
    Lo que hace:
    - Dibuja un gráfico de pastel que muestra la distribución de datos
    - Destaca la porción con el valor más alto separándola del resto
    """
    
    # Crear una figura con un tamaño específico
    plt.figure(figsize=(8, 8))

    # Encontrar el índice del valor más alto en los datos
    max_index = datos.index(max(datos))
    
    # Crear una lista de separaciones para destacar la porción con el valor más alto
    separaciones = [0.08 if i == max_index else 0 for i in range(len(datos))]

    # Dibujar el gráfico de pastel
    plt.pie(datos,
            # Separar la porción con el valor más alto
            explode=separaciones,
            # Dirección de rotación del gráfico
            counterclock=False,
            # Ángulo de inicio del gráfico
            startangle=90,
            # Formato para mostrar el porcentaje en cada porción
            autopct="%0.1f%%",
            # Distancia entre el centro del gráfico y las etiquetas de porcentaje
            pctdistance=0.8,
            # Etiquetas para cada porción del gráfico
            labels=marcas_texto)

    # Título del gráfico
    plt.title("Gráfico de Pastel", fontsize=15)
    
    # Mostrar el gráfico
    plt.show()
