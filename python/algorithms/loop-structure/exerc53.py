#
# Crie um programa que simule um caixa eletrônico. O programa deve pedir ao usuário
#
balance = 1000

print(f"Your balance is: {balance}")

while True:
    withdrawn = int(input("Enter the amount to be withdrawn (multiple of 10): "))

    if withdrawn % 10 != 0:
        print("The amount must be a multiple of 10.")
    elif withdrawn > balance:
        print("Insufficient balance.")
    elif withdrawn <= 0:
        print("The amount must be greater than zero.")
    else:
        balance -= withdrawn
        print(f"Withdrawal of ${withdrawn} successfully completed!. Your new balance is: ${balance}")
        break