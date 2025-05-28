#
# Escreva um programa que solicite ao usuário um número inteiro. Se o número for menor que zero, o programa deverá imprimir o número multiplicado por -1. Caso contrário, o programa imprime o número como está.
#
number = int(input("Enter a integer number: "))

if number < 0:
    result = number * (-1)
    print(result)
else:
    print(number)