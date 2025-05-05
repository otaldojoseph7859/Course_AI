#
# Peça a idade do usuário e classifique conforme a faixa etária:
# Criança (até 12 anos)
# Adolescente (13 a 17 anos)
# Adulto (18 a 59 anos)
# Idoso (60 anos ou mais)

age = int(input("Enter your age: "))

if (age <= 12):
    print("Child")
elif (age > 13 and age <= 17):
    print("Adolescent")
elif (age > 18 and age <= 59):
    print("Adult")
elif (age > 59):
    print("Elderly")
