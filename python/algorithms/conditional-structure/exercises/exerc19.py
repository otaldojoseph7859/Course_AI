#
# Por favor, escreva um programa que solicite os nomes e idades de duas pessoas. O programa deverá então imprimir o nome do idoso.
#
name1 = input("Enter the name of the first person: ")
age1 = int(input("Enter the age of the first person: "))
name2 = input("Enter the name of the second person: ")
age2 = int(input("Enter the age of the second person: "))

if age1> age2:
    print(f"The older person is {name1}.")
elif age2 > age1:
    print(f"The older person is {name2}.")
else:
    print("Both persons are of the same age.")
    