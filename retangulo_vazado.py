largura = int(input('digite a largura: ')) 
altura = int(input('digite a altura: '))

cont = 1
linha = 1

while cont <= altura:
    
    while linha <= largura:
        if (cont == 1 or cont == altura) or (linha == 1 or linha == largura):
            print('#', end='')
        else:
            print(' ', end='')
        
        linha += 1
        
    print('')
    cont += 1
    linha = 1