#
# Escreva uma função chamada caixa_de_hastag, que iprima um retângulo de caracteres hash. A fnção recebe um argumento, que especifica a altura do retângulo. O retângulo deve ter caracteres de largura. A função deve chamar linha do exercício anterior para a impressão real. Copie sua solução para esse exercício acima do código para este exercício. Por favor, não altere nada em sua função linha.
#
def linha(argument1, argument2):

    if argument2 == "":
        linha = "*" * argument1
        print(linha)
    else:
        comprimento_linha = argument2[0] * argument1
        print(comprimento_linha)
        
width = int(input("Enter the size of rectangle: "))

def caixa_de_hashtag(width):
    cont = 0
    while cont < width:
        linha(10, "#")
        cont += 1

caixa_de_hashtag(width)