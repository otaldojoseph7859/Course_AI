#
# Crie um programa que solicite ao usuário o capital inicial, a taxa de juros anual e o tempo em anos, calcule os juros simples (Juros = Capital * Taxa * Tempo) e imprima o montante final.
#
initial_value = float(input("Enter the initial capital: R$ "))
interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time in years: "))
interest = initial_value * interest_rate * time
final_amount = initial_value + interest
print(f"The final amount after {time} years is: R$ {final_amount:.2f}")