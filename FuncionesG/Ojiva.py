import matplotlib.pyplot as plt

def plot_ojiva(marcas_clase, valores_ref_eje, fa, fr, facum, sabores):
    # Crea una lista de datos para el eje x, agregando un 0 al principio
    datos_x_ojiva = [0] + valores_ref_eje
    
    # Crea una lista de datos para el eje y, agregando un 0 al principio
    datos_y_ojiva = [0] + facum

    # Crea una figura con un tamaño de 15x5 pulgadas
    plt.figure(figsize=(15, 5)) 

    # Crea un gráfico de línea con los datos x e y
    # El ancho de la línea es de 3 puntos
    # El color de la línea es "#1C2833"
    # El estilo de la línea es discontinuo (linestyle="--")
    # El marcador es un triángulo hacia abajo (marker="v")
    # El tamaño del marcador es de 10 puntos
    # El color de relleno del marcador es "#EB7AF5"
    # El color del borde del marcador es "#003DA2"
    # El ancho del borde del marcador es de 1.5 puntos
    plt.plot(datos_x_ojiva, datos_y_ojiva, 
         linewidth=3, 
         color="#1C2833",
         linestyle="--", 
         marker="v", 
         markersize=10, 
         markerfacecolor="#9CFF33", 
         markeredgecolor="#09FFFB",
         markeredgewidth=1.5) 

    # Establece las etiquetas del eje x con las marcas de clase
    # El tamaño de la fuente es de 10 puntos
    plt.xticks(valores_ref_eje, marcas_clase, fontsize=10)

    # Establece la etiqueta del eje x
    plt.xlabel("Sabores", fontsize=15)

    # Establece la etiqueta del eje y
    plt.ylabel("Frecuencia acumulada", fontsize=15)

    # Establece el título del gráfico
    plt.title("Ojiva", fontsize=20)

    # Agrega una rejilla al gráfico
    plt.grid()

    # Muestra el gráfico
    plt.show()
    