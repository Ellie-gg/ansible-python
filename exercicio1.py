def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n -1
    return fat


def testa_fatorial():
    if fatorial(1) == 1:
        print("Funcional para 1")
    else:
        print("não funciona")
    