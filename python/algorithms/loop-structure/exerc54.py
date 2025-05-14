#
# Escreva um programa que solicite ao usuário para dgitar duas palavras. O programa deve continuar pedindo até que ambas as palavras tenham a mesma quantidade de caracteres.
#
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

while len(word1) != len(word2):
    print("The words must have the same number of characters.")
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

print("The words have the same number of characters.")