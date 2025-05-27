#
# Escreva uma função chamada aagrams, que recebe duas strings como argumento. A função retorna Tre se as strings são anagramas uma da outra. Duas palavras são anagramas se elas contêm exatamente os mesmos caracteres. Dca: a função sorted também pode ser usada em strings.
#
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

def anagrams(a, b):
    return sorted(a) == sorted(b)

anagrams(string1, string2)