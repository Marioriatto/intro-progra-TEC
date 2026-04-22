"""
Escriba una función llamada cambie_todos(num) que reciba un número entero y
sustituya todos los valores que aparezcan dos o más veces por un cero. No puede
usar la función count. Ejemplo: 18025382 => 1000500
"""
def decorarxd(func):
    def wrapper(*args):
        return int((func(0, [int(i) for i in list(str(args[0]))], 1, False)))
    return wrapper

@decorarxd
def funcion(checkThisNumber:int, num:list, index:int, isRepeated:bool):
    lista = cambie_todos(checkThisNumber, num, index, isRepeated)
    return sum([(10 ** ((len(lista) - 1) - i)) * lista[i]  for i in range(len(lista))])

def cambie_todos(checkThisNumber:int, num:list, index:int, isRepeated:bool):
    print(f'numero {num} revisando {checkThisNumber}, indice:{index}')
    #Replace
    if num[checkThisNumber] != 0 and num[checkThisNumber] == num[index] and checkThisNumber != index:
        num[index] = 0
        isRepeated = True
    #Iterate
    if checkThisNumber != len(num) - 1:
        #End of Iteration
        if index == (len(num) - 1):
            if isRepeated:
                num[checkThisNumber] = 0
            if checkThisNumber < len(num) - 1:
                num = cambie_todos(checkThisNumber + 1, num, checkThisNumber + 1, False)
            return num
        else:
            cambie_todos(checkThisNumber, num, index + 1, isRepeated)
        # ...
    return num
print(funcion(1234567890))
print(funcion(335))