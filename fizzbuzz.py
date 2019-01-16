x = int(input("entrada: "))
z = x % 3
y = x % 5
if z == 0 and y == 0:
    print("FizzBuzz")
else:
    print(x)
