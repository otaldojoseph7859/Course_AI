#
# Crie um programa que peça ao usuário para adivinhar um número entre 1 e 100. O programa deve continuar pedindo até que o usuário advinhe o número corretamente. Dê dicas se o número é maior ou menor a cada tentativa.
#
import random

secret_number = random.randint(1, 100)

asnwer = int(input("Write a number between 1 and 100: "))

while asnwer != secret_number:
    if asnwer < secret_number:
        print("The number is greater")
    else:
        print("The number is less")
    asnwer = int(input("Write a number between 1 and 100: "))

print("Congratulations! You guessed the number.")