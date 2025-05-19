#
# Escreva um programa que solicite ao usuário dois números e uma operação. Se a operação for adicionar, multiplicar ou subtrair, o programa deverá calcular e imprimir o resultado da operação com os números fornecidos. Se o usuário digitar qualquer outra coisa, o programa não deverá imprimir nada.
#
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, /, *, **, %, //): ")

if operation == "+":
    result = number1 + number2
    print(f"The result of {number1} + {number2} is: {result}")
elif operation == "-":
    result = number1 - number2
    print(f"The result of {number1} - {number2} is: {result}")
elif operation == "*":
    result = number1 * number2
    print(f"The result of {number1} * {number2} is: {result}")
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print(f"The result of {number1} / {number2} is: {result}")
    else:
        print("Division by zero is not allowed.")
elif operation == "**":
    result = number1 ** number2
    print(f"The result of {number1} ** {number2} is: {result}")
elif operation == "%":
    result = number1 % number2
    print(f"The result of {number1} % {number2} is: {result}")
elif operation == "//":
    if number2 != 0:
        result = number1 // number2
        print(f"The result of {number1} // {number2} is: {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation. No result to display.")