"""
Escriba una función llamada elimine(num, dig) que reciba un número entero y un
dígito válido, y elimine los dígitos del número que sean iguales al dígito dado.
"""
def elimine(num: int, dig: int):
    num = [int(i) for i in list(str(num))]
    if dig not in num:
        print(f'{dig} is not in the string')
        return
    return recursiva(0, num, dig)

def recursiva(index: int, num: list, dig: int):
    print(index, num)
    if index >= len(num):
        return num
    elif dig == num[index]:
        return recursiva(index, num[:index]+num[index+1:], dig)
    else:
        return recursiva(index + 1, num, dig)
print(elimine(3456788764, 8))
print(elimine(5555555555555, 5))