#
# Escreva um programa que peça ao usuário para digitar uma string. O programa então imprime cada caractere de entrada em uma linha separada. Depois de cada caractere deve haver um asterisco (*) impresso em sua própria linha.
#
text = input("Enter a string: ")

for caracter in text:
    print(caracter, end="*")