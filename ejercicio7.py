"""
Escriba una función recursiva borde(matriz) que reciba una matriz y genere una lista
con los elementos de la matriz que conforman su borde. Por ejemplo:
borde([[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20]])
Resultado: [1,2,3,4,5,6,10,11,15,16,17,18,19,20]
"""
def borde(matrix:list):
    return recursiva(matrix, 0, [])
def recursiva(matrix:list, index:int, lista:list) -> list:
    if index == len(matrix):
        return lista
    lista.extend(matrix[index])
    return recursiva(matrix, index + 1, lista)
print(borde([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]))