#
# Escreva uma função chamada conta_elementos_match(minha_matriz: list, elemento: int), que recebe um array bidimensional de inteiros e um único valor iteiro como seus argumentos. A função então conta quantos elementos dentro da matriz correspondem ao valor do argumento.
#
number = int(input("Enter a element: "))

my_list = [[0,1,2,3],[0,4,6,9],[1,2,7,4],[4,5,6,8]]

def conta_elementos_match(my_matriz, x):
    cont = 0
    for i in my_matriz:
        for j in i:
            if j == x:
                cont += 1
    return cont

print(conta_elementos_match(my_list, number))