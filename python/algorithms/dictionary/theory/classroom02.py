#
# Escreva uma função chamada histogram, que recebe uma string como argumento. A função deve imprimir um histograma representando o número de vezes que cada letra ocorre na string. Cada ocorrência de uma letra deve ser representada por um asterístico na linha específica para aquela letra. Por exemplo, a chamada de função histogram("abba") deve imprimir: a ** e b **.
#

def histogram(x):
    for i in x:
        