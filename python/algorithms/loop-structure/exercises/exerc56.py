#
# Escreva um programa que peça strings ao usuário usando um loop. O programa imprime cada string sublinhada como mostrado nos exemplos abaixo. A execução termina quando o usário insere uma string vazia - ou seja, apenas pressiona Enter no prompt.
#

while True:
    word = input("Enter a word (or press Enter to quit): ")
    if word == "":
        break
    else:
        print(f"{word}\n{'-' * len(word)}")