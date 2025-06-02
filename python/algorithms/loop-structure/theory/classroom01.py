#
# Aula teórica 01
#
my_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeiras"
print(my_string.count("a"))

my_list = [1,2,3,5,6,6,9,9,8]
print(my_list.count(6))

# replace

my_word = "Oi, Oi, Oi, amigos"
new_word = my_word.replace("Oi", "Olá")
print(new_word)

# Lista bidmensional
two_dimensional_list = [
    [0,1,2,3],
    [0,8,6,9],
    [1,2,7,4],
    [4,5,6,8]
]
print(two_dimensional_list[2][2])

#
# Escreva um algoritmo que imprime na tela o tabuleiro de sudoku baseado na lista enviada no teams.
#
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

for i in sudoku:
    for j in i:
        if j == 0:
            print("_", end=" ")
        else:
            print(j, end=" ")
    print("")