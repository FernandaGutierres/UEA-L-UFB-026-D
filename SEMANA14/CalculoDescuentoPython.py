def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def main():
    # Llamadas a la función calcular_descuento
    compra_1 = 2000
    descuento_1 = calcular_descuento(compra_1)
    monto_final_1 = compra_1 - descuento_1
    print(f"Monto total de compra: ${compra_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}\n")

    compra_2 = 4000
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(compra_2, porcentaje_descuento_2)
    monto_final_2 = compra_2 - descuento_2
    print(f"Monto total de compra: ${compra_2}")
    print(f"Porcentaje de descuento: {porcentaje_descuento_2}%")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")

if __name__ == "__main__": main()
