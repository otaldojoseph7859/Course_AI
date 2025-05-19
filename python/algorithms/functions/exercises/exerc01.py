#
# Escreva uma função chamada média, que recebe três argumentos inteiros. A função deve imprimir a média aritimética dos três argumentos.
#
x = float(input("Enter a first number: "))
y = float(input("Enter a second number: "))
z = float(input("Enter a third number: "))

def media(x, y, z):
    media = (x + y + z) / 3
    return print(f"A média é: {media:.2f}")

media(x, y, z)