#
# Crie um programa que solicite 3 notas ao usuário e calcule a média dessas notas. 
#
note1 = float(input("Enter first note: "))
note2 = float(input("Enter second note: "))
note3 = float(input("Enter third note: "))
average = (note1 + note2 + note3) / 3
print(f"The average of the notes is: {average:.2f}")