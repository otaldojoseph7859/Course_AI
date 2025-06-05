#
# Verifique o nome de um mês do ano. Informe um número de 1 a 12 representando o mês e, utilizando uma estrutura de decisão, exiba o nome do mês correspondente. Caso o número informado não seja válido, exiba a mensagem "Mês Inválido".
#
month = int(input("Enter a month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid Month")