import matplotlib.pyplot as plt

def plot_grafOjiva(marcas_clase, valores_ref_eje, facum):
    """
    Función para dibujar una ojiva que muestra la frecuencia acumulada por marca de clase.
    
    Parámetros:
    - marcas_clase (list): lista de strings que representan las marcas de clase
    - valores_ref_eje (list): lista de números que representan los valores de referencia para cada marca de clase
    - facum (list): lista de números que representan la frecuencia acumulada para cada marca de clase
    
    Lo que hace:
    - Dibuja una ojiva que muestra la frecuencia acumulada por marca de clase
    - Muestra la frecuencia acumulada de cada marca de clase en la gráfica
    """
    
    # Crear listas para los datos de la ojiva
    datos_x_ojiva = [0] + valores_ref_eje
    datos_y_ojiva = [0] + facum

    # Crear una figura con un tamaño específico
    plt.figure(figsize=(15, 5))
    
    # Dibujar la ojiva
    plt.plot(datos_x_ojiva, datos_y_ojiva, 
             # Ancho de la línea
             linewidth=3, 
             # Color de la línea
             color="#1C2833",
             # Estilo de la línea
             linestyle="--", 
             # Marcador de puntos
             marker="v", 
             # Tamaño del marcador
             markersize=10, 
             # Color de relleno del marcador
             markerfacecolor="#FFF700", 
             # Color del borde del marcador
             markeredgecolor="#EC0000",
             # Ancho del borde del marcador
             markeredgewidth=1.5) 

    # Etiquetas para el eje x
    plt.xticks(valores_ref_eje, marcas_clase, fontsize=10)
    
    # Título y etiquetas para los ejes
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia acumulada", fontsize=15)
    plt.title("Ojiva", fontsize=20)
    
    # Agregar una grilla
    plt.grid()
    
    # Mostrar el gráfico
    plt.show()
    