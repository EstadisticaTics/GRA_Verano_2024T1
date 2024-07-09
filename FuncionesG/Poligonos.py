import matplotlib.pyplot as plt

def plot_poligono(marcas_clase, fa, fr, sabores):
    # Crea una lista de valores de referencia para el eje x
    valores_ref_eje = list(range(1, len(marcas_clase) + 1))
    
    # Crea las listas de datos para el polígono
    # Agrega un 0 al principio y al final para cerrar el polígono
    datos_x_poligono = [0] + valores_ref_eje + [valores_ref_eje[-1] + 1]
    datos_y_poligono = [0] + fr + [0]

    # Crea una figura con un tamaño de 15x5 pulgadas
    plt.figure(figsize=(15, 5))
    
    # Crea un gráfico de línea con los datos x e y
    # El ancho de la línea es de 3 puntos
    # El color de la línea es "#1C2833"
    # El estilo de la línea es discontinuo (linestyle="--")
    # El marcador es un círculo (marker="o")
    # El tamaño del marcador es de 10 puntos
    # El color de relleno del marcador es "#EB7AF5"
    # El color del borde del marcador es "#003DA2"
    # El ancho del borde del marcador es de 1.5 puntos
    plt.plot(datos_x_poligono, datos_y_poligono, 
             linewidth=3, 
             color="#1C2833", 
             linestyle="--", 
             marker="o", 
             markersize=10, 
             markerfacecolor="#9CFF33", 
             markeredgecolor="#09FFFB",
             markeredgewidth=1.5) 

    # Establece las etiquetas del eje x con los sabores
    # El tamaño de la fuente es de 10 puntos
    plt.xticks(valores_ref_eje, sabores, fontsize=10)

    # Establece la etiqueta del eje x
    plt.xlabel("Sabores", fontsize=15)

    # Establece la etiqueta del eje y
    plt.ylabel("Frecuencia relativa", fontsize=15)

    # Establece el título del gráfico
    plt.title("Polígono de frecuencias", fontsize=20)

    # Agrega una rejilla al gráfico
    plt.grid()

    # Muestra el gráfico
    plt.show()
    