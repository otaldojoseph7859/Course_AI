#
# Peça uma nota entre 0 e 10 e informe:
# Aprovado (nota maior ou igual a 7)
# Recuperação (nota entre 5 e 6.9)
# Reprovado (nota menor que 5)

note = float(input("Enter a score between 0 and 7: "))

if (note >= 0 and note <= 10):
    if (note >= 7):
        print("Approved!")
    elif (note >= 5 and note < 7):
        print("Recovery!")
    if (note < 5):
        print("Failed!")
else:
    print("Enter a valid value!")