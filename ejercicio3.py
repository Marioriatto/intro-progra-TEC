"""
Construya una función de nombre split(lista). Esta función toma una lista y la divide
en sublistas usando como punto de corte cada vez que aparezca un cero.No puede
utilizar la función split de python.
"""
def split(lista: list):
    return recursiva(lista)
def recursiva(lista: list):
    if len(lista) == 0:
        return []
    i = 0
    while(True):
        if i >= len(lista):
            return lista
        if lista[i] == 0:
            break
        else:
            i += 1
    print(lista[:i], lista[i + 1:])
    return lista[:i] + recursiva(lista[i + 1:])
print(split([9,0,8,7,0,6,4,0,9]))