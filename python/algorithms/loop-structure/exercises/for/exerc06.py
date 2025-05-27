#
# Escreva uma função chamada soma_positivos, que recebe uma lista de inteiros como argumento. A função retorna a soma dos valores positivos na lista.
#
list = [-15,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def soma_positivo(list):
    sum = 0 
    for number in list:
        if number > 0:
            sum += number
    return sum

print(soma_positivo(list))