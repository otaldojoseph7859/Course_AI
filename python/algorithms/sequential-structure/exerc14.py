#
# Escreva um programa que calcule o preço por hora de um trabalhador. O usuário deve inserir o salário e o número de horas trabalhadas no mês. O programa deve gerar o preço por hora.
#
salary = float(input("Enter the salary: "))
month_hours = float(input("Enter the number of hours worked in the month: "))
price_hour = salary / month_hours

print(f"The price per hour is: {price_hour:.2f}")