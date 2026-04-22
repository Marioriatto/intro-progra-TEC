"""
Escriba una función llamada natural(lista) que reciba una lista de números
desordenados y produzca una lista de listas, donde cada sublista agrupe los
elementos que se encuentren en orden ascendente correcto. Es decir, se van a tener
sublistas que mantienen el orden de sus componentes, pero que terminan si el
siguiente número en la lista original es menor al actual. Por ejemplo:
natural([3, 4, 5, 1, 2, 3, 4, 7, 3, 2, 1])
Resultado: [[3, 4, 5], [1, 2, 3, 4, 7], [3], [2], [1]]
"""
def natural(lista:list):
    return recursiva(lista, [[lista[0]]], 1)
def recursiva(lista:list, listas:list, index:int):
    if index == len(lista):
        return listas
    else:
        print(listas)
        if lista[index] >= lista[index-1]:
            listas[len(listas)-1].append(lista[index])
        else:
            listas.append([lista[index]])
        print(listas)
        return recursiva(lista, listas, index + 1)

print(natural([1,2,3,4,5,6,9,6,5,4,2,3,4,5]))