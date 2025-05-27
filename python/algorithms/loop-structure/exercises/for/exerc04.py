#
# Escreva uma função chamada lista_estrelas, que recebe um lista de inteiros como argumento. A função deve imprimir linhas de caracteres de asterisco. Os números na lista especificam quantos asteriscos cada linha deve conter. Por exemplo, com a chamada de função, lista_estrelas
#
list_stars = [3,7,11,2]

def stars_caracter(list: list):
    for i in list:
        stars = "*" * i
        print(stars)
    
stars_caracter(list_stars)