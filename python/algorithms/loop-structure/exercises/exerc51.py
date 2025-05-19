#
# Escreva um programa que continue solicitando ao usuário para digitar uma senha até que ele insira uma senha que tenha pelo menos 8 caracteres, contenha pelo menos uma letra maiúscula, uma letra minuscula e um número.
#
import re

password = input("Enter a password: ")

while True:

    if len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[a-z]", password):
        print("Password must be at least 8 characters long, contain at least one uppercase letter and one number.")
        password = input("Enter a password: ")
    else:
        print("Password is valid.")
        print("Starting the system...")
        break
    