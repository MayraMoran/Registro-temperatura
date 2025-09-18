# CalculoDescuentoPython.py
# Autor: Mayra Morán
# Descripción: Programa en Python para calcular descuentos en compras

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar en una compra.

    Parámetros:
        monto_total (float): El valor total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Ejemplo 1: Usando el valor por defecto (10%)
    compra1 = 100.0
    descuento1 = calcular_descuento(compra1)
    monto_final1 = compra1 - descuento1

    print("Compra 1:")
    print(f"  Monto total: ${compra1}")
    print(f"  Descuento aplicado (10%): ${descuento1}")
    print(f"  Monto final a pagar: ${monto_final1}\n")

    # Ejemplo 2: Usando un porcentaje personalizado (20%)
    compra2 = 200.0
    descuento2 = calcular_descuento(compra2, 20)
    monto_final2 = compra2 - descuento2

    print("Compra 2:")
    print(f"  Monto total: ${compra2}")
    print(f"  Descuento aplicado (20%): ${descuento2}")
    print(f"  Monto final a pagar: ${monto_final2}")
