#
# Escreva um programa que pergunte ao usuário sua idade. O programa deve então imprimir uma mensagem com base se o usuário é maior de idade ou não, usando 18 como a idade de maturidade.
#
age = int(input("Enter your age: "))

if age > 17:
    print("You is adult!")
else: 
    print("You are not an adult, you are young or a child!")