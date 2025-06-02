# Dicionários arquivados dentro de listas

pessoa1 = {"nome": "Pippa Python", "altura": 154, "peso": 61, "idade": 44}
pessoa2 = {"nome": "Peter Pythons", "altura": 174, "peso": 103, "idade": 31}
pessoa3 = {"nome": "Pedro Python", "altura": 191, "peso": 71, "idade": 14}
pessoas = [pessoa1, pessoa2, pessoa3]
 
for pessoa in pessoas:
    print(pessoa["nome"])
 
altura_combinada = 0
for pessoa in pessoas:
    altura_combinada += pessoa["altura"]
print("A altura média é", altura_combinada / len(pessoas))
 