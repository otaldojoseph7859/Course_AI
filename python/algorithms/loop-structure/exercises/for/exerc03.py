#
# Escreva um programa que peça ao usuário um inteiro positivo N. O programa então imprime todos os números entre -N e N inclusive, mas deixa de fora o número 0. Cada número deve ser impresso em uma linha separada.
#
n = int(input("Enter a positive integer number: "))

for integer in range(-n, n + 1):
    if integer != 0:
        print(integer, end=", ")
