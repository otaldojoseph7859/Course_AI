#
#
#
main_list = ["Camaro 79'", "Corvette 04'", "Dodge Charger 69'"]

print("Esta é a nossa lista atual: ", main_list)
asnwer = int(input("Você deseja apagar esta lista? \n[1 - SIM] [2 - NÃO] \n"))
if (asnwer == 1):
    main_list.clear()
    print("Todos os dados da lista foram apagados, esta é a nossa lista atual: \n", main_list)
elif (asnwer == 2):
    print("Ok, redirecionando ao menu principal...")
else:
    print("Digite um valor válido! [1 - SIM] [2 - NÃO]")