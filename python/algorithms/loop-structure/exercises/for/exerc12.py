#
# O jogo da velha é jogado em uma grade 3 por 3, por dois jogadores que se revezam inserindo cruzes e círculos. Se qualquer jogador conseguir colocar três de seus próprios símbolos em qualquer linha, coluna ou diagonal, ele ganha. Se nenhum jogador coseguir isso, é um empate. Escreva uma função chamada ogue_o_jogo(mesa: list, x: int, y: int, caracter: str), que coloca o símbolo dado nas coordenadas dadas no tabuleiro. Os valores das cordenadas no tabuleiro estão entre 0 e 2.
#

symbol1 = "X"
symbol2 = "O"
board = [[" "," "," "],[" "," "," "],[" "," "," "]]

# Função para verificar qual é o jogador da vez!
def player_turn(cont):
    if cont % 2 == 0:
        print("Player 1's turn")
        player = 1
        return player
    else:
        print("Player 2's turn")
        player = 2
        return player

# Função para validar se os valores inseridos são válidos e se for válido inseri o valor na posição selecionada!
def position_validation(x, o, player):
    player_turn(cont)
    if player == 1:
        exio_x = int(input("Enter a position in exio x: "))
        if exio_x < 0 or exio_x > 2:
            print("Enter a valid value!")
            return False
        else:
            exio_y = int(input("Enter a position in exio y: "))
            if exio_y < 0 or exio_x > 2:
                print("Enter a valid value!")
                return False
            else:
                if board[exio_x][exio_y] != " ":
                    print("Location already selected, choose another position!")
                else:
                    board[exio_x][exio_y] = x
        cont += 1
        print(board)
    elif player == 2:
        exio_x = int(input("Enter a position in exio x: "))
        if exio_x < 0 or exio_x > 2:
            print("Enter a valid value!")
        else:
            exio_y = int(input("Enter a position in exio y: "))
            if exio_y < 0 or exio_x > 2:
                print("Enter a valid value!")
            else:
                if board[exio_x][exio_y] != " ":
                    print("Location already selected, choose another position!")
                else:
                    board[exio_x][exio_y] = o
        cont += 1
        print(board)

# Função para rodar o jogo
def tic_tac_toe(x, o):
    print(board)
    cont = 0
    while cont < 9:
        player_turn(cont)








    print("this is finish result: ", board)

tic_tac_toe(symbol1, symbol2)
