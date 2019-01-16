def remove_repetidos(lista):
    lista1 = []
    for x in lista:
        if x not in lista1:
            lista1.append(x)
    return sorted(lista1)


