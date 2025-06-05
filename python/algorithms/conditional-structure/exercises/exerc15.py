#
# Crie um programa em Python que verifique a categoria de um produto. Verifique em qual categoria o produto se enquadra. Se o preço for menor ou igual a R$ 50,00, exiba a mensagem "Categoria Econômica". Se for maior que R$ 50,00 e menor ou igual a R$ 100,00, exiba a mensagem "Categoria Intermediária". Caso contrario, exiba a mensagem "Categoria Premium".
#
price = float(input("Enter the product price: "))

if price <= 50.00:
    print("Economic Category")
elif price > 50.00 and price <= 100.00:
    print("Intermediate Category")
else:
    print("Premium Category")