#
# Este programa calcula o bônus de final de ano que um cliente recebe em seu cartão fidelidade. O bônus é calculado com a seguinte formula: 1 - se houver menos de cem pontos no cartão, o bônus é de 10%, 2 - Em qualquer outro caso o bônus é de 15%.
#
points = int(input("Enter the number of points: "))

if points < 100:
    print("10% bonus")
else:
    print("15% bonus")