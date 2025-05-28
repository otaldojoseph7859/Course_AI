#
# Por favor, escreva um programa que solicite o nome de usuário. Se o nome não for "Jerry", o programa solicita o número de porções e imprime o custo total. O preço da porção é 5,90.
#
name = input("Enter your name: ")
if name != "Jerry":
    portions = int(input("Enter the number of portions: "))
    cost = portions * 5.90
    print(f"The total cost is: ${cost:.2f}")
else:
    print("Access denied for Jerry.")