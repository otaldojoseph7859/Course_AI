#
# Por favor, escreva uma função chamada o_maior_numero, que recebe três argumentos. A função retorna o maior valor dos três.
#
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

def o_maior_numero(x, y, z):
    return max(x, y, z)

print(o_maior_numero(x, y, z))