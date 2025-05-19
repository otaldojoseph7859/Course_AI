#
# Escreva um programa que pergunte ao usuário seu nome e ano de nascmineto. O programa então imprime uma mensagem como segue: 
#
name = input("Whats is your name? ")
year = int(input("Whats is your year of birth? "))

age = 2025 - year

print(f"Hello {name}, you will be {age} years old at the end of 2025.")