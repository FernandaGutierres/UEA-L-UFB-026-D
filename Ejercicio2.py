gutierresmaria=[
           [10, 20, 30],

           [40, 50, 60],

           [70, 80, 90]]



def sort_row(gutierresmaria, row_index):
    if row_index < 0 or row_index >= len(gutierresmaria):
        print("Índice de fila fuera de rango")
        return

    gutierresmaria[row_index] = sorted(gutierresmaria[row_index])

    row_index = 2  # Ordenar la segunda fila (índice 1)

    print("Array antes de ordenar:")
    for row in gutierresmaria:
        print(row)

    sort_row(gutierresmaria, row_index)

    print("\nArray después de ordenar la fila", row_index, "en orden ascendente:")
    for row in gutierresmaria:
        print(row)
