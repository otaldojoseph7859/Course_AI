#
# Escreva uma função chamada printa_varias_vezes(texto, vezes), que recebe uma string e um inteiro como argumentos. O argumento inteiro especifica quantas vezes o argumento string deve ser impresso:
#
texto = input("Enter a string: ")
vezes = int(input("Enter the number of times it will repeat: "))

def printa_varias_vezes(texto, vezes):
    return texto * vezes

print(printa_varias_vezes(texto, vezes))