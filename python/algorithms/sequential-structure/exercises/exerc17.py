#
# Crie um programa que solicite ao usuário o preço de um produto e o percentual de desconto, calcule o valor do desconto e o novo preço, e imprima os resultados.
#
price_product = float(input("Write the price to product: $ "))
discount = float(input("Write the discount percentage: "))

discount_value = price_product * (discount / 100)
new_price = price_product - discount_value

print(f"The discount amount is: $ {discount_value:.2f}")
print(f"The new price of the product is: $ {new_price:.2f}")