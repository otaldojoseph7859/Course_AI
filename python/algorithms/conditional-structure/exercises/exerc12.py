#
# Por favor, escreva um programa que solicite a previsão do tempo para amanhã e depois sugira roupas adequadas ao clima. A sugestão deve mudar se a temperatura estiver acima de 20, 10 ou 5 graus, e também se houver chuva no radar.
#
temperature = int(input("Enter the temperature: "))
storm = int(input("Is there a storm? [1 - yes][2 - no] "))

if temperature > 20:
    if storm == 1:
        print("Good weather. Wear pants and a t-shirt.")
    else:
        print("Good weather. Wear pants and a t-shirt. Bring an umbrella.")
elif temperature >= 10 and temperature <= 20:
    if storm == 1:
        print("Attention! Cold and rainy weather. Wear pants, a shirt and bring a jacket.")
    else:
        print("Attention! Cold and rainy weather. Wear pants, shirt and coat.")
elif temperature >= 5 and temperature < 10:
    if storm == 1:
        print("Warning! Very freezeing weather. Use a coat and a hat")
    else:
        print("Warning! Very cold and rainy weather. Wear a coat and hat.")
else:
    print("Warning! Very cold weather. Stay at home.")