import matplotlib.pyplot as plt

def plot_grafBarras(frecuencias_relativas, marcas_clase, marcas_texto):
    """
    Función para dibujar un gráfico de barras horizontales que muestra la distribución de frecuencias relativas por marca de clase.
    
    Parámetros:
    - frecuencias_relativas (list): lista de números que representan la frecuencia relativa de cada marca de clase
    - marcas_clase (list): lista de strings que representan las marcas de clase
    - marcas_texto (list): lista de strings que representan los nombres de cada marca de clase
    
    Lo que hace:
    - Dibuja un gráfico de barras horizontales que muestra la distribución de frecuencias relativas por marca de clase
    - Muestra la frecuencia relativa de cada marca de clase en la gráfica
    - Invierte el eje y para que las marcas de clase aparezcan en orden alfabético
    """
    
    # Crear una figura con un tamaño específico
    plt.figure(figsize=(12, 6))
    
    # Dibujar las barras horizontales
    plt.barh(marcas_clase, frecuencias_relativas,
             # Altura de cada barra
             height=0.5,
             # Color del borde de cada barra
             edgecolor="k",
             # Colores de cada barra
             color=["#FF5733", "#33FF57", "#5733FF", "#FF33A6", "#33FFF6"])
    
    # Etiquetas para el eje y
    plt.yticks(marcas_clase, marcas_texto, fontsize=12)
    
    # Título y etiquetas para los ejes
    plt.xlabel("Frecuencias Relativas", fontsize=15)
    plt.ylabel("Marcas de Clase", fontsize=15)
    plt.title("Diagrama de barras", fontsize=20)
    
    # Agregar una grilla en el eje x
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    # Invertir el eje y para que las marcas de clase aparezcan en orden alfabético
    plt.gca().invert_yaxis()  
    
    # Mostrar el gráfico
    plt.show()
    