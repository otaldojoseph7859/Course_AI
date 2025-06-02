#
# Dictionary
#

# Usado para armazenar dados no formato: Chave:valor
# São ordenados
# Mutáveis
# Não permite elementos duplicados

my_dictionary = {}
my_dictionary["apina"] = "Macaco"
my_dictionary["nome"] = "Jhon"

word = input("Write a word: ")

if word in my_dictionary:
    print("Tanslater: ", my_dictionary[word])
else:
    print("Word not found")

result = {}
result["maria"] = 5
result["julia"] = 10

sum = result["maria"] + result["julia"]
print(sum)

# Imprimir chave e valor

dictionary = {}

dictionary["apina"] = "Macaco"
dictionary["banana"] = "Amarela"
dictionary["cembalo"] = "Cravo"

for key in dictionary:
    print("Chave: ", key)
    print("Valor: ", dictionary[key])

# Popular """

word_list = ["banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"]

def count(my_list):
    words = {}
    for word in my_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words

print(count(word_list))