#
# Escreva uma função chamada lista_soma que recebe duas listas de inteiros como argumentos. A função retorna uma nova lista que contém as somas dos itens em cada ídice nas duas listas originais. Você pode assumir que ambas as listas têm o mesmo número de itens.
#
list1 = [13,27,3,34,45]
list2 = [12,15,16,17,27]

def lista_soma(a, b):
    new_list = []
    for i in range(5):
        new_value = a[i] + b[i]
        new_list.append(new_value)
    return new_list

print(lista_soma(list1, list2))