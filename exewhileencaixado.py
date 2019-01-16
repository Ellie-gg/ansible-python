l = int(input("digite a largura"))
a = int(input("digite a altura"))
lar = l
contador = 0 
while contador < a:
    while a > 0:
        while l > 0:
            print("#", end = "")
            l = l - 1
        print()
        a = a -1
        l = lar
        contador += 1