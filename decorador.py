def decorator(func):
    def wrapper(*args, **kwargs):
        listaNumeros = list()
        cadenaNumeros = list()
        if 'listaNumeros' in kwargs:
            cadenaNumeros = list(kwargs['listaNumeros'])
        else:
            cadenaNumeros = list(args[0])

        for i in cadenaNumeros:
            if i.isdigit():
                listaNumeros.append(int(i))
            else:
                continue
        return func(listaNumeros, 0, list(), list())
    return wrapper
