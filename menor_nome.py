def menor_nome(lista):
    c = 1
    menor = lista[0].strip()
    while c < len(lista):
        if len(menor) > len(lista[c].strip()):
            menor = lista[c].strip()
        c += 1
    return menor.lower().capitalize()