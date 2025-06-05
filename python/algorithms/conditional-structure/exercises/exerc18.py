#
# Escreva um programa que solicite dois números inteiros. O programa deve então imprimir o que for maior. Se os números forem iguais, o programa deverá imprimir uma mensagem diferente.
#
number1 = int(input("Enter the first integer: "))
number2 - int(input("Enter the second integer: "))

if number1 > number2:
    print(f"The greater number is: {number1}")
elif number2 > number1:
    print(f"The greater number is: {number2}")
else:
    print("Both numbers are equal.")