#
# Esreva uma função chamada add_filme(database: list, nome: str, diretor: str, ano: int, duracao: int), que adiciona um novo objeto de filme em um banco de dados de filmes. O banco de dados é uma lista, e cada objeto de filme na lista é um dcionário. O dicionário deve conter as seguintes chaves. Nome, diretor, Ano, Tempo de execução. Os valores anexados a essas chaves são fornecidos como argumentos para a função.
#
database = []

def add_film(db: list, name_film, name_director, year_film, duraction_film):
    film = {
        "name": name_film,
        "director": name_director,
        "year": year_film,
        "duraction": duraction_film
    }
    db.append(film)

while True:

    answer = int(input("Want to add a movie? [1 - Yes][2 - Not][3 - View]"))

    if answer == 1:

        name = input("Type the name to film: ")
        director = input("Type the director name: ")
        year = int(input("Type the year to film: "))
        duraction = int(input("Type the duraction to film: "))

        add_film(database, name, director, year, duraction)

    elif answer == 2:
        print("Ending the program...")
        break

    elif answer == 3:
        for film in database:
            print(film)