#
# Verifique a média de duas notas de um aluno. Verifique se a média é maior ou igual a 7. Se for, exiba a mensagem "Aprovado", caso contrário, exiba a mensagem "Reprovado".
#
note1 = float(input("Enter the first note: "))
note2 = float(input("Enter the secound note: "))
average = (note1 + note2) / 2

if average > 7:
    print("You are approved with successes!")
else:
    print("You are reproved!")