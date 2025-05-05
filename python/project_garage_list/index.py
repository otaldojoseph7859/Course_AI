#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]

print("Esta é a nossa lista atual: \n")
print(main_list)

asnwer = input("Digite o nome e ano do carro que deseja descobrir a posição: ")

print("a posição do ", asnwer, " é: ", main_list.index(asnwer))