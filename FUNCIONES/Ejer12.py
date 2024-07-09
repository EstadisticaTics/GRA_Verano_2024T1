import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calcular_estadisticas_intervalos(datos):
    rango_datos = np.max(datos) - np.min(datos)
    num_clases_calculado = 1 + 3.3 * np.log10(len(datos))
    parte_entera_num_clases = int(num_clases_calculado)
    parte_decimal_num_clases = num_clases_calculado - parte_entera_num_clases

    if (parte_decimal_num_clases < 0.5):
        num_clases_redondeado = parte_entera_num_clases
    else:
        num_clases_redondeado = parte_entera_num_clases + 1

    ancho_clase_calculado = rango_datos / num_clases_redondeado

    limite_inferior_array, limite_superior_array, marcas_clases = obtener_limites_y_marcas(datos, num_clases_redondeado, ancho_clase_calculado)

    return limite_inferior_array, limite_superior_array, marcas_clases

def obtener_limites_y_marcas(datos, num_clases, ancho_clase):
    limites_clases = []
    limite_inferior_array = []
    limite_superior_array = []
    marcas_clases = []

    for i in range(int(num_clases)):
        limite_inferior = np.min(datos) + i * ancho_clase
        limite_superior = limite_inferior + ancho_clase
        limite_medio = (limite_inferior + limite_superior) / 2
        limites_clases.append((limite_inferior, limite_superior))
        limite_inferior_array.append(limite_inferior)
        limite_superior_array.append(limite_superior)
        marcas_clases.append(limite_medio)

    return limite_inferior_array, limite_superior_array, marcas_clases

def calcular_frecuencias(datos, limite_inferior, limite_superior):
    frecuencia_absoluta = []
    for lim_inf, lim_sup in zip(limite_inferior, limite_superior):
        frec_abs = np.sum((datos >= lim_inf) & (datos < lim_sup))
        frecuencia_absoluta.append(frec_abs)

    frecuencia_relativa = frec_rel(frecuencia_absoluta)
    frecuencia_acumulada = frec_acum(frecuencia_relativa)

    return frecuencia_absoluta, frecuencia_relativa, frecuencia_acumulada

def frec_rel(fa_absoluta):
    total_datos = sum(fa_absoluta)
    fr = [(frec / total_datos) * 100 for frec in fa_absoluta]
    return fr

def frec_acum(fr_relativa):
    fr_acumulada = []
    fr_ac = 0
    for fr in fr_relativa:
        fr_ac += fr
        fr_acumulada.append(fr_ac)
    return fr_acumulada

def crear_tabla(datos):
    limite_inferior, limite_superior, marcas_clases = calcular_estadisticas_intervalos(datos)
    frec_abs, frec_rel, frec_acum = calcular_frecuencias(datos, limite_inferior, limite_superior)

    tabla = pd.DataFrame({
        'Clase': np.arange(1, len(limite_inferior) + 1),
        'Limite Inferior': limite_inferior,
        'Limite Superior': limite_superior,
        'Marca de Clase': marcas_clases,
        'Frecuencia Absoluta': frec_abs,
        'Frecuencia Relativa': frec_rel,
        'Frecuencia Acumulada': frec_acum
    })

    return tabla

def plot_grafOjiva(marcas_clase, facum):
    """
    Función para dibujar una ojiva que muestra la frecuencia acumulada por marca de clase.
    
    Parámetros:
    - marcas_clase (list): lista de valores que representan las marcas de clase
    - facum (list): lista de números que representan la frecuencia acumulada para cada marca de clase
    """
    
    datos_x_ojiva = list(range(len(marcas_clase) + 1))
    datos_y_ojiva = [0] + facum

    plt.figure(figsize=(15, 5))
    
    plt.plot(datos_x_ojiva, datos_y_ojiva, 
             linewidth=3, 
             color="#1C2833",
             linestyle="--", 
             marker="v", 
             markersize=10, 
             markerfacecolor="#FFF700", 
             markeredgecolor="#EC0000",
             markeredgewidth=1.5) 

    plt.xticks(datos_x_ojiva, [f"{marca:.2f}" for marca in [0] + marcas_clase], fontsize=10)
    
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia acumulada (%)", fontsize=15)
    plt.title("Ojiva", fontsize=20)
    
    plt.grid()
    
    plt.show()

def plot_grafHist(frecuencias_relativas, marcas_clase, marcas_texto):
    """
    Función para dibujar un histograma que muestra la distribución de frecuencias relativas por marca de clase.
    
    Parámetros:
    - frecuencias_relativas (list): lista de números que representan la frecuencia relativa de cada marca de clase
    - marcas_clase (list): lista de valores que representan las marcas de clase
    - marcas_texto (list): lista de strings que representan los nombres de cada marca de clase
    """
    
    plt.figure(figsize=(12, 6))
    
    x = np.arange(len(marcas_clase))
    width = 0.5
    
    plt.bar(x, frecuencias_relativas, width, 
             edgecolor="k", 
             color=["#FF5733", "#33FF57", "#5733FF", "#FF33A6", "#33FFF6"])
    
    plt.xticks(x, marcas_texto, fontsize=15, rotation=45)
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencia relativa (%)", fontsize=20)
    plt.title("Histograma", fontsize=25)
    
    plt.ylim(0, max(frecuencias_relativas) * 1.1)
    
    plt.grid()
    
    plt.show()
