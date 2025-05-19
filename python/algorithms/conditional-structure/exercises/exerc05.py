#
# Escreva um programa onde você armazena 4 valores de variáveis (nome, cidade, estado e cep) e peça para o usuário escrever um nome no input. Se o nome for igual ao definido na variável, ele exibirá osdados das outras variáveis. Se for diferente, exiba a mensagem ("esse usuário não existe em nossa bases de dados")
#
name = "Chrystopher"
city = "Curitiba"
state = "Paraná"
cep = "81130-260"

name_user = input("Enter a name: ")

if name_user == name:
    print(f"Name: {name}\nCity: {city}\nState: {state}\nCEP: {cep}")
else:
    print("This user does not exist in our database.")