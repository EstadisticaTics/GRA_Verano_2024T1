import matplotlib.pyplot as plt

def plot_hist(marcas_clase, frecuencias, marcas_texto):
    # Crea una figura con un tamaño de 12x6 pulgadas
    plt.figure(figsize=(12, 6))

    # Crea un gráfico de barras con las marcas de clase en el eje x y las frecuencias en el eje y
    # El ancho de cada barra es de 1 unidad
    # El borde de cada barra es negro (edgecolor="k")
    # Los colores de las barras se definen en una lista de colores hexadecimales
    plt.bar(marcas_clase, frecuencias, 
            width=1, edgecolor="k", 
            color=["#A832CA", "#F3FF99", "#CA5A37", "#4EE74E", "#298CFC", "#E7DEE4"])

    # Establece las etiquetas del eje x con las marcas de texto
    # El tamaño de la fuente es de 15 puntos y se rotan 45 grados para que sean más legibles
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)

    # Establece la etiqueta del eje x
    plt.xlabel("Marcas de clase", fontsize=20)

    # Establece la etiqueta del eje y
    plt.ylabel("Frecuencias", fontsize=20)

    # Establece el título del gráfico
    plt.title("Histograma", fontsize=25)

    # Agrega una rejilla al gráfico
    plt.grid()

    # Muestra el gráfico
    plt.show()
    