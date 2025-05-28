#
# Escreva uma função chamada sem_vogal, que recebe um argumento string. A função retorna uma nova string, que deve ser a mesma que a original, mas com todas as vogais removidas. Você pode assumir que a sequência conterá apenas caracteres do alfabeto inglês minúsculo de a a z.
#
text = input("Enter a string: ")

def sem_vogal(text):
    vowels = "aeiou"
    new_text = ""

    for letter in text:
        if letter not in vowels:
            new_text += letter
        
    return new_text

print(sem_vogal(text))