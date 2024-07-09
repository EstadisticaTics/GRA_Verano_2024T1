import matplotlib.pyplot as plt 

def plot_grafPoligono(clases, mrks, fr):
    """
    Función para dibujar un polígono de frecuencias que muestra la distribución de frecuencias relativas por marca de clase.
    
    Parámetros:
    - clases (list): lista de strings que representan las marcas de clase
    - mrks (list): lista de strings que representan las etiquetas para cada marca de clase
    - fr (list): lista de números que representan las frecuencias relativas para cada marca de clase
    
    Lo que hace:
    - Dibuja un polígono de frecuencias que muestra la distribución de frecuencias relativas por marca de clase
    - Muestra la frecuencia relativa de cada marca de clase en la gráfica
    """
    
    # Crear listas para los datos del polígono
    datos_x_poligono = [0] + list(range(1, len(clases) + 1)) + [list(range(1, len(clases) + 1))[-1] + 1]
    datos_y_poligono = [0] + fr + [0]

    # Crear una figura con un tamaño específico
    plt.figure(figsize=(15, 5))
    
    # Dibujar el polígono
    plt.plot(datos_x_poligono, datos_y_poligono, 
             # Ancho de la línea
             linewidth=3, 
             # Color de la línea
             color="#1C2833", 
             # Estilo de la línea
             linestyle="--", 
             # Marcador de puntos
             marker="o", 
             # Tamaño del marcador
             markersize=10, 
             # Color de relleno del marcador
             markerfacecolor="#FFF700", 
             # Color del borde del marcador
             markeredgecolor="#EC0000",
             # Ancho del borde del marcador
             markeredgewidth=1.5)
    
    # Etiquetas para el eje x
    plt.xticks(list(range(1, len(clases) + 1)), mrks, fontsize=10)
    
    # Título y etiquetas para los ejes
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia relativa", fontsize=15)
    plt.title("Polígono de frecuencias", fontsize=20)
    
    # Agregar una grilla
    plt.grid()
    
    # Mostrar el gráfico
    plt.show()
    