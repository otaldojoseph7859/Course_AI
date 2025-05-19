#
# Escreva uma função chamada mesaXadrez, que imprima um tablueiro feito de uns e zeros. A função recebe um argumento inteiro, que especifica o comprimento do lado do tabuleiro. Veja os exemplos para detalhes.
#
n = int(input("Enter the number of repetitions: "))

def mesaXadrez(n):
    row1 = "○ "
    row2 = "◙ "
    cont = n

    while cont > 0:
        if cont % 2 != 0:
            if n % 2 == 0:
                print(f"{(row1 + row2) * (n // 2)}")
            else:
                print(f"{(row1 + row2) * (n // 2) + row1}")

            cont -= 1
        else:
            if n % 2 == 0:
                print(f"{(row2 + row1) * (n // 2)}")
            else:
                print(f"{(row2 + row1) * (n // 2) + row2}")

            cont -= 1

mesaXadrez(n)
