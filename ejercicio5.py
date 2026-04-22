"""
Escriba una función llamada coincide(lista) que recibe una lista de números enteros
e indique si algún elemento de la lista coincide con la suma de todos los que le
preceden. Por ejemplo
coincide([2, 4, 3, 9, 14]) → 2 + 4 + 3 = 9
Resultado: True
coincide([5, 6, 14, 18, 20, 41])
Resultado: False
"""
def coincide(lista:list):
    isIt = recursiva(lista, -1, False, 0, 0)
    print(type(isIt))
    return isIt

def recursiva(lista:list, index:int, isIt:bool, buscar: int, suma: int):
    if index == -1:
        if suma == lista[buscar]:
            print(f'suma:{suma} Numero:{lista[buscar]}')
            isIt = True
        if not isIt and buscar < len(lista) - 1:
            isIt = recursiva(lista, buscar, isIt, buscar + 1, 0)
        return isIt
    else:
        if index != buscar:
            suma += lista[index]
        return recursiva(lista, index - 1, isIt, buscar, suma)
print(coincide([2, 4, 3, 9, 14]))
print(coincide([5, 6, 14, 18, 20, 41]))