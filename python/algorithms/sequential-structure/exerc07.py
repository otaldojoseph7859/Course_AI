#
# Crie um programa que calcule o IMC (Índice de Massa Corporal).
# Fórmula: IMC = peso / altura ** 2

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

imc = weight / (height ** 2)

print("Your BMI is: ", imc)
