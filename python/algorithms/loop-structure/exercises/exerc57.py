#
# Escreva um programa que peça ao usuário uma string e então a imprima de modo que exatamente 20 caracteres sejam exibidos. Se a entrada for menor que 20 caracteres, o começo da liha é preenchido com * caracteres.
#
word = input("Enter a string: ")
if len(word) < 20:
    print("*" * (20 - len(word)) + word)
else:
    print(word[:20])
