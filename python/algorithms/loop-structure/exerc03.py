#
# Verifique se o número está dentro do intervalo permitido:
# Se estiver, imprima a tabuada completa desse número (de 1 a 10).
# Se não estiver, exiba uma mensagem de erro informando que o número deve estar entre 1 e 10.

number = int(input("Enter a number between 1 and 10: "))
result = number
cont = 0

if (number > 0 and number <= 10):
    while (cont < 10):
        cont = cont + 1
        result = number * cont

        print(number, " X ", cont, " = ", result)

else:
    print("Enter a valid value!")