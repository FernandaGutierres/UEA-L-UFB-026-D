def sort_row(gutierres , row_index):
    if row_index < 0 or row_index >= len(gutierres):
        print("Índice de fila fuera de rango")
        return

    gutierres[row_index] = sorted(gutierres[row_index])

# Ejemplo de uso
gutierres = [
    [3, 7, 2],
    [5, 1, 4],
    [9, 0, 3]
]
# Ordenar la segunda fila (índice 1)
row_index = 1

print("Matriz antes de ordenar:")
for row in gutierres:
    print(row)

sort_row(gutierres, row_index)

print("\nMatriz después de ordenar la fila", row_index, "en orden ascendente:")
for row in gutierres:
    print(row)
