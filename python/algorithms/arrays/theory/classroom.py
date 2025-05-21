#
# Escreva um programa que peça ao usuário para escolher entre adição e remoção. Dependendo da escolha, o programa adiciona um item ou remove um item do final de uma lista. O item que é adicionado deve ser sempre um a mais que o último item da lista. O primeiro item a ser adicionado deve ser 1. A lista é impressa no começo e depois de cada operação. A lista é impressa no começo e depois de cada operação. Você pode presumir que, se a lista estiver vazia, não haverá tentativa de reover itens. Se o item especificado não estiver na lista, a remove função causa erro.
#
list = [1]

while True:
    
    answer = int(input("To add an item to the list, type 1, to remove an item from the list, type 2: "))

    if answer == 1:
        new_value = int(input("Enter the new value: "))
        list.append(new_value)
    elif answer == 2:
        remove_value = int(input("Enter the value to remove: "))
        list.remove(remove_value)
    print(list)