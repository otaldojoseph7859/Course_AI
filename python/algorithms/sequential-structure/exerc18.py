#
# Crie um programa que solicite ao usuário o valor da conta e o percentual de gorjeta, calcule o valor da gorjeta e o valor total a pagar, e imprima os resultados.
#

account_value = input("Write the account value: $ ")
tip = input("Write the tip percentage: ")

finish_price = account_value * (1 + tip / 100)

print(f"The finish price wich the discount applied is: $ {finish_price:.2f}")