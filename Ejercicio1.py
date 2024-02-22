gutierres=[
           [1, 2, 3],

           [4, 5, 6],

           [7, 8, 9]]

def buscar(gutierres, valor):
    for i in range(len(gutierres)):
        for j in range(len(gutierres[i])):
            if gutierres[i][j] == valor:
               return f"El valor {valor}, se encuentra en la posiòn ({i}, {j},)"
    return f"El valor {valor}, no se encuentra en la Array"

valor_a_buscar =2

resultado = buscar(gutierres, valor_a_buscar)

print(resultado)

