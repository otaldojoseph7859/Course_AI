#
# Escreva uma função chamada quadradoString, que recebe um argumento de string e um argumento inteiro e imprime um quadrado de caracteres conforme especificado pelo exemplo abaixo: 
# 
# aybabtu
# 
# aybab
# tuayb
# abtua
# ybatt
# uayba
#
word = input("Enter a word: ")
word_height = int(input("Enter a number: "))

def quadradoString(word, word_height):

    cont = word_height
    while cont > 0:
        cont -= 1
        if len(word) > word_height:
            a = word_height - len(word)
            print(word[:a])
        elif len(word) == word_height:
            print(word)
        elif len(word) < word_height:
            a = word_height - len(word)
            while a < word_height:
                a = len(word) + len(word)
                word += word
            a = word_height - len(word)
            print(word[:a])

quadradoString(word, word_height)

