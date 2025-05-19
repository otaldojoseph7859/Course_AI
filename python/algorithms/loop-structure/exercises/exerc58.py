#
# Escreva um programa que peça ao usário uma string e então imprima um quadro de *caracteres com a palavra no centro. A largura do quadro deve ser  de 30 caracteres. Você pode assumir que a string de entrada sempre caberá dentro do quadro. Se o comprimeto da sequência de entrada for um número ímpar, você pode imprimir a palavra em qualquer um dos dois possíveis locais centrais.
#
word = input("Enter a string: ")
width = len(word)

total_padding = 30 - width
left_padding = total_padding // 2
right_padding = total_padding - left_padding

print("*" * 30)
print(((" " * left_padding) - 2) + "*" + " " + word + " " + "*" + ((" " * right_padding) - 1))
print("*" * 30)