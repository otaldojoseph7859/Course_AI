#
# Escreva uma função chamada mais_caracteres, que recebe um argumento string. A função retorna o caractere que tem mais ocorrências dentro da string.
#
text = input("Enter a string: ")

def mais_caracteres(text):

    largest_letter = ""
    highest_cont = 0

    for letter in text:
        cont = text.count(letter)
        if cont > highest_cont:
            highest_cont = cont
            largest_letter = letter

    return largest_letter

print(mais_caracteres(text.replace(" ","")))