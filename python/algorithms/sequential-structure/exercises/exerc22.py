#
# Crie um programa que solicite ao usuário a largura e a altura de um retângulo, calcule a área (largura * altura) e o perímetro (2(largura+altura)), e imprima os resultados.
#
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = width * height
perimeter = 2 * (width + height)
print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")

