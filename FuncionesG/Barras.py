import matplotlib.pyplot as plt

def plot_barras(marcas_clase, frecuencias, marcas_texto):
    # Crea una figura con un tamaño de 12x6 pulgadas
    plt.figure(figsize=(12, 6))

    # Crea un gráfico de barras horizontal con las marcas de clase en el eje y y las frecuencias en el eje x
    # El alto de cada barra es de 0.75 unidades
    # El borde de cada barra es negro (edgecolor="k")
    # Los colores de las barras se definen en una lista de colores hexadecimales
    plt.barh(marcas_clase, frecuencias, 
             height=0.75, edgecolor="k", 
             color=["#A832CA", "#F3FF99", "#CA5A37", "#4EE74E", "#298CFC", "#E7DEE4"])

    # Establece las etiquetas del eje y con las marcas de texto
    # El tamaño de la fuente es de 15 puntos
    plt.yticks(marcas_clase, marcas_texto, fontsize=15)

    # Establece la etiqueta del eje x
    plt.xlabel("Frecuencias", fontsize=20)

    # Establece la etiqueta del eje y
    plt.ylabel("Marcas de clase", fontsize=20)

    # Establece el título del gráfico
    plt.title("Diagrama de barras", fontsize=25)

    # Agrega una rejilla al gráfico
    plt.grid()

    # Muestra el gráfico
    plt.show()
    