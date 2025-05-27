#
# Altere o programa do exercício anterior para que o usuário possa inserir também a base que é multiplicada (no programa anterior, a base era sempre 2).
#
limit  = int(input("Enter an upper limit: "))
awnser = int(input("Enter the base number: "))
number = 1
print("Powers of 2 up to the defined limit:")
while number <= limit:
    print(number)
    number *= awnser