#
# Cie um programa que solicite ao usuário para digitar uma série de números até que a soma desses núeros seja maior que 100. Mostre a soma total ao final.
#
sum = 0

while sum <= 100:
    num = int(input("Enter a number: "))
    sum += num
print(f"The sum is: {sum}")
