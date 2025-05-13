#
# Escreva um programa que imprima todos os números pares entre dois e trinta, usando um loop. Imprima cada número em uma linha separada. O início da sua saída deve ficar assim: 2 4 6 8 etc...
#
number = 0
while number <= 30:
    if number % 2 == 0 and number != 0:
        print(number)
    number += 1
print("End of program")
