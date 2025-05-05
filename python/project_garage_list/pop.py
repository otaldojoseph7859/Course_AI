#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]

print("Esta é a nossa lista atual: \n", list)
answer = int(input("Digite o número da posição que você quer remover da lista: "))

list.pop(answer)

print("O veículo da posição ", answer, " foi removido da nossa lista!\n")
print("Esta é a nossa lista atual: \n")
print(list)

