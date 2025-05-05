#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]

answer1 = input("Digite o nome do carro que você quer adicionar à lista: ")
answer2 = int(input("Digite a posição que você deseja adicionar: "))

list.insert(answer2, answer1)
print(answer1, " foi adicionado com sucesso a lista na posição !", answer2)

print(list)