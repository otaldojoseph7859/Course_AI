#
# Peça ao usuário dois números para dividir. Use try e except para capturar erros de divisão por zero e exibir uma mensagem apropriada.
#
try:
    number1 = float(input("Enter a firt number: "))
    number2 = float(input("Enter a secound number: "))
    result = number1 / number2
    print(f"The result of dividing {number1} by {number2} is: {result}")

except ZeroDivisionError:
    print("ERROR: Can't divide by zero")

else:
    print("Calculation performed successfully")