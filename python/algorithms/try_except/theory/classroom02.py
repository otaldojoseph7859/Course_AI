#
# Digite um número intero. Use try e except para garantir que, se o usuário digitar algo que não seja número, o programa não quebre e mostre uma mensagem de erro personalizada.
#
try: 
    integer_number = int(input("Type a integer number: "))
    print(f"You type: {integer_number}")

except ValueError:
    print("ERROR: You not type a integer number. Try again")

else:
    print("Program worked successfully")