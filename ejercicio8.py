"""
Escriba una función recursiva divida(dig, num) que reciba un dígito y un número
entero y obtenga dos números:
a. el primero compuesto por los dígitos mayores o iguales al dígito dado
b. el segundo compuesto por los dígitos menores al dígito dado
"""
def divida(dig:int, num:int):
    return recursiva(dig, [int(i) for i in list(str(num))], 0, {'mayores':[], 'menores':[]})
def recursiva(dig:int, num:int, index:int, resultado: dict) -> dict:
    if index == len(num):
        return resultado
    else:
        if num[index] >= dig:
            resultado['mayores'].append(num[index])
        else:
            resultado['menores'].append(num[index])
        return recursiva(dig, num, index + 1, resultado)
print(divida(5, 90123456789))