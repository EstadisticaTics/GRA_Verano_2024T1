import matplotlib.pyplot as plt

def plot_pie(datos, marcas_texto):
    """
    Función para dibujar un gráfico de pie (tarta) que muestra la distribución de sabores.
    
    Parámetros:
    - datos (list): lista de números que representan la frecuencia o cantidad de cada sabor
    - marcas_texto (list): lista de strings que representan los nombres de cada sabor
    
    Lo que hace:
    - Identifica el sabor más popular (el que tiene la frecuencia más alta) y lo destaca en el gráfico
    - Dibuja un gráfico de pie que muestra la distribución de sabores
    - Muestra el porcentaje de cada sabor en el gráfico
    """
    plt.figure(figsize=(8, 8))
    # Identificar el índice del sabor más popular (el que tiene la frecuencia más alta)
    max_index = datos.index(max(datos))
    
    # Crear una lista de separaciones para destacar el sabor más popular
    # La separación será de 0.08 para el sabor más popular y 0 para los demás
    separaciones = [0.08 if i == max_index else 0 for i in range(len(datos))]
    
    # Dibujar el gráfico de pie
    plt.pie(datos,
            # Separaciones para destacar el sabor más popular
            explode=separaciones,
            # Dirección de rotación del gráfico (en este caso, no se rota)
            counterclock=False,
            # Ángulo de inicio del gráfico (en este caso, 90 grados)
            startangle=90,
            # Formato para mostrar el porcentaje de cada sabor
            autopct="%0.1f%%",
            # Distancia entre el porcentaje y el centro del gráfico
            pctdistance=0.8,
            # Etiquetas para cada sabor
            labels=marcas_texto)
    
    # Título del gráfico
    plt.title("Diagrama de pastel", fontsize=20)
    
    # Mostrar el gráfico
    plt.show()
       