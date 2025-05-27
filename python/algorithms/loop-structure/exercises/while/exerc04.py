#
# Crie um programa em Python que:
# Possua uma senha pré-definida no código, como por exemplo: "python123".
# Peça ao usuário que digite a senha.
# O usuário terá no máximo 3 tentativas para acertar a senha.
# Se acertar, o programa deve exibir a mensagem:
# "Acesso concedido!"
# Se errar todas as tentativas, o programa deve exibir:
# "Acesso bloqueado! Tentativas esgotadas."
# Use a estrutura de repetição while para controlar o número de tentativas.

password = "Usuario0"
user_password = input("Enter your password: ")
cont = 3

while (cont != 0):
    if (password == user_password):
        print("Acesso concedido!")
    else:
        cont = cont - 1
        print("Senha incorreta. Tentativas restantes: ", cont)