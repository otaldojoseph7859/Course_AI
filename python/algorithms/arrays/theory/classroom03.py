#
# Escreva um programa que prieiro pergunte ao usuário o número de itens a serem adicionados. Então o programa deve perguntar o número para ser inserido, um por um, e adicioná-lo a uma lista na ordem e que foram digitados. finalmente, a lista é impressa.
#
size_list = int(input("Enter the size of list: "))

cont = 0
list = []

while cont < size_list:
    new_value = int(input("Enter the new value: "))
    list.append(new_value)
    cont += 1

print(f"This is the list now: {list}")