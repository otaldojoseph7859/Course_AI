#
# Escreva um programa que pergunte a idade do usuário. Se a idade não for plausível, ou seja, for menor de 5 anos ou algo que não possa ser a idade humana real, o programa deverá imprimir um comentário. Dê uma olhada nos exemplos de comportamento esperado abaixo para descobrir qual comentário é aplicável em cada caso.
#
age = int(input("Enter your age: "))

if age < 5:
    print("You are too young to be here.")
elif age > 120:
    print("You are too old to be here.")
elif age < 0:
    print("You are not born yet.")
else:
    print(f"Ok, you have {age} years old.")