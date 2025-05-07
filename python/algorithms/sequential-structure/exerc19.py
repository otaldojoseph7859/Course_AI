#
# Crie um programa que solicite um valor em reais, converta para dólares (utilize uma taxa de câmbio fixa e imprima o resutado).
#
value = float(input("enter the value: R$ "))
dolar = 5.80
exchange = value / dolar
print(f"The value {value} in dollars is: $ {exchange:.2f}")
