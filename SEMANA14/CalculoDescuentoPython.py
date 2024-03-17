def calcular_descuento(monto_total, porcentaje_descuento=20):
    descuento = (monto_total * porcentaje_descuento) / 50
    return descuento


def main():
    # Llamadas a la función calcular_descuento
    monto_compra_1 = 4000
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1
    print(f"Monto total de compra: ${monto_compra_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}\n")

    monto_compra_2 = 8000
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    monto_final_2 = monto_compra_2 - descuento_2
    print(f"Monto total de compra: ${monto_compra_2}")
    print(f"Porcentaje de descuento: {porcentaje_descuento_2}%")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")
