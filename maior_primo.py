 
from math import sqrt
def maior_primo(numero):
    aux = 0
    aux1 = 0
    while numero > 1:
        aux = sqrt(numero)
        aux = int(aux)
        aux1 = 0
        while aux >= 2:
            if numero%aux == 0:
                aux1 += 1
            if aux == 2:
                if aux1 == 0:
                    return (numero)
                    numero = 1
            aux -=1
        numero -=1