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