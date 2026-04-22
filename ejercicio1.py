"""
Escriba una función que reciba un número (que debe ser entero) y retorne dos listas:
una con los dígitos entre 0 y 4 y otra con los dígitos entre 5 y 9.
"""
from decorador import decorator
@decorator
def operacion(listaNumeros:list, index, ceroAlCuatro: list, cincoAlNueve: list):
    return numeros(listaNumeros=listaNumeros, index=index, ceroAlCuatro=ceroAlCuatro, cincoAlNueve=cincoAlNueve)

def numeros(listaNumeros:list, index, ceroAlCuatro: list, cincoAlNueve: list) -> list: # Updated list
    print(ceroAlCuatro, cincoAlNueve)
    if index >= len(listaNumeros) - 1:
        return (ceroAlCuatro, cincoAlNueve)
    elif listaNumeros[index] < 5:
        ceroAlCuatro.append(listaNumeros[index])
        return numeros(listaNumeros, index + 1, ceroAlCuatro, cincoAlNueve)
    elif listaNumeros[index] >= 5:
        cincoAlNueve.append(listaNumeros[index])
        return numeros(listaNumeros, index + 1, ceroAlCuatro, cincoAlNueve)

print(operacion('95423.4jh57890'))