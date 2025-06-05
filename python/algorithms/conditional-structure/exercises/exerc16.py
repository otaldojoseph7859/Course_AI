#
# Verifique se uma pessoa pode votar. Verifgique se a idade é maior ou igual a 16. Se for, exiba a mensagem "Pode votar", caso contrário, exiba a mensagem "Não pode votar".
#
age = int(input("Enter your age: "))

if age >= 16:
    print("Ok, you can vote.")
else:
    print("Sorry, you cannot vote yet.")
