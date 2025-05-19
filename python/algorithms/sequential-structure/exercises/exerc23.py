#
# Crie um programa que solicite ao usário uma temperatura em graus celsius, converta para Fahrenheit (F = C * 9/5 + 32) e imprima o resultado.
#
temperature_celsius = float(input("Enter the temperature in Celsius: "))
temperature_fahrenheit = temperature_celsius * 1.8 + 32
print(f"The temperature in Fahrenheit is: {temperature_fahrenheit:.2f}°F")