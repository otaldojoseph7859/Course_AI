#
# Escreva um programa que solicite ao usuário uma temperatura em graus Fahrenheit e depois imprima a mesma em graus Celsius. Se a temperatura convertida cair abaixo de zero graus Celsius, o programa também deverá imprimir "Brr! Está frio aqui". A fórmula para converter graus Fahrenheit em graus Celsius pode ser fcilmente encontrada em qualquer mecanismo de busca de sua escolha.
#
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 1.8

if celsius < 0:
    print("Freezing point")
else:
    print("Not freezing point")