#
# Escreva uma função chamada range, que recebe uma lista de inteiros como argumento. A função retorna a diferença entre o menor e o maior valor na lista.
#
values = [8,3,15,1,9]

def range(list):
    return max(list) - min(list)

print(range(values))