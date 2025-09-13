# temperaturas.py
# Autor: Mayra Morán
# Descripción: Función para calcular temperaturas promedio de varias ciudades y semanas.

def calcular_promedios(datos):
    """
    Calcula la temperatura promedio de varias ciudades a lo largo de varias semanas.

    Parámetros:
    datos (dict): Diccionario donde la clave es el nombre de la ciudad
                  y el valor es una lista de temperaturas semanales.

                  Ejemplo:
                  {
                      "Guaranda": [20, 22, 19, 21],
                      "Quito": [15, 16, 14, 17],
                      "Ambato": [18, 19, 20, 21]
                  }

    Retorna:
    dict: Diccionario con el promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = round(promedio, 2)
    return promedios


# Ejemplo de uso
if __name__ == "__main__":
    datos_temperaturas = {
        "Guaranda": [20, 22, 19, 21],
        "Quito": [15, 16, 14, 17],
        "Ambato": [18, 19, 20, 21]
    }

    resultados = calcular_promedios(datos_temperaturas)
    print("Promedios de temperatura por ciudad:")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad}: {promedio} °C")
