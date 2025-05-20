#
# Escreva uma função chamada linha, que recebe dois argumentos: um inteiro e uma string. A função imprime uma linha de texto, cujo comprimento é especificado pelo primeiro argumento. O caractere usado para desenhar a linha deve ser o primeiro caractere no segundo argumento. Se o segundo argumento for uma string vazia, a linha deve consistir em asteriscos.
#
argument1 = int(input("Enter the number of characters: "))
argument2 = input("Enter a word: ")

def linha(argument1, argument2):

    if argument2 == "":
        linha = "*" * argument1
        print(linha)
    else:
        comprimento_linha = argument2[0] * argument1
        print(comprimento_linha)

linha(argument1, argument2)