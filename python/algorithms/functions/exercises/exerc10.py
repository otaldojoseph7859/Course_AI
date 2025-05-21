#
# Por favor, escreva uma função chamada mesmo_caracter, que recebe uma string e dois interos como argumentos. Os inteiros se referem a índices desntro da string. a função deve retornar True se os dois caracteres nos índices especificados forem os mesmos. Caso contrário, e especialmente se qualquer um dos índices estiver fora do escopo da string, a função retorna False.
#
argument1 = input("Enter a string: ")
argument2 = int(input("Write first index: "))
argument3 = int(input("Write secound index: "))

def mesmo_caracter(argument1, argument2, argument3):

    if argument1[argument2] == argument1[argument3]:
        print(True)
    else:
        print(False)

mesmo_caracter(argument1, argument2, argument3)