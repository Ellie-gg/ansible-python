n = int(input("Digite o valor de n: "))
z = int(0)
while n > 0:
    z += n % 10
    n = int(n / 10)
print (z)
