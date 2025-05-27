# 
# Escreva uma função chamada numeros_pares, que recebe uma lista de inteiros como argumento. A função retorna um nova lista contendo os números pares da lista original.
# 
list = [-15,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def numeros_pares(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(numeros_pares(list))