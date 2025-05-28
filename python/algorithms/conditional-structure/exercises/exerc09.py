#
# Escreva um programa que solicite o salário por hora, as horas trabalhadas e o dia da semana. O programa deverá então imprimir o salário diário, que é igual ao salário por hora multiplicado pelas horas trabalhadas, exceto aos domingos, quando o salário por hora é duplicado.
#
hour_salary = float(input("Enter the hourly salary: "))
hours_worked = float(input("Enter the number of hours worked: "))
day_week = input("Enter the day of the week : ")

if day_week == "Sunday":
    day_salary = (hour_salary * 2) * hours_worked
else:
    day_salary = hour_salary * hours_worked
print(f"The salary is: $ {day_salary:.2f}")
