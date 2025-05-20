#
# Escreva uma função chamada triângulo, qe desenha um triângulo de hashtag. O tamanho deve ser tão alto e tão largo quanto o valor do argumento.
#
def triangulo(x):
    cont = 0
    while cont < x:
        element = "#" * (cont + 1)
        print(element)
        cont += 1

triangulo(5)