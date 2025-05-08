#
# Escreva um programa que solicite ao usuário um núero inteiro. O programa deve então imprimir a magnitude do número de acordo com os exemplos a seguir. 
#
number = int(input("enter a number: "))

if number < 1000 and number >= 100:
    print("This number is less than 1000, thank you!")
elif number < 100 and number >= 10:
    print("This number is less than 1000 and lessa than 100, thank you!")
elif number < 10:
    print("This number is less than 1000 and lessa than 100 and less than 10, thank you!")
else:
    print("Thank you!")


number 