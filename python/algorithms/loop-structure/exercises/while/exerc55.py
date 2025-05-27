#
# Escreva um programa que imprima uma linha de caracteres hash, cuja largura é escolhida pelo usuário.
#
width = int(input("Enter the width of the line: "))
result = "#"

while True:
    if width > 0: 
        result *= width
        print(result)
        break
    else:
        print("Please enter a positive integer.")
        width = int(input("Enter the width of the line: "))
        continue

