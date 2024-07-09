def format_str(datos):
    """
    Función para formatear una lista de strings eliminando espacios y convirtiendo a título.
    
    Parámetros:
    - datos (list): lista de strings que representan los datos a formatear
    
    Lo que hace:
    - Elimina los espacios en blanco al principio y al final de cada string
    - Convierte cada string a título (primera letra mayúscula, resto en minúscula)
    - Devuelve la lista de strings formateados
    
    Uso:
    - Se utiliza para preparar los datos de entrada para su posterior análisis y visualización
    - Se aplica a la lista de datos de entrada para eliminar espacios y excepciones en cadena
    """
    
    datos_str = []
    for elemento in datos:
        # Eliminar espacios en blanco al principio y al final de cada string
        # y convertir a título (primera letra mayúscula, resto en minúscula)
        datos_str.append(elemento.strip().lower().title())
    return datos_str
