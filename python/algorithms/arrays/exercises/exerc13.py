#
# Escreva uma função que peça ao usuário para digitar 5 nomes. Se o nome já estiver na lista, ele não deve ser adicionado novamente. Ao final, imprima todos os nomes cadastrados.
#
def register_names():
    list = []

    while len(list) < 5:
        name = input("Enter a name: ")

        if name in list:
            print("This name is already in the list, please enter another name: ")
        else:
            list.append(name)

    print(list)

register_names()