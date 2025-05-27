#
# Escreva um programa que pergunte ao usuário um ano e imprima o próximo ano bissexto
#
year = int(input("Enter a year: "))

while True:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"The next leap year is {year}.")
        break
    year += 1