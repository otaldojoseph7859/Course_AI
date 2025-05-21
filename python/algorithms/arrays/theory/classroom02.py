#
# Escreva um programa que inicialize uma lista com valores [1, 2, 3, 4, 5]. Então o programa deve pedir ao usuário um indíce de um novo valor, substituir o valor no índice fornecido e imprimir a lista novamente. Isso deve ser repetido até que o usuário forneça -1 para o índice.
#

list = [1, 2, 3, 4, 5]

print(f"This is the list now: {list}")

while True:

    index = int(input("Enter the index to be changed: (Enter -1 in index to close the program!)"))

    if index == -1:
        print("Terminating the program...")
        break

    if index < 0 or index > (len(list) - 1):

        print("You entered an invalid index, terminating the program...")
    
    else:

        new_value = int(input("Enter new value: "))
        list[index] = new_value
        print(f"This is the list of changes : {list}")