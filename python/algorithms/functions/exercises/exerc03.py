#
# Escreva uma função chamada quadrado_hastag(tamanho), que recebe o argumento iinteiro. A função imprime um quadrado de caracteres hash, e o argumento especifica o comprimento do lado do quadrado.
#
tamanho = int(input("Enter a size in centimeters: "))

def quadrado_hastag(tamanho):
    cont = tamanho
    
    while cont > 0:
        print("#" * tamanho)
        cont -= 1
    return

print(quadrado_hastag(tamanho))