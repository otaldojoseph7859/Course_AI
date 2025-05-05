#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]

print("Esta é a nossa lista de carros atual: \n", list)
print(main_list)
car = input("Digite o nome e ano do carro que deseja remover: ")

list.remove(car)

print("O carro ", car, " foi removido da nossa lista!\n", "Esta é a lista atual", list)



