#
# Escreva um programa que peça ao usuário para digitar um limite superior. O programa então imprime números de modo que cada número subsequente seja o anterior dobrado, começando do número 1. Ou seja, o programa imprime potências de dois em ordem. A execução do programa termina quando o próximo número a ser impresso for maior que o limite definido pelo usuário. Nenhum número maior que o limite deve ser impresso.
#
limit  = int(input("Enter an upper limit: "))
number = 1
print("Powers of 2 up to the defined limit:")
while number <= limit:
    print(number)
    number *= 2