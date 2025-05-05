#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]
list2 = []

print("Vamos crair a nova lista para unir com a lista atual: \n", main_list)
answer1 = input("Digite o nome do primeiro carro que você quer adicionar à lista: ")
list2.append(answer1)
answer2 = input("Digite o nome do segundo carro que você quer adicionar à lista: ")
list2.append(answer2)
answer3 = input("Digite o nome do terceiro carro que você quer adicionar à lista: ")
list2.append(answer3)

print("Agora que criamos a nova lista\n", list2, "\n Vamos unir as duas listas!")

main_list.extend(list2)

print(main_list)